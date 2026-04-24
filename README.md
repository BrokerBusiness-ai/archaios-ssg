# Zdrowie.fit

Holistyczna strona o zdrowiu — ciało i umysł. Backend FastAPI + statyczny generator → hosting Cyber_Folks.

## Struktura

```
zdrowie-fit-generator/
├── backend/              # FastAPI — admin panel + API (źródło artykułów)
│   ├── app/              # kod aplikacji
│   ├── templates/        # Jinja2 — panel admina
│   ├── venv/             # Python env
│   ├── .env              # SECRET_KEY, ADMIN_PASSWORD (nie commituj!)
│   └── zdrowiefit.db     # SQLite (auto-tworzona)
├── src/                  # ŹRÓDŁA generatora statycznej strony
│   ├── templates/        # Jinja2 szablony (base, index, article, ...)
│   └── static/           # CSS, JS, img do skopiowania do output
├── zdrowie-fit/          # OUTPUT — gotowa strona do wrzucenia na hosting
├── build.py              # Generator: fetch z API → render Jinja → statyczny HTML
└── .env                  # SITE_URL, FB_PIXEL_ID, GA4_ID, itp.
```

## Szybki start

```bash
# 1. Uruchom backend (admin panel + API)
cd backend
./venv/Scripts/python.exe -m uvicorn app.main:app --host 127.0.0.1 --port 8765 --reload

# 2. W nowym terminalu — zbuduj stronę
cd ..
./backend/venv/Scripts/python.exe build.py --clean

# 3. Podgląd lokalny
cd zdrowie-fit
python -m http.server 8766
# → http://127.0.0.1:8766
```

## Ważne URL-e (lokalnie)

| Co | URL |
|----|-----|
| Strona publiczna | http://127.0.0.1:8766/ |
| Panel admina | http://127.0.0.1:8765/admin/login |
| API Swagger | http://127.0.0.1:8765/api/docs |
| RSS | http://127.0.0.1:8766/rss.xml |
| Sitemap | http://127.0.0.1:8766/sitemap.xml |

## Deploy na Cyber_Folks

```
1. Zbuduj: python build.py --clean
2. Przez FTP/SFTP: wrzuć zawartość `zdrowie-fit/` do public_html/ na hostingu
3. (opcjonalnie) Backend na shared hostingu Cyber_Folks nie działa — musisz mieć VPS albo zostawić backend lokalnie do zarządzania artykułami, a potem builda i deployować HTML
```

## Konfiguracja produkcyjna

### `backend/.env`
- `SECRET_KEY` — wygeneruj: `python -c "import secrets; print(secrets.token_hex(32))"`
- `ADMIN_PASSWORD` — silne hasło (min. 16 znaków, mieszane)

### `.env` (generator)
- `SITE_URL=https://zdrowie.fit`
- `GA4_ID=G-XXXXXXXXXX` — po założeniu GA4
- `FB_PIXEL_ID=1234567890` — po założeniu Pixela
- `FB_PAGE=https://facebook.com/zdrowie.fit` — link do fanpage
- `NEWSLETTER_ENDPOINT` — endpoint Brevo / Mailchimp po konfiguracji

## Co jest w środku

### Backend (FastAPI)
- CRUD artykułów (publiczne + admin z JWT)
- Kategorie, tagi, paginacja, search, sort
- Admin panel server-rendered (`/admin`)
- Seed 5 artykułów + 5 kategorii przy pierwszym uruchomieniu

### Generator (build.py)
- Fetch artykułów z API (fallback: SQLite bezpośrednio)
- Renderowanie przez Jinja2
- Osobne pliki HTML na każdy artykuł
- Automatyczny `sitemap.xml`, `robots.txt`, `rss.xml`
- Schema.org: WebSite, Organization, Article, BreadcrumbList
- Open Graph + Twitter Card
- Generowane OG image przez Pillow
- Manifest PWA, favicon SVG

### Strona
- Warm color palette (sage green + terracotta + ivory)
- Inter + Fraunces (sans + serif display)
- Mobile bottom nav (thumb zone)
- Sticky scroll CTA (newsletter po scrollu)
- Reading progress bar
- Mobile search overlay
- RODO: cookie consent + polityka + regulamin
- Accessibility: skip link, aria, focus-visible, reduced-motion
```
