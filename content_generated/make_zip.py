"""
Pakuje zestaw artykułów + design dla domeny do pliku ZIP.

Użycie:
    python make_zip.py zdrowie-fit             # paczka jednej domeny
    python make_zip.py --all                   # paczki dla wszystkich domen
    python make_zip.py zdrowie-fit psychosen-pl  # paczki kilku domen

Zip ląduje obok katalogów domen, np.:
    content_generated/zdrowie-fit.zip
"""
from __future__ import annotations

import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).parent

def make_zip(domain_dir: Path) -> None:
    if not domain_dir.is_dir():
        print(f"  SKIP brak katalogu: {domain_dir}")
        return
    zip_path = ROOT / f"{domain_dir.name}.zip"
    n_files = 0
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for p in sorted(domain_dir.rglob("*")):
            if p.is_file() and p.name != "Thumbs.db":
                zf.write(p, p.relative_to(ROOT))
                n_files += 1
    size_kb = zip_path.stat().st_size / 1024
    print(f"  OK {zip_path.name}: {n_files} plików, {size_kb:.1f} KB")

def main() -> None:
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(0)

    if "--all" in args:
        targets = [d for d in ROOT.iterdir() if d.is_dir() and not d.name.startswith("_")]
    else:
        targets = [ROOT / name for name in args]

    print(f"Pakowanie {len(targets)} domen...")
    for d in targets:
        make_zip(d)
    print("Gotowe.")

if __name__ == "__main__":
    main()
