# Archaios SSG — Master plik tworzenia nowej satelity

**Wersja**: 1.0 (2026-05-01) · **Bazuje na**: realnym deployu zdrowie.fit
**Czas**: ~2h (1.5h pracy + 30 min czekania na DNS) · **Powtarzalna procedura dla każdej z ~12 satelit rodziny Archaios**

---

# CZĘŚĆ 1 — KRÓTKI PROMPT (wklej do nowego czatu)

```
Tworzymy nową satelitę z rodziny Archaios SSG.

PEŁNA PROCEDURA, GOTCHY, KOMENDY: docs/SATELLITE_MASTER.md (część 2-4 tego pliku)
WZÓR DZIAŁAJĄCY: domains/zdrowie-fit.yaml

INPUTS dla tej satelity:

DOMAIN_FQDN: {{np. testnis2.pl}}
DOMAIN_SLUG: {{slug bez kropki, np. testnis2-pl}}
BRAND_NAME: {{np. Test NIS2}}
TAGLINE: {{1 zdanie, max 80 znaków}}
DESCRIPTION: {{120-160 znaków, do meta description}}
LOGO_TEXT: {{wyświetlana nazwa, np. Test}}
LOGO_ACCENT: {{terakotowa końcówka, np. NIS2}}
ROLE: {{satellite | flagship}}
FUNNEL_TYPE: {{article_cta | lead_magnet | direct_sale | brand_awareness}}
MAIN_DOMAIN: {{flagowiec, np. archaios.ai}}
COLOR_PRIMARY: {{#hex}}
COLOR_ACCENT: {{#hex terakotowy}}
COLOR_TRUST: {{#hex niebieski (badania/źródła)}}
CONTACT_EMAIL: kontakt@{{DOMAIN_FQDN}}

KATEGORIE (2-5):
1. {{nazwa, slug, icon emoji, color hex}}
2. ...

PILLARS (4-6 klikalnych kafelków):
1. {{icon, title, desc 1 zdanie, link do /kategoria/{slug}.html}}
2. ...

PRODUCTS (1-3 affiliate/own dla CTA w artykułach):
1. {{name, target_url z UTM, target_category_slugs CSV, target_tags CSV}}

DEPLOY_BACKEND: false  # true tylko gdy realna potrzeba API/webhook

INSTRUKCJE DLA CIEBIE:
1. Przeczytaj `docs/SATELLITE_MASTER.md` (CZĘŚĆ 2-4) — to twój master plan
2. Przeczytaj `domains/zdrowie-fit.yaml` jako wzór dla nowego YAML-a
3. Prowadź mnie FAZAMI 0-7 (8 i 9 opcjonalne) — jedna faza = jedna wiadomość
4. Po każdej fazie pytaj o output (screenshot/PowerShell) zanim ruszysz dalej
5. Gotchy z CZĘŚCI 4 znaj na pamięć — nie pozwól mi w nie wpaść
6. Gdy faza zakończona poprawnie, napisz "✅ Faza X done" i przejdź do następnej
7. Cel: ~2h całość (1.5h pracy + 30 min czekania)
8. Definition of Done: checklist na końcu CZĘŚCI 5

Startujemy od FAZY 1 (DNS + domena Cyber_Folks). Daj mi step-by-step co klikam.
```

---

# CZĘŚĆ 2 — INPUTS TEMPLATE (skopiuj jako `domains/{{DOMAIN_SLUG}}.yaml`)

```yaml
# Wzór działający: domains/zdrowie-fit.yaml

domain: ""                # np. "testnis2.pl"
name: ""                  # np. "Test NIS2"
tagline: ""               # np. "Compliance NIS2 oparty na faktach"
description: ""           # 120-160 znaków, meta description
lang: "pl"
locale: "pl_PL"

brand: ""                 # np. "archaios"
main_domain: ""           # flagowiec, np. "archaios.ai"
role: "satellite"         # satellite | flagship
funnel_type: "article_cta"  # article_cta | lead_magnet | direct_sale | brand_awareness

logo_mark: "◐"
logo_text: ""             # np. "Test"
logo_accent: ""           # terakotowa końcówka, np. "NIS2"

colors:
  primary: "#4a7c59"
  primary_dark: "#3a6347"
  primary_light: "#7fb3a3"
  accent: "#d9724a"
  accent_dark: "#b85a38"
  trust: "#5b8def"

hero:
  eyebrow: ""             # np. "Compliance dla średnich firm"
  h1: ""                  # główny komunikat, max 80 znaków
  subtitle: ""            # 1 zdanie pod h1
  cta_primary:
    text: "Czytaj artykuły"
    url: "/artykuly.html"
  cta_secondary:
    text: "O projekcie"
    url: "#o-nas"

pillars:
  - icon: ""              # emoji
    title: ""
    desc: ""
    link: ""              # /kategoria/{slug}.html

categories:
  - name: ""
    slug: ""
    icon: ""
    color: "#4a7c59"

about:
  intro: ""               # 1-2 zdania
  values:
    - ""                  # 3-4 valuesy

newsletter:
  endpoint: ""            # Form Action URL z Brevo (https://sibforms.com/serve/...)
  provider: "brevo"
  title_highlight: ""
  title_rest: ""
  subtitle: ""

analytics:
  ga4_id: ""              # G-XXXXXXXXXX z Google Analytics 4
  fb_pixel_id: ""

footer:
  tagline: ""
  disclaimer: ""

email: ""                 # kontakt@DOMAIN

founder: "Marek Porycki"
foundingDate: "2026-05"
address:
  locality: "Warszawa"
  region: "mazowieckie"
  country: "PL"

social:
  fb: ""
  ig: ""
  yt: ""
  tw: ""

products:
  - name: ""
    slug: ""
    brand: ""
    tagline_short: ""
    cta_text: "Sprawdź"
    target_url: ""
    placement: "end"
    target_category_slugs: ""
    target_tags: ""
    priority: 50
    kind: "own"
```

---

# CZĘŚĆ 3 — FAZY (kolejność z dependencies)

## FAZA 0 — Pre-flight (5 min, raz dla całej rodziny)

- [ ] Konto Cyber_Folks bestios działa: `ssh -p 222 bestios@s159.cyber-folks.pl`
- [ ] Konto Brevo z verified senderem
- [ ] Konto Google Analytics + Search Console
- [ ] `cd C:\PYTHON\ARCHAIOS Demand Engine\zdrowie-fit-generator && git pull`

## FAZA 1 — DNS + domena Cyber_Folks (15 min + 30 min czekania)

1. **Domena dodana w Cyber_Folks** (DirectAdmin → Domeny → Dodaj domenę)
2. **Subdomena `www`** (DirectAdmin → Zarządzanie subdomenami)
3. **DNS dla Brevo** (z Brevo → Senders → Domains → Authenticate, daje 4 rekordy):
   - `@` TXT `brevo-code:{{KOD}}`
   - `brevo1._domainkey` CNAME `b1.{{DOMAIN-SLUG}}.dkim.brevo.com.`
   - `brevo2._domainkey` CNAME `b2.{{DOMAIN-SLUG}}.dkim.brevo.com.`
   - `_dmarc` TXT `v=DMARC1; p=none; sp=none; rua=mailto:rua@dmarc.brevo.com`
   - **SPF MODYFIKUJ** istniejący na: `@` TXT `v=spf1 a mx include:_spf.cyberfolks.pl include:spf.brevo.com -all`
4. ⚠️ **Każdy rekord = klik „Zapisz formularz"** — bez tego strefa się nie commituje
5. **Forwarder anty-greylisting**: E-Mail Manager → Forwarders → `kontakt@DOMAIN` → Twój Gmail
6. **Skrzynka kontakt@**: E-Mail Accounts → Create
7. **Czekaj 15-30 min**, potem weryfikacja:

```powershell
nslookup -type=TXT DOMAIN_FQDN ns1.cyberfolks.pl
# Sprawdź czy widać Brevo code + nowy SPF
```

## FAZA 2 — Brevo configuration (15 min)

1. **Lista**: Contacts → Lists → New → `{{DOMAIN_FQDN}} — newsletter`
2. **Domain Authentication**: Settings → Senders/Domains → `{{DOMAIN_FQDN}}` → Authenticate → 4× zielony
3. **Sender**: kontakt@DOMAIN → kod weryfikacyjny dotrze przez forwarder na Gmail
4. **Form**: Marketing → Sign-up Forms → Create (Full page/embedded):
   - Name: `{{DOMAIN_FQDN}} — newsletter`
   - List: utworzona w pkt 1
   - **Confirmation type: Double opt-in** (KRYTYCZNE)
   - Confirmation email: wklej `email-templates/confirmation.html`
   - Welcome email: wklej `email-templates/welcome.html`
   - Spolszcz 4 messages (success/invalid/error/empty)
   - Sender: kontakt@DOMAIN
   - Final URL: `https://{{DOMAIN_FQDN}}/dziekujemy.html`
5. **Skopiuj Form Action URL** (`https://sibforms.com/serve/...`) — używamy w fazie 3

## FAZA 3 — `domains/{{DOMAIN_SLUG}}.yaml` (10 min)

Skopiuj template z CZĘŚCI 2, podmień wszystkie placeholdery, zapisz jako `domains/{{DOMAIN_SLUG}}.yaml`.

Wklej Form Action URL z FAZY 2 do `newsletter.endpoint`.

## FAZA 4 — Build + sanity (3 min)

```powershell
cd "C:\PYTHON\ARCHAIOS Demand Engine\zdrowie-fit-generator"
python build.py --domain {{DOMAIN_FQDN}} --clean

# Sanity (bez tego = ślepy strzał)
$idx = "output\{{DOMAIN_SLUG}}\index.html"
$css = "output\{{DOMAIN_SLUG}}\css\style.css"
"klikalne pillars: "         + (Select-String $idx -Pattern 'class="pillar pillar--link"' -AllMatches).Matches.Count
"calc() OK (>=3): "          + (Select-String $css -Pattern 'calc\([^)]*\s\+\s[^)]*\)' -AllMatches).Matches.Count
"calc() ZLAMANE (=0): "      + (Select-String $css -Pattern 'calc\([^)]*[a-z%0-9]\+[a-z0-9]' -AllMatches).Matches.Count
"sibforms (Brevo Action): "  + (Select-String $idx -Pattern 'sibforms\.com' -AllMatches).Matches.Count
"<h1 (=1): "                 + (Select-String $idx -Pattern '<h1[\s>]' -AllMatches).Matches.Count
"selektor h1,h2,h3,h4 (=0): "+ (Select-String $idx -Pattern 'h1,h2,h3,h4' -AllMatches).Matches.Count
Test-Path "output\{{DOMAIN_SLUG}}\dziekujemy.html","output\{{DOMAIN_SLUG}}\wypisano.html"
```

## FAZA 5 — Analytics (5 min)

1. **GA4**: https://analytics.google.com → Property (NIE konto), nazwa `{{DOMAIN_FQDN}}`, strefa Warszawa, waluta PLN. Skopiuj **G-XXXXXXXXXX**
2. Wklej do YAML → `analytics.ga4_id: "G-XXX"`
3. **Search Console**: Add property URL prefix `https://{{DOMAIN_FQDN}}/` → verify przez **Google Analytics** (instant)
4. **Sitemap**: SC → Mapy witryn → wpisz `sitemap.xml` → Wyślij
5. **Bing**: https://www.bing.com/webmasters → Import from GSC (1 klik)
6. Rebuild ponowny (żeby GA4 wjechał do HTML):

```powershell
python build.py --domain {{DOMAIN_FQDN}} --clean
```

## FAZA 6 — Deploy SFTP (3 min)

```powershell
$winscp = "C:\Program Files (x86)\WinSCP\WinSCP.com"
$local  = "C:\PYTHON\ARCHAIOS Demand Engine\zdrowie-fit-generator\output\{{DOMAIN_SLUG}}"
$remote = "/home/bestios/domains/{{DOMAIN_FQDN}}/public_html"
$srv = "s159.cyber-folks.pl"; $port = 222; $user = "bestios"
$hostkey = "ssh-ed25519 255 SHA256:l/jfbMOzZibqe/kD2WHuhdbpRiVIg/YcG8M9mt67lHM"
do {
    $secure = Read-Host "Haslo SFTP" -AsSecureString
    $bstr = [Runtime.InteropServices.Marshal]::SecureStringToBSTR($secure)
    $plain = [Runtime.InteropServices.Marshal]::PtrToStringAuto($bstr)
    [Runtime.InteropServices.Marshal]::ZeroFreeBSTR($bstr)
} while (-not $plain)
Add-Type -AssemblyName System.Web
$enc = [System.Web.HttpUtility]::UrlEncode($plain)
$script = @"
open sftp://${user}:${enc}@${srv}:${port}/ -hostkey="$hostkey"
option batch abort
option confirm off
option transfer binary
synchronize remote -mirror "$local" "$remote"
close
exit
"@
$tmp = [IO.Path]::GetTempFileName() + ".txt"
Set-Content -Path $tmp -Value $script -Encoding ASCII
& $winscp /script=$tmp
"Exit: $LASTEXITCODE (0=OK)"
Remove-Item $tmp; $plain = $null
```

## FAZA 7 — Verification (5 min)

```powershell
# Compression check (oczekiwane: br = Brotli)
$req = [System.Net.WebRequest]::Create("https://{{DOMAIN_FQDN}}/")
$req.Headers.Add("Accept-Encoding", "gzip, deflate, br")
$req.AutomaticDecompression = [System.Net.DecompressionMethods]::None
$resp = $req.GetResponse()
"Compression: " + $resp.Headers["Content-Encoding"]
$resp.Close()

# Sitemap check
$r = Invoke-WebRequest -Uri "https://{{DOMAIN_FQDN}}/sitemap.xml" -UseBasicParsing
"Sitemap status: $($r.StatusCode), Content-Type: $($r.Headers.'Content-Type')"
```

Otwórz w **incognito** + Ctrl+Shift+R:
- [ ] `https://{{DOMAIN_FQDN}}/` — kafelki klikalne, hero, newsletter form z RODO checkbox
- [ ] Klik kafelek → `/kategoria/{slug}.html` — lista artykułów
- [ ] Klik artykuł → TOC, sticky-box po prawej (≥1100px), bibliografia
- [ ] Newsletter test: wpisz Gmail + zaznacz checkbox → mail confirmation w 1 min
- [ ] Klik link confirmation → `/dziekujemy.html` + welcome mail przyjdzie

**GA4 Real-time** powinien pokazać 1 user.

## FAZA 8 — Brevo Automation (45 min, opcjonalne ale zalecane)

1. Brevo → Automations → Custom workflow:
   - Trigger: Contact added to list `{{DOMAIN_FQDN}} — newsletter`
   - Step 1: Wait 0 → Send `welcome.html`
   - Step 2: Wait 2d → `welcome-day-2.html`
   - Step 3: Wait 3d → `welcome-day-5.html`
   - Step 4: Wait 4d → `welcome-day-9.html` (ankieta segmentująca)
   - Step 5: Wait 5d → `welcome-day-14.html` + tag `regular_subscriber`

2. Brevo → Automations → "RSS to Email":
   - Schedule: Mon 8:00 Europe/Warsaw
   - RSS source: `https://{{DOMAIN_FQDN}}/rss.xml`
   - Template: `weekly-digest.html`
   - Recipients: lista filtrowana tag `regular_subscriber`

## FAZA 9 — Backend deployment (OPCJONALNE, tylko DEPLOY_BACKEND=true)

> Dla większości satelit NIEPOTRZEBNE. GA4 zapewnia pełen tracking.

Plan: subdomena `api.{{DOMAIN_FQDN}}` + Cyber_Folks Aplikacje Python (3.11.14, `passenger_wsgi.py` + `a2wsgi`) + SFTP upload backend (bez venv/.env/db) + env vars (SECRET, ADMIN_PASSWORD, DATABASE_URL, CORS, BREVO_API_KEY) + Run Pip Install + Restart + Let's Encrypt SSL. Szczegóły: `backend/API_INTEGRATIONS.md`.

---

# CZĘŚĆ 4 — COMMON GOTCHAS (z bólu zdrowie.fit, NIE pozwól userowi w nie wpaść)

| Problem | Symptom | Fix |
|---|---|---|
| Cyber_Folks DNS panel zapisuje, ale strefa nie commituje | `nslookup ns1.cyberfolks.pl` zwraca stary stan po 30 min | Usuń + dodaj rekord z klikiem „Zapisz formularz". Jak nie pomoże — chat support, force rebuild zone |
| Brevo OTP nie dochodzi do skrzynki kontakt@DOMAIN | Brak maila w Inbox + Spam | **Forwarder kontakt@DOMAIN → Gmail** Marka. Plus użyj **Domain Authentication** zamiast per-email Verify (jak masz DKIM/DMARC zielone, sender automatic verified) |
| `calc(100%+2rem)` invalid CSS po minify | Sticky-box po lewej zamiast prawo (przykrywa tytuł) | `build.py` minifier: usuń `+` z klasy znaków regex `\s*([{}:;,>~+])\s*` → `\s*([{}:;,>~])\s*` |
| WCAG kontrast `--color-text-light: #8a857d` na cream tle | PageSpeed audytor fail (3.23 ratio) | Zmień na `--color-text-muted: #6b665f` lub ciemniejszy custom |
| Newsletter section biały na białym w dark mode | `.newsletter` używa `var(--color-ink)` który flippuje | Hardcoded `#2d2a26` zamiast var() — zawsze ciemny |
| Audytor SEO: „wiele h1 na 8/10 stron" | Audytor liczy CSS selektory `h1,h2,h3,h4{}` jako h1 | Usuń selektor z critical CSS, zamień `.hero h1` → `.hero__h1` jako klasa |
| Backend FastAPI 500 na Cyber_Folks | Passenger WSGI ≠ FastAPI ASGI | `passenger_wsgi.py` z `a2wsgi.ASGIMiddleware` jako bridge |
| pip.exe „Fatal error in launcher" | venv przeniesiony, hardcoded ścieżka | `python -m pip install ...` zamiast `pip install ...` |
| Search Console „Nie udało się pobrać" sitemap | Pierwszy submit | Normalne, czekaj 24-48h |
| Audytor: „brak kompresji" | False positive — Cyber_Folks ma Brotli | PowerShell `WebRequest` + `Accept-Encoding: br` zwraca `Content-Encoding: br` ✅ |
| Cookie consent link kontrast 2.97 | A11y issue | Override `.cookie-consent a { color: #f5a280 }` (jasny terakota na ciemnym tle) |
| Inputy bez label = a11y fail | 10/21 inputs bez label | Każdy `<input>` ma `aria-label="..."` lub powiązany `<label for="...">` |
| Hierarchia nagłówków pominięcia | Audytor: h1→h3 skip h2 | `<h2 class="visually-hidden">...</h2>` przed `articles-grid` w category.html / articles.html |
| sticky-box `<h4>Udostępnij</h4>` w article.html | Audytor liczy jako pominięcie hierarchii | Zamień na `<p class="sticky-box__label" aria-hidden="true">` |

---

# CZĘŚĆ 5 — DEFINITION OF DONE

- [ ] Strona dostępna pod `https://{{DOMAIN_FQDN}}/` z HTTPS + Brotli
- [ ] PageSpeed: Performance ≥95, A11y ≥95, Best Practices 100, SEO 100
- [ ] GA4 Real-time pokazuje user przy wizycie
- [ ] Search Console verified + sitemap submitted
- [ ] Newsletter form: submit → confirmation mail w Inbox/Gmail w <1 min → klik → welcome mail
- [ ] Wszystkie kafelki klikalne do kategorii
- [ ] `/dziekujemy.html`, `/wypisano.html`, `/polityka-prywatnosci.html` dostępne
- [ ] Brevo Automation Welcome Series 5-mail aktywne
- [ ] Brevo Weekly Digest RSS-driven aktywne (poniedziałek 8:00)
- [ ] Pierwszy artykuł napisany i opublikowany (proof of life)

---

# CZĘŚĆ 6 — TIMELINE

| Faza | Czas | Można równolegle |
|---|---|---|
| Faza 1 (DNS + domena) | 15 min + 30 min czekania | Faza 2 |
| Faza 2 (Brevo) | 15 min | Faza 3 (YAML) |
| Faza 3 (YAML) | 10 min | — |
| Faza 4 (build + sanity) | 3 min | — |
| Faza 5 (GA4 + SC + Bing) | 5 min | — |
| Faza 6 (deploy SFTP) | 3 min | — |
| Faza 7 (verification) | 5 min | — |
| Faza 8 (Brevo Automation) | 45 min | następnego dnia |
| Faza 9 (backend, opcjonalnie) | 60-90 min | później / nigdy |

**Suma 1 satelita bez backendu**: ~1.5h pracy aktywnej + 30 min czekania = **~2h całość**.

---

# CZĘŚĆ 7 — POMOCNICZE LINKI / KOMENDY

**Cyber_Folks**:
- Panel: https://s159.cyber-folks.pl:2223/
- SSH: `ssh -p 222 bestios@s159.cyber-folks.pl`
- Hostkey ED25519: `l/jfbMOzZibqe/kD2WHuhdbpRiVIg/YcG8M9mt67lHM`

**Brevo**:
- Panel: https://app.brevo.com/
- Senders: https://app.brevo.com/senders/list
- Forms: Marketing → Sign-up Forms

**Google**:
- Analytics: https://analytics.google.com
- Search Console: https://search.google.com/search-console

**Bing**:
- Webmaster Tools: https://www.bing.com/webmasters/

**Generator lokalny**:
- Folder: `C:\PYTHON\ARCHAIOS Demand Engine\zdrowie-fit-generator`
- Backend admin: http://127.0.0.1:8765/admin/login (admin / hasło z `backend/.env`)
- Preview lokalny: `cd output\{{DOMAIN_SLUG}} && python -m http.server 8766` → http://127.0.0.1:8766

**Email templates** (gotowe HTML do wklejenia w Brevo Automation):
- `email-templates/confirmation.html` — double opt-in
- `email-templates/welcome.html` — dzień 0
- `email-templates/welcome-day-{2,5,9,14}.html` — welcome series
- `email-templates/weekly-digest.html` — RSS-driven cotygodniowy
- `email-templates/reactivation-day-{30,45}.html` — re-engagement
- `email-templates/re-engagement.html` — final 60d sunset
- `email-templates/anniversary-1y.html` — rocznica subskrypcji

**Build commands**:
```powershell
python build.py --domain {{DOMAIN_FQDN}} --clean    # jedna domena
python build.py --all --clean                      # wszystkie domeny
```

**Środowiska**:
- USE_API=true (default) — generator pobiera z backendu na 8765 (musi działać)
- USE_API=false — SQLite direct (do CI/CD bez backendu)

---

**Koniec master pliku.** Wszystko czego potrzeba do replikowanej deploy nowej satelity Archaios SSG w ~2h.
