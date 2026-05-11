# Deploy nowej satelity Archaios SSG — prompt wykonawczy v1.0

**Wersja**: 2026-05-01
**Bazuje na**: realnym deployu zdrowie.fit (skróty + gotchy z bólu)
**Przeznaczenie**: replikowalna procedura dla każdej z ~12 pozostałych satelit rodziny Archaios

---

## INPUTS — uzupełnij PRZED rozpoczęciem

```yaml
DOMAIN_FQDN: "{{np. testnis2.pl}}"
DOMAIN_SLUG: "{{slug bez kropki, np. testnis2-pl}}"
BRAND_NAME: "{{np. Test NIS2}}"
TAGLINE: "{{np. Compliance NIS2 oparty na faktach}}"
DESCRIPTION: "{{1 zdanie meta description, 120-160 znaków}}"
LOGO_TEXT: "{{wyświetlana nazwa, np. Test}}"
LOGO_ACCENT: "{{terakotowy człon, np. NIS2}}"
ROLE: "{{satellite | flagship}}"
FUNNEL_TYPE: "{{article_cta | lead_magnet | direct_sale | brand_awareness}}"
MAIN_DOMAIN: "{{flagowiec do którego prowadzi, np. archaios.ai}}"
LANG: "pl"
LOCALE: "pl_PL"
COLOR_PRIMARY: "{{np. #4a7c59}}"
COLOR_ACCENT: "{{np. #d9724a}}"
COLOR_TRUST: "{{np. #5b8def}}"
CONTACT_EMAIL: "{{np. kontakt@DOMAIN_FQDN}}"
PILLARS: # 4-6 filarów
  - { icon: "🔒", title: "...", desc: "...", link: "/kategoria/...html" }
CATEGORIES: # 2-5 kategorii
  - { name: "...", slug: "...", icon: "...", color: "#..." }
PRODUCTS: # 1-3 affiliate/own
  - { name, slug, brand, tagline_short, target_url, target_category_slugs, target_tags }
HOSTING: "cyber_folks"  # opcje: cyber_folks | hetzner_vps
GA4_PROPERTY_NAME: "{{nazwa w GA4}}"
BREVO_LIST_NAME: "{{DOMAIN_FQDN}} — newsletter"
DEPLOY_BACKEND: false  # default false; true tylko gdy realnie potrzebny tracker server-side
```

---

## ARCHITEKTURA — co dostaje user

```
[ Cyber_Folks Apache+Brotli ]   ←   SFTP upload statyczny HTML
        ↓
   DOMAIN_FQDN/                    ← strona główna z 4-6 klikalnymi pillars
   /artykuly.html                  ← pełna lista z filtrami
   /artykuly/{slug}.html           ← artykuł (TOC, share, bibliografia, sticky-box)
   /kategoria/{slug}.html          ← lista per kategoria (visually-hidden h2)
   /autor/{slug}.html              ← profil autora E-E-A-T
   /sitemap.xml + /rss.xml + /llms.txt + /llms-full.txt
   /dziekujemy.html + /wypisano.html (noindex, dla Brevo redirect)
   /polityka-prywatnosci.html (z sekcją Brevo + RODO art. 13)
   /robots.txt (25+ AI crawlers dozwolonych + sitemap declaration)

[ Brevo SaaS ]   ←   form POST z public_html → confirmation + welcome + automation
[ Google Analytics 4 ]   ←   gtag.js zbiera page views, scroll, share, sign_up
[ Search Console + Bing Webmaster ]   ←   sitemap submitted, indexowanie
```

---

## FAZY — kolejność z dependencies

### FAZA 0 — Pre-flight (5 min, raz dla całej rodziny)

- [ ] Konto Cyber_Folks bestios działa: SSH `ssh -p 222 bestios@s159.cyber-folks.pl`
- [ ] Konto Brevo z verified senderem
- [ ] Konto Google Analytics + Search Console
- [ ] Lokalny generator: `cd C:\PYTHON\ARCHAIOS Demand Engine\zdrowie-fit-generator && git pull`

### FAZA 1 — DNS + domena Cyber_Folks (15 min + 30 min czekania na propagację)

1. **Domena dodana w Cyber_Folks** (DirectAdmin → Domeny → Dodaj domenę)
2. **Subdomena `www`** (DirectAdmin → Zarządzanie subdomenami)
3. **DNS TXT/CNAME dla Brevo** (z Brevo → Senders → Domains → Authenticate):
   - Brevo code: `@` TXT `brevo-code:{{KOD}}`
   - DKIM 1: `brevo1._domainkey` CNAME `b1.{{DOMAIN-SLUG}}.dkim.brevo.com.`
   - DKIM 2: `brevo2._domainkey` CNAME `b2.{{DOMAIN-SLUG}}.dkim.brevo.com.`
   - DMARC: `_dmarc` TXT `v=DMARC1; p=none; sp=none; rua=mailto:rua@dmarc.brevo.com`
   - SPF (MODYFIKUJ istniejący!): `@` TXT `v=spf1 a mx include:_spf.cyberfolks.pl include:spf.brevo.com -all`
4. **WAŻNE: KAŻDY rekord = klik „Zapisz formularz"** — bez tego Cyber_Folks nie commituje
5. **Forwarder anty-greylisting**: E-Mail Manager → Forwarders → `kontakt@DOMAIN` → Twój Gmail
6. **Skrzynka kontakt@**: E-Mail Accounts → Create
7. **Czekaj 15-30 min** propagacja DNS, weryfikacja:

```powershell
nslookup -type=TXT DOMAIN_FQDN ns1.cyberfolks.pl
# Sprawdź czy widać Brevo code + nowy SPF
```

### FAZA 2 — Brevo configuration (15 min)

1. **Lista**: Contacts → Lists → New → `{{DOMAIN_FQDN}} — newsletter` (zapisz LIST_ID)
2. **Domain Authentication**: Settings → Senders/Domains → `{{DOMAIN_FQDN}}` → Authenticate → 4× zielony
3. **Sender**: kontakt@DOMAIN → kod weryfikacyjny dotrze przez forwarder na Gmail
4. **Form**: Marketing → Sign-up Forms → Create:
   - Type: Subscription form (Full page/embedded)
   - Name: `{{DOMAIN_FQDN}} — newsletter`
   - List: utworzona w pkt 1
   - **Confirmation type: Double opt-in** (KRYTYCZNE)
   - Confirmation email: wklej `email-templates/confirmation.html`
   - Welcome email: wklej `email-templates/welcome.html`
   - Spolszcz 4 messages (success/invalid/error/empty)
   - Sender: kontakt@DOMAIN
   - Final URL: `https://{{DOMAIN_FQDN}}/dziekujemy.html`
5. **Skopiuj Form Action URL** (zaczyna się `https://sibforms.com/serve/...`) — używamy w fazie 3

### FAZA 3 — domains/{{DOMAIN_SLUG}}.yaml (10 min)

Skopiuj `domains/zdrowie-fit.yaml` jako template, podmień wartości — patrz `docs/SATELLITE_INPUTS_TEMPLATE.yaml`.

### FAZA 4 — Build + sanity (3 min)

```powershell
cd "C:\PYTHON\ARCHAIOS Demand Engine\zdrowie-fit-generator"
python build.py --domain {{DOMAIN_FQDN}} --clean

# Sanity (bez tego = ślepy strzał)
$idx = "output\{{DOMAIN_SLUG}}\index.html"
"klikalne pillars: "          + (Select-String $idx -Pattern 'class="pillar pillar--link"' -AllMatches).Matches.Count
"calc() OK (>=3): "           + (Select-String "output\{{DOMAIN_SLUG}}\css\style.css" -Pattern 'calc\([^)]*\s\+\s[^)]*\)' -AllMatches).Matches.Count
"calc() ZLAMANE (=0): "       + (Select-String "output\{{DOMAIN_SLUG}}\css\style.css" -Pattern 'calc\([^)]*[a-z%0-9]\+[a-z0-9]' -AllMatches).Matches.Count
"sibforms (Brevo Action): "   + (Select-String $idx -Pattern 'sibforms\.com' -AllMatches).Matches.Count
"<h1 (=1): "                  + (Select-String $idx -Pattern '<h1[\s>]' -AllMatches).Matches.Count
"selektor h1,h2,h3,h4 (=0): " + (Select-String $idx -Pattern 'h1,h2,h3,h4' -AllMatches).Matches.Count
Test-Path "output\{{DOMAIN_SLUG}}\dziekujemy.html","output\{{DOMAIN_SLUG}}\wypisano.html"
```

### FAZA 5 — Analytics setup (5 min)

1. **GA4**: https://analytics.google.com → Property (NIE konto), nazwa `{{DOMAIN_FQDN}}`, strefa Warszawa, waluta PLN. Skopiuj **Measurement ID G-XXX**
2. Wklej do YAML → `analytics.ga4_id: "G-XXX"`
3. **Search Console**: Add property URL prefix `https://{{DOMAIN_FQDN}}/` → verify przez **Google Analytics** (instant)
4. **Sitemap**: SC → Mapy witryn → `sitemap.xml` → Wyślij
5. **Bing**: https://www.bing.com/webmasters → Import from GSC (1 klik)
6. Rebuild ponowny:

```powershell
python build.py --domain {{DOMAIN_FQDN}} --clean
```

### FAZA 6 — Deploy SFTP (3 min)

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

### FAZA 7 — Verification (5 min)

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
- [ ] Klik artykuł → `/artykuly/{slug}.html` — TOC, sticky-box po prawej (≥1100px), bibliografia
- [ ] Newsletter test: wpisz Gmail + zaznacz checkbox → submit → mail confirmation w 1 min
- [ ] Klik link confirmation → `/dziekujemy.html` + welcome mail przyjdzie

**GA4 Real-time** powinien pokazać 1 user.

### FAZA 8 — Brevo Automation (45 min, opcjonalnie ale bardzo zalecane)

1. Brevo → Automations → New Custom workflow:
   - Trigger: Contact added to list `{{DOMAIN_FQDN}} — newsletter`
   - Step 1: Wait 0 → Send `welcome.html`
   - Step 2: Wait 2d → Send `welcome-day-2.html`
   - Step 3: Wait 3d → Send `welcome-day-5.html`
   - Step 4: Wait 4d → Send `welcome-day-9.html` (segmentująca ankieta)
   - Step 5: Wait 5d → Send `welcome-day-14.html` + Add tag `regular_subscriber`

2. Brevo → Automations → Template "RSS to Email":
   - Schedule: Mon 8:00 Europe/Warsaw
   - RSS source: `https://{{DOMAIN_FQDN}}/rss.xml`
   - Template: `weekly-digest.html`
   - Recipients: list filtrowana tag `regular_subscriber`

### FAZA 9 — Backend deployment (OPCJONALNIE, tylko DEPLOY_BACKEND=true)

> Dla większości satelit NIEPOTRZEBNE. GA4 zapewnia pełen tracking.

Plan w `backend/API_INTEGRATIONS.md` — kroki identyczne jak dla zdrowie.fit:
- Subdomena `api.{{DOMAIN_FQDN}}` + Cyber_Folks Aplikacje Python (3.11.14, passenger_wsgi.py + a2wsgi)
- SFTP upload backend, env vars (SECRET, ADMIN_PASSWORD, DATABASE_URL, CORS, BREVO_API_KEY)
- Run Pip Install + Restart, Let's Encrypt SSL, BACKEND_URL w YAML

---

## COMMON GOTCHAS — z bólu zdrowie.fit

| Problem | Symptom | Fix |
|---|---|---|
| Cyber_Folks DNS panel zapisuje, ale strefa nie commituje | `nslookup ns1.cyberfolks.pl` zwraca stary stan po 30 min | Usuń + dodaj rekord z klikiem „Zapisz formularz". Jak nie pomoże — chat support |
| Brevo OTP nie dochodzi do skrzynki kontakt@DOMAIN | Brak maila w Inbox + Spam | Forwarder kontakt@DOMAIN → Gmail Marka. Plus użyj Domain Authentication zamiast per-email Verify |
| `calc(100%+2rem)` invalid CSS po minify | Element pozycjonowany na lewo zamiast prawo | `build.py` minifier: usuń `+` z klasy znaków regex `\s*([{}:;,>~+])\s*` → `\s*([{}:;,>~])\s*` |
| WCAG kontrast `--color-text-light: #8a857d` na cream tle | Audytor PageSpeed fail (ratio 3.23) | Zmień na `--color-text-muted: #6b665f` lub ciemniejszy custom |
| Newsletter section biały na białym w dark mode | `.newsletter` używa `var(--color-ink)` | Hardcoded `#2d2a26` — zawsze ciemny niezależnie od dark mode |
| Audytor SEO: „wiele h1 na 8/10 stron" | Audytor liczy CSS selektory `h1,h2,h3,h4{}` jako h1 | Usuń selektor z critical CSS w `build.py`, zamień `.hero h1` → `.hero__h1` jako klasa |
| Backend FastAPI 500 na Cyber_Folks | Passenger WSGI ≠ FastAPI ASGI | `passenger_wsgi.py` z `a2wsgi.ASGIMiddleware` jako bridge |
| pip.exe „Fatal error in launcher" | venv przeniesiony, hardcoded ścieżka | `python -m pip install ...` zamiast `pip install ...` |
| Search Console „Nie udało się pobrać" sitemap | Pierwszy submit | Normalne, czekaj 24-48h |
| Audytor: „brak kompresji" | False positive — Cyber_Folks ma Brotli | Test PowerShell `WebRequest` + `Accept-Encoding: br` zwraca `Content-Encoding: br` |

---

## TIMELINE — realne dla 1 osoby

| Faza | Czas | Można równolegle |
|---|---|---|
| Fazy 0-1 (DNS + domena) | 15 min + 30 min czekania | Faza 2 |
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

## DEFINITION OF DONE

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
