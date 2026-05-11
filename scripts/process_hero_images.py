"""
Process hero images dla zdrowie.fit:
  1. Czyta wszystkie hero PNG z content_generated/zdrowie-fit/_deployment/ (lub /downloads/)
  2. Konwertuje do WebP 1200x675 q80 (~150-250 KB) + JPG q85 fallback
  3. Zapisuje do src/static/img/articles/
  4. Aktualizuje pole image_url w bazie SQLite (backend/zdrowiefit.db)
  5. Wypisuje podsumowanie

Mapowanie nazwy pliku -> slug artykułu jest stałe (patrz HERO_MAP).

Wymagania:
    pip install Pillow --break-system-packages

Użycie:
    python scripts/process_hero_images.py            # full run
    python scripts/process_hero_images.py --dry-run  # tylko symulacja
    python scripts/process_hero_images.py --skip-convert  # tylko update bazy
"""
from __future__ import annotations

import argparse
import shutil
import sqlite3
import sys
from datetime import datetime
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print("Brakujący pakiet: pip install Pillow --break-system-packages", file=sys.stderr)
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent

# Folder gdzie Marek wrzuca hero PNG-i (akceptujemy oba miejsca)
SOURCE_CANDIDATES = [
    ROOT / "content_generated" / "zdrowie-fit" / "_deployment" / "downloads",
    ROOT / "content_generated" / "zdrowie-fit" / "_deployment",
]

# Docelowy folder na webp/jpg (serwowany przez build.py jako /static/img/articles/...)
TARGET_DIR = ROOT / "src" / "static" / "img" / "articles"

DB_PATH = ROOT / "backend" / "zdrowiefit.db"

# Mapowanie nazwy pliku source (bez rozszerzenia) -> slug artykułu w bazie
# UWAGA: Marek zapisał z podwójnym .png.png — obsługujemy też taki case (dotyka name basename'a).
HERO_MAP: dict[str, dict] = {
    "01-mikrobiom-hero": {
        "slug": "mikrobiom-os-jelita-mozg-depresja",
        "alt": "Sylwetka człowieka z podświetlonymi obszarami mózgu i jelit połączonymi linią — wizualizacja osi jelita-mózg",
    },
    "02-trening-silowy-hero": {
        "slug": "trening-silowy-antydepresant-metaanaliza",
        "alt": "Mężczyzna w średnim wieku trzyma kettlebell w domowej siłowni — codzienna praktyka treningu jako forma regulacji",
    },
    "03-glimfatyk-hero": {
        "slug": "uklad-glimfatyczny-sen-mozg",
        "alt": "Profil śpiącej osoby w niebieskim świetle nocy z subtelnym świetlnym strumieniem nad skronią — wizualizacja przepływu glimfatycznego",
    },
    "04-dieta-hero": {
        "slug": "dieta-mind-vs-srodziemnomorska-mozg",
        "alt": "Drewniany stół z produktami diety śródziemnomorskiej i MIND obok siebie — porównanie dwóch wzorców żywieniowych",
    },
    "05-polywagal-hero": {
        "slug": "polywagal-theory-nerw-bledny-emocje",
        "alt": "Szyja i obojczyk osoby z nałożoną schematyczną linią nerwu błędnego — anatomia wagusa w stylu vintage medical illustration",
    },
    "06-cold-exposure-hero": {
        "slug": "cold-exposure-zimne-prysznice-nauka",
        "alt": "Osoba zanurzona po pierś w lodowatej wodzie zimowego jeziora, widoczna para z oddechu — autentyczna ekspozycja na zimno",
    },
    "07-kortyzol-serce-hero": {
        "slug": "kortyzol-a-serce-stres-chroniczny",
        "alt": "Osoba siedząca w słabo oświetlonym biurze późno wieczorem, twarz oświetlona ekranem laptopa, postawa znamionująca chroniczny stres zawodowy",
    },
    "08-cztery-filary-hero": {
        "slug": "cztery-filary-odpornosci-psychicznej",
        "alt": "Cztery klasyczne kolumny w porannym świetle — bluszcz, kłosy zboża, opadająca chalk, uścisk dłoni — symbole snu, diety, ruchu i relacji",
    },
    "09-kawa-hero": {
        "slug": "kawa-a-zdrowie-metaanaliza-2024",
        "alt": "Filiżanka czarnej kawy obok rozłożonego artykułu naukowego z rozmytym tekstem — kawa i medycyna oparta na dowodach",
    },
    "10-audyt-hero": {
        "slug": "audyt-zdrowia-5-testow-z-domu",
        "alt": "Pięć narzędzi domowego audytu zdrowia ułożone na drewnianym biurku z góry: smartwatch z HRV, ciśnieniomierz, glukometr, kwestionariusz, miarka krawiecka",
    },
}

TARGET_W = 1200
TARGET_H = 675  # 16:9 (1200/675 = 1.778)
WEBP_QUALITY = 80
JPG_QUALITY = 85


def find_source_files() -> dict[str, Path]:
    """Znajdź wszystkie hero PNG/JPG/WebP, niezależnie od podwójnego rozszerzenia."""
    found: dict[str, Path] = {}
    for source_dir in SOURCE_CANDIDATES:
        if not source_dir.exists():
            continue
        for ext in ("*.png", "*.jpg", "*.jpeg", "*.webp", "*.png.png", "*.jpg.jpg"):
            for path in source_dir.glob(ext):
                # Wyłuskaj base name z dowolnego rozszerzenia (raz lub dwa razy)
                stem = path.name
                for _ in range(2):  # max 2 rounds — obsługuje .png.png
                    if "." in stem:
                        stem = stem.rsplit(".", 1)[0]
                    if stem in HERO_MAP:
                        break
                if stem in HERO_MAP and stem not in found:
                    found[stem] = path
    return found


def convert_one(src: Path, base_name: str, dry_run: bool) -> tuple[Path, Path, int, int]:
    """Konwertuje jeden plik do .webp + .jpg. Zwraca ścieżki + rozmiary w KB."""
    webp_path = TARGET_DIR / f"{base_name}.webp"
    jpg_path = TARGET_DIR / f"{base_name}.jpg"

    if dry_run:
        return webp_path, jpg_path, 0, 0

    img = Image.open(src)
    # Resize z zachowaniem proporcji do 1200x675 (cover, nie fit)
    src_w, src_h = img.size
    src_ratio = src_w / src_h
    target_ratio = TARGET_W / TARGET_H

    if src_ratio > target_ratio:
        # Źródło szersze niż 16:9 — przycinamy boki
        new_w = int(src_h * target_ratio)
        offset = (src_w - new_w) // 2
        img = img.crop((offset, 0, offset + new_w, src_h))
    elif src_ratio < target_ratio:
        # Źródło wyższe niż 16:9 — przycinamy górę/dół
        new_h = int(src_w / target_ratio)
        offset = (src_h - new_h) // 2
        img = img.crop((0, offset, src_w, offset + new_h))

    img = img.resize((TARGET_W, TARGET_H), Image.LANCZOS)

    # WebP
    img.save(webp_path, "webp", quality=WEBP_QUALITY, method=6)
    webp_kb = webp_path.stat().st_size // 1024

    # JPG fallback
    img.convert("RGB").save(jpg_path, "jpeg", quality=JPG_QUALITY, optimize=True)
    jpg_kb = jpg_path.stat().st_size // 1024

    return webp_path, jpg_path, webp_kb, jpg_kb


def update_db(slug: str, image_url: str, image_alt: str, dry_run: bool) -> bool:
    if dry_run:
        return True
    if not DB_PATH.exists():
        print(f"[ERR] Brak bazy {DB_PATH}", file=sys.stderr)
        return False

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    # Sprawdź czy artykuł istnieje
    row = cur.execute("SELECT id FROM articles WHERE slug=?", (slug,)).fetchone()
    if not row:
        print(f"  [WARN] Artykuł '{slug}' nie istnieje w bazie — pomijam UPDATE")
        conn.close()
        return False

    # Aktualizuj image_url i image_alt (jeśli kolumna istnieje)
    cols = {r[1] for r in cur.execute("PRAGMA table_info(articles)").fetchall()}
    sets = ["image_url=?"]
    params: list = [image_url]
    if "image_alt" in cols:
        sets.append("image_alt=?")
        params.append(image_alt)
    if "updated_at" in cols:
        sets.append("updated_at=?")
        params.append(datetime.utcnow().isoformat())

    params.append(slug)
    cur.execute(f"UPDATE articles SET {', '.join(sets)} WHERE slug=?", params)
    conn.commit()
    conn.close()
    return True


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--dry-run", action="store_true", help="Symulacja, bez zapisu")
    p.add_argument("--skip-convert", action="store_true", help="Pomiń konwersję, tylko update bazy (jeśli .webp już istnieją)")
    args = p.parse_args()

    if not args.dry_run:
        TARGET_DIR.mkdir(parents=True, exist_ok=True)

    found = find_source_files()
    print(f"\nZnaleziono {len(found)}/{len(HERO_MAP)} plików źródłowych:\n")
    for base, src in sorted(found.items()):
        print(f"  ✓ {base} <- {src.name} ({src.stat().st_size // 1024} KB)")

    missing = sorted(set(HERO_MAP.keys()) - set(found.keys()))
    if missing:
        print(f"\n[WARN] Brakuje {len(missing)} plików:")
        for base in missing:
            print(f"  ✗ {base}.png  (slug: {HERO_MAP[base]['slug']})")
        print("\nMożesz kontynuować — istniejące zostaną przetworzone, brakujące pominięte.\n")

    print("─" * 64)
    total_webp_kb = 0
    total_jpg_kb = 0
    processed = 0
    db_updated = 0

    for base in sorted(found.keys()):
        src = found[base]
        meta = HERO_MAP[base]
        slug = meta["slug"]
        alt = meta["alt"]

        print(f"\n[{base}]")

        # Konwersja
        if args.skip_convert:
            webp_path = TARGET_DIR / f"{base}.webp"
            jpg_path = TARGET_DIR / f"{base}.jpg"
            if not webp_path.exists():
                print(f"  [SKIP] Brak {webp_path.name} — odpal bez --skip-convert")
                continue
            print(f"  [SKIP-CONV] {webp_path.name} już istnieje")
        else:
            webp_path, jpg_path, webp_kb, jpg_kb = convert_one(src, base, args.dry_run)
            if args.dry_run:
                print(f"  [DRY] Konwersja -> {webp_path.name} + {jpg_path.name}")
            else:
                print(f"  [OK] WebP: {webp_kb} KB | JPG: {jpg_kb} KB")
                total_webp_kb += webp_kb
                total_jpg_kb += jpg_kb
            processed += 1

        # Update bazy: image_url wskazuje na ścieżkę publiczną serwowaną przez build.py.
        # build.py:copy_static kopiuje src/static/img/articles/X -> output/img/articles/X
        # (bez prefixu /static/), więc URL publiczny to /img/articles/X.webp.
        public_url = f"/img/articles/{base}.webp"
        if update_db(slug, public_url, alt, args.dry_run):
            print(f"  [DB] image_url -> {public_url}")
            print(f"       slug      -> {slug}")
            db_updated += 1
        else:
            if args.dry_run:
                print(f"  [DRY-DB] image_url -> {public_url} (slug: {slug})")
                db_updated += 1

    print("\n" + "─" * 64)
    print(f"\nPodsumowanie:")
    print(f"  Przetworzonych:  {processed}/{len(HERO_MAP)}")
    print(f"  Update DB:       {db_updated}")
    if not args.dry_run and not args.skip_convert and processed:
        print(f"  Łączny rozmiar WebP: {total_webp_kb} KB ({total_webp_kb/1024:.1f} MB)")
        print(f"  Łączny rozmiar JPG:  {total_jpg_kb} KB ({total_jpg_kb/1024:.1f} MB)")
    if missing:
        print(f"\n  [BRAKUJE]: {', '.join(missing)}")

    if not args.dry_run and processed:
        print(f"\nNastępny krok:")
        print(f"  python build.py --domain zdrowie.fit --clean")
        print(f"  → wpięte hero zdjęcia pojawią się w cards i article pages")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
