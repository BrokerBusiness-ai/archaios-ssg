"""
Podpina ścieżki hero images w SQLite dla aidzisiaj.pl.
Dla każdego artykułu ustawia articles.image_url = /img/articles/<slug>-hero.webp
o ile plik fizycznie istnieje w src/static/img/articles/.

Użycie:
    python update_hero_images.py
    python update_hero_images.py --domain aidzisiaj-pl
    python update_hero_images.py --dry-run
"""
import sqlite3
import argparse
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).parent.parent
DB = ROOT / "backend" / "zdrowiefit.db"
IMG_DIR = ROOT / "src" / "static" / "img" / "articles"

parser = argparse.ArgumentParser()
parser.add_argument("--domain", default="aidzisiaj-pl")
parser.add_argument("--dry-run", action="store_true")
args = parser.parse_args()

if not DB.exists():
    raise SystemExit(f"Brak bazy: {DB}")
if not IMG_DIR.exists():
    raise SystemExit(f"Brak katalogu obrazów: {IMG_DIR}")

# Lista slugów dla domeny
DOMAIN_DIR = ROOT / "content_generated" / args.domain
if not DOMAIN_DIR.exists():
    raise SystemExit(f"Brak content folder: {DOMAIN_DIR}")

slugs = []
for md in sorted(DOMAIN_DIR.glob("*.md")):
    if md.name.startswith("_"):
        continue
    # parsuj YAML frontmatter ręcznie (bez zależności)
    text = md.read_text(encoding="utf-8")
    if not text.startswith("---"):
        continue
    end = text.find("---", 3)
    if end == -1:
        continue
    fm = text[3:end]
    for line in fm.splitlines():
        if line.strip().startswith("slug:"):
            slug = line.split(":", 1)[1].strip().strip('"').strip("'")
            slugs.append(slug)
            break

print(f"📦 Znaleziono {len(slugs)} slugów w {args.domain}/")

conn = sqlite3.connect(str(DB))
conn.row_factory = sqlite3.Row
cur = conn.cursor()

updated = 0
skipped_no_file = 0
skipped_no_article = 0
now = datetime.utcnow().isoformat()

for slug in slugs:
    webp_path = IMG_DIR / f"{slug}-hero.webp"
    if not webp_path.exists():
        print(f"  ⚠ BRAK pliku: {webp_path.name}")
        skipped_no_file += 1
        continue

    # sprawdź czy artykuł istnieje
    row = cur.execute("SELECT id, image_url FROM articles WHERE slug = ?", (slug,)).fetchone()
    if not row:
        print(f"  ⚠ BRAK artykułu w bazie: {slug}")
        skipped_no_article += 1
        continue

    new_url = f"/img/articles/{slug}-hero.webp"
    if row["image_url"] == new_url:
        print(f"  = bez zmian: {slug}")
        continue

    if args.dry_run:
        print(f"  [DRY] UPDATE {slug}: {row['image_url']} → {new_url}")
    else:
        cur.execute(
            "UPDATE articles SET image_url = ?, updated_at = ? WHERE id = ?",
            (new_url, now, row["id"]),
        )
        print(f"  ✓ UPDATE: {slug} → {new_url}")
        updated += 1

conn.commit()
conn.close()

print(f"\n📊 Podsumowanie:")
print(f"  Zaktualizowano:        {updated}")
print(f"  Brak pliku webp:       {skipped_no_file}")
print(f"  Brak artykułu w bazie: {skipped_no_article}")
print(f"  Wszystkie slugi:       {len(slugs)}")
