#!/usr/bin/env python3
"""
domain_config.py — Loader konfiguracji domen satelitarnych.

Wczytuje YAML z katalogu domains/ i zwraca dict gotowy do użycia
przez build.py jako CONFIG + kontekst Jinja2.

Użycie:
    from domain_config import load_domain_config, list_domains
    cfg = load_domain_config("testnis2.pl")
    all_domains = list_domains()
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any

import yaml


DOMAINS_DIR = Path(__file__).resolve().parent / "domains"


def _find_config_file(domain: str) -> Path:
    """Szuka pliku YAML dla domeny — próbuje różne konwencje nazewnictwa."""
    # Bezpośrednie mapowanie: domena → slug pliku
    slug = domain.replace(".", "-").replace("_", "-")
    candidates = [
        DOMAINS_DIR / f"{slug}.yaml",
        DOMAINS_DIR / f"{slug}.yml",
        DOMAINS_DIR / f"{domain}.yaml",
        DOMAINS_DIR / f"{domain}.yml",
    ]
    for path in candidates:
        if path.exists():
            return path

    # Fallback: przeszukaj wszystkie pliki i dopasuj po polu 'domain'
    for path in DOMAINS_DIR.glob("*.yaml"):
        if path.name.startswith("_"):
            continue
        try:
            with open(path, encoding="utf-8") as f:
                data = yaml.safe_load(f)
            if isinstance(data, dict) and data.get("domain") == domain:
                return path
        except Exception:
            continue

    raise FileNotFoundError(
        f"Brak konfiguracji dla domeny '{domain}' w {DOMAINS_DIR}.\n"
        f"Sprawdzone pliki: {[c.name for c in candidates]}\n"
        f"Dostępne domeny: {', '.join(list_domains())}"
    )


def load_domain_config(domain: str) -> dict[str, Any]:
    """Wczytuje konfigurację domeny i zwraca dict kompatybilny z build.py CONFIG."""
    path = _find_config_file(domain)
    with open(path, encoding="utf-8") as f:
        raw = yaml.safe_load(f)

    if not isinstance(raw, dict):
        raise ValueError(f"Nieprawidłowy format konfiguracji w {path}")

    # Uzupełnij brakujące wartości domyślnymi
    raw.setdefault("lang", "pl")
    raw.setdefault("locale", "pl_PL")
    raw.setdefault("role", "satellite")
    raw.setdefault("funnel_type", "article_cta")
    raw.setdefault("email", f"kontakt@{raw['domain']}")
    raw.setdefault("social", {})
    raw.setdefault("analytics", {})
    raw.setdefault("newsletter", {})
    raw.setdefault("pillars", [])
    raw.setdefault("categories", [])
    raw.setdefault("products", [])
    raw.setdefault("about", {})
    raw.setdefault("hero", {})
    raw.setdefault("footer", {})
    raw.setdefault("colors", {})
    raw.setdefault("theme", {})

    url = f"https://{raw['domain']}"

    # Buduj CONFIG w formacie build.py
    config = {
        "site": {
            "url": url,
            "name": raw.get("name", raw["domain"]),
            "tagline": raw.get("tagline", ""),
            "description": raw.get("description", ""),
            "author": raw.get("name", raw["domain"]),
            "lang": raw["lang"],
            "locale": raw["locale"],
            "fb": raw["social"].get("fb", ""),
            "ig": raw["social"].get("ig", ""),
            "yt": raw["social"].get("yt", ""),
            "tw": raw["social"].get("tw", ""),
            "email": raw["email"],
            # Dodatkowe pola per domena
            "brand": raw.get("brand", ""),
            "main_domain": raw.get("main_domain", ""),
            "role": raw["role"],
            "funnel_type": raw["funnel_type"],
            "logo_mark": raw.get("logo_mark", "◐"),
            "logo_text": raw.get("logo_text", raw.get("name", "")),
            "logo_accent": raw.get("logo_accent", ""),
        },
        "analytics": {
            "ga4_id": raw["analytics"].get("ga4_id", os.environ.get("GA4_ID", "")),
            "fb_pixel_id": raw["analytics"].get("fb_pixel_id", os.environ.get("FB_PIXEL_ID", "")),
        },
        "newsletter": {
            "endpoint": raw["newsletter"].get("endpoint", os.environ.get("NEWSLETTER_ENDPOINT", "")),
            "provider": raw["newsletter"].get("provider", os.environ.get("NEWSLETTER_PROVIDER", "")),
            "title_highlight": raw["newsletter"].get("title_highlight", "cotygodniowy przegląd"),
            "title_rest": raw["newsletter"].get("title_rest", "nowości"),
            "subtitle": raw["newsletter"].get("subtitle", ""),
        },
        "colors": {
            "primary": raw["colors"].get("primary", "#4a7c59"),
            "primary_dark": raw["colors"].get("primary_dark", "#3a6347"),
            "primary_light": raw["colors"].get("primary_light", "#7fb3a3"),
            "accent": raw["colors"].get("accent", "#d9724a"),
            "accent_dark": raw["colors"].get("accent_dark", "#b85a38"),
            "trust": raw["colors"].get("trust", "#5b8def"),
        },
        "theme": raw["theme"],
        "hero": raw["hero"],
        "pillars": raw["pillars"],
        "categories": raw["categories"],
        "products": raw["products"],
        "about": raw["about"],
        "footer": raw["footer"],
        # Meta
        "_domain": raw["domain"],
        "_config_path": str(path),
        "_raw": raw,
    }

    return config


def list_domains() -> list[str]:
    """Zwraca listę wszystkich skonfigurowanych domen."""
    domains = []
    for path in sorted(DOMAINS_DIR.glob("*.yaml")):
        if path.name.startswith("_"):
            continue
        try:
            with open(path, encoding="utf-8") as f:
                data = yaml.safe_load(f)
            if isinstance(data, dict) and "domain" in data:
                domains.append(data["domain"])
        except Exception:
            continue
    return domains


def _hex_to_rgb(h: str) -> tuple[int, int, int]:
    h = h.lstrip("#")
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))


def _rgb_to_hex(r: int, g: int, b: int) -> str:
    return f"#{r:02x}{g:02x}{b:02x}"


def _relative_luminance(r: int, g: int, b: int) -> float:
    """WCAG 2.1 relative luminance. sRGB → linear."""
    def linearize(v: int) -> float:
        s = v / 255.0
        return s / 12.92 if s <= 0.04045 else ((s + 0.055) / 1.055) ** 2.4
    return 0.2126 * linearize(r) + 0.7152 * linearize(g) + 0.0722 * linearize(b)


def contrast_ratio(hex1: str, hex2: str) -> float:
    """WCAG contrast ratio between two hex colors."""
    l1 = _relative_luminance(*_hex_to_rgb(hex1))
    l2 = _relative_luminance(*_hex_to_rgb(hex2))
    lighter = max(l1, l2)
    darker = min(l1, l2)
    return (lighter + 0.05) / (darker + 0.05)


def wcag_level(hex_fg: str, hex_bg: str, font_size: str = "normal") -> str:
    """Zwraca 'AAA', 'AA', lub 'FAIL' dla pary kolorów."""
    cr = contrast_ratio(hex_fg, hex_bg)
    if font_size == "large":
        if cr >= 4.5: return "AAA"
        if cr >= 3.0: return "AA"
    else:
        if cr >= 7.0: return "AAA"
        if cr >= 4.5: return "AA"
    return "FAIL"


def _darken(hex_color: str, amount: float = 0.15) -> str:
    """Przyciemnia kolor o podany procent."""
    r, g, b = _hex_to_rgb(hex_color)
    return _rgb_to_hex(
        max(0, int(r * (1 - amount))),
        max(0, int(g * (1 - amount))),
        max(0, int(b * (1 - amount)))
    )


def _lighten(hex_color: str, amount: float = 0.3) -> str:
    """Rozjaśnia kolor o podany procent."""
    r, g, b = _hex_to_rgb(hex_color)
    return _rgb_to_hex(
        min(255, int(r + (255 - r) * amount)),
        min(255, int(g + (255 - g) * amount)),
        min(255, int(b + (255 - b) * amount))
    )


def auto_generate_palette(primary: str, accent: str = "", trust: str = "") -> dict:
    """Auto-generuje pełną paletę z primary color, z walidacją WCAG AA minimum."""
    if not accent:
        # Komplementarny accent: przesuń hue
        r, g, b = _hex_to_rgb(primary)
        accent = _rgb_to_hex(
            min(255, max(0, 255 - r + 40)),
            min(255, max(0, g - 20)),
            min(255, max(0, b - 30))
        )
    if not trust:
        trust = "#5b8def"

    palette = {
        "primary": primary,
        "primary_dark": _darken(primary, 0.20),
        "primary_light": _lighten(primary, 0.35),
        "accent": accent,
        "accent_dark": _darken(accent, 0.18),
        "accent_light": _lighten(accent, 0.30),
        "trust": trust,
        "trust_dark": _darken(trust, 0.15),
    }

    # Walidacja kontrastu na białym/ivory tle (#fdfcf9)
    bg = "#fdfcf9"
    bg_dark = "#1a1815"
    warnings = []
    for name, color in palette.items():
        if "light" in name:
            continue  # light variants nie muszą być czytelne na jasnym tle
        cr = contrast_ratio(color, bg)
        if cr < 4.5:
            # Auto-koryguj: przyciemnij aż do AA
            adjusted = color
            for _ in range(20):
                adjusted = _darken(adjusted, 0.05)
                if contrast_ratio(adjusted, bg) >= 4.5:
                    break
            palette[name] = adjusted
            warnings.append(f"  ⚠ {name}: {color} → {adjusted} (contrast {cr:.1f} → {contrast_ratio(adjusted, bg):.1f})")

    if warnings:
        print("🎨 WCAG auto-korekta kolorów:")
        for w in warnings:
            print(w)

    return palette


def validate_domain_colors(colors: dict) -> list[str]:
    """Waliduje kolory domeny pod kątem WCAG AA/AAA. Zwraca listę problemów."""
    issues = []
    bg_light = "#fdfcf9"
    bg_dark = "#1a1815"

    checks = [
        ("primary na jasnym tle", colors.get("primary", ""), bg_light, "normal"),
        ("primary_dark na jasnym tle", colors.get("primary_dark", ""), bg_light, "normal"),
        ("accent na jasnym tle", colors.get("accent", ""), bg_light, "large"),
        ("trust na jasnym tle", colors.get("trust", ""), bg_light, "normal"),
        ("biały na primary (buttons)", "#ffffff", colors.get("primary", ""), "normal"),
        ("biały na accent (CTA)", "#ffffff", colors.get("accent", ""), "large"),
    ]

    for label, fg, bg, size in checks:
        if not fg or not bg:
            continue
        level = wcag_level(fg, bg, size)
        cr = contrast_ratio(fg, bg)
        if level == "FAIL":
            issues.append(f"❌ FAIL: {label} — contrast {cr:.1f}:1 (min 4.5:1)")
        elif level == "AA":
            issues.append(f"⚠️  AA: {label} — contrast {cr:.1f}:1 (AAA wymaga 7:1)")

    return issues


def get_css_variables(colors: dict[str, str]) -> str:
    """Generuje blok CSS variables override z kolorów domeny — z pełną semantyką."""
    # Auto-generuj brakujące kolory
    if colors.get("primary") and not colors.get("accent_light"):
        colors = auto_generate_palette(
            colors["primary"],
            colors.get("accent", ""),
            colors.get("trust", "")
        )

    return f"""    /* Core brand */
    --color-primary: {colors.get('primary', '#4a7c59')};
    --color-primary-dark: {colors.get('primary_dark', '#3a6347')};
    --color-primary-light: {colors.get('primary_light', '#7fb3a3')};
    --color-accent: {colors.get('accent', '#d9724a')};
    --color-accent-dark: {colors.get('accent_dark', '#b85a38')};
    --color-accent-light: {colors.get('accent_light', '#e8a48a')};
    --color-trust: {colors.get('trust', '#5b8def')};
    --color-trust-dark: {colors.get('trust_dark', '#4d78cb')};"""


def _shadow_variables(warmth: str = "warm") -> str:
    """Generates shadow CSS variables based on warmth preference."""
    if warmth == "cool":
        base = "0, 0, 0"
    elif warmth == "none":
        return """    --shadow-sm: none;
    --shadow-md: none;
    --shadow-lg: none;
    --shadow-xl: none;"""
    else:  # warm (default)
        base = "61, 58, 53"
    return f"""    --shadow-sm: 0 1px 2px rgba({base}, 0.05);
    --shadow-md: 0 4px 12px rgba({base}, 0.08);
    --shadow-lg: 0 16px 32px rgba({base}, 0.10);
    --shadow-xl: 0 24px 48px rgba({base}, 0.14);"""


def get_full_css_variables(colors: dict[str, str], theme: dict[str, Any] | None = None) -> str:
    """Generuje pełny blok CSS variables — kolory + typografia + geometria + spacing + transitions + shadows."""
    t = theme or {}

    # Kolory (deleguj do istniejącej logiki)
    color_block = get_css_variables(colors)

    # Typografia
    font_body = t.get("font_body", "Inter")
    font_heading = t.get("font_heading", "Fraunces")
    font_size_base = t.get("font_size_base", "16px")
    line_height = t.get("line_height", "1.65")
    heading_weight = t.get("heading_weight", "600")
    letter_spacing_heading = t.get("letter_spacing_heading", "-0.01em")

    # Geometria
    radius_sm = t.get("radius_sm", "8px")
    radius = t.get("radius", "14px")
    radius_lg = t.get("radius_lg", "20px")
    radius_pill = t.get("radius_pill", "50px")

    # Layout
    container_max = t.get("container_max", "1180px")
    prose_max = t.get("prose_max", "720px")
    gutter = t.get("gutter", "clamp(1rem, 4vw, 2rem)")
    section_spacing = t.get("section_spacing", "clamp(3rem, 8vw, 6rem)")

    # Transitions
    transition_fast = t.get("transition_fast", "150ms")
    transition_base = t.get("transition_base", "250ms")
    transition_slow = t.get("transition_slow", "400ms")

    # Shadows
    shadow_warmth = t.get("shadow_warmth", "warm")
    shadow_block = _shadow_variables(shadow_warmth)

    return f"""{color_block}

    /* Shadows */
{shadow_block}

    /* Typography */
    --font-sans: '{font_body}', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    --font-serif: '{font_heading}', Georgia, 'Times New Roman', serif;
    --font-size-base: {font_size_base};
    --line-height-base: {line_height};
    --heading-weight: {heading_weight};
    --letter-spacing-heading: {letter_spacing_heading};

    /* Geometry */
    --radius-sm: {radius_sm};
    --radius: {radius};
    --radius-lg: {radius_lg};
    --radius-pill: {radius_pill};

    /* Layout */
    --container: {container_max};
    --container-prose: {prose_max};
    --space-gutter: {gutter};
    --section-y: {section_spacing};

    /* Transitions */
    --t-fast: {transition_fast};
    --t-base: {transition_base};
    --t-slow: {transition_slow};"""


if __name__ == "__main__":
    print("Dostępne domeny:")
    for d in list_domains():
        cfg = load_domain_config(d)
        role = cfg["site"]["role"]
        brand = cfg["site"]["brand"]
        main = cfg["site"].get("main_domain", "")
        arrow = f" → {main}" if main else ""
        print(f"  {d:30s} [{role}] brand={brand}{arrow}")
