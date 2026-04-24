#!/usr/bin/env python3
"""
backup_db.py — codzienny backup SQLite (uruchamiaj przez cron na Cyber_Folks lub Task Scheduler)

Użycie:
    python scripts/backup_db.py                    # backup do backups/
    python scripts/backup_db.py --keep-days 30     # zachowaj 30 dni

Cron na Cyber_Folks (codziennie o 3:00):
    0 3 * * * cd /home/USER/domains/zdrowie.fit/app && python3 scripts/backup_db.py >> backups/backup.log 2>&1

Task Scheduler na Windows:
    schtasks /create /tn "ZdrowieFit Backup" /tr "python C:\\MEV-1\\zdrowie-fit-generator\\scripts\\backup_db.py" /sc DAILY /st 03:00
"""

import argparse
import gzip
import shutil
import sys
from datetime import datetime, timedelta
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "backend" / "zdrowiefit.db"
BACKUP_DIR = ROOT / "backups"
UPLOADS_DIR = ROOT / "backend" / "uploads"


def backup_db(keep_days: int = 30):
    BACKUP_DIR.mkdir(exist_ok=True)
    if not DB_PATH.exists():
        print(f"❌ Baza nie istnieje: {DB_PATH}")
        return 1

    ts = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    out_file = BACKUP_DIR / f"zdrowiefit-{ts}.db.gz"

    # Kompresuj (~5-10x mniejsze)
    with open(DB_PATH, "rb") as fin, gzip.open(out_file, "wb", compresslevel=9) as fout:
        shutil.copyfileobj(fin, fout)

    size_kb = out_file.stat().st_size // 1024
    print(f"✅ Backup: {out_file.name} ({size_kb} KB)")

    # Usuń stare
    cutoff = datetime.now() - timedelta(days=keep_days)
    removed = 0
    for old in BACKUP_DIR.glob("zdrowiefit-*.db.gz"):
        try:
            file_date_str = old.stem.replace(".db", "").replace("zdrowiefit-", "")[:10]
            file_date = datetime.strptime(file_date_str, "%Y-%m-%d")
            if file_date < cutoff:
                old.unlink()
                removed += 1
        except (ValueError, OSError):
            pass
    if removed:
        print(f"🧹 Usunięto {removed} starych backupów (>{keep_days} dni)")

    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--keep-days", type=int, default=30, help="Ile dni trzymać backupy (default: 30)")
    args = ap.parse_args()
    sys.exit(backup_db(keep_days=args.keep_days))


if __name__ == "__main__":
    main()
