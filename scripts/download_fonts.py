#!/usr/bin/env python3
"""
Pobiera woff2 fontów Inter + Fraunces z google-webfonts-helper.
Uruchom raz, potem fonty są serwowane lokalnie.

Użycie:
    python scripts/download_fonts.py
"""

import os
import sys
from pathlib import Path

try:
    import httpx
except ImportError:
    print("pip install httpx")
    sys.exit(1)

FONTS_DIR = Path(__file__).resolve().parent.parent / "src" / "static" / "fonts"
FONTS_DIR.mkdir(parents=True, exist_ok=True)

# Google Fonts direct woff2 URLs (latin-ext subset)
FONT_URLS = {
    # Inter
    "inter-v18-latin-ext-300.woff2": "https://fonts.gstatic.com/s/inter/v18/UcCO3FwrK3iLTeHuS_nVMrMxCp50SjIw2boKoduKmMEVuOKfAZBhiI2B.woff2",
    "inter-v18-latin-ext-regular.woff2": "https://fonts.gstatic.com/s/inter/v18/UcCO3FwrK3iLTeHuS_nVMrMxCp50SjIw2boKoduKmMEVuLyfAZBhiI2B.woff2",
    "inter-v18-latin-ext-500.woff2": "https://fonts.gstatic.com/s/inter/v18/UcCO3FwrK3iLTeHuS_nVMrMxCp50SjIw2boKoduKmMEVuI6fAZBhiI2B.woff2",
    "inter-v18-latin-ext-600.woff2": "https://fonts.gstatic.com/s/inter/v18/UcCO3FwrK3iLTeHuS_nVMrMxCp50SjIw2boKoduKmMEVuGKYAZBhiI2B.woff2",
    "inter-v18-latin-ext-700.woff2": "https://fonts.gstatic.com/s/inter/v18/UcCO3FwrK3iLTeHuS_nVMrMxCp50SjIw2boKoduKmMEVuFuYAZBhiI2B.woff2",
    "inter-v18-latin-ext-800.woff2": "https://fonts.gstatic.com/s/inter/v18/UcCO3FwrK3iLTeHuS_nVMrMxCp50SjIw2boKoduKmMEVuDyYAZBhiI2B.woff2",
    # Fraunces v38 (URLs obtained from gwfh.mranftl.com — update if 404s return)
    "fraunces-v38-latin-ext-regular.woff2": "https://fonts.gstatic.com/s/fraunces/v38/6NUh8FyLNQOQZAnv9bYEvDiIdE9Ea92uemAk_WBq8U_9v0c2Wa0K7iN7hzFUPJH58nib1603gg7S2nfgRYIctxuTB_7T.woff2",
    "fraunces-v38-latin-ext-500.woff2": "https://fonts.gstatic.com/s/fraunces/v38/6NUh8FyLNQOQZAnv9bYEvDiIdE9Ea92uemAk_WBq8U_9v0c2Wa0K7iN7hzFUPJH58nib1603gg7S2nfgRYIchRuTB_7T.woff2",
    "fraunces-v38-latin-ext-600.woff2": "https://fonts.gstatic.com/s/fraunces/v38/6NUh8FyLNQOQZAnv9bYEvDiIdE9Ea92uemAk_WBq8U_9v0c2Wa0K7iN7hzFUPJH58nib1603gg7S2nfgRYIcaRyTB_7T.woff2",
    "fraunces-v38-latin-ext-700.woff2": "https://fonts.gstatic.com/s/fraunces/v38/6NUh8FyLNQOQZAnv9bYEvDiIdE9Ea92uemAk_WBq8U_9v0c2Wa0K7iN7hzFUPJH58nib1603gg7S2nfgRYIcUByTB_7T.woff2",
}


def main():
    print(f"Pobieranie fontów do {FONTS_DIR}\n")
    client = httpx.Client(
        headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"},
        follow_redirects=True,
        timeout=30.0,
    )
    for filename, url in FONT_URLS.items():
        dest = FONTS_DIR / filename
        if dest.exists():
            print(f"  ✓ {filename} (already exists, {dest.stat().st_size // 1024}KB)")
            continue
        print(f"  ↓ {filename}...", end=" ", flush=True)
        try:
            r = client.get(url)
            r.raise_for_status()
            dest.write_bytes(r.content)
            print(f"OK ({len(r.content) // 1024}KB)")
        except Exception as e:
            print(f"FAILED: {e}")

    client.close()
    total = sum(f.stat().st_size for f in FONTS_DIR.glob("*.woff2"))
    print(f"\nGotowe. Łączny rozmiar fontów: {total // 1024}KB")
    print("Fonty będą serwowane z /fonts/ — zero external requests.")


if __name__ == "__main__":
    main()
