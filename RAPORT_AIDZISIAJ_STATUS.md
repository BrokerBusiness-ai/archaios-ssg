# Raport statusu satelity aidzisiaj.pl

**Data**: 2026-05-07 (automatyczny run)

---

## Co zostalo zrobione w tej sesji

### 1. Fix build.py — rekursywne kopiowanie assetów per-domena
- **Zmiana**: `custom_assets.iterdir()` → `custom_assets.rglob("*")`
- **Powod**: dotychczasowa logika kopiowala tylko pliki z top-level `domains/assets/<slug>/`, pomijajac podkatalogi (np. `testimonials/`)
- **Efekt**: teraz `domains/assets/aidzisiaj-pl/testimonials/messenger-01.webp` zostanie skopiowany do `output/aidzisiaj-pl/img/testimonials/messenger-01.webp`
- **Lokalizacja**: build.py, sekcja "6b) DODATKOWE assety per-domena"

### 2. Struktura katalogow na testimonials
- Utworzono: `domains/assets/aidzisiaj-pl/testimonials/README.md`
- README zawiera liste wymaganych plikow i zasady (format, rozmiar, anonimizacja, zgody)

### 3. Weryfikacja YAML aidzisiaj-pl.yaml
- Sekcja `testimonials` juz istnieje z 6 itemami (2x Messenger, 2x WhatsApp, 2x Signal)
- Kazdy item ma: channel, image, name, role, quote, alt
- Template `_testimonials.html` istnieje i jest wlaczony w `index.html`
- CSS dla `.testimonials*` i `.testimonial-card*` istnieje w `style.css` (36 regul)
- Lightbox JS jest inline w `_testimonials.html`

---

## Co POZOSTAJE do zrobienia (wymaga akcji uzytkownika)

### FAZA 1 — DNS + domena Cyber_Folks
- **Status**: Prawdopodobnie zrobione (domena istnieje na Cyber_Folks wg URL w tasku)
- **Sprawdzic**: rekordy DNS Brevo (DKIM, DMARC, SPF) — `nslookup -type=TXT aidzisiaj.pl ns1.cyberfolks.pl`

### FAZA 2 — Brevo configuration
- **BRAK** `newsletter.endpoint` w YAML — formularz Brevo nie zostal jeszcze utworzony
- **Do zrobienia**:
  1. Lista: Contacts → Lists → New → `aidzisiaj.pl — newsletter`
  2. Domain Authentication dla aidzisiaj.pl
  3. Sender: kontakt@aidzisiaj.pl
  4. Form: Sign-up z double opt-in
  5. Skopiowac Form Action URL do YAML `newsletter.endpoint`

### FAZA 3 — YAML
- **Zrobione** (plik istnieje, kompletny z testimonials)
- **Brakuje**: `newsletter.endpoint`, `analytics.ga4_id`

### FAZA 4 — Build + sanity
- **NIE zrobione** (brak output/aidzisiaj-pl/)
- **Komenda**: `python build.py --domain aidzisiaj.pl --clean`
- **UWAGA**: Build zakonczy sie sukcesem ale testimonials beda bez obrazkow (brak plikow .webp)

### FAZA 5 — Analytics
- **BRAK** `analytics.ga4_id` w YAML
- **Do zrobienia**:
  1. GA4: nowa property `aidzisiaj.pl`
  2. Search Console: verify przez GA4
  3. Sitemap: submit `sitemap.xml`
  4. Bing Webmaster: import z GSC
  5. Wpisac G-XXXXXXXXXX do YAML

### FAZA 6 — Deploy SFTP
- **NIE zrobione**
- WinSCP script w SATELLITE_MASTER.md (port 222, user bestios)

### FAZA 7 — Verification
- **NIE zrobione**
- Incognito check: HTTPS, Brotli, kafelki, newsletter form, GA4 real-time

### FAZA 8 — Brevo Automation (opcjonalna)
- **NIE zrobione**
- Welcome Series 5-mail + Weekly Digest RSS

### Testimonials — screeny od klientow
- **YAML gotowy** z 6 placeholderami
- **BRAKUJE plikow graficznych** — 6 screenow do dodania:
  - `domains/assets/aidzisiaj-pl/testimonials/messenger-01.webp`
  - `domains/assets/aidzisiaj-pl/testimonials/messenger-02.webp`
  - `domains/assets/aidzisiaj-pl/testimonials/whatsapp-01.webp`
  - `domains/assets/aidzisiaj-pl/testimonials/whatsapp-02.webp`
  - `domains/assets/aidzisiaj-pl/testimonials/signal-01.webp`
  - `domains/assets/aidzisiaj-pl/testimonials/signal-02.webp`
- **Pamietaj**: zanonimizuj dane kontaktowe, uzyskaj zgode na publikacje

---

## Kolejnosc krokow (rekomendowana)

1. Dodaj screeny testimoniali do `domains/assets/aidzisiaj-pl/testimonials/`
2. Skonfiguruj Brevo (lista, form, sender) → wpisz endpoint do YAML
3. Utworz GA4 property → wpisz ID do YAML
4. `python build.py --domain aidzisiaj.pl --clean`
5. Preview: `cd output\aidzisiaj-pl && python -m http.server 8766`
6. Deploy SFTP
7. Verify: HTTPS, compression, GA4 real-time, newsletter test
