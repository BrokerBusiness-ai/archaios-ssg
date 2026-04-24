#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build.py — Archaios SSG: generator statycznych stron dla sieci domen satelitarnych.

Obsługuje WIELE domen z jednego codebase. Konfiguracja per domena
w katalogu domains/*.yaml.

Generuje:
  - index.html, artykuly.html, autorzy.html
  - artykuly/<slug>.html (osobny plik na artykuł, z TOC + bibliografią + CTA produktów)
  - kategoria/<slug>.html (strona każdej kategorii)
  - autor/<slug>.html (strona każdego autora — E-E-A-T)
  - polityka-prywatnosci.html, regulamin.html
  - sitemap.xml, robots.txt, rss.xml
  - css/domain-colors.css (override kolorów per domena)
  - img/og/<slug>.png (auto-generowany OG image per artykuł — Pillow)
  - manifest.json, favicon.svg

Uruchomienie:
    python build.py --domain testnis2.pl          # build jednej domeny
    python build.py --domain testnis2.pl --clean  # z czyszczeniem
    python build.py --all                         # build wszystkich domen
    python build.py --list                        # lista dostępnych domen
    python build.py                               # domyślnie: zdrowie.fit (kompatybilność)
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import sqlite3
import sys
from datetime import datetime, timezone
from email.utils import format_datetime
from pathlib import Path
from typing import Any

try:
    sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
    sys.stderr.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
except Exception:
    pass

from jinja2 import Environment, FileSystemLoader, select_autoescape

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass


ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
TPL_DIR = SRC / "templates"
STATIC_DIR = SRC / "static"

from domain_config import load_domain_config, list_domains, get_css_variables, get_full_css_variables


def cfg(key: str, default: str = "") -> str:
    return os.environ.get(key, default).strip()


# CONFIG i PILLARS ładowane dynamicznie per domena — patrz build()
CONFIG: dict = {}
PILLARS: list = []


def init_config(domain: str | None = None) -> None:
    """Inicjalizuje CONFIG i PILLARS z pliku domeny lub ze zmiennych env (fallback)."""
    global CONFIG, PILLARS

    if domain:
        dcfg = load_domain_config(domain)
        CONFIG = {
            "site": dcfg["site"],
            "analytics": dcfg["analytics"],
            "newsletter": dcfg["newsletter"],
            "colors": dcfg["colors"],
            "hero": dcfg["hero"],
            "about": dcfg["about"],
            "footer": dcfg["footer"],
            "domain_products": dcfg["products"],
            "domain_categories": dcfg["categories"],
            "api_url": cfg("API_URL", "http://127.0.0.1:8765/api"),
            "use_api": cfg("USE_API", "true").lower() in ("1", "true", "yes"),
            "output": ROOT / "output" / domain.replace(".", "-"),
            "backend_url": cfg("BACKEND_URL", "http://127.0.0.1:8765"),
        }
        PILLARS = dcfg["pillars"]
        CONFIG["theme"] = dcfg.get("theme", {})
    else:
        # Fallback: tryb kompatybilności (zdrowie.fit z .env)
        CONFIG = {
            "site": {
                "url": cfg("SITE_URL", "https://zdrowie.fit").rstrip("/"),
                "name": cfg("SITE_NAME", "Zdrowie Fit"),
                "tagline": cfg("SITE_TAGLINE", "Ciało i umysł w harmonii"),
                "description": cfg("SITE_DESCRIPTION", "Holistyczne podejście do zdrowia."),
                "author": cfg("SITE_AUTHOR", "Zdrowie Fit"),
                "lang": cfg("SITE_LANG", "pl"),
                "locale": cfg("SITE_LOCALE", "pl_PL"),
                "fb": cfg("FB_PAGE"),
                "ig": cfg("IG_HANDLE"),
                "yt": cfg("YT_CHANNEL"),
                "tw": cfg("TW_HANDLE"),
                "email": cfg("CONTACT_EMAIL", "kontakt@zdrowie.fit"),
                "logo_mark": "◐",
                "logo_text": "Zdrowie",
                "logo_accent": ".fit",
            },
            "analytics": {
                "ga4_id": cfg("GA4_ID"),
                "fb_pixel_id": cfg("FB_PIXEL_ID"),
            },
            "newsletter": {
                "endpoint": cfg("NEWSLETTER_ENDPOINT"),
                "provider": cfg("NEWSLETTER_PROVIDER"),
                "title_highlight": "cotygodniowy przegląd",
                "title_rest": "badań o zdrowiu",
                "subtitle": "Raz w tygodniu: 3 konkretne wskazówki oparte na badaniach, zero spamu.",
            },
            "colors": {
                "primary": "#4a7c59",
                "primary_dark": "#3a6347",
                "primary_light": "#7fb3a3",
                "accent": "#d9724a",
                "accent_dark": "#b85a38",
                "trust": "#5b8def",
            },
            "hero": {},
            "about": {},
            "footer": {"tagline": "Holistyczne podejście do zdrowia.", "disclaimer": "Treści mają charakter edukacyjny."},
            "domain_products": [],
            "domain_categories": [],
            "api_url": cfg("API_URL", "http://127.0.0.1:8765/api"),
            "use_api": cfg("USE_API", "true").lower() in ("1", "true", "yes"),
            "output": ROOT / cfg("OUTPUT_DIR", "zdrowie-fit"),
            "backend_url": cfg("BACKEND_URL", "http://127.0.0.1:8765"),
        }
        PILLARS = [
            {"icon": "🏃", "title": "Ruch", "desc": "Trening siłowy, cardio, rozciąganie — jak ciało wpływa na umysł."},
            {"icon": "🧠", "title": "Umysł", "desc": "Mindfulness, terapia, zarządzanie stresem i emocjami."},
            {"icon": "🥗", "title": "Odżywianie", "desc": "Dieta oparta na badaniach, mikrobiom, suplementacja."},
            {"icon": "😴", "title": "Regeneracja", "desc": "Sen, odpoczynek, higiena dnia. Bez tego nic nie działa."},
            {"icon": "🌿", "title": "Natura", "desc": "Shinrin-yoku, światło dzienne, kontakt z przyrodą."},
            {"icon": "❤️", "title": "Relacje", "desc": "Więzi społeczne to jeden z najsilniejszych predyktorów zdrowia."},
        ]


# ═════════════════ UTILITIES ═════════════════

MONTHS_PL = {1:"stycznia",2:"lutego",3:"marca",4:"kwietnia",5:"maja",6:"czerwca",
             7:"lipca",8:"sierpnia",9:"września",10:"października",11:"listopada",12:"grudnia"}


def format_date_pl(iso: str | None) -> str:
    if not iso: return ""
    try:
        dt = datetime.fromisoformat(str(iso).replace("Z", "+00:00"))
    except ValueError:
        return str(iso)[:10]
    return f"{dt.day} {MONTHS_PL[dt.month]} {dt.year}"


def to_rfc822(iso: str | None) -> str:
    if not iso: return ""
    try:
        dt = datetime.fromisoformat(str(iso).replace("Z", "+00:00"))
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
    except ValueError:
        return ""
    return format_datetime(dt)


def strip_html(html: str) -> str:
    return re.sub(r"<[^>]+>", "", html or "")


def abs_url(url: str) -> str:
    """Jeśli URL jest względny (/uploads/...) zamienia na absolutny z backend_url."""
    if not url: return ""
    if url.startswith(("http://", "https://")): return url
    return CONFIG["backend_url"].rstrip("/") + url


# ═════════════════ FETCH ═════════════════

def fetch_from_api() -> dict:
    import httpx
    api = CONFIG["api_url"].rstrip("/")
    print(f"📡 Łączenie z API: {api}")
    try:
        with httpx.Client(timeout=15.0) as client:
            # Artykuły — paginacja
            articles: list[dict] = []
            page = 1
            while True:
                r = client.get(f"{api}/articles/?per_page=100&page={page}&published_only=true&sort=newest")
                r.raise_for_status()
                data = r.json()
                items = data.get("items", [])
                articles.extend(items)
                if page >= data.get("pages", 1) or not items:
                    break
                page += 1
            # Dopełnij pełną treść (listItem nie ma content)
            full_articles = []
            for a in articles:
                fr = client.get(f"{api}/articles/{a['id']}")
                if fr.status_code == 200:
                    full_articles.append(fr.json())
                else:
                    full_articles.append(a)
            categories = client.get(f"{api}/categories/").json()
            authors = client.get(f"{api}/authors/").json()
            products = client.get(f"{api}/products/?active_only=true").json()
        return {"articles": full_articles, "categories": categories, "authors": authors, "products": products}
    except Exception as exc:
        print(f"⚠️  API niedostępne ({exc}). Fallback na SQLite...")
        return fetch_from_db()


def fetch_from_db() -> dict:
    db_path = ROOT / "backend" / "zdrowiefit.db"
    if not db_path.exists():
        print(f"❌ Brak bazy {db_path}")
        return {"articles": [], "categories": [], "authors": [], "products": []}
    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row

    cats = [dict(r) for r in conn.execute("SELECT * FROM categories ORDER BY sort_order")]
    cat_by_id = {c["id"]: c for c in cats}

    authors = [dict(r) for r in conn.execute("SELECT * FROM authors ORDER BY sort_order, name")]
    auth_by_id = {a["id"]: a for a in authors}

    products = [dict(r) for r in conn.execute("SELECT * FROM products WHERE is_active = 1 ORDER BY priority DESC, name")]

    articles = []
    for r in conn.execute("SELECT * FROM articles WHERE is_published = 1 ORDER BY published_at DESC"):
        a = dict(r)
        cat = cat_by_id.get(a.get("category_id"))
        if cat:
            a["category_name"] = cat["name"]; a["category_slug"] = cat["slug"]; a["category_icon"] = cat.get("icon", "")
        au = auth_by_id.get(a.get("author_id"))
        if au:
            a["author"] = au["name"]; a["author_slug"] = au["slug"]
        articles.append(a)

    conn.close()
    # Article counts
    for c in cats:
        c["article_count"] = sum(1 for a in articles if a.get("category_id") == c["id"])
    return {"articles": articles, "categories": cats, "authors": authors, "products": products}


def enrich_articles(articles: list[dict], categories: list[dict], authors: list[dict]):
    """Dodaje pola pomocnicze do artykułów."""
    cat_by_id = {c["id"]: c for c in categories}
    auth_by_id = {a["id"]: a for a in authors}
    for a in articles:
        cat = cat_by_id.get(a.get("category_id"))
        if cat:
            a.setdefault("category_name", cat["name"])
            a.setdefault("category_slug", cat["slug"])
            a["category_icon"] = cat.get("icon", "")
        au = auth_by_id.get(a.get("author_id"))
        if au:
            a["author"] = au["name"]
            a["author_slug"] = au["slug"]
        else:
            a.setdefault("author_slug", "")
        # URL-e uploadów → absolutne
        if a.get("image_url"):
            a["image_url"] = abs_url(a["image_url"])
        a["published_date_pl"] = format_date_pl(a.get("published_at") or a.get("created_at"))
        a["pubdate_rfc822"] = to_rfc822(a.get("published_at") or a.get("created_at"))
        a["word_count"] = len(strip_html(a.get("content") or "").split())


def match_products(article: dict, products: list[dict]) -> list[dict]:
    """Dopasowuje produkty do artykułu: manual override → auto-match po kategorii/tagach."""
    now = datetime.utcnow()

    def active(p):
        if not p.get("is_active"): return False
        vf, vt = p.get("valid_from"), p.get("valid_to")
        try:
            if vf and datetime.fromisoformat(str(vf).replace("Z", "+00:00")).replace(tzinfo=None) > now: return False
            if vt and datetime.fromisoformat(str(vt).replace("Z", "+00:00")).replace(tzinfo=None) < now: return False
        except (ValueError, TypeError):
            pass
        return True

    active_products = [p for p in products if active(p)]

    # Manual override
    manual = [s.strip() for s in (article.get("product_slugs") or "").split(",") if s.strip()]
    if manual:
        by_slug = {p["slug"]: p for p in active_products}
        return [by_slug[s] for s in manual if s in by_slug]

    # Auto-match
    art_cat_slug = article.get("category_slug", "")
    art_tags = [t.strip().lower() for t in (article.get("tags") or "").split(",") if t.strip()]
    matched = []
    for p in active_products:
        target_cats = [c.strip() for c in (p.get("target_category_slugs") or "").split(",") if c.strip()]
        target_tags = [t.strip().lower() for t in (p.get("target_tags") or "").split(",") if t.strip()]

        matches_cat = not target_cats or (art_cat_slug and art_cat_slug in target_cats)
        matches_tag = not target_tags or any(t in art_tags for t in target_tags)

        # Musi pasować ALBO po kategorii ALBO po tagu (jeśli są oba zdefiniowane)
        if target_cats and target_tags:
            if matches_cat or matches_tag: matched.append(p)
        elif matches_cat and matches_tag:
            matched.append(p)

    matched.sort(key=lambda p: p.get("priority", 50), reverse=True)
    return matched[:3]  # max 3 produkty per artykuł


def add_cta_urls(products: list[dict], campaign_slug: str = ""):
    """Dodaje pole cta_url z UTM-ami do każdego produktu."""
    default_source = CONFIG.get("_domain", CONFIG.get("site", {}).get("url", "zdrowie.fit")).replace("https://", "")
    for p in products:
        url = p.get("target_url", "")
        sep = "&" if "?" in url else "?"
        parts = [f"utm_source={p.get('utm_source', default_source)}", f"utm_medium={p.get('utm_medium','article')}"]
        if campaign_slug:
            parts.append(f"utm_campaign={campaign_slug}")
        p["cta_url"] = f"{url}{sep}{'&'.join(parts)}" if url else ""


# ═════════════════ AUTO OG IMAGE ═════════════════

def optimize_image(src_url: str, output_dir: Path, slug: str, backend_url: str = "") -> dict:
    """Przetwarza obraz artykułu: konwertuje do WebP, tworzy thumbnail.

    Zwraca dict z nowymi ścieżkami:
      - image_webp: /img/articles/{slug}.webp (max 1200px, quality 82)
      - image_thumb: /img/articles/{slug}-thumb.webp (400px, quality 75)
      - image_social: oryginał (PNG/JPG) — fallback dla social media
    """
    try:
        from PIL import Image
    except ImportError:
        return {}

    if not src_url:
        return {}

    img_dir = output_dir / "img" / "articles"
    img_dir.mkdir(parents=True, exist_ok=True)

    webp_path = img_dir / f"{slug}.webp"
    thumb_path = img_dir / f"{slug}-thumb.webp"

    if webp_path.exists() and thumb_path.exists():
        return {
            "image_webp": f"/img/articles/{slug}.webp",
            "image_thumb": f"/img/articles/{slug}-thumb.webp",
        }

    # Załaduj obraz
    img = None

    # Spróbuj z localnego uploadu
    if src_url.startswith("/uploads/"):
        local_path = Path(__file__).resolve().parent / "backend" / src_url.lstrip("/")
        if local_path.exists():
            try:
                img = Image.open(local_path)
            except Exception:
                pass

    # Spróbuj z URL-a (backend lub external)
    if img is None and src_url.startswith(("http://", "https://")):
        try:
            import httpx
            r = httpx.get(src_url, timeout=10, follow_redirects=True)
            if r.status_code == 200:
                from io import BytesIO
                img = Image.open(BytesIO(r.content))
        except Exception:
            pass

    if img is None:
        return {}

    # Konwertuj do RGB (WebP nie obsługuje RGBA z przezroczystością ładnie)
    if img.mode in ("RGBA", "P"):
        bg = Image.new("RGB", img.size, (253, 252, 249))  # ivory background
        if img.mode == "P":
            img = img.convert("RGBA")
        bg.paste(img, mask=img.split()[3] if len(img.split()) == 4 else None)
        img = bg
    elif img.mode != "RGB":
        img = img.convert("RGB")

    # Full size WebP (max 1200px wide)
    if not webp_path.exists():
        full = img.copy()
        if full.width > 1200:
            ratio = 1200 / full.width
            full = full.resize((1200, int(full.height * ratio)), Image.LANCZOS)
        full.save(webp_path, "WebP", quality=82, method=6)

    # Thumbnail (400px wide)
    if not thumb_path.exists():
        thumb = img.copy()
        ratio = 400 / thumb.width
        thumb = thumb.resize((400, int(thumb.height * ratio)), Image.LANCZOS)
        thumb.save(thumb_path, "WebP", quality=75, method=6)

    return {
        "image_webp": f"/img/articles/{slug}.webp",
        "image_thumb": f"/img/articles/{slug}-thumb.webp",
    }


def generate_og_image(article: dict, output_dir: Path, colors: dict | None = None) -> bool:
    """Generuje custom OG image (1200×630) z tytułem artykułu. Używa Pillow."""
    try:
        from PIL import Image, ImageDraw, ImageFont
    except ImportError:
        return False

    if colors is None:
        colors = CONFIG.get("colors", {})

    og_dir = output_dir / "img" / "og"
    og_dir.mkdir(parents=True, exist_ok=True)
    out_path = og_dir / f"{article['slug']}.png"
    if out_path.exists():
        article["og_generated"] = True
        return True

    bg_color = colors.get("primary", "#4a7c59")
    img = Image.new("RGB", (1200, 630), bg_color)
    d = ImageDraw.Draw(img)

    # Gradient + wzór — dynamiczny z kolorów domeny
    def hex_to_rgb(h: str) -> tuple:
        h = h.lstrip("#")
        return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

    bg_rgb = hex_to_rgb(bg_color)
    for y in range(630):
        alpha = int(40 * (y / 630))
        d.line([(0, y), (1200, y)], fill=(
            max(0, bg_rgb[0] - alpha // 3),
            max(0, bg_rgb[1] - alpha // 3),
            max(0, bg_rgb[2] - alpha // 3),
        ))

    # Fonty
    font_big = None
    font_small = None
    font_tiny = None
    for font_path in ["C:/Windows/Fonts/seguisb.ttf", "C:/Windows/Fonts/segoeui.ttf", "arial.ttf"]:
        try:
            font_big = ImageFont.truetype(font_path, 64)
            font_small = ImageFont.truetype(font_path, 28)
            font_tiny = ImageFont.truetype(font_path, 22)
            break
        except (OSError, IOError):
            continue
    if not font_big:
        font_big = ImageFont.load_default()
        font_small = font_big
        font_tiny = font_big

    accent_color = colors.get("accent", "#d9724a")

    # Kategoria (eyebrow)
    if article.get("category_name"):
        d.text((100, 100), article["category_name"].upper(), fill=accent_color, font=font_small)

    # Tytuł — zawinięty
    title = article.get("title", "")
    max_chars = 36
    words = title.split()
    lines: list[str] = []
    current = ""
    for word in words:
        test = (current + " " + word).strip()
        if len(test) <= max_chars:
            current = test
        else:
            if current: lines.append(current)
            current = word
    if current: lines.append(current)
    lines = lines[:4]

    y = 180
    for line in lines:
        d.text((100, y), line, fill="#fdfcf9", font=font_big)
        y += 85

    # Author + date
    meta = f"{article.get('author', '')} · {article.get('published_date_pl', '')}"
    d.text((100, 520), meta, fill="#f6f0e6", font=font_tiny)

    # Brand dół
    site_name = CONFIG.get("site", {}).get("name", "")
    d.text((100, 560), site_name or "zdrowie.fit", fill=accent_color, font=font_small)

    # Pasek na dole
    d.rectangle((0, 620, 1200, 630), fill=accent_color)

    img.save(out_path, "PNG", optimize=True)
    # WebP version (much smaller)
    webp_path = og_dir / f"{article['slug']}.webp"
    if webp_path.exists():
        article["og_webp"] = True
    else:
        try:
            img.save(webp_path, "WebP", quality=85, method=6)
            article["og_webp"] = True
        except Exception:
            article["og_webp"] = False  # Pillow without WebP support — PNG is fine
    article["og_generated"] = True
    return True


# ═════════════════ RENDER ═════════════════

def make_env() -> Environment:
    env = Environment(
        loader=FileSystemLoader(str(TPL_DIR)),
        autoescape=select_autoescape(["html", "xml"]),
    )
    def urlencode_filter(s: Any) -> str:
        from urllib.parse import quote
        return quote(str(s), safe="")
    env.filters["urlencode"] = urlencode_filter
    env.filters["striptags"] = lambda s: strip_html(s) if s else ""
    env.filters["truncate"] = lambda s, length=255: (str(s)[:length-3] + "...") if s and len(str(s)) > length else (s or "")
    env.filters["wordwrap"] = lambda s, width=80: s or ""  # plain text passthrough
    return env


def render(env: Environment, template: str, out: Path, **ctx):
    tpl = env.get_template(template)
    content = tpl.render(**ctx)
    # Minify HTML (nie .xml, .txt, .json)
    if out.suffix == '.html':
        content = minify_html(content)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(content, encoding="utf-8")
    print(f"  ✓ {out.relative_to(ROOT)}")


def extract_faq_items(content: str) -> list[dict]:
    """Wyciąga FAQ z contentu artykułu — szuka <h2>/<h3> kończących się '?' i następnego <p>."""
    if not content:
        return []
    # Szukaj headingów kończących się znakiem zapytania
    pattern = re.compile(
        r'<h[23][^>]*>(.*?\?)</h[23]>\s*<p[^>]*>(.*?)</p>',
        re.DOTALL | re.IGNORECASE
    )
    items = []
    for match in pattern.finditer(content):
        question = strip_html(match.group(1)).strip()
        answer = strip_html(match.group(2)).strip()
        if question and answer and len(answer) > 20:
            items.append({"q": question, "a": answer})
    return items[:10]  # max 10 FAQ per artykuł


def extract_howto_steps(content: str) -> list[dict]:
    """Auto-detects HowTo steps from ordered lists or 'Krok X' headings."""
    steps = []
    # Pattern 1: <ol> with <li> items
    ol_match = re.search(r'<ol[^>]*>(.*?)</ol>', content, re.DOTALL | re.IGNORECASE)
    if ol_match:
        li_pattern = re.compile(r'<li[^>]*>(.*?)</li>', re.DOTALL | re.IGNORECASE)
        for li in li_pattern.findall(ol_match.group(1)):
            text = re.sub(r'<[^>]+>', '', li).strip()
            if text:
                # Split on first period or colon for name vs text
                split = re.split(r'[.:]', text, maxsplit=1)
                steps.append({
                    "name": split[0].strip(),
                    "text": split[1].strip() if len(split) > 1 else text
                })

    # Pattern 2: "Krok X:" or "Step X:" headings
    if not steps:
        step_pattern = re.compile(
            r'<h[234][^>]*>\s*(?:Krok|Step)\s+\d+[.:]\s*(.*?)</h[234]>\s*<p[^>]*>(.*?)</p>',
            re.DOTALL | re.IGNORECASE
        )
        for name, text in step_pattern.findall(content):
            steps.append({
                "name": re.sub(r'<[^>]+>', '', name).strip(),
                "text": re.sub(r'<[^>]+>', '', text).strip()[:300]
            })

    return steps if len(steps) >= 2 else []  # Need at least 2 steps


def get_related(all_articles: list[dict], current: dict, n: int = 3) -> list[dict]:
    # Manual override
    manual = [s.strip() for s in (current.get("related_slugs") or "").split(",") if s.strip()]
    if manual:
        by_slug = {a["slug"]: a for a in all_articles}
        return [by_slug[s] for s in manual if s in by_slug][:n]
    # Auto: same category first
    same_cat = [a for a in all_articles
                if a["slug"] != current["slug"] and a.get("category_id") == current.get("category_id")]
    others = [a for a in all_articles if a["slug"] != current["slug"] and a not in same_cat]
    return (same_cat + others)[:n]


def minify_css(css: str) -> str:
    """Prosty minifier CSS — usuwa komentarze, zbędne whitespace."""
    css = re.sub(r'/\*.*?\*/', '', css, flags=re.DOTALL)  # komentarze
    css = re.sub(r'\s+', ' ', css)  # multiple whitespace → single space
    css = re.sub(r'\s*([{}:;,>~+])\s*', r'\1', css)  # whitespace wokół operatorów
    css = re.sub(r';\s*}', '}', css)  # trailing semicolons
    css = css.strip()
    return css


def minify_js(js: str) -> str:
    """Prosty minifier JS — usuwa komentarze, zbędne whitespace. Bezpieczny."""
    js = re.sub(r'//[^\n]*', '', js)  # single-line comments
    js = re.sub(r'/\*.*?\*/', '', js, flags=re.DOTALL)  # block comments
    js = re.sub(r'\n\s*\n', '\n', js)  # empty lines
    lines = [line.rstrip() for line in js.split('\n') if line.strip()]
    return '\n'.join(lines)


def minify_html(html: str) -> str:
    """Minifikacja HTML — bez ruszania <script>/<style>/<pre> content."""
    # Zachowaj pre/script/style bloki
    preserved = {}
    counter = [0]
    def preserve(match):
        key = f"__PRESERVED_{counter[0]}__"
        counter[0] += 1
        preserved[key] = match.group(0)
        return key
    html = re.sub(r'<(script|style|pre)[^>]*>.*?</\1>', preserve, html, flags=re.DOTALL | re.IGNORECASE)
    # Minify
    html = re.sub(r'<!--(?!\[if).*?-->', '', html, flags=re.DOTALL)  # komentarze (zachowaj IE conditional)
    html = re.sub(r'>\s+<', '> <', html)  # whitespace między tagami
    html = re.sub(r'\s{2,}', ' ', html)  # multiple spaces
    # Przywróć
    for key, val in preserved.items():
        html = html.replace(key, val)
    return html


def extract_critical_css(css_path: Path) -> str:
    """Wyciąga critical CSS (above-the-fold) z style.css."""
    if not css_path.exists():
        return ""
    css = css_path.read_text(encoding="utf-8")
    # Critical selectors: root vars, body, header, hero, container, btn, nav, skip-link, logo
    critical_patterns = [
        r':root\s*\{[^}]+\}',
        r'@media\s*\(prefers-color-scheme:\s*dark\)\s*\{[^}]*:root\.dark-auto\s*\{[^}]+\}[^}]*\}',
        r'\*,\s*\*::before,\s*\*::after\s*\{[^}]+\}',
        r'html\s*\{[^}]+\}',
        r'body\s*\{[^}]+\}',
        r'img,[^{]*\{[^}]*max-width:\s*100%[^}]*\}',
        r'a\s*\{[^}]+\}',
        r'h1,[^{]*\{[^}]+\}',
        r'\.container\s*\{[^}]+\}',
        r'\.visually-hidden\s*\{[^}]+\}',
        r'\.skip-link[^{]*\{[^}]+\}',
        r'\.header[^{]*\{[^}]+\}',
        r'\.logo[^{]*\{[^}]+\}',
        r'\.nav__list\s*\{[^}]+\}',
        r'\.nav__link[^{]*\{[^}]+\}',
        r'\.nav__toggle[^{]*\{[^}]+\}',
        r'\.hero[^{]*\{[^}]+\}',
        r'\.btn[^{]*\{[^}]+\}',
        r'\.highlight\s*\{[^}]+\}',
    ]
    parts = []
    for pattern in critical_patterns:
        matches = re.findall(pattern, css, re.DOTALL)
        parts.extend(matches)
    critical = '\n'.join(parts)
    return minify_css(critical)


def copy_static(out: Path):
    if not STATIC_DIR.exists(): return
    for item in STATIC_DIR.rglob("*"):
        if item.is_file():
            dest = out / item.relative_to(STATIC_DIR)
            dest.parent.mkdir(parents=True, exist_ok=True)
            # Minify CSS/JS during copy
            if item.suffix == '.css':
                raw = item.read_text(encoding="utf-8")
                dest.write_text(minify_css(raw), encoding="utf-8")
            elif item.suffix == '.js':
                raw = item.read_text(encoding="utf-8")
                dest.write_text(minify_js(raw), encoding="utf-8")
            else:
                shutil.copy2(item, dest)
    print(f"📦 Statyczne pliki (minified) → {out.name}/")


def ensure_default_assets(out: Path):
    img_dir = out / "img"
    img_dir.mkdir(exist_ok=True)

    colors = CONFIG.get("colors", {})
    primary = colors.get("primary", "#4a7c59")
    logo_mark = CONFIG.get("site", {}).get("logo_mark", "◐")
    site_name = CONFIG.get("site", {}).get("name", "Zdrowie Fit")

    fav = out / "favicon.svg"
    if not fav.exists():
        fav.write_text(
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">'
            f'<rect width="64" height="64" rx="12" fill="{primary}"/>'
            f'<text x="32" y="44" text-anchor="middle" font-family="Georgia" font-size="36" fill="#fdfcf9" font-weight="700">{logo_mark}</text>'
            f'</svg>', encoding="utf-8")

    og_default = img_dir / "og-default.png"
    if not og_default.exists():
        try:
            generate_og_image({"slug": "og-default", "title": CONFIG.get("site", {}).get("tagline", ""),
                              "category_name": site_name, "author": site_name,
                              "published_date_pl": ""}, out, colors)
            # rename
            gen = img_dir / "og" / "og-default.png"
            if gen.exists():
                shutil.move(str(gen), str(og_default))
        except Exception:
            pass

    logo = img_dir / "logo.png"
    if not logo.exists():
        try:
            from PIL import Image, ImageDraw
            img = Image.new("RGBA", (512, 512), (0,0,0,0))
            d = ImageDraw.Draw(img)
            def hex_to_rgba(h: str) -> tuple:
                h = h.lstrip("#")
                return tuple(int(h[i:i+2], 16) for i in (0, 2, 4)) + (255,)
            d.rounded_rectangle((0,0,512,512), radius=80, fill=hex_to_rgba(primary))
            d.text((180, 140), logo_mark, fill="#fdfcf9")
            img.save(logo, "PNG")
        except ImportError:
            pass

    short_name = CONFIG["site"]["name"].replace(" ", "")[:12]
    mani = out / "manifest.json"
    if not mani.exists():
        mani.write_text(json.dumps({
            "name": CONFIG["site"]["name"], "short_name": short_name,
            "description": CONFIG["site"]["description"], "start_url": "/",
            "display": "standalone", "background_color": "#fdfcf9", "theme_color": primary,
            "icons": [{"src": "/img/logo.png", "sizes": "512x512", "type": "image/png"},
                     {"src": "/favicon.svg", "sizes": "any", "type": "image/svg+xml"}],
        }, ensure_ascii=False, indent=2), encoding="utf-8")


# ═════════════════ MAIN ═════════════════

def generate_htaccess(out: Path) -> None:
    """Generuje .htaccess z security headers, compression, cache i HTTPS redirect."""
    site_url = CONFIG.get("site", {}).get("url", "")
    domain = site_url.replace("https://", "").replace("http://", "")
    htaccess = f"""# === Security Headers ===
<IfModule mod_headers.c>
    Header set X-Content-Type-Options "nosniff"
    Header set X-Frame-Options "SAMEORIGIN"
    Header set X-XSS-Protection "0"
    Header set Referrer-Policy "strict-origin-when-cross-origin"
    Header set Permissions-Policy "camera=(), microphone=(), geolocation=(), payment=()"
    Header set Content-Security-Policy "default-src 'self'; script-src 'self' 'unsafe-inline' https://www.googletagmanager.com https://connect.facebook.net; style-src 'self' 'unsafe-inline'; font-src 'self' data:; img-src 'self' data: https:; connect-src 'self' https://www.google-analytics.com https://www.facebook.com; frame-ancestors 'none'"
    Header always set Strict-Transport-Security "max-age=31536000; includeSubDomains; preload"
</IfModule>

# === Compression ===
<IfModule mod_deflate.c>
    AddOutputFilterByType DEFLATE text/html text/css text/javascript application/javascript application/json image/svg+xml application/xml text/xml text/plain
</IfModule>

# === Cache Control ===
<IfModule mod_expires.c>
    ExpiresActive On
    ExpiresDefault "access plus 1 month"
    ExpiresByType text/html "access plus 1 hour"
    ExpiresByType text/css "access plus 1 year"
    ExpiresByType application/javascript "access plus 1 year"
    ExpiresByType image/png "access plus 1 year"
    ExpiresByType image/webp "access plus 1 year"
    ExpiresByType image/jpeg "access plus 1 year"
    ExpiresByType image/svg+xml "access plus 1 year"
    ExpiresByType image/x-icon "access plus 1 year"
    ExpiresByType application/json "access plus 1 day"
    ExpiresByType application/xml "access plus 1 hour"
    ExpiresByType application/rss+xml "access plus 1 hour"
    ExpiresByType font/woff2 "access plus 1 year"
</IfModule>

# === HTTPS Redirect ===
<IfModule mod_rewrite.c>
    RewriteEngine On
    RewriteCond %{{HTTPS}} off
    RewriteRule ^ https://%{{HTTP_HOST}}%{{REQUEST_URI}} [L,R=301]
</IfModule>

# === Error Pages ===
ErrorDocument 404 /404.html

# === Prevent directory listing ===
Options -Indexes

# === Block sensitive files ===
<FilesMatch "\\.(env|yml|yaml|db|sqlite|log|bak|py)$">
    Order Allow,Deny
    Deny from all
</FilesMatch>
"""
    (out / ".htaccess").write_text(htaccess, encoding="utf-8")
    print(f"  ✓ .htaccess (security headers + cache + compression)")


def generate_domain_css(out: Path, colors: dict, theme: dict | None = None) -> None:
    """Generuje plik CSS z override kolorów i theme dla domeny."""
    css_dir = out / "css"
    css_dir.mkdir(parents=True, exist_ok=True)
    css_content = f""":root {{
{get_full_css_variables(colors, theme or {})}
}}
"""
    (css_dir / "domain-colors.css").write_text(css_content, encoding="utf-8")
    print(f"  ✓ css/domain-colors.css")


def build(clean: bool = False, domain: str | None = None):
    init_config(domain)
    domain_name = domain or CONFIG["site"].get("name", "zdrowie.fit")
    print(f"\n🚀 Build {domain_name} — start\n")
    out: Path = CONFIG["output"]
    if clean and out.exists():
        print(f"🧹 Czyszczę {out.name}/")
        shutil.rmtree(out)
    out.mkdir(parents=True, exist_ok=True)

    # Fetch
    data = fetch_from_api() if CONFIG["use_api"] else fetch_from_db()
    articles = data["articles"]
    categories = data["categories"]
    authors = data["authors"]
    products = data["products"]

    if not articles:
        print("❌ Brak artykułów — build przerwany.")
        return 1

    enrich_articles(articles, categories, authors)

    env = make_env()
    now = datetime.now()

    # Critical CSS — extract and inline
    critical_css = extract_critical_css(STATIC_DIR / "css" / "style.css")

    common = {"site": CONFIG["site"], "analytics": CONFIG["analytics"],
              "newsletter": CONFIG["newsletter"], "colors": CONFIG.get("colors", {}),
              "hero_cfg": CONFIG.get("hero", {}), "about_cfg": CONFIG.get("about", {}),
              "footer_cfg": CONFIG.get("footer", {}), "now": now,
              "critical_css": critical_css,
              "theme": CONFIG.get("theme", {})}

    print(f"\n📊 Dane: {len(articles)} artykułów, {len(categories)} kategorii, {len(authors)} autorów, {len(products)} aktywnych produktów\n")
    print("📝 Renderowanie:")

    # 1) Strona główna
    render(env, "index.html", out / "index.html",
           page={"slug": "home", "path": "/"},
           articles=articles, categories=categories, pillars=PILLARS, **common)

    # 2) Lista artykułów
    render(env, "articles.html", out / "artykuly.html",
           page={"slug": "articles", "path": "/artykuly.html"},
           articles=articles, categories=categories, **common)

    # 3) Pojedyncze artykuły + auto OG
    arts_dir = out / "artykuly"
    arts_dir.mkdir(exist_ok=True)
    for a in articles:
        # Image pipeline: WebP + thumbnail
        if a.get("image_url"):
            img_result = optimize_image(
                a["image_url"], out, a["slug"],
                backend_url=CONFIG.get("backend_url", "")
            )
            if img_result:
                a["image_webp"] = img_result.get("image_webp", "")
                a["image_thumb"] = img_result.get("image_thumb", "")

        # Auto OG jeśli brak og_image_custom
        if not a.get("og_image_custom"):
            generate_og_image(a, out, CONFIG.get("colors", {}))
        # Dopasuj produkty
        matched = match_products(a, products)
        add_cta_urls(matched, campaign_slug=a["slug"])
        by_placement = {"end": [], "sidebar": [], "inline": []}
        for p in matched:
            by_placement.setdefault(p.get("placement", "end"), []).append(p)

        # FAQ auto-detection
        faq_items = extract_faq_items(a.get("content", ""))
        # HowTo auto-detection
        howto_steps = extract_howto_steps(a.get("content", ""))

        render(env, "article.html", arts_dir / f"{a['slug']}.html",
               page={"slug": "article", "path": f"/artykuly/{a['slug']}.html"},
               article=a, related=get_related(articles, a, 3),
               products_end=by_placement["end"],
               products_sidebar=by_placement["sidebar"],
               products_inline=by_placement["inline"],
               faq_items=faq_items,
               howto_steps=howto_steps,
               article_slug=a["slug"], **common)

    # 4) Strony kategorii
    cat_dir = out / "kategoria"
    cat_dir.mkdir(exist_ok=True)
    for c in categories:
        cat_articles = [a for a in articles if a.get("category_id") == c["id"]]
        render(env, "category.html", cat_dir / f"{c['slug']}.html",
               page={"slug": "category", "path": f"/kategoria/{c['slug']}.html"},
               category=c, articles=cat_articles, categories=categories, **common)

    # 5) Strony autorów
    auth_dir = out / "autor"
    auth_dir.mkdir(exist_ok=True)
    active_authors = [a for a in authors if a.get("is_active")]
    for au in active_authors:
        # Dorzuć pomocnik: lista specjalizacji
        au["specializations_list"] = [s.strip() for s in (au.get("specializations") or "").split(",") if s.strip()]
        # Artykuły tego autora
        au_articles = [a for a in articles if a.get("author_id") == au["id"]]
        render(env, "author.html", auth_dir / f"{au['slug']}.html",
               page={"slug": "author", "path": f"/autor/{au['slug']}.html"},
               author=au, articles=au_articles, **common)

    # 6) Polityka / regulamin
    render(env, "polityka-prywatnosci.html", out / "polityka-prywatnosci.html",
           page={"slug": "privacy", "path": "/polityka-prywatnosci.html"}, **common)
    render(env, "regulamin.html", out / "regulamin.html",
           page={"slug": "terms", "path": "/regulamin.html"}, **common)

    # 7) sitemap / robots / RSS / AEO
    render(env, "sitemap.xml", out / "sitemap.xml",
           articles=articles, categories=categories, authors=active_authors, **common)
    render(env, "robots.txt", out / "robots.txt", **common)
    render(env, "rss.xml", out / "rss.xml", articles=articles, **common)
    render(env, "llms.txt", out / "llms.txt",
           articles=articles, categories=categories, authors=active_authors, **common)
    render(env, "llms-full.txt", out / "llms-full.txt",
           articles=articles, categories=categories, authors=active_authors, **common)

    # 7b) Strona 404 + Service Worker
    render(env, "404.html", out / "404.html",
           page={"slug": "404", "path": "/404.html"}, **common)
    render(env, "sw.js", out / "sw.js", **common)

    # 8) Statyczne + default assets + domain CSS
    copy_static(out)
    ensure_default_assets(out)
    generate_domain_css(out, CONFIG.get("colors", {}), CONFIG.get("theme", {}))

    # 8b) Security headers (.htaccess)
    generate_htaccess(out)

    # 9) JSON eksport dla client-side search
    (out / "data").mkdir(exist_ok=True)
    (out / "data" / "articles.json").write_text(
        json.dumps([{
            "slug": a["slug"], "title": a["title"], "excerpt": a.get("excerpt", ""),
            "category": a.get("category_name", ""), "category_slug": a.get("category_slug", ""),
            "author": a.get("author", ""), "tags": a.get("tags", ""),
            "published_at": str(a.get("published_at") or a.get("created_at")),
            "image_url": a.get("image_url", ""), "image_webp": a.get("image_webp", ""),
            "image_thumb": a.get("image_thumb", ""), "icon": a.get("icon", ""),
            "reading_time": a.get("reading_time", 5),
        } for a in articles], ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"\n✨ Gotowe. Output: {out}")
    print(f"🌐 Podgląd: cd {out.name} && python -m http.server 8766\n")
    return 0


def main():
    ap = argparse.ArgumentParser(description="Generator statycznych stron — multi-domain")
    ap.add_argument("--domain", type=str, default=None,
                    help="Domena do zbudowania (np. testnis2.pl)")
    ap.add_argument("--all", action="store_true",
                    help="Zbuduj wszystkie skonfigurowane domeny")
    ap.add_argument("--list", action="store_true",
                    help="Wyświetl listę dostępnych domen")
    ap.add_argument("--clean", action="store_true",
                    help="Wyczyść output przed buildem")
    args = ap.parse_args()

    if args.list:
        print("\nDostępne domeny:")
        for d in list_domains():
            dcfg = load_domain_config(d)
            role = dcfg["site"]["role"]
            brand = dcfg["site"]["brand"]
            main = dcfg["site"].get("main_domain", "")
            arrow = f" → {main}" if main else ""
            print(f"  {d:30s} [{role}] brand={brand}{arrow}")
        print()
        sys.exit(0)

    if args.all:
        domains = list_domains()
        print(f"\n🏗  Build ALL — {len(domains)} domen\n")
        failed = []
        for d in domains:
            try:
                result = build(clean=args.clean, domain=d)
                if result != 0:
                    failed.append(d)
            except Exception as exc:
                print(f"❌ {d}: {exc}")
                failed.append(d)
        print(f"\n{'='*60}")
        print(f"✅ Zbudowano: {len(domains) - len(failed)}/{len(domains)}")
        if failed:
            print(f"❌ Błędy: {', '.join(failed)}")
        sys.exit(1 if failed else 0)

    # Pojedyncza domena (domyślnie zdrowie.fit dla kompatybilności)
    sys.exit(build(clean=args.clean, domain=args.domain))


if __name__ == "__main__":
    main()
