# Newsletter — Lifecycle Email Strategy dla Zdrowie.fit

Kompletny kalendarz automation w Brevo. **Każdy mail ma cel, triger, warunki, KPI**. Czytaj od góry — zachowuje chronologię życia subskrybenta.

---

## Zasada nadrzędna — „Mniej, lecz lepiej"

- **Maksymalnie 4 maile w pierwszych 14 dniach** (welcome series). Powyżej tego ludzie się wypisują.
- **Stała kadencja** raz w tygodniu (poniedziałek 8:00, kawa+praca routine).
- **Każdy mail ma 1 główny CTA**, max 2 dodatkowe linki. Nie rozpraszamy.
- **Czas wysyłki**: pon. 8:00 (otwarcia ~32%), nigdy weekendy (~12%), nigdy 17:00-21:00 (rozpraszacze).
- **Przerwa**: jak user otwiera 0 maili przez 30 dni — automatycznie zwalniamy do raz na 2 tygodnie. 60 dni — re-engagement. 75 dni bez akcji — auto-unsubscribe (clean list = lepsza deliverability).

---

## Lifecycle — pełna mapa

```
[Zapis na formularzu]
    ↓ instant
[1. Confirmation — double opt-in]            confirmation.html
    ↓ user kliknął link aktywacyjny
[2. Welcome day 0]                            welcome.html
    ↓ +2 dni (jeśli otworzył welcome)
[3. Welcome day 2 — najmocniejsze badania]    welcome-day-2.html
    ↓ +3 dni
[4. Welcome day 5 — pierwszy mały krok]       welcome-day-5.html
    ↓ +4 dni
[5. Welcome day 9 — ankieta preferencji]      welcome-day-9.html
    ↓ +5 dni
[6. Welcome day 14 — kierunkowanie]           welcome-day-14.html
    ↓ user wpada w tryb stały
═══════════════════════════════════════════════════════════════════
[7. Weekly digest]                            weekly-digest.html
       co poniedziałek 8:00
       (RSS-driven, automatyczny)
═══════════════════════════════════════════════════════════════════

       │ INACTIVITY DETECTION (sprawdzane co 24h)
       │
       ├─ 30 dni bez open/click
       │     ↓
       │   [8. Reactivation light — przypomnienie wartości]   reactivation-day-30.html
       │     ↓ (otworzył albo kliknął) → wraca do digestów
       │     ↓ (nadal cisza)
       │
       ├─ 45 dni bez akcji
       │     ↓
       │   [9. Reactivation oferta monthly]   reactivation-day-45.html
       │     ↓ (klika "weekly") → wraca, (klika "monthly") → mniej maili, (cisza) →
       │
       ├─ 60 dni bez akcji
       │     ↓
       │   [10. Re-engagement final]   re-engagement.html
       │     ↓ (klika "zostaję") → reset, (cisza)
       │     ↓ +14 dni
       │   [Auto-unsubscribe + tag "churned_inactive"]
       │
       └─ 365 dni od zapisu (i jest aktywny)
             ↓
           [11. Anniversary]   anniversary-1y.html
             ↓ + nudge do polecenia znajomym
```

---

## Detale każdego automation

### 1. Confirmation (double opt-in)

| Pole | Wartość |
|---|---|
| Plik | `confirmation.html` |
| Trigger | Submit formularza newslettera |
| Subject | `Potwierdź zapis na newsletter Zdrowie.fit` |
| Sender | `kontakt@zdrowie.fit` |
| KPI cel | 70%+ confirmation rate (branża: 60-80%) |
| Brevo workflow | Form settings → "Confirmation type: Double opt-in" → wklej HTML |

**Diagnostyka**: Jeśli confirmation rate <50% — sprawdź czy mail nie ląduje w spamie (DKIM/SPF), preheader jest mocny, subject nie wygląda jak sales.

---

### 2. Welcome day 0 — zaraz po confirm

| Pole | Wartość |
|---|---|
| Plik | `welcome.html` |
| Trigger | Confirmation klik |
| Subject | `Witaj w Zdrowie.fit — co dalej` |
| Wysłanie | Instant po confirmation |
| KPI cel | 50%+ open, 25%+ click |
| Brevo workflow | Form settings → "Welcome email" |

---

### 3. Welcome day 2 — najmocniejsze badania

| Pole | Wartość |
|---|---|
| Plik | `welcome-day-2.html` |
| Trigger | +48h od confirmation, contact ma tag `welcome_series_active` |
| Subject | `5 badań, które warto znać — żeby filtrować bzdury` |
| Cel | Zaprezentować pozycjonowanie: jesteśmy oparci na badaniach, nie biohacking-mistyce. Buduje trust. |
| KPI cel | 35%+ open (welcome series ma high engagement) |
| Brevo workflow | Automation → New workflow → Trigger "Contact added to list `zdrowie.fit — newsletter`" + Wait 48h + Send email |

---

### 4. Welcome day 5 — pierwszy mały krok

| Pole | Wartość |
|---|---|
| Plik | `welcome-day-5.html` |
| Trigger | +5 dni od confirmation |
| Subject | `Jeden mały eksperyment na ten tydzień (5 minut, free)` |
| Cel | **Aktywacja** — od czytania do działania. Konkretne mikro-zalecenie (np. 30s zimnego prysznica na koniec normalnego, lub 10 minut spaceru po obiedzie). Buduje habit subskrybenta = czytasz → robisz → wracasz po więcej. |
| KPI cel | 30%+ open, 15%+ click do artykułu źródłowego |
| Brevo workflow | Wait 5d od trigger zapisu |

---

### 5. Welcome day 9 — ankieta preferencji

| Pole | Wartość |
|---|---|
| Plik | `welcome-day-9.html` |
| Trigger | +9 dni od confirmation |
| Subject | `Krótkie pytanie — co Cię najbardziej interesuje?` |
| Cel | **Segmentacja**. Klikalne 4 buttony: Ruch / Umysł / Odżywianie / Wszystko po równo. Każdy klik dodaje tag (`pref_ruch`, `pref_umysl`, `pref_dieta`, `pref_all`). Te tagi potem decydują w Weekly Digest, które artykuły dostawiamy na top. |
| KPI cel | 18%+ click (ankieta to high-friction, ale przy welcome series wyjątkowo działa) |
| Brevo workflow | Wait 9d, każdy klik → Add tag → możemy targetować segmenty |

---

### 6. Welcome day 14 — kierunkowanie

| Pole | Wartość |
|---|---|
| Plik | `welcome-day-14.html` |
| Trigger | +14 dni od confirmation |
| Subject | `Mamy wspólnie 2 tygodnie. Co dalej?` |
| Cel | Reflective check-in. „Jeśli to nie dla Ciebie — wypisz się jednym klikiem (link w stopce). Jeśli zostajesz, oto co dalej będziemy robić." Buduje zaufanie przez **explicit przyzwolenie na odejście**. Paradoksalnie zmniejsza unsubscribe rate. |
| KPI cel | <2% unsubscribe rate (krytyczna metryka) |
| Brevo workflow | Wait 14d od confirmation, zakończenie welcome series → remove tag `welcome_series_active`, add tag `regular_subscriber` |

---

### 7. Weekly digest — RSS-driven

| Pole | Wartość |
|---|---|
| Plik | `weekly-digest.html` |
| Trigger | **Cron**: każdy poniedziałek 8:00 Europe/Warsaw |
| Warunek | `regular_subscriber` tag + RSS feed `https://zdrowie.fit/rss.xml` ma przynajmniej 1 nowy item od ostatniej wysyłki |
| Subject | Dynamiczny: `Tydzień {{params.iso_week}} — 3 rzeczy z minionego tygodnia` |
| Cel | **Stały rytm zaufania.** Bez wytrycha „ostatnia szansa", bez clickbaitu. Trzy rzeczy, każda z linkiem, jedno pytanie do refleksji na koniec. |
| KPI cel | 25%+ open (top 25% branży), 8%+ click do artykułu, <0.3% unsubscribe |
| Brevo workflow | Automation template **„RSS to Email"** → trigger Schedule (Mon 08:00) → RSS source `https://zdrowie.fit/rss.xml` → email content `weekly-digest.html` → recipients: list `zdrowie.fit — newsletter` filtered by tag `regular_subscriber` |

**Personalizacja**: Jeśli contact ma tag `pref_ruch` — Brevo Automation może wybrać 3 najnowsze artykuły z kategorii fizyczne. Jeśli `pref_umysl` — z psychiczne. Domyślnie: chronologicznie z całego feedu.

---

### 8. Reactivation 30 days — light touch

| Pole | Wartość |
|---|---|
| Plik | `reactivation-day-30.html` |
| Trigger | Contact: `regular_subscriber` AND `last_open_or_click > 30 days ago` |
| Subject | `Hej, dawno nas nie czytałeś — wszystko OK?` |
| Cel | **Empatyczny check-in**, nie defensywne „zostań proszę". Treść: „skrzynka jest zapchana, rozumiemy. Jeśli newsletter nadal Ci pasuje — kliknij którykolwiek z trzech ostatnich artykułów. Jeśli nie — totalnie bez urazy." |
| KPI cel | 12%+ click → wraca do segmentu aktywnego |
| Brevo workflow | Trigger "Has not opened/clicked in 30 days" → Send email → After 7d sprawdź czy kliknął cokolwiek → tag accordingly |

---

### 9. Reactivation 45 days — oferta monthly

| Pole | Wartość |
|---|---|
| Plik | `reactivation-day-45.html` |
| Trigger | 45d bez akcji + reactivation_30d nie zadziałało |
| Subject | `Może raz w miesiącu, zamiast co tydzień?` |
| Cel | **Częstotliwość ratunkowa**. Daje opcję „mniej maili" zamiast wypisu. Klik „chcę monthly" → tag `frequency_monthly` → user dostaje weekly digest tylko 1 raz/miesiąc (pierwszy poniedziałek). |
| KPI cel | 8%+ click → save subscriber as monthly. Lepiej monthly niż unsubscribed. |
| Brevo workflow | Automation: 45d od ostatniej akcji + nie ma tag `frequency_monthly` → email |

---

### 10. Re-engagement final 60 days

| Pole | Wartość |
|---|---|
| Plik | `re-engagement.html` |
| Trigger | 60d bez akcji + reactivation 30d i 45d nie zadziałały |
| Subject | `Ostatnie pytanie — zostajesz czy się żegnamy?` |
| Cel | **Sunset path** — albo ratuje, albo świadomie wypisuje. **Auto-unsubscribe po 14 dniach od tego maila bez kliknięcia.** Czysta lista = lepsza deliverability dla aktywnych. |
| KPI cel | Wszystko ok > 5% reactivation; reszta — graceful exit, nie bóg wie jaki spam-trap |
| Brevo workflow | Automation: 60d bez akcji → email + tag `reengagement_sent` → Wait 14d → if no click → tag `churned_inactive` + remove from main list |

---

### 11. Anniversary — 1 rok od zapisu

| Pole | Wartość |
|---|---|
| Plik | `anniversary-1y.html` |
| Trigger | Dokładnie 365 dni od `subscribed_at`, contact = `regular_subscriber` |
| Subject | `Już rok jesteś z nami. Mała statystyka i podziękowanie.` |
| Cel | **Loyalty + referral nudge**. „Przeczytałeś ~52 maile, 156 artykułów łącznie. Jeśli to dla Ciebie wartościowe — poleć newsletter komuś jednym klikiem." Z linkiem do tweet-prefilled / share na FB. |
| KPI cel | 4%+ referral click |
| Brevo workflow | Schedule: contact.subscribed_at == today - 365d (sprawdzane codziennie) |

---

## Bonus — kampanie tematyczne (manualne, nie automation)

Te NIE chodzą w pętli. Marek odpala je ręcznie kiedy ma sens.

### Sezonowy: Cold exposure (listopad-marzec)
- **Plik**: `seasonal-cold-exposure.html`
- **Trigger**: Manualne, np. 3 listopada (start sezonu).
- **Cel**: Wykorzystać sezon na deep-dive temat. Przyciąga clicki w tygodniu, kiedy newsletter konkurencji jest słaby (przed świętami).
- **Kogo wysłać**: cała lista z tagiem `regular_subscriber`, opcjonalnie wykluczyć `pref_ruch_only`.

### Topical: Stres chroniczny (drip 7-dniowy)
- **Plik**: `topical-stress.html`
- **Trigger**: User kliknął cokolwiek z tagiem stres w ostatnich 14 dniach.
- **Cel**: Pogłębić zainteresowanie. Wzmacnia pozycję eksperta w temacie.
- **Drip**: 1 mail + opcjonalnie 2 follow-upy w odstępach 4 dni z dodatkowymi badaniami.

### Reader survey — raz w roku (np. luty)
- Manualnie wysyłany do całej listy.
- 5 pytań max (Google Forms / Tally — zewnętrzny embed).
- Inkubator nowych tematów + segmentacja.

---

## Konfiguracja Brevo — krok po kroku per automation

### Setup tagów (raz, na początku)

W Brevo → Contacts → Settings → Contact attributes — sprawdź czy są:

| Atrybut | Typ | Cel |
|---|---|---|
| `EMAIL` | text (built-in) | identyfikator |
| `NAME` | text | personalizacja "Cześć [imię]" |
| `OPT_IN` | boolean | RODO consent flag |
| `subscribed_at` | date | start wszystkich timerów |
| `last_engagement_at` | date | aktualizowane przez Brevo automation przy każdym open/click |
| `pref_ruch` / `pref_umysl` / `pref_dieta` / `pref_all` | boolean | preferencje content (z welcome day 9) |
| `frequency_monthly` | boolean | rzadszy digest |
| `welcome_series_active` | boolean | flag dla automation |
| `regular_subscriber` | boolean | po welcome series |
| `reengagement_sent` | boolean | flag re-engagement |
| `churned_inactive` | boolean | wypisani z powodu nieaktywności |

### Workflowy do utworzenia (Automations → New workflow)

1. **Welcome series (5 maili w 14 dni)** — template "Welcome series", trigger "Contact added to list", waits 0/2/5/9/14 dni.
2. **Weekly digest** — template "RSS to Email", schedule Mon 08:00, RSS `https://zdrowie.fit/rss.xml`.
3. **Reactivation 30d** — template "Reactivate inactive contacts", trigger "no engagement 30 days".
4. **Reactivation 45d** — drugi workflow, trigger "no engagement 45 days + no `frequency_monthly`".
5. **Re-engagement final 60d** — trigger 60d, follow-up 14d → unsubscribe.
6. **Anniversary 1y** — trigger date-based on `subscribed_at` field.
7. **Topical drip stres** (manual setup, opcjonalne) — trigger "clicked link with parameter `?utm_topic=stres`".

---

## KPI cel dla całego newslettera (cele realistyczne dla niche zdrowotnego)

| Metryka | Cel 3 mies. | Cel 12 mies. | Branża benchmark |
|---|---|---|---|
| Open rate (weekly) | 30% | 35-40% | 21% |
| Click rate (weekly) | 8% | 12% | 2.6% |
| Confirmation rate (DOI) | 70% | 75% | 65% |
| Unsubscribe rate (per send) | <0.3% | <0.2% | 0.26% |
| Spam complaint rate | <0.1% | <0.05% | 0.02% |
| List growth (mom) | +5% | +8% | varies |

Te liczby (jeśli osiągnięte) lokują newsletter Zdrowie.fit w **top 10% branży „zdrowie/wellness"** — bo robimy double opt-in, RODO compliance, evidence-based content i czysty design. Większość konkurencji wzbiera leady przez ebooki-bait.

---

## Co Marek ma robić w praktyce, raz na tydzień (15-30 min)

**Poniedziałek 7:30** (przed wyjściem digestu):
1. Wejdź do Brevo → Automations → Weekly digest
2. Sprawdź podgląd (preview) — czy RSS wciągnął dobre 3-5 artykułów
3. Edytuj „pytanie do przemyślenia" w `params.weekly_question` — wpisz coś świeżego, oryginalnego
4. Uruchom (jeśli automatic, sprawdź że jest enabled)

**Co miesiąc** (1 godzina):
- Otwórz Brevo Analytics → przeglądnij open/click rates
- Identyfikuj 1-2 najsłabsze maile, popraw subject/copy
- Sprawdź segment `pref_*` — które tematy zbierają więcej preferencji, kalibruj strategię contentową

**Co kwartał** (2 godziny):
- A/B test subject lines weekly digest
- Reader survey jeśli wielki contentowy pivot (raz w roku)
