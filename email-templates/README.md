# Email templates dla Brevo (Sendinblue) — kompletny lifecycle newsletter

**11 szablonów HTML** pokrywających pełen cykl życia subskrybenta — od double opt-in przez 5-mailową welcome series, weekly digest, reactivation funnel, anniversary, aż po sezonowe i topical campaigns.

**Wszystkie inline CSS** (klienci pocztowi nie obsługują zewnętrznych stylów). **Wszystkie responsywne** (table-based layout, max-width 600px, działa na Gmail / Outlook / Apple Mail / Yahoo). **Każdy z preheaderem** (preview text w skrzynce).

> **Pełna logika kalendarza/automation: [`AUTOMATION-CALENDAR.md`](./AUTOMATION-CALENDAR.md)** — KIEDY, do KOGO, w jakich WARUNKACH, z jakim CELEM. Czytaj to najpierw, jeśli planujesz pełny setup.

## Pliki — przegląd

### Lifecycle automatyczny (Brevo Automation)

| Plik | Cel | Trigger | Wysyłka |
|---|---|---|---|
| `confirmation.html` | Double opt-in po zapisie | Form submit | Instant |
| `welcome.html` | Powitanie po potwierdzeniu | Confirmation klik | Instant (dzień 0) |
| `welcome-day-2.html` | 5 najmocniejszych badań — pozycjonowanie | +48h od confirm | Dzień 2 |
| `welcome-day-5.html` | Pierwszy mały eksperyment (30s zimnego prysznica) | +5d od confirm | Dzień 5 |
| `welcome-day-9.html` | Ankieta segmentująca (Ruch/Umysł/Dieta/All) | +9d od confirm | Dzień 9 |
| `welcome-day-14.html` | Checkpoint — kontrakt + opcja wypisu | +14d od confirm | Dzień 14 |
| `weekly-digest.html` | Cotygodniowy przegląd RSS | Cron Mon 8:00 | Weekly |
| `reactivation-day-30.html` | Light touch dla nieaktywnych | 30d bez akcji | Dzień 30 |
| `reactivation-day-45.html` | Oferta monthly digest (zamiast unsubscribe) | 45d bez akcji | Dzień 45 |
| `re-engagement.html` | Final sunset path | 60d bez akcji | Dzień 60 |
| `anniversary-1y.html` | Rocznica subskrypcji + referral nudge | 365d od subscribed_at | Rocznie |

### Manualne kampanie tematyczne (Marketing → Campaigns)

| Plik | Cel | Kiedy odpalić |
|---|---|---|
| `seasonal-cold-exposure.html` | Sezonowy deep-dive na zimę | Pierwszy poniedziałek listopada |
| `topical-stress.html` | Drip dla zainteresowanych stresem (1/3 z serii) | Trigger: klik artykułu z `?utm_topic=stres` |

## Konfiguracja Brevo — krok po kroku

### 1. Konto + lista

1. Zarejestruj się: https://www.brevo.com/ (free, 300 maili/dzień)
2. Settings → SMTP & API → notuj **API key** (do kontaktu)
3. Contacts → Lists → "Create new list" → nazwa: `zdrowie.fit — newsletter`
4. Notuj `LIST_ID` (zobaczysz w URL po wejściu w listę)

### 2. Custom field „NAME" (opcjonalnie, do personalizacji)

Contacts → Settings → Contact attributes → Add → `NAME` (text). To pole będziemy mogli wypełnić, jeśli formularz będzie zbierał imię.

### 3. Form

Contacts → Forms → Create new form. Skonfiguruj:
- **Pole 1**: `EMAIL` (required)
- **Pole 2**: checkbox zgody RODO (required) — tekst: *„Wyrażam zgodę na przetwarzanie moich danych w celu otrzymywania newslettera. Mogę wycofać zgodę w każdej chwili."*
- **Double opt-in**: ✅ Enable (KRYTYCZNE dla RODO)
- **Confirmation email**: wklej `confirmation.html` (subject: *„Potwierdź zapis na newsletter Zdrowie.fit"*)
- **Welcome email** (po potwierdzeniu): wklej `welcome.html` (subject: *„Witaj w Zdrowie.fit — co dalej"*)
- **Redirect po sukcesie**: `https://zdrowie.fit/` (lub stwórz `/dziekujemy.html`)

Po zapisaniu formularza Brevo da Ci **Action URL** — wklej ten URL do `domains/zdrowie-fit.yaml`:

```yaml
newsletter:
  endpoint: "https://sibforms.com/serve/MUIFA..."  # ← TUTAJ
  title_highlight: "cotygodniowy przegląd"
  ...
```

Po `python build.py --domain zdrowie.fit --clean` + upload formularz na stronie zacznie POST-ować do Brevo.

### 4. Welcome Series (5 maili w 14 dni) — Brevo Automation

Automation → Create new workflow → **Custom workflow**:

**Trigger**: `Contact added to list "zdrowie.fit — newsletter"` AND `OPT_IN = true`

Krok po kroku:
1. **Wait 0** → Send `welcome.html` (subject: *Witaj w Zdrowie.fit — co dalej*)
2. **Wait 2 days** → Send `welcome-day-2.html` (subject: *5 badań, które warto znać — żeby filtrować bzdury*)
3. **Wait 3 days** → Send `welcome-day-5.html` (subject: *Jeden mały eksperyment na ten tydzień (5 minut, free)*)
4. **Wait 4 days** → Send `welcome-day-9.html` (subject: *Krótkie pytanie — co Cię najbardziej interesuje?*)
5. **Wait 5 days** → Send `welcome-day-14.html` (subject: *Mamy razem 2 tygodnie. Co dalej?*) → **Add tag `regular_subscriber`**

**Po zakończeniu welcome series** contact dostaje tag `regular_subscriber` i wpada w pętlę weekly digest.

### 5. Weekly digest — Brevo Automation (RSS-driven)

Automation → Create new workflow → Template **„RSS to Email"**:
- **Trigger**: Schedule (Every Monday 08:00 Europe/Warsaw)
- **Condition**: RSS feed has new items since last run AND contact has tag `regular_subscriber`
- **RSS URL**: `https://zdrowie.fit/rss.xml`
- **Email content**: wklej `weekly-digest.html`
- **Subject line**: dynamiczny — *„Tydzień {{params.iso_week}} — 3 rzeczy z minionego tygodnia"*
- **From**: `kontakt@zdrowie.fit` (wymaga **DKIM authenticated**)
- **Recipients**: List `zdrowie.fit — newsletter` filtered by `regular_subscriber`
- **WAŻNE**: Wyklucz contacts z tagiem `frequency_monthly` (oni dostają digest tylko 1× w miesiącu)

### 6. Reactivation Funnel — 3 etapowy (30d → 45d → 60d)

#### 6.1 — Reactivation 30d (light touch)
- **Trigger**: Contact has `regular_subscriber` AND `last_engagement < 30 days ago` AND no tag `reactivation_30_sent`
- **Email**: `reactivation-day-30.html`
- **Subject**: *Hej, dawno Cię nie czytaliśmy — wszystko OK?*
- **Po wysyłce**: dodaj tag `reactivation_30_sent`
- **Jeśli klik w 7 dni**: usuń tag `reactivation_30_sent` (reset cyklu)

#### 6.2 — Reactivation 45d (oferta monthly)
- **Trigger**: Contact has `reactivation_30_sent` AND `last_engagement < 45 days ago` AND no tag `reactivation_45_sent`
- **Email**: `reactivation-day-45.html`
- **Subject**: *Może raz w miesiącu, zamiast co tydzień?*
- **CTA „switch to monthly"** → kliknięcie linku z `?action=monthly` → dodaj tag `frequency_monthly`, usuń `regular_subscriber`
- **CTA „stay weekly"** → reset cyklu

#### 6.3 — Re-engagement Final 60d (sunset path)
- **Trigger**: Contact has `reactivation_45_sent` AND `last_engagement < 60 days ago`
- **Email**: `re-engagement.html`
- **Subject**: *Ostatnie pytanie — zostajesz czy się żegnamy?*
- **Po 14 dniach bez klika**: automatic unsubscribe + tag `churned_inactive`
- Dlaczego: clean list → lepsza deliverability dla aktywnych subscriberów

### 7. Anniversary 1y — Brevo Automation (date-based)

Automation → Custom workflow:
- **Trigger**: contact attribute `subscribed_at` exists AND today = subscribed_at + 365 days AND tag `regular_subscriber`
- **Email**: `anniversary-1y.html`
- **Subject**: *Już rok jesteś z nami. Mała statystyka i podziękowanie.*
- **Personalizacja**: w `params` ustaw `subscribed_date`, `articles_count` (z bazy), `referral_url`

### 6. DKIM + SPF (deliverability)

To jest **KRYTYCZNE** — bez tego Gmail/Outlook wrzucą maile w spam.

Brevo: Senders & IP → Domains → Add domain `zdrowie.fit` → daje 3 rekordy DNS:
- 2× CNAME (DKIM)
- 1× TXT (DMARC)

Dodaj je w panelu **Cyber_Folks → DirectAdmin → DNS Management → zdrowie.fit**. Po 24h Brevo zweryfikuje. Status musi być zielony przed startem wysyłki.

### 8. Manualne kampanie tematyczne

#### 8.1 — Sezonowy cold exposure (`seasonal-cold-exposure.html`)
- **Wysyłka manualna**: pierwszy poniedziałek listopada (start sezonu)
- Marketing → Campaigns → New Campaign → Wklej HTML
- **Recipients**: cała lista `regular_subscriber`, **wyklucz** tagi `pref_dieta_only` i `pref_umysl_only`
- **Subject**: *Zima przyszła. Czas na 30 sekund.*

#### 8.2 — Topical drip stres (`topical-stress.html`)
- **Trigger**: Contact kliknął link z parameterem `?utm_topic=stres` w ostatnich 14 dniach (Brevo Automation: behavior-based trigger)
- **Wait 3 days** → Send `topical-stress.html`
- **Subject**: *Skoro czytałeś nasz artykuł o stresie…*
- **Możesz rozszerzyć**: dodaj 2 kolejne maile w odstępach 4 dni (deep-dive #2, #3 z dodatkowymi badaniami)

## Placeholdery w szablonach

Szablony używają zmiennych Brevo (`{{ ... }}`):

### Auto-fillable przez Brevo
- `{{ doubleoptin }}` — link aktywacyjny (auto, w confirmation)
- `{{ unsubscribe }}` — link wypisu (auto, każdy email MUSI mieć)
- `{{ contact.NAME }}` — imię (jeśli zebrane w formularzu, używamy z fallbackiem `{% if contact.NAME %}`)

### W params (ustaw przy wysyłce campaign / w Automation steps)
- `{{ params.year }}` — rok np. `2026`
- `{{ params.iso_week }}` — numer tygodnia np. `2026-W17` (do weekly digest subject + header)
- `{{ params.weekly_question }}` — pytanie do refleksji (manualne, edytowane co wysyłkę)
- `{{ params.subscribed_date }}` — data zapisu (anniversary)
- `{{ params.articles_count }}` — ile artykułów na serwisie (anniversary)
- `{{ params.citations_count }}` — ile cytowań w bibliografiach (anniversary)
- `{{ params.referral_url }}` — link polecenia (anniversary)
- `{{ params.confirm_stay_url }}` — link „chcę zostać" (re-engagement)
- `{{ params.switch_monthly_url }}` — link przepisania na monthly (reactivation 45d)
- `{{ params.stay_weekly_url }}` — link „zostaję na weekly" (reactivation 45d)

### W reactivation-day-30.html — 3 najnowsze artykuły (manualne lub przez RSS)
- `{{ params.article1_title }}`, `{{ params.article1_url }}`, `{{ params.article1_excerpt }}`, `{{ params.article1_category }}`
- (i analogicznie article2_*, article3_*)

### W weekly-digest.html — RSS items (Brevo RSS-to-Email auto-iteruje)
- `{% for item in rss_items %}` z `{{ item.title }}`, `{{ item.link }}`, `{{ item.description }}`, `{{ item.pubDate }}`

## Testowanie przed wysyłką do listy

1. Stwórz listę testową `zdrowie.fit — TEST` z 1-2 adresami (Twój + drugi)
2. Wyślij każdy szablon do tej listy → sprawdź:
   - Renderowanie w Gmail web + Gmail Android + Outlook desktop + Apple Mail
   - Linki działają
   - Unsubscribe działa
   - Preheader text widoczny w skrzynce
   - Spam score: https://www.mail-tester.com/ (cel: 9-10/10)

## Dla pozostałych domen rodziny Archaios

Szablony są szyte pod zdrowie.fit (linki w `welcome.html`, gradient kolorów). Dla innych domen (psycho-edu.pl, archaios.ai, testnis2.pl…) **skopiuj folder, podmień**:

- Logo / nazwę w headerze
- Linki w `welcome.html` (top 3 artykuły z danej domeny)
- Kolor accent / primary (CSS gradient w `welcome.html` header)
- URL feedu w Brevo Automation
- Tagline footer

Zachowaj strukturę — table-based layout i inline CSS są niezbędne.
