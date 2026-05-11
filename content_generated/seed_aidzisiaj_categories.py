"""
Seed kategorii dla aidzisiaj.pl do bazy SQLite.
Uruchom RAZ przed import_articles.py aidzisiaj-pl.

Użycie:
    python seed_aidzisiaj_categories.py
"""
import sqlite3
from datetime import datetime
from pathlib import Path

DB = Path(__file__).parent / ".." / "backend" / "zdrowiefit.db"
DB = DB.resolve()

if not DB.exists():
    raise SystemExit(f"Brak bazy: {DB}")

CATEGORIES = [
    ("Strategia", "strategia",
     "Pillar i cornerstone dla zarządów: strategia AI, ROI, governance, ryzyka, audyt dojrzałości.",
     "🎯", "#00d9ff", 1),
    ("Use cases", "use-cases",
     "Use cases AI z udokumentowanym ROI: customer service, lead scoring, backoffice, produkcja, predictive maintenance.",
     "💡", "#a78bfa", 2),
    ("Wdrożenia", "wdrozenia",
     "Wdrożenia AI od zera do produkcji: planowanie, krok po kroku, błędy do uniknięcia.",
     "🚀", "#ff2d92", 3),
]

conn = sqlite3.connect(str(DB))
conn.row_factory = sqlite3.Row
cur = conn.cursor()

existing = {r["slug"] for r in cur.execute("SELECT slug FROM categories")}
now = datetime.utcnow().isoformat()
added = 0

for name, slug, desc, icon, color, order in CATEGORIES:
    if slug in existing:
        print(f"  SKIP istnieje: {slug}")
        continue
    cur.execute(
        """INSERT INTO categories (name, slug, description, icon, color, sort_order, created_at)
           VALUES (?, ?, ?, ?, ?, ?, ?)""",
        (name, slug, desc, icon, color, order, now),
    )
    print(f"  OK: {slug} ({name})")
    added += 1

conn.commit()
conn.close()
print(f"\nDodano {added}/{len(CATEGORIES)} kategorii. Baza: {DB}")
