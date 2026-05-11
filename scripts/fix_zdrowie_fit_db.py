"""
Jednorazowa naprawa bazy zdrowiefit.db przed importem 10 nowych artykułów.

Robi trzy rzeczy:
1. Backup bazy do scripts/backups/zdrowiefit-<timestamp>.db.bak
2. Aktualizuje slugi kategorii do spójnych z domains/zdrowie-fit.yaml:
     fitness     -> fizyczne   (+ name, color, icon zaktualizowane)
     odzywianie  -> dieta      (+ name, color, icon)
     zdrowie     -> usunięta (artykuły o śnie idą do "fizyczne")
     wellbeing   -> usunięta (artykuły o naturze idą do "fizyczne")
3. Usuwa 5 starych demo artykułów (z seed_service) — robimy clean slate
   przed importem 10 nowych premium artykułów.

Tryb dry-run pokazuje co zrobi bez zapisywania:
    python scripts/fix_zdrowie_fit_db.py --dry-run

Wykonanie zmian:
    python scripts/fix_zdrowie_fit_db.py

Skrypt jest IDEMPOTENTNY — można odpalić wielokrotnie, nie zepsuje stanu.
"""
from __future__ import annotations

import argparse
import shutil
import sqlite3
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "backend" / "zdrowiefit.db"
BACKUP_DIR = ROOT / "scripts" / "backups"

# Plan migracji: stary_slug -> nowy_slug (lub None = USUŃ kategorię, artykuły remap'ujemy)
SLUG_RENAMES = {
    "fitness": "fizyczne",
    "odzywianie": "dieta",
}

# Kategorie do usunięcia po remappingu artykułów. Wartość = slug docelowy
# dla osieroconych artykułów (fallback).
SLUG_REMOVALS = {
    "zdrowie": "fizyczne",       # sen, odporność -> fizyczne
    "wellbeing": "fizyczne",     # natura, styl życia -> fizyczne
}

# Pełne docelowe definicje kategorii (zgodne z domains/zdrowie-fit.yaml).
# Aktualizujemy też name, color, icon, description po renamie.
TARGET_CATEGORIES = {
    "fizyczne": {
        "name": "Zdrowie fizyczne",
        "description": "Trening, ruch, aktywność fizyczna, neurobiologia ciała",
        "icon": "🏃",
        "color": "#4a7c59",
        "sort_order": 1,
    },
    "psychiczne": {
        "name": "Zdrowie psychiczne",
        "description": "Mindfulness, stres, regulacja emocji, neuropsychologia",
        "icon": "🧠",
        "color": "#5b8def",
        "sort_order": 2,
    },
    "dieta": {
        "name": "Dieta i odżywianie",
        "description": "Mikrobiom, dieta śródziemnomorska, MIND, suplementacja",
        "icon": "🥗",
        "color": "#d9724a",
        "sort_order": 3,
    },
}


def backup_db() -> Path:
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d-%H%M%S")
    target = BACKUP_DIR / f"zdrowiefit-{ts}.db.bak"
    shutil.copy2(DB_PATH, target)
    return target


def fetch_categories(cur: sqlite3.Cursor) -> dict[str, dict]:
    rows = cur.execute("SELECT id, name, slug, description, icon, color, sort_order FROM categories").fetchall()
    return {r["slug"]: dict(r) for r in rows}


def fetch_articles(cur: sqlite3.Cursor) -> list[dict]:
    rows = cur.execute("SELECT id, slug, title, category_id FROM articles").fetchall()
    return [dict(r) for r in rows]


def main() -> int:
    p = argparse.ArgumentParser(description="Naprawa bazy zdrowiefit.db przed importem 10 nowych artykułów")
    p.add_argument("--dry-run", action="store_true", help="Pokaż co zrobi, nic nie zapisuj")
    p.add_argument("--keep-demo", action="store_true", help="NIE usuwaj 5 starych demo artykułów (default: usuwa)")
    args = p.parse_args()

    if not DB_PATH.exists():
        print(f"[ERR] Brak bazy: {DB_PATH}", file=sys.stderr)
        return 2

    if not args.dry_run:
        backup = backup_db()
        print(f"[OK] Backup: {backup}")
    else:
        print("[DRY] Backup pominięty.")

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    cats = fetch_categories(cur)
    arts = fetch_articles(cur)
    print(f"\nObecnie w bazie: {len(cats)} kategorii, {len(arts)} artykułów")
    print("  Kategorie:", ", ".join(sorted(cats.keys())))

    cat_id_by_slug = {s: c["id"] for s, c in cats.items()}

    # Krok 1: REMAP artykułów ze slugów do usunięcia na cel fallback
    for old_slug, fallback_slug in SLUG_REMOVALS.items():
        if old_slug not in cat_id_by_slug:
            continue
        old_id = cat_id_by_slug[old_slug]
        # Po renamingu może już istnieć; jeśli fallback ma stary slug który będzie
        # przeniesiony, użyjmy nowego docelowego.
        target_slug = SLUG_RENAMES.get(fallback_slug, fallback_slug)
        target_id = cat_id_by_slug.get(target_slug) or cat_id_by_slug.get(fallback_slug)
        if not target_id:
            print(f"[WARN] Brak kategorii fallback '{target_slug}' — pomijam remap z '{old_slug}'", file=sys.stderr)
            continue
        affected = [a for a in arts if a["category_id"] == old_id]
        for a in affected:
            print(f"  REMAP art '{a['slug']}': category_id {old_id} ({old_slug}) -> {target_id} ({target_slug})")
            if not args.dry_run:
                cur.execute("UPDATE articles SET category_id=? WHERE id=?", (target_id, a["id"]))

    # Krok 2: USUŃ kategorie SLUG_REMOVALS
    for old_slug in SLUG_REMOVALS:
        if old_slug in cat_id_by_slug:
            print(f"  DEL kategoria '{old_slug}' (id={cat_id_by_slug[old_slug]})")
            if not args.dry_run:
                cur.execute("DELETE FROM categories WHERE slug=?", (old_slug,))

    # Krok 3: RENAME slugów istniejących kategorii
    for old_slug, new_slug in SLUG_RENAMES.items():
        if old_slug not in cat_id_by_slug:
            continue
        if new_slug in cat_id_by_slug and new_slug != old_slug:
            # Konflikt: docelowy slug już istnieje — przenosimy artykuły i usuwamy stary
            old_id = cat_id_by_slug[old_slug]
            new_id = cat_id_by_slug[new_slug]
            print(f"  CONFLICT: '{new_slug}' już istnieje. Przenoszę artykuły z '{old_slug}' i usuwam dup.")
            if not args.dry_run:
                cur.execute("UPDATE articles SET category_id=? WHERE category_id=?", (new_id, old_id))
                cur.execute("DELETE FROM categories WHERE slug=?", (old_slug,))
        else:
            print(f"  RENAME slug '{old_slug}' -> '{new_slug}'")
            if not args.dry_run:
                cur.execute("UPDATE categories SET slug=? WHERE slug=?", (new_slug, old_slug))

    # Krok 4: UPSERT docelowych kategorii (tworzy brakujące, aktualizuje name/color/icon)
    if not args.dry_run:
        cur.execute("SELECT id, slug FROM categories")
        live = {r["slug"]: r["id"] for r in cur.fetchall()}
    else:
        live = {**cat_id_by_slug}
        for old, new in SLUG_RENAMES.items():
            if old in live:
                live[new] = live.pop(old)
        for old in SLUG_REMOVALS:
            live.pop(old, None)

    for slug, defn in TARGET_CATEGORIES.items():
        if slug in live:
            print(f"  UPDATE kategoria '{slug}' (name/color/icon/desc)")
            if not args.dry_run:
                cur.execute(
                    """UPDATE categories
                       SET name=?, description=?, icon=?, color=?, sort_order=?
                       WHERE slug=?""",
                    (defn["name"], defn["description"], defn["icon"], defn["color"], defn["sort_order"], slug),
                )
        else:
            print(f"  INSERT kategoria '{slug}' ({defn['name']})")
            if not args.dry_run:
                cur.execute(
                    """INSERT INTO categories (name, slug, description, icon, color, sort_order, created_at)
                       VALUES (?, ?, ?, ?, ?, ?, ?)""",
                    (defn["name"], slug, defn["description"], defn["icon"],
                     defn["color"], defn["sort_order"], datetime.utcnow().isoformat()),
                )

    # Krok 5: USUŃ 5 starych demo artykułów (chyba że --keep-demo)
    if not args.keep_demo:
        demo_slugs = [
            "jak-ruch-wplywa-na-nastroj-naukowe-fakty",
            "sen-kiedy-twoj-mozg-pracuje-najciezej",
            "co-jesz-tym-myslisz-dieta-a-funkcje-poznawcze",
            "mindfulness-5-minut-ktore-zmienia-twoj-dzien",
            "shinrin-yoku-jak-las-leczy-cialo-i-umysl",
        ]
        for slug in demo_slugs:
            row = cur.execute("SELECT id, title FROM articles WHERE slug=?", (slug,)).fetchone()
            if row:
                print(f"  DEL demo art '{slug}' (id={row['id']}): {row['title']}")
                if not args.dry_run:
                    cur.execute("DELETE FROM articles WHERE id=?", (row["id"],))

    if not args.dry_run:
        conn.commit()
        print("\n[OK] Zmiany zapisane.")
    else:
        print("\n[DRY] Brak zapisu — uruchom bez --dry-run żeby wykonać.")

    # Stan końcowy
    cur.execute("SELECT slug, name FROM categories ORDER BY sort_order")
    final_cats = cur.fetchall()
    cur.execute("SELECT COUNT(*) AS n FROM articles")
    final_count = cur.fetchone()["n"]
    print(f"\nStan końcowy: {len(final_cats)} kategorii, {final_count} artykułów")
    for r in final_cats:
        print(f"  - {r['slug']:12s}  {r['name']}")

    conn.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
