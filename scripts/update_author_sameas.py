#!/usr/bin/env python3
"""
update_author_sameas.py — wstawia URL-e sameAs autora do bazy authors.

Strategia (bez migracji schemy):
  - website  = primary URL autora (https://marekporycki.pl)
  - linkedin = LinkedIn URL (daj mi gdy będziesz miał)
  - twitter  = X/Twitter URL ALBO psychozdrowie.online (drugi serwis autora)

Author template (author.html) używa wszystkich trzech pól w sameAs JSON-LD,
więc każde wypełnione pole = jeden URL w schema.org Person.sameAs.

UWAGA: 'twitter' field jest semantycznie mylące dla psychozdrowie.online,
ale technicznie działa — Google/AI patrzą na sameAs jako listę URL-i,
nie sprawdzają czy każdy slot jest "tym czym się nazywa".

Użycie:
    python scripts/update_author_sameas.py
    python scripts/update_author_sameas.py --linkedin https://linkedin.com/in/marek-porycki
"""
from __future__ import annotations

import argparse
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DB = ROOT / "backend" / "zdrowiefit.db"

DEFAULTS = {
    "website": "https://marekporycki.pl",
    "twitter": "https://psychozdrowie.online",  # 2-gi serwis Marka
    "linkedin": "",                              # uzupełnij --linkedin URL
}


def main() -> int:
    ap = argparse.ArgumentParser(description="Update author sameAs URLs in sqlite.")
    ap.add_argument("--author-name", default="Marek Porycki",
                    help="Nazwa autora (LIKE match, default: 'Marek Porycki')")
    ap.add_argument("--db", default=str(DB), help=f"Ścieżka do bazy (default: {DB})")
    ap.add_argument("--website", default=DEFAULTS["website"])
    ap.add_argument("--linkedin", default=DEFAULTS["linkedin"])
    ap.add_argument("--twitter", default=DEFAULTS["twitter"])
    ap.add_argument("--dry-run", action="store_true", help="Tylko pokaż co by zaktualizował")
    args = ap.parse_args()

    db_path = Path(args.db)
    if not db_path.exists():
        print(f"❌ Baza nie istnieje: {db_path}")
        return 1

    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row

    # Pokaż obecny stan
    print(f"📂 Baza: {db_path}")
    print(f"🔍 Szukam autora: {args.author_name!r}\n")

    cur = conn.execute(
        "SELECT id, name, slug, website, linkedin, twitter FROM authors WHERE name LIKE ?",
        (f"%{args.author_name}%",),
    )
    rows = list(cur)
    if not rows:
        print(f"❌ Nie znaleziono autora: {args.author_name}")
        # Pokaż wszystkich autorów dla orientacji
        print("\nDostępni autorzy:")
        for r in conn.execute("SELECT id, name, slug FROM authors"):
            print(f"   {r['id']}: {r['name']} ({r['slug']})")
        return 1

    for r in rows:
        print(f"📄 Autor #{r['id']}: {r['name']} ({r['slug']})")
        print(f"   PRZED:  website={r['website']!r}")
        print(f"           linkedin={r['linkedin']!r}")
        print(f"           twitter={r['twitter']!r}")
        print(f"   PO:     website={args.website!r}")
        print(f"           linkedin={args.linkedin!r}")
        print(f"           twitter={args.twitter!r}")

    if args.dry_run:
        print("\n🔍 DRY RUN — nic nie zaktualizowane. Usuń --dry-run żeby zapisać.")
        return 0

    # Update
    conn.execute(
        "UPDATE authors SET website = ?, linkedin = ?, twitter = ? "
        "WHERE name LIKE ?",
        (args.website, args.linkedin, args.twitter, f"%{args.author_name}%"),
    )
    conn.commit()
    print(f"\n✅ Zaktualizowano {len(rows)} autora(ów).")
    print(f"   Po następnym build (python build.py --domain zdrowie.fit --clean):")
    print(f"   - Person.sameAs będzie zawierać {sum(1 for v in [args.website, args.linkedin, args.twitter] if v)} URL-i")
    print(f"   - Walidator: warning 'Person sameAs' zniknie")

    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
