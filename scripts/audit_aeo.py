#!/usr/bin/env python3
"""
audit_aeo.py — Audyt gotowości AEO/GEO wygenerowanej strony.

Sprawdza output domeny pod kątem:
  1. Pliki AI: llms.txt, llms-full.txt
  2. robots.txt: dostęp AI crawlerów
  3. JSON-LD Schema: walidacja struktury
  4. Sitemap: kompletność
  5. WCAG: kolory domeny
  6. Bezpieczeństwo: .htaccess
  7. PWA: sw.js, manifest.json
  8. Fonty: self-hosted (brak Google Fonts)

Użycie:
    python scripts/audit_aeo.py                      # domyślnie output/zdrowie-fit/
    python scripts/audit_aeo.py --domain zdrowie.fit
    python scripts/audit_aeo.py --output output/psycho-edu-pl/
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Dodaj root do path, żeby importować domain_config
sys.path.insert(0, str(ROOT))

REQUIRED_AI_BOTS = [
    "GPTBot", "ChatGPT-User", "Claude-Web", "PerplexityBot",
    "Amazonbot", "Google-Extended", "CCBot",
]

REQUIRED_SCHEMA_TYPES = [
    "WebSite", "Organization", "Article", "BreadcrumbList", "Person",
]

OPTIONAL_SCHEMA_TYPES = [
    "FAQPage", "HowTo", "Review", "ClaimReview", "SpeakableSpecification",
]


def _find_output(domain: str | None, output_path: str | None) -> Path:
    if output_path:
        return Path(output_path)
    if domain:
        slug = domain.replace(".", "-")
        return ROOT / "output" / slug
    # Szukaj pierwszego istniejącego outputu
    output_dir = ROOT / "output"
    if output_dir.exists():
        for d in sorted(output_dir.iterdir()):
            if d.is_dir() and not d.name.startswith("."):
                return d
    return ROOT / "output" / "zdrowie-fit"


def check_file_exists(path: Path, name: str) -> tuple[bool, str]:
    if path.exists():
        size = path.stat().st_size
        return True, f"✅ {name} ({size:,} bajtów)"
    return False, f"❌ {name} — BRAK"


def audit_llms(out: Path) -> list[str]:
    results = []
    results.append("\n📄 1. PLIKI AI (llms.txt)")
    results.append("─" * 40)

    ok1, msg1 = check_file_exists(out / "llms.txt", "llms.txt")
    results.append(msg1)
    if ok1:
        content = (out / "llms.txt").read_text(encoding="utf-8")
        lines = content.strip().splitlines()
        results.append(f"   → {len(lines)} linii")
        if "# Articles" in content or "# Artykuły" in content or "articles" in content.lower():
            results.append("   → Sekcja artykułów: ✅")
        else:
            results.append("   → Sekcja artykułów: ❌ brak")

    ok2, msg2 = check_file_exists(out / "llms-full.txt", "llms-full.txt")
    results.append(msg2)
    if ok2:
        content = (out / "llms-full.txt").read_text(encoding="utf-8")
        word_count = len(content.split())
        results.append(f"   → ~{word_count:,} słów (pełna treść)")

    return results


def audit_robots(out: Path) -> list[str]:
    results = []
    results.append("\n🤖 2. ROBOTS.TXT — AI CRAWLERS")
    results.append("─" * 40)

    path = out / "robots.txt"
    ok, msg = check_file_exists(path, "robots.txt")
    results.append(msg)
    if not ok:
        return results

    content = path.read_text(encoding="utf-8")

    for bot in REQUIRED_AI_BOTS:
        if bot.lower() in content.lower():
            # Sprawdź czy Allow
            pattern = re.compile(
                rf"User-agent:\s*{re.escape(bot)}.*?(?:Allow|Disallow)",
                re.IGNORECASE | re.DOTALL
            )
            match = pattern.search(content)
            if match and "disallow: /" not in match.group().lower().replace("disallow: /data", ""):
                results.append(f"   ✅ {bot} — dozwolony")
            else:
                results.append(f"   ⚠️  {bot} — wymieniony, sprawdź reguły")
        else:
            results.append(f"   ❌ {bot} — nie wymieniony")

    if "sitemap:" in content.lower():
        results.append("   ✅ Sitemap zadeklarowany")
    else:
        results.append("   ❌ Sitemap niezadeklarowany")

    if "llms.txt" in content or "llms-full.txt" in content:
        results.append("   ✅ Odniesienie do llms.txt")
    else:
        results.append("   ⚠️  Brak odniesienia do llms.txt")

    return results


def audit_schema(out: Path) -> list[str]:
    results = []
    results.append("\n🏷️  3. SCHEMA MARKUP (JSON-LD)")
    results.append("─" * 40)

    # Zbierz wszystkie JSON-LD z HTML
    all_types: set[str] = set()
    html_files = list(out.rglob("*.html"))
    results.append(f"   Plików HTML: {len(html_files)}")

    schema_pattern = re.compile(
        r'<script\s+type=["\']application/ld\+json["\']>(.*?)</script>',
        re.DOTALL | re.IGNORECASE
    )

    errors = 0
    for html_file in html_files:
        content = html_file.read_text(encoding="utf-8", errors="ignore")
        for match in schema_pattern.findall(content):
            try:
                data = json.loads(match)
                # Zbierz typy
                if isinstance(data, dict):
                    if "@type" in data:
                        all_types.add(data["@type"])
                    if "@graph" in data:
                        for item in data["@graph"]:
                            if isinstance(item, dict) and "@type" in item:
                                all_types.add(item["@type"])
            except json.JSONDecodeError:
                errors += 1
                rel = html_file.relative_to(out)
                results.append(f"   ❌ Błąd JSON-LD w {rel}")

    if errors == 0:
        results.append(f"   ✅ Wszystkie JSON-LD poprawne składniowo")

    results.append(f"   Znalezione typy: {', '.join(sorted(all_types)) or '(brak)'}")

    for st in REQUIRED_SCHEMA_TYPES:
        if st in all_types:
            results.append(f"   ✅ {st}")
        else:
            results.append(f"   ❌ {st} — BRAK (wymagany)")

    for st in OPTIONAL_SCHEMA_TYPES:
        if st in all_types:
            results.append(f"   ✅ {st} (opcjonalny)")
        else:
            results.append(f"   ℹ️  {st} — brak (opcjonalny, pojawi się gdy artykuły mają odpowiedni content)")

    return results


def audit_sitemap(out: Path) -> list[str]:
    results = []
    results.append("\n🗺️  4. SITEMAP")
    results.append("─" * 40)

    path = out / "sitemap.xml"
    ok, msg = check_file_exists(path, "sitemap.xml")
    results.append(msg)
    if not ok:
        return results

    content = path.read_text(encoding="utf-8")
    url_count = content.count("<url>") or content.count("<loc>")
    results.append(f"   → {url_count} URL-i")

    if "image:" in content or "image:loc" in content:
        results.append("   ✅ Image namespace (obrazki w sitemap)")
    else:
        results.append("   ❌ Brak image namespace")

    if "<lastmod>" in content:
        results.append("   ✅ lastmod timestamps")
    else:
        results.append("   ⚠️  Brak lastmod")

    if "<changefreq>" in content:
        results.append("   ✅ changefreq")

    if "<priority>" in content:
        results.append("   ✅ priority")

    return results


def audit_security(out: Path) -> list[str]:
    results = []
    results.append("\n🔒 5. BEZPIECZEŃSTWO")
    results.append("─" * 40)

    path = out / ".htaccess"
    ok, msg = check_file_exists(path, ".htaccess")
    results.append(msg)
    if not ok:
        return results

    content = path.read_text(encoding="utf-8")

    checks = [
        ("X-Content-Type-Options", "nosniff"),
        ("X-Frame-Options", "SAMEORIGIN"),
        ("Strict-Transport-Security", "HSTS"),
        ("Content-Security-Policy", "CSP"),
        ("Referrer-Policy", "Referrer-Policy"),
        ("Permissions-Policy", "Permissions-Policy"),
    ]

    for header, label in checks:
        if header.lower() in content.lower():
            results.append(f"   ✅ {label}")
        else:
            results.append(f"   ❌ {label} — BRAK")

    if "mod_deflate" in content or "AddOutputFilterByType" in content:
        results.append("   ✅ Kompresja GZIP/Deflate")
    else:
        results.append("   ❌ Brak kompresji")

    if "ExpiresByType" in content or "max-age" in content:
        results.append("   ✅ Cache headers")
    else:
        results.append("   ❌ Brak cache headers")

    return results


def audit_pwa(out: Path) -> list[str]:
    results = []
    results.append("\n📱 6. PWA / OFFLINE")
    results.append("─" * 40)

    ok1, msg1 = check_file_exists(out / "sw.js", "sw.js (Service Worker)")
    results.append(msg1)

    ok2, msg2 = check_file_exists(out / "manifest.json", "manifest.json")
    results.append(msg2)

    return results


def audit_fonts(out: Path) -> list[str]:
    results = []
    results.append("\n🔤 7. FONTY (self-hosted)")
    results.append("─" * 40)

    fonts_dir = out / "fonts"
    if fonts_dir.exists():
        woff2_files = list(fonts_dir.glob("*.woff2"))
        results.append(f"   ✅ {len(woff2_files)} plików woff2 w /fonts/")
        total = sum(f.stat().st_size for f in woff2_files)
        results.append(f"   → Łączny rozmiar: {total // 1024} KB")
    else:
        results.append("   ❌ Brak katalogu /fonts/ — uruchom scripts/download_fonts.py")

    # Sprawdź czy HTML nie odwołuje się do Google Fonts
    for html in (out.rglob("*.html")):
        content = html.read_text(encoding="utf-8", errors="ignore")
        if "fonts.googleapis.com" in content:
            results.append(f"   ❌ Google Fonts w {html.relative_to(out)}")
            break
    else:
        results.append("   ✅ Zero requestów do Google Fonts")

    return results


def audit_wcag(domain: str | None) -> list[str]:
    results = []
    results.append("\n🎨 8. WCAG KOLORY")
    results.append("─" * 40)

    if not domain:
        results.append("   ℹ️  Podaj --domain żeby sprawdzić kolory WCAG")
        return results

    try:
        from domain_config import load_domain_config, validate_domain_colors
        cfg = load_domain_config(domain)
        colors = cfg["colors"]
        issues = validate_domain_colors(colors)
        if issues:
            for issue in issues:
                results.append(f"   {issue}")
        else:
            results.append("   ✅ Wszystkie kolory spełniają WCAG AA/AAA")
    except Exception as e:
        results.append(f"   ⚠️  Nie udało się sprawdzić: {e}")

    return results


def audit_content_quality(out: Path) -> list[str]:
    results = []
    results.append("\n📝 9. JAKOŚĆ TREŚCI (AEO)")
    results.append("─" * 40)

    html_files = list(out.rglob("*.html"))
    articles = [f for f in html_files if "artykul" in str(f).lower() or f.parent.name == out.name]

    question_headings = 0
    with_bibliography = 0
    with_author = 0
    with_og_image = 0

    for html_file in html_files:
        content = html_file.read_text(encoding="utf-8", errors="ignore")

        # Nagłówki jako pytania
        q_h = re.findall(r'<h[23][^>]*>.*?\?</h[23]>', content, re.DOTALL)
        question_headings += len(q_h)

        # Bibliografia
        if 'role="doc-bibliography"' in content or "bibliography" in content.lower():
            with_bibliography += 1

        # Autor
        if 'itemprop="author"' in content:
            with_author += 1

        # OG image
        if 'og:image' in content:
            with_og_image += 1

    results.append(f"   Nagłówki-pytania (FAQ): {question_headings}")
    results.append(f"   Strony z bibliografią: {with_bibliography}")
    results.append(f"   Strony z autorem: {with_author}")
    results.append(f"   Strony z OG image: {with_og_image}")

    # Sprawdź data-nosnippet na CTA
    cta_nosnippet = 0
    for html_file in html_files:
        content = html_file.read_text(encoding="utf-8", errors="ignore")
        if "data-nosnippet" in content:
            cta_nosnippet += 1
    results.append(f"   Strony z data-nosnippet (CTA): {cta_nosnippet}")

    return results


def main():
    parser = argparse.ArgumentParser(description="Audyt AEO/GEO strony")
    parser.add_argument("--domain", help="Domena (np. zdrowie.fit)")
    parser.add_argument("--output", help="Ścieżka do katalogu output")
    args = parser.parse_args()

    out = _find_output(args.domain, args.output)

    print("=" * 50)
    print("  ARCHAIOS SSG — AUDYT AEO/GEO")
    print("=" * 50)
    print(f"  Output: {out}")

    if not out.exists():
        print(f"\n❌ Katalog {out} nie istnieje.")
        print("   Uruchom najpierw: python build.py --domain <domena> --clean")
        sys.exit(1)

    all_results: list[str] = []
    all_results.extend(audit_llms(out))
    all_results.extend(audit_robots(out))
    all_results.extend(audit_schema(out))
    all_results.extend(audit_sitemap(out))
    all_results.extend(audit_security(out))
    all_results.extend(audit_pwa(out))
    all_results.extend(audit_fonts(out))
    all_results.extend(audit_wcag(args.domain))
    all_results.extend(audit_content_quality(out))

    for line in all_results:
        print(line)

    # Podsumowanie
    done = sum(1 for r in all_results if "✅" in r)
    fail = sum(1 for r in all_results if "❌" in r)
    warn = sum(1 for r in all_results if "⚠️" in r)

    print("\n" + "=" * 50)
    print(f"  WYNIK: {done} ✅  |  {fail} ❌  |  {warn} ⚠️")
    score = int(done / max(done + fail, 1) * 100)
    print(f"  SCORE AEO: {score}%")
    print("=" * 50)

    return 0 if fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
