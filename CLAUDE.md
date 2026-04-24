# Archaios SSG — Instrukcje dla Claude

Wieloddomenowy silnik statycznych stron (dawniej `zdrowie-fit-generator`, od v1.0.0 `archaios-ssg`). Obsługuje ~20 domen satelitarnych z jednego codebase (zdrowie.fit, psycho-edu.pl, testnis2.pl, archaios.ai i inne — patrz `domains/*.yaml`).

Architektura: **FastAPI backend (CMS + API) → build.py (Jinja2 + Pillow, multi-domain) → statyczny HTML per domena → SFTP do Cyber_Folks**.

## Kluczowe ścieżki

| Co | Gdzie |
|---|---|
| Generator (AKTYWNY) | `build.py` (584 linii) |
| Generator LEGACY (nie używać) | `generate.py` (824 linii — archiwum) |
| Config strony | `.env` (SITE_URL, GA4_ID, API_URL, USE_API) |
| Backend | `backend/app/main.py` (FastAPI, port 8765) |
| Config backendu | `backend/.env` (SECRET_KEY, ADMIN_PASSWORD min. 16 znaków) |
| Szablony HTML | `src/templates/` (base, index, article, author, category, sitemap.xml, rss.xml, robots.txt) |
| CSS/JS | `src/static/` (vanilla, bez bundlera) |
| Output (do deployu) | `output/<domain-slug>/` (np. `output/zdrowie-fit/`) |
| Backup DB | `scripts/backup_db.py` |
| CI/CD | `.github/workflows/deploy.yml` (push → main → SFTP) |

## Stack — co NIE używać

- **BRAK**: npm, package.json, Vite, Webpack, TypeScript, React, Tailwind, Bootstrap
- **BRAK**: integracji z AI (OpenAI/Anthropic) w kodzie — to czysty CMS + SSG
- **NIE edytować**: `generate.py` (legacy), `output/` (auto-generowane — edytuj `src/templates/`)

## Golden path — uruchomienie lokalne

**Terminal 1 — backend:**
```bash
cd backend
.\venv\Scripts\python.exe -m uvicorn app.main:app --host 127.0.0.1 --port 8765 --reload
```
- Admin: http://127.0.0.1:8765/admin/login
- API docs: http://127.0.0.1:8765/api/docs
- Login z `backend/.env` (ADMIN_USERNAME/ADMIN_PASSWORD)
- Przy pierwszym starcie: seed_service tworzy admina, 5 kategorii, 5 artykułów, autorów, produkty

**Terminal 2 — generator + preview:**
```bash
python build.py --domain zdrowie.fit --clean     # jedna domena
# python build.py --all --clean                  # wszystkie naraz
cd output/zdrowie-fit && python -m http.server 8766
```
- Podgląd: http://127.0.0.1:8766

**Flagi build.py:**
- `USE_API=true` (default) → pobiera z http://127.0.0.1:8765/api (backend musi działać)
- `USE_API=false` → SQLite direct (używane na CI, backend nie jest potrzebny)
- `--clean` → usuwa `output/<domain>/` przed buildem

## Modele danych (SQLAlchemy)

- **Article**: title, slug, excerpt, content, category_id, author_id, image_url, og_image_custom, tags (CSV), reading_time, bibliography (HTML), related_slugs, product_slugs, is_published, is_featured, meta_title, meta_description, views, published_at
- **Category**: name, slug, description, icon, color, sort_order
- **Author (E-E-A-T)**: name, slug, credentials, bio_short, bio_long, photo_url, email, linkedin, twitter, specializations (CSV), sort_order
- **Product**: name, slug, brand, tagline_short/long, cta_text, target_url (z UTM), target_category_slugs, target_tags, placement (sidebar/inline/end), priority (0–100), valid_from/to, kind (affiliate/own/partner)
- **AdminUser**: username, password_hash (bcrypt)

Auto-matching produktów do artykułów: [build.py:231](build.py#L231) `match_products()` — po target_tags/target_category_slugs/priority.
Auto-generacja OG images (1200x630, Pillow): [build.py:287](build.py#L287) `generate_og_image()`.

## Deployment

Push do `main` → GitHub Actions (`deploy.yml`, matrix strategy — jeden job per domena):
1. `matrix-setup` job czyta `domains/*.yaml` i generuje listę domen (albo jedną z `workflow_dispatch` input).
2. Per-domain: `pip install -r backend/requirements.txt Pillow python-dotenv httpx pyyaml`
3. `python build.py --domain <real-domain> --clean` (z `USE_API=false` + secrets)
4. SFTP mirror (`pressidium/lftp-mirror-action@v1`) do `/home/bestios/domains/<real-domain>/public_html`

Ręczne odpalenie pojedynczej domeny: GitHub Actions UI → workflow_dispatch → input `domain=zdrowie-fit` (slug bez `.yaml`).

**GitHub Secrets wymagane**: `FTP_HOST`, `FTP_PORT` (Cyber_Folks = **222**, nie 22!), `FTP_USER`, `FTP_PASS`, `GA4_ID`, `FB_PIXEL_ID`, `FB_PAGE`, `IG_HANDLE`, `NEWSLETTER_ENDPOINT`. `SITE_URL` i `FTP_REMOTE_DIR` są **wyliczane z `domains/<slug>.yaml`**, nie trzeba ich trzymać w sekretach.

**Parametry Cyber_Folks (produkcja)**:
- Host SSH/SFTP: `s159.cyber-folks.pl`
- Port SSH/SFTP: `222` (NIE 22; port 2223 to panel DirectAdmin, inna usługa)
- User: `bestios`
- Hasło SFTP = hasło do DirectAdmin (trzymane w GitHub Secrets jako `FTP_PASS`, nigdy w repo ani `.env` commitowanym)
- Fingerprint serwera (ED25519 SHA256): `l/jfbMOzZibqe/kD2WHuhdbpRiVIg/YcG8M9mt67lHM` — porównać przy pierwszym połączeniu
- DirectAdmin ma fail2ban: kilka złych logowań → ban IP na porcie 2223. Ban może też dotyczyć 222. Odblokowanie: ticket do supportu Cyber_Folks.
- Home: `/home/bestios`. `~/public_html` to **symlink do `domains/bestios.pl/public_html`** (domena główna konta) — NIE tam deployować.
- **Ścieżka deployu zdrowie.fit**: `/home/bestios/domains/zdrowie.fit/public_html` (wartość dla `FTP_REMOTE_DIR`).
- Na koncie są liczne inne domeny (archaios.ai, brokerbusiness.eu, psychozdrowie.online, spine.fit, yerbata.eu itp.) — uwaga żeby nie pomylić katalogów przy deployu.

## Zasady pracy nad projektem

1. **Zawsze edytuj `src/templates/`**, nie `output/<domain>/` (auto-generowany przez build.py).
2. **Po zmianach w `.env` / szablonach / CSS** → `python build.py --clean` + odśwież preview.
3. **Zmiana schematu DB** (modele w `backend/app/models/`) wymaga migracji — `Base.metadata.create_all()` robi tylko CREATE nowych tabel, nie ALTER. Rozważ Alembic przy większych zmianach.
4. **Kolorystyka** (sage green `#4a7c59`, terracotta `#d9724a`, ivory `#fdfcf9`) + fonty (Inter + Fraunces) — zmienne CSS w `src/static/css/style.css` na górze.
5. **SEO/A11y już ogarnięte**: Schema.org (Article, Author, BreadcrumbList), OG, Twitter Card, sitemap.xml, rss.xml, skip links, aria, focus-visible, reduced-motion. Nie psuć.
6. **Nigdy nie commituj `.env`** (już w `.gitignore`). Nigdy nie loguj `SECRET_KEY`/`ADMIN_PASSWORD`.
7. **Testuj zmiany UI w przeglądarce** na http://127.0.0.1:8766 — sprawdź homepage, artykuł, kategorię, autora, mobile (DevTools throttle).

## Częste zadania

- **Nowy artykuł**: admin panel → uzupełnij pola → `is_published=true` → rebuild + deploy.
- **Nowa kategoria/autor/produkt**: admin panel lub prosty SQL na `backend/zdrowiefit.db`.
- **Edycja layoutu**: `src/templates/base.html` (nav, footer, meta).
- **Dodaj nową stronę statyczną** (np. "O nas"): stwórz szablon w `src/templates/`, dodaj routing w [build.py:576](build.py#L576) `build()`, dodaj do `sitemap.xml`.
- **Zmiana OG image defaultowego**: podmień `src/static/img/og-default.png` (1200x630).
- **Backup przed destrukcyjnymi zmianami DB**: `python scripts/backup_db.py`.

## Checklist pre-deploy

- [ ] Build przechodzi bez błędów (`python build.py --clean`)
- [ ] Preview działa (http://127.0.0.1:8766) — homepage, artykuł, kategoria, autor, sitemap.xml, rss.xml
- [ ] `SITE_URL` w `.env` ustawione na produkcję (https://zdrowie.fit)
- [ ] `GA4_ID` i `FB_PIXEL_ID` uzupełnione (produkcja)
- [ ] Wszystkie linki wewnętrzne działają (brak 404)
- [ ] Mobile view OK (DevTools responsive)
- [ ] `ADMIN_PASSWORD` w produkcji ≠ lokalnego, 16+ znaków
