"""
Uniwersalny import artykułów z plików .md do bazy danych Archaios SSG.

Obsługuje wszystkie domeny w content_generated/<domain-slug>/.
Parsuje YAML frontmatter, konwertuje markdown → HTML, wpisuje do bazy.

Tryby:
    USE_API=true  (default) → POST do FastAPI (http://127.0.0.1:8765)
    USE_API=false           → bezpośrednio do SQLite (backend/zdrowiefit.db)

Wymagania:
    pip install python-frontmatter markdown httpx pyyaml --break-system-packages

Użycie:
    python import_articles.py zdrowie-fit                       # jedna domena
    python import_articles.py zdrowie-fit --dry-run             # symulacja
    python import_articles.py zdrowie-fit --force-update        # nadpisz istniejące
    python import_articles.py --all                             # wszystkie domeny

Bezpieczeństwo:
    - Domyślnie SKIP istniejących slugów. --force-update nadpisuje.
    - --dry-run pokazuje co zostałoby zrobione, nie zapisuje nic.
    - Backup bazy: scripts/backup_db.py PRZED uruchomieniem.
"""
from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path
from typing import Any

try:
    import frontmatter
    import markdown
except ImportError:
    print("Brakujące pakiety: pip install python-frontmatter markdown httpx pyyaml", file=sys.stderr)
    sys.exit(1)

# ─────────────────────────────────────────────────────────────────────────
# KONFIGURACJA
# ─────────────────────────────────────────────────────────────────────────

USE_API = os.environ.get("USE_API", "true").lower() == "true"
API_URL = os.environ.get("API_URL", "http://127.0.0.1:8765/api")
DB_PATH = os.environ.get("DB_PATH", "../backend/zdrowiefit.db")
ADMIN_USER = os.environ.get("ADMIN_USERNAME", "admin")
ADMIN_PASS = os.environ.get("ADMIN_PASSWORD", "")

ROOT = Path(__file__).parent

# Domyślny autor (Marek Porycki)
DEFAULT_AUTHOR_SLUG = "marek-porycki"
DEFAULT_AUTHOR_NAME = "Marek Porycki"
DEFAULT_AUTHOR_CREDENTIALS = "psycholog, biegły sądowy, mediator, prorektor"
DEFAULT_AUTHOR_BIO_SHORT = (
    "Psycholog kliniczny, biegły sądowy, mediator. CEO Archaios.ai. "
    "Autor publikacji naukowych i thrillerów psychologicznych."
)

# ─────────────────────────────────────────────────────────────────────────
# PARSOWANIE PLIKU MD
# ─────────────────────────────────────────────────────────────────────────

def parse_article(path: Path) -> dict[str, Any]:
    post = frontmatter.load(path)
    fm = post.metadata
    body = post.content

    # Split content vs bibliography
    bib_match = re.search(r"\n---\s*\n\s*##\s*Bibliografia\s*\n", body, re.IGNORECASE)
    if bib_match:
        content_md = body[: bib_match.start()].strip()
        bibliography_html = body[bib_match.end():].strip()
    else:
        content_md = body
        bibliography_html = ""

    # Markdown → HTML
    md_engine = markdown.Markdown(
        extensions=["extra", "tables", "footnotes", "attr_list", "smarty"],
        output_format="html5",
    )
    content_html = md_engine.convert(content_md)

    return {
        "title": fm.get("title", ""),
        "slug": fm.get("slug", path.stem),
        "excerpt": fm.get("excerpt", ""),
        "content": content_html,
        "category_slug": fm.get("category_slug", ""),
        "author_slug": fm.get("author_slug", DEFAULT_AUTHOR_SLUG),
        "tags": fm.get("tags", ""),
        "reading_time": fm.get("reading_time", 10),
        "bibliography": bibliography_html,
        "related_slugs": fm.get("related_slugs", ""),
        "product_slugs": fm.get("product_slugs", ""),
        "is_published": fm.get("is_published", True),
        "is_featured": fm.get("is_featured", False),
        "meta_title": fm.get("meta_title", fm.get("title", "")),
        "meta_description": fm.get("meta_description", fm.get("excerpt", "")),
    }

# ─────────────────────────────────────────────────────────────────────────
# IMPORT VIA API
# ─────────────────────────────────────────────────────────────────────────

def import_via_api(articles: list[dict], domain_slug: str, dry_run: bool, force: bool) -> None:
    try:
        import httpx
    except ImportError:
        print("Brakujący pakiet: pip install httpx", file=sys.stderr)
        sys.exit(1)

    with httpx.Client(timeout=30.0) as client:
        if not ADMIN_PASS:
            print("Ustaw ADMIN_PASSWORD w env (matching backend/.env)", file=sys.stderr)
            sys.exit(2)
        r = client.post(
            f"{API_URL}/auth/login",
            data={"username": ADMIN_USER, "password": ADMIN_PASS},
        )
        if r.status_code != 200:
            print(f"Login failed: {r.status_code} {r.text}", file=sys.stderr)
            sys.exit(3)
        token = r.json().get("access_token")
        headers = {"Authorization": f"Bearer {token}"}

        r = client.get(f"{API_URL}/articles?limit=1000", headers=headers)
        existing_slugs = {a["slug"] for a in r.json().get("items", [])} if r.status_code == 200 else set()

        r = client.get(f"{API_URL}/categories", headers=headers)
        cat_map = {c["slug"]: c["id"] for c in r.json()} if r.status_code == 200 else {}

        r = client.get(f"{API_URL}/authors", headers=headers)
        author_map = {a["slug"]: a["id"] for a in r.json()} if r.status_code == 200 else {}

        if DEFAULT_AUTHOR_SLUG not in author_map:
            print(f"  Tworzę autora: {DEFAULT_AUTHOR_NAME}")
            if not dry_run:
                r = client.post(
                    f"{API_URL}/authors",
                    json={
                        "name": DEFAULT_AUTHOR_NAME,
                        "slug": DEFAULT_AUTHOR_SLUG,
                        "credentials": DEFAULT_AUTHOR_CREDENTIALS,
                        "bio_short": DEFAULT_AUTHOR_BIO_SHORT,
                    },
                    headers=headers,
                )
                if r.status_code in (200, 201):
                    author_map[DEFAULT_AUTHOR_SLUG] = r.json()["id"]

        for art in articles:
            slug = art["slug"]
            if slug in existing_slugs and not force:
                print(f"  SKIP istnieje: {slug}")
                continue

            cat_id = cat_map.get(art["category_slug"])
            author_id = author_map.get(art["author_slug"])
            if not cat_id:
                print(f"  WARN brak kategorii '{art['category_slug']}' — pomijam {slug}")
                continue

            payload = {
                "title": art["title"],
                "slug": art["slug"],
                "excerpt": art["excerpt"],
                "content": art["content"],
                "bibliography": art["bibliography"],
                "category_id": cat_id,
                "author_id": author_id,
                "tags": art["tags"],
                "reading_time": art["reading_time"],
                "related_slugs": art["related_slugs"],
                "product_slugs": art["product_slugs"],
                "is_published": art["is_published"],
                "is_featured": art["is_featured"],
                "meta_title": art["meta_title"],
                "meta_description": art["meta_description"],
            }

            if dry_run:
                print(f"  [DRY] {'UPD' if slug in existing_slugs else 'NEW'}: {slug}")
                continue

            if slug in existing_slugs and force:
                r = client.put(f"{API_URL}/articles/{slug}", json=payload, headers=headers)
            else:
                r = client.post(f"{API_URL}/articles", json=payload, headers=headers)

            if r.status_code in (200, 201):
                print(f"  OK: {slug}")
            else:
                print(f"  ERR {r.status_code}: {slug} — {r.text[:200]}", file=sys.stderr)

# ─────────────────────────────────────────────────────────────────────────
# IMPORT VIA SQLITE
# ─────────────────────────────────────────────────────────────────────────

def import_via_sqlite(articles: list[dict], domain_slug: str, dry_run: bool, force: bool) -> None:
    import sqlite3
    from datetime import datetime

    db_path = (Path(__file__).parent / DB_PATH).resolve()
    if not db_path.exists():
        print(f"Brak bazy: {db_path}", file=sys.stderr)
        sys.exit(4)

    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    cat_map = {row["slug"]: row["id"] for row in cur.execute("SELECT id, slug FROM categories")}
    author_map = {row["slug"]: row["id"] for row in cur.execute("SELECT id, slug FROM authors")}
    existing_slugs = {row["slug"] for row in cur.execute("SELECT slug FROM articles")}

    if DEFAULT_AUTHOR_SLUG not in author_map:
        if dry_run:
            print(f"  [DRY] Stwórz autora {DEFAULT_AUTHOR_SLUG}")
        else:
            cur.execute(
                """INSERT INTO authors (name, slug, credentials, bio_short, sort_order, created_at)
                   VALUES (?, ?, ?, ?, 0, ?)""",
                (DEFAULT_AUTHOR_NAME, DEFAULT_AUTHOR_SLUG, DEFAULT_AUTHOR_CREDENTIALS,
                 DEFAULT_AUTHOR_BIO_SHORT, datetime.utcnow().isoformat()),
            )
            author_map[DEFAULT_AUTHOR_SLUG] = cur.lastrowid

    for art in articles:
        slug = art["slug"]
        cat_id = cat_map.get(art["category_slug"])
        author_id = author_map.get(art["author_slug"])
        if not cat_id:
            print(f"  WARN brak kategorii '{art['category_slug']}' — pomijam {slug}")
            continue

        if slug in existing_slugs and not force:
            print(f"  SKIP istnieje: {slug}")
            continue

        if dry_run:
            print(f"  [DRY] {'UPD' if slug in existing_slugs else 'NEW'}: {slug}")
            continue

        now = datetime.utcnow().isoformat()
        if slug in existing_slugs:
            cur.execute(
                """UPDATE articles SET title=?, excerpt=?, content=?, bibliography=?,
                   category_id=?, author_id=?, tags=?, reading_time=?,
                   related_slugs=?, product_slugs=?, is_published=?, is_featured=?,
                   meta_title=?, meta_description=?, updated_at=? WHERE slug=?""",
                (art["title"], art["excerpt"], art["content"], art["bibliography"],
                 cat_id, author_id, art["tags"], art["reading_time"],
                 art["related_slugs"], art["product_slugs"], art["is_published"], art["is_featured"],
                 art["meta_title"], art["meta_description"], now, slug),
            )
        else:
            cur.execute(
                """INSERT INTO articles (title, slug, excerpt, content, bibliography,
                   category_id, author_id, tags, reading_time, related_slugs, product_slugs,
                   is_published, is_featured, meta_title, meta_description,
                   views, published_at, created_at, updated_at)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 0, ?, ?, ?)""",
                (art["title"], art["slug"], art["excerpt"], art["content"], art["bibliography"],
                 cat_id, author_id, art["tags"], art["reading_time"],
                 art["related_slugs"], art["product_slugs"], art["is_published"], art["is_featured"],
                 art["meta_title"], art["meta_description"], now, now, now),
            )
        print(f"  OK: {slug}")

    conn.commit()
    conn.close()

# ─────────────────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────────────────

def import_domain(domain_slug: str, dry_run: bool, force: bool) -> int:
    domain_dir = ROOT / domain_slug
    if not domain_dir.is_dir():
        print(f"  SKIP brak katalogu: {domain_dir}")
        return 0

    md_files = sorted([
        p for p in domain_dir.glob("[0-9][0-9]-*.md")
        if not p.name.startswith("_")
    ])
    print(f"\n=== {domain_slug}: {len(md_files)} artykułów ===")

    articles = []
    for path in md_files:
        try:
            articles.append(parse_article(path))
        except Exception as e:
            print(f"  ERR parse {path.name}: {e}", file=sys.stderr)

    if USE_API:
        import_via_api(articles, domain_slug, dry_run, force)
    else:
        import_via_sqlite(articles, domain_slug, dry_run, force)

    return len(articles)

def main() -> None:
    parser = argparse.ArgumentParser(description="Import artykułów Archaios SSG")
    parser.add_argument("domains", nargs="*", help="Slug domeny (np. zdrowie-fit). Pusty + --all = wszystkie.")
    parser.add_argument("--all", action="store_true", help="Importuj wszystkie domeny w content_generated/")
    parser.add_argument("--dry-run", action="store_true", help="Symulacja bez zapisu")
    parser.add_argument("--force-update", action="store_true", help="Nadpisuj istniejące slugi")
    args = parser.parse_args()

    if args.all:
        domains = sorted([d.name for d in ROOT.iterdir()
                         if d.is_dir() and not d.name.startswith("_")])
    elif args.domains:
        domains = args.domains
    else:
        parser.print_help()
        sys.exit(0)

    print(f"Tryb: {'API (' + API_URL + ')' if USE_API else 'SQLite'}")
    print(f"Dry-run: {args.dry_run}  Force: {args.force_update}")

    total = 0
    for d in domains:
        total += import_domain(d, args.dry_run, args.force_update)

    print(f"\nZakończono. Łącznie {total} artykułów w {len(domains)} domenach.")

if __name__ == "__main__":
    main()
