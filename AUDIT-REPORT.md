# AUDYT SILNIKA SSG — Archaios Demand Engine

**Data:** 2026-04-25  
**Audytor:** Claude Opus 4.6  
**Zakres:** Pełny audyt silnika pod kątem uniwersalności, 4×100 Lighthouse, SEO/AEO/GEO, bezpieczeństwo, responsywność, AI-readiness, automatyzacja  
**Skonfigurowane domeny:** 19 (zdrowie.fit + 18 satelitarnych)

---

## 1. OCENA OGÓLNA: 70/100

Silnik ma solidną bazę architektoniczną — multi-domain YAML config, Jinja2 templating, auto OG images, Schema.org, consent mode. Do osiągnięcia 4×100 Lighthouse i pełnej dominacji SEO/AEO/GEO brakuje **~15 kluczowych zmian**, większość to low-effort/high-impact.

---

## 2. SCORECARD SZCZEGÓŁOWY

| Obszar | Ocena | Status |
|--------|-------|--------|
| Schema.org (Article, Person, Breadcrumb, Org) | 92/100 | ✅ Dobra |
| Meta tags / OG / Twitter Card | 95/100 | ✅ Bardzo dobra |
| Sitemap / RSS / robots.txt | 75/100 | ⚠️ Do poprawy |
| AEO — AI-crawlable content | 35/100 | ❌ Krytyczne |
| Semantic HTML / heading hierarchy | 90/100 | ✅ Dobra |
| GEO — E-E-A-T / citations / fluency | 70/100 | ⚠️ Do poprawy |
| CSS/JS performance | 78/100 | ⚠️ Do poprawy |
| Image optimization | 45/100 | ❌ Krytyczne |
| Security headers | 30/100 | ❌ Krytyczne |
| GDPR / consent | 88/100 | ✅ Dobra |
| Responsywność / mobile | 85/100 | ✅ Dobra |
| Automatyzacja / API pipeline | 80/100 | ✅ Dobra |

---

## 3. CO DZIAŁA GENIALNIE (nie ruszać)

1. **Multi-domain architecture** — 19 domen z jednego codebase via YAML, `domain_config.py` + `build.py --domain X`. To jest MVP silnika i działa dobrze.
2. **Schema.org @graph** — WebSite + Organization + SearchAction w base.html, Article + BreadcrumbList + Person per strona. Lepsze niż 90% polskich serwisów.
3. **GA4 Consent Mode v2** — `gtag('consent', 'default', {denied})` → update po akceptacji. Zgodne z wymogami Google od marca 2024.
4. **Auto OG images** — Pillow generuje 1200×630 z kolorami domeny. Unikalne per artykuł.
5. **E-E-A-T author pages** — Person schema, credentials, specializations, bio, linki social. To jest fundament GEO.
6. **Mobile bottom nav** — thumb zone, safe-area-inset, 48px min touch targets. Dobre.
7. **Reading progress + scroll depth tracking** — GA4 events na 25/50/75/100%. Dobre dla analizy engagement.
8. **Product matching engine** — auto-match po kategoriach/tagach z priority scoring. Lejek sprzedażowy wbudowany.
9. **Dark mode** — CSS variables + localStorage + prefers-color-scheme. Gotowe.
10. **Print styles** — ukrywa header/newsletter/sidebar. Rzadko kto to robi.

---

## 4. CO TRZEBA NAPRAWIĆ — KRYTYCZNE (❌)

### 4.1 AEO: Brak llms.txt i AI-dedykowanego contentu

**Problem:** Boty AI (ChatGPT, Perplexity, Claude) nie mają dedykowanego endpointu do crawlowania. llms.txt to nowy standard (analogiczny do robots.txt dla AI).

**Rozwiązanie:** Dodać do build.py generowanie:
- `/llms.txt` — krótki opis serwisu + lista najważniejszych URL-i
- `/llms-full.txt` — pełna treść wszystkich artykułów w plain text (bez HTML)
- Rozszerzenie robots.txt o reguły dla AI botów

### 4.2 Image Optimization: Brak WebP/AVIF, srcset, width/height

**Problem:**
- OG images generowane jako PNG (~200-400KB każdy), nie WebP (~30-60KB)
- Brak `srcset` i `sizes` na `<img>` — przeglądarka nie może wybrać optymalnego rozmiaru
- Brak explicit `width` i `height` na `<img>` → CLS (Cumulative Layout Shift)
- Brak lazy loading na article cards (tylko hero image ma `loading="eager"`)

**Rozwiązanie:**
- Pillow: generuj WebP oprócz PNG (fallback)
- Dodaj `<picture>` z `<source type="image/webp">`
- Dodaj `width="1200" height="630"` na OG images
- Dodaj `loading="lazy"` na article cards
- Rozważ `srcset` dla responsive images

### 4.3 Security Headers: Brak CSP, HSTS, X-Frame-Options

**Problem:** Statyczny site na Cyber_Folks nie ma żadnych security headers. To obniża:
- Lighthouse Security score
- Ochronę przed XSS, clickjacking, MIME sniffing
- Ranking w Google (HTTPS + headers = sygnał)

**Rozwiązanie:** Dodać `.htaccess` do outputu (Cyber_Folks = Apache):
```apache
Header set X-Content-Type-Options "nosniff"
Header set X-Frame-Options "SAMEORIGIN"
Header set X-XSS-Protection "0"
Header set Referrer-Policy "strict-origin-when-cross-origin"
Header set Permissions-Policy "camera=(), microphone=(), geolocation=()"
Header set Content-Security-Policy "default-src 'self'; script-src 'self' 'unsafe-inline' https://www.googletagmanager.com https://connect.facebook.net; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; font-src https://fonts.gstatic.com; img-src 'self' data: https:; connect-src 'self' https://www.google-analytics.com"
Header set Strict-Transport-Security "max-age=31536000; includeSubDomains"
```

---

## 5. CO TRZEBA NAPRAWIĆ — WAŻNE (⚠️)

### 5.1 Sitemap: Brakuje kategorii, autorów, sitemap-index

**Problem:**
- Sitemap zawiera tylko artykuły + privacy/terms. Brak stron kategorii i autorów.
- Brak `<image:title>` i `<image:caption>` w image sitemap
- Przy 19 domenach powinien być sitemap-index.xml

**Rozwiązanie:** Rozszerzyć template sitemap.xml o kategorie i autorów. Dodać sitemap-index dla multi-domain.

### 5.2 CSS Performance: Google Fonts render-blocking, brak minify

**Problem:**
- `<link rel="stylesheet" href="https://fonts.googleapis.com/css2?...">` blokuje rendering
- CSS nie jest minifikowany (~12KB raw)
- Brak critical CSS inline w `<head>`

**Rozwiązanie:**
- `<link rel="preload" as="style">` + `onload` swap dla fontów
- Lub self-host fontów (Inter + Fraunces) → eliminacja external request
- CSS minify w build.py (cssmin lub regex)
- Critical CSS: inline above-the-fold styles w `<style>` w `<head>`

### 5.3 GEO: Brak claim source linking i FAQ schema

**Problem:**
- Artykuły mają bibliografię, ale twierdzenia w treści nie linkują do konkretnych pozycji bibliografii (brak `[1]`, `[2]` inline)
- Brak FAQPage schema (Google + AI engines kochają FAQ)
- Brak HowTo schema dla poradnikowych artykułów

### 5.4 RSS: Brak `<author>` i `<enclosure>` (image)

**Problem:** RSS nie zawiera autora ani obrazka artykułu. Agregatory (Feedly, Inoreader) i AI crawlery potrzebują tych danych.

### 5.5 CI/CD: Deploy.yml hardcodowany na zdrowie-fit

**Problem:** `localDir: './zdrowie-fit'` — nie działa z multi-domain `output/domain-name/`. Workflow nie obsługuje `--domain` ani `--all`.

---

## 6. CO DODAĆ — NICE TO HAVE (do 100/100)

1. **Service Worker** — offline reading, push notifications
2. **Prerender hints** — `<link rel="prerender">` dla likely next pages
3. **JSON-LD FAQ schema** — auto z `<details>` lub `<h3>` + `<p>` patterns
4. **Structured data testing** — walidacja w build pipeline
5. **Core Web Vitals monitoring** — CrUX API integration
6. **RSS autodiscovery** per kategoria
7. **hreflang** — jeśli będą wersje en/de
8. **`<link rel="dns-prefetch">` dla third-party** — GA, FB pixel
9. **Minifikacja HTML** — htmlmin w build.py
10. **Compression** — `.htaccess` gzip/brotli

---

## 7. PROPOZYCJA NOWEJ NAZWY

Obecna nazwa `zdrowie-fit-generator` jest specyficzna dla jednej domeny. Przy 19 domenach potrzeba nazwy uniwersalnej.

**Propozycje:**

| Nazwa | Uzasadnienie |
|-------|-------------|
| **archaios-ssg** | Prosto, w brand Archaios. SSG = Static Site Generator |
| **archaios-forge** | "Forge" = kuźnia stron. Mocne, universalne |
| **archaios-press** | Nawiązanie do "publishing". Eleganckie |
| **demand-engine-ssg** | Zachowuje "Demand Engine" z parent katalogu |
| **orbit-ssg** | Domeny satelitarne "orbitują" wokół głównej |

**Rekomendacja: `archaios-ssg`** — spójne z organizacją GitHub `archaios-ai`, krótkie, profesjonalne.

---

## 8. WERSJONOWANIE NA GITHUB

### Setup:

```bash
# W katalogu projektu
git init  # jeśli jeszcze nie ma
git remote add origin git@github.com:archaios-ai/archaios-ssg.git

# Semantic versioning
git tag -a v1.0.0 -m "Initial release: multi-domain SSG with 19 domains"
git push origin main --tags
```

### Konwencja wersji:

- **v1.0.0** — obecny stan (multi-domain, working build)
- **v1.1.0** — po dodaniu AEO (llms.txt, image optimization)
- **v1.2.0** — po dodaniu security headers + sitemap fix
- **v2.0.0** — po major refactor (np. API-first, headless CMS)

### GitHub repo structure:

```
archaios-ssg/
├── .github/workflows/deploy.yml  # multi-domain deploy
├── build.py                       # generator
├── domain_config.py               # domain loader
├── domains/                       # YAML configs per domain
├── src/templates/                 # Jinja2 templates
├── src/static/                    # CSS/JS
├── backend/                       # FastAPI CMS
├── scripts/                       # backup, utils
├── CLAUDE.md                      # instrukcje AI
├── CHANGELOG.md                   # historia zmian
├── VERSION                        # current version
└── README.md                      # dokumentacja
```

---

## 9. PROMPTY DO NAPRAWY

### PROMPT 1: AEO — llms.txt + AI-readiness (Claude Code / DeepSeek)

```
Dodaj do build.py generowanie dwóch plików AEO:

1. `/llms.txt` — format:
```
# {site.name}
> {site.description}

## Artykuły
{lista artykułów: tytuł + URL, po jednym na linię}

## Autorzy  
{lista autorów: imię + credentials + URL}

## Kontakt
{site.email}
```

2. `/llms-full.txt` — pełna treść plain text:
```
# {site.name} — Pełna treść

---
Tytuł: {article.title}
Autor: {article.author}
Data: {article.published_at}
Kategoria: {article.category_name}
URL: {site.url}/artykuly/{article.slug}.html

{article.content — stripped HTML, plain text}

Źródła:
{article.bibliography — stripped HTML}
---
{następny artykuł}
```

3. Rozszerz robots.txt template o:
```
# AI Crawlers
User-agent: GPTBot
Allow: /
User-agent: ChatGPT-User  
Allow: /
User-agent: Claude-Web
Allow: /
User-agent: PerplexityBot
Allow: /
User-agent: Amazonbot
Allow: /

# llms.txt
# See /llms.txt and /llms-full.txt
```

Pliki: build.py (dodaj render llms.txt i llms-full.txt w sekcji "7) sitemap / robots / RSS"), src/templates/llms.txt (nowy), src/templates/llms-full.txt (nowy), src/templates/robots.txt (rozszerz).
```

### PROMPT 2: Image Optimization — WebP + srcset + CLS fix (Claude Code)

```
Zoptymalizuj obrazy w silniku SSG:

1. build.py — generate_og_image():
   - Dodaj zapis WebP obok PNG: `img.save(out_path_webp, "WebP", quality=85, method=6)`
   - Ustaw article["og_webp"] = True po generacji

2. src/templates/article.html — hero image:
   Zamień:
   <img src="{{ article.image_url }}" alt="{{ article.title }}" itemprop="image" loading="eager" fetchpriority="high">
   Na:
   <picture>
     <source srcset="{{ article.image_url | replace('.png', '.webp') | replace('.jpg', '.webp') }}" type="image/webp">
     <img src="{{ article.image_url }}" alt="{{ article.title }}" itemprop="image" loading="eager" fetchpriority="high" width="1200" height="675" decoding="async">
   </picture>

3. src/templates/_article_card.html:
   - Dodaj loading="lazy" na wszystkie img w kartach
   - Dodaj width i height

4. src/templates/base.html:
   - Dodaj <link rel="preconnect" href="https://fonts.googleapis.com"> (już jest)
   - Zamień Google Fonts <link rel="stylesheet"> na:
   <link rel="preload" as="style" href="https://fonts.googleapis.com/css2?..." onload="this.onload=null;this.rel='stylesheet'">
   <noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?..."></noscript>
```

### PROMPT 3: Security Headers — .htaccess (Claude Code)

```
Dodaj generowanie pliku .htaccess w build.py:

W funkcji build(), po copy_static(out), dodaj:
```python
htaccess_content = """# Security Headers
<IfModule mod_headers.c>
    Header set X-Content-Type-Options "nosniff"
    Header set X-Frame-Options "SAMEORIGIN"
    Header set X-XSS-Protection "0"
    Header set Referrer-Policy "strict-origin-when-cross-origin"
    Header set Permissions-Policy "camera=(), microphone=(), geolocation=()"
    Header set Content-Security-Policy "default-src 'self'; script-src 'self' 'unsafe-inline' https://www.googletagmanager.com https://connect.facebook.net; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; font-src https://fonts.gstatic.com; img-src 'self' data: https:; connect-src 'self' https://www.google-analytics.com https://www.facebook.com"
    Header always set Strict-Transport-Security "max-age=31536000; includeSubDomains; preload"
</IfModule>

# Compression
<IfModule mod_deflate.c>
    AddOutputFilterByType DEFLATE text/html text/css text/javascript application/javascript application/json image/svg+xml application/xml text/xml
</IfModule>

# Cache
<IfModule mod_expires.c>
    ExpiresActive On
    ExpiresByType text/html "access plus 1 hour"
    ExpiresByType text/css "access plus 1 year"
    ExpiresByType application/javascript "access plus 1 year"
    ExpiresByType image/png "access plus 1 year"
    ExpiresByType image/webp "access plus 1 year"
    ExpiresByType image/svg+xml "access plus 1 year"
    ExpiresByType application/json "access plus 1 day"
    ExpiresByType application/xml "access plus 1 hour"
</IfModule>

# Pretty URLs (opcjonalnie)
RewriteEngine On
RewriteCond %{HTTPS} off
RewriteRule ^ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]

# Error pages
ErrorDocument 404 /404.html
"""
(out / ".htaccess").write_text(htaccess_content, encoding="utf-8")
```

Dodaj też template `src/templates/404.html` (extends base.html, przyjazna strona 404).
```

### PROMPT 4: Sitemap fix — kategorie, autorzy, images (Claude Code)

```
Rozszerz src/templates/sitemap.xml:

1. Dodaj namespace image: xmlns:image="http://www.google.com/schemas/sitemap-image/1.1"
2. Po artykułach dodaj bloki kategorii:
   {% for c in categories %}
   <url>
       <loc>{{ site.url }}/kategoria/{{ c.slug }}.html</loc>
       <changefreq>weekly</changefreq>
       <priority>0.7</priority>
   </url>
   {% endfor %}

3. Dodaj autorów (przekaż authors do kontekstu render w build.py):
   {% for au in authors %}
   <url>
       <loc>{{ site.url }}/autor/{{ au.slug }}.html</loc>
       <changefreq>monthly</changefreq>
       <priority>0.6</priority>
   </url>
   {% endfor %}

4. Rozszerz image sitemap o:
   <image:title>{{ a.title | e }}</image:title>
   <image:caption>{{ a.excerpt | e }}</image:caption>

5. W build.py: przekaż authors i categories do render sitemap.xml
```

### PROMPT 5: CSS Performance — critical CSS + minify (Claude Code)

```
Zoptymalizuj CSS w build.py:

1. Dodaj minifikację CSS w copy_static():
   - Po skopiowaniu style.css, zminifikuj: usuń komentarze, zbędne whitespace
   - Prosty regex: re.sub(r'/\*.*?\*/', '', css, flags=re.DOTALL) + re.sub(r'\s+', ' ', css)

2. Wyekstrahuj critical CSS (above-the-fold):
   - Wyciągnij z style.css: :root, body, .header, .hero, .container, .btn, .nav, .skip-link
   - Wstaw jako <style> w <head> base.html (nowy blok {% block critical_css %})
   - Resztę CSS załaduj async: <link rel="preload" as="style" href="/css/style.css" onload="...">

3. Minifikuj JS (main.js, article.js):
   - Prosty strip: usuń komentarze //, /* */ i zbędne whitespace
```

### PROMPT 6: Schema.org rozszerzenia — FAQ + HowTo (Claude Code)

```
Dodaj auto-generowanie dodatkowych Schema.org w article.html:

1. FAQPage schema:
   - W build.py: parsuj content artykułu, szukaj <h2> lub <h3> kończących się "?" → to FAQ
   - Zbierz pary pytanie + następny paragraf (odpowiedź)
   - Dodaj do article context: article["faq_items"] = [{"q": "...", "a": "..."}, ...]
   - W article.html, jeśli faq_items:
   <script type="application/ld+json">
   {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
     {% for faq in article.faq_items %}
     {"@type":"Question","name":{{ faq.q | tojson }},"acceptedAnswer":{"@type":"Answer","text":{{ faq.a | tojson }}}}{% if not loop.last %},{% endif %}
     {% endfor %}
   ]}
   </script>

2. HowTo schema (opcjonalnie):
   - Jeśli artykuł ma ordered list <ol> w content → rozważ HowTo
```

### PROMPT 7: CI/CD Multi-domain deploy (Claude Code)

```
Zrefaktoruj .github/workflows/deploy.yml dla multi-domain:

1. Zmień build step:
   run: |
     python build.py --all --clean
   # Lub dla konkretnej domeny:
   # python build.py --domain ${{ github.event.inputs.domain }} --clean

2. Dodaj matrix strategy dla deploymentu:
   - Każda domena ma swoje FTP_REMOTE_DIR
   - Secrets per domena: FTP_REMOTE_DIR_ZDROWIE_FIT, FTP_REMOTE_DIR_TESTNIS2_PL, etc.
   - Lub: plik domains/deploy-map.json z mapowaniem domena → remote_dir

3. Dodaj workflow_dispatch z input domain:
   on:
     workflow_dispatch:
       inputs:
         domain:
           description: 'Domena do deployu (lub "all")'
           required: true
           default: 'all'

4. Zmień localDir na dynamiczny:
   localDir: './output/${{ matrix.domain }}/'
```

### PROMPT 8: Rename projektu + versioning (Claude Code)

```
Zmień nazwę projektu z zdrowie-fit-generator na archaios-ssg:

1. Utwórz CHANGELOG.md z historią zmian
2. Utwórz VERSION z "1.0.0"
3. Zaktualizuj CLAUDE.md — zmień referencje do starej nazwy
4. Zaktualizuj build.py docstring
5. Zaktualizuj backend/app/core/config.py — APP_NAME na "Archaios SSG API"
6. Dodaj tag git: git tag -a v1.0.0 -m "v1.0.0: Multi-domain SSG engine"
7. Ustaw remote na archaios-ai/archaios-ssg
```

---

## 10. PRIORYTETYZACJA (co robić najpierw)

| Priorytet | Zadanie | Impact | Effort |
|-----------|---------|--------|--------|
| 1 | Security headers (.htaccess) | Wysoki | 15 min |
| 2 | Image optimization (WebP + width/height) | Wysoki | 1h |
| 3 | AEO: llms.txt | Wysoki | 30 min |
| 4 | Sitemap rozszerzenie | Średni | 20 min |
| 5 | CSS performance (fonts + minify) | Średni | 45 min |
| 6 | Schema.org FAQ | Średni | 30 min |
| 7 | CI/CD multi-domain | Średni | 1h |
| 8 | Rename + versioning | Niski | 20 min |

**Łączny czas do 4×100:** ~4-5h pracy z Claude Code.

---

## 11. PORÓWNANIE Z NAJLEPSZYMI SERWISAMI

| Feature | Archaios SSG | Healthline | WebMD | Medical News Today |
|---------|-------------|------------|-------|-------------------|
| Schema.org Article | ✅ | ✅ | ✅ | ✅ |
| FAQPage schema | ❌ | ✅ | ✅ | ✅ |
| llms.txt | ❌ | ❌ | ❌ | ❌ |
| WebP images | ❌ | ✅ | ✅ | ✅ |
| Critical CSS | ❌ | ✅ | ✅ | ✅ |
| Security headers | ❌ | ✅ | ✅ | ✅ |
| E-E-A-T author pages | ✅ | ✅ | ✅ | ✅ |
| Consent Mode v2 | ✅ | ✅ | ✅ | ✅ |
| Dark mode | ✅ | ❌ | ❌ | ❌ |
| Multi-domain | ✅ | ❌ | ❌ | ❌ |
| Auto OG images | ✅ | ❌ | ❌ | ❌ |
| PWA manifest | ✅ | ✅ | ❌ | ❌ |
| Product matching | ✅ | ✅ (ads) | ✅ (ads) | ✅ (ads) |

**Wniosek:** Po implementacji promptów 1-6, silnik będzie na poziomie lub POWYŻEJ dużych serwisów — z przewagą w AEO (llms.txt) i multi-domain.
