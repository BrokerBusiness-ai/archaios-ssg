# STRATEGIA KLASTRA NIS2 — 5 SATELITÓW → archaios.ai

> Dokument operacyjny. Każda domena ma kartę strategiczną z gotowymi promptami do wklejenia w ChatGPT (grafiki) i Claude (design/content). Wygenerowane materiały trafiają do `src/static/img/` danej domeny.

---

## ARCHITEKTURA KLASTRA

```
testnis2.pl ──────┐
karynis2.pl ──────┤
skanujfirme.pl ───┤──→ archaios.ai (konwersja: audyt NIS2, wdrożenie, consulting)
onpremiseai.pl ───┤
aidzisiaj.pl ─────┘
```

**Mechanizm orbity**: Każdy satelita przechwytuje ruch z innego kąta intencji wyszukiwania. Użytkownik trafia na satelitę przez SEO, konsumuje wartościowy content, a CTA kieruje go do archaios.ai jako jedynego miejsca, gdzie może ROZWIĄZAĆ swój problem.

**Techniki perswazji wspólne dla klastra**:
- **Urgency framing** — NIS2 ma twardy deadline (17 X 2024 → transpozycja krajowa). Każdy artykuł przypomina o czasie.
- **Loss aversion** — kary do 10M EUR lub 2% obrotu. Strach przed stratą > chęć zysku.
- **Authority bias** — cytowanie ENISA, CSIRT, aktów prawnych UE. Buduje zaufanie przez źródła.
- **Social proof** — "67% polskich firm nie jest gotowych na NIS2" (dane z raportów).
- **Commitment & consistency** — darmowy test → wynik → plan → kontakt z archaios.ai.

---

## SATELITA 1: testnis2.pl

### IDENTYFIKACJA

| Element | Wartość |
|---------|---------|
| **Domena** | testnis2.pl |
| **Rola** | Brama wejściowa — darmowy test/quiz gotowości NIS2 |
| **Intencja SEO** | "test NIS2", "czy moja firma podlega NIS2", "sprawdź NIS2", "quiz NIS2" |
| **Emocja docelowa** | Niepewność → potrzeba diagnozy → ulga (wiem, co robić) |
| **CTA końcowe** | → archaios.ai/audyt |

### KOLORYSTYKA

| Rola | Kolor | Hex | Użycie |
|------|-------|-----|--------|
| Primary | Granatowy | `#1a365d` | Nagłówki, nawigacja, footer — autorytet, profesjonalizm |
| Accent | Czerwony | `#c0392b` | CTA buttony, alerty, wyniki testu "nie spełniasz" |
| Trust | Niebieski | `#2980b9` | Linki, źródła, cytaty z regulacji |
| Success | Zielony | `#27ae60` | Wynik testu "spełniasz", checklisty zaliczone |
| Warning | Pomarańczowy | `#e67e22` | Deadline, "zostało X dni", częściowa zgodność |

**Psychologia kolorów**: Granat buduje autorytet (jak garnitur). Czerwony aktywuje urgency. Niebieski uspokaja i buduje zaufanie przy cytowaniu regulacji. Pomarańczowy sygnalizuje "jeszcze nie za późno, ale działaj".

### TYPY NEWSÓW / ARTYKUŁÓW

| Typ | Częstotliwość | Cel psychologiczny | Przykładowy tytuł |
|-----|---------------|--------------------|--------------------|
| **Quiz/Test interaktywny** | 1 główny + warianty | Commitment — użytkownik inwestuje czas → chce wynik | "Test: Czy Twoja firma jest gotowa na NIS2? [12 pytań]" |
| **Checklista** | 2/mies. | Zeigarnik effect — otwarta lista ciągnie do ukończenia | "Checklista NIS2: 23 punkty, które musisz spełnić" |
| **Deadline countdown** | 1/mies. (stały update) | Urgency + loss aversion | "NIS2 w Polsce: zostało X miesięcy. Co musisz zrobić TERAZ" |
| **Explainer** | 2/mies. | Authority — edukujemy, budujemy pozycję eksperta | "Kim jest 'podmiot kluczowy' w NIS2? Sprawdź, czy to Ty" |
| **Case study / scenariusz** | 1/mies. | Narrative transportation — historia wciąga | "Firma X zignorowała NIS2. Oto co się stało" |
| **Nowości prawne** | ad hoc | Recency + informational | "Nowy projekt ustawy o KSC — co zmienia dla NIS2" |

### TECHNIKI PERSWAZJI NA STRONIE

1. **Hero z licznikiem** — na głównej stronie odliczanie do deadline NIS2. Wizualne tykanie zegara.
2. **Progress bar testu** — użytkownik widzi 1/12, 2/12... Zeigarnik effect nie pozwala przerwać.
3. **Wynik testu z kolorowym gauge** — czerwony/pomarańczowy/zielony. Natychmiast wizualizuje status.
4. **CTA po wyniku** — "Twój wynik: 4/12. Potrzebujesz profesjonalnego audytu → archaios.ai"
5. **Exit-intent popup** — "Pobierz PDF checklisty NIS2" → email capture → nurturing → archaios.ai
6. **Social proof banner** — "Ponad 1200 firm sprawdziło swoją gotowość na NIS2"

### SCHEMAT INFORMACYJNY (ARCHITEKTURA TREŚCI)

```
STRONA GŁÓWNA
├── Hero: Countdown + "Sprawdź gotowość" CTA
├── 4 filary (Audyt, Zgodność, Wdrożenie, Szkolenia)
├── Najnowsze artykuły (3 karty)
└── Newsletter signup

ARTYKUŁY (3 kategorie):
├── Audyt NIS2 → artykuły diagnostyczne, testy, checklisty
├── Regulacje → explainer prawa, nowości, interpretacje
└── Wdrożenia → how-to, plany, harmonogramy

KAŻDY ARTYKUŁ:
├── Breadcrumb (SEO)
├── H1 + excerpt
├── TOC (automatyczny)
├── Treść z H2/H3 (min. 1500 słów)
├── Bibliografia (E-E-A-T)
├── CTA produktowy (sidebar: archaios.ai, end: pełny blok)
├── Related articles (3)
└── Newsletter inline
```

### GRAFIKI — PROMPTY DO CHATGPT (DALL-E / GPT-4o)

> Wklej poniższe prompty do ChatGPT aby wygenerować grafiki dla testnis2.pl

#### OG Image (1200×630)

```prompt
Create a professional OG image (1200x630px) for a website called "TestNIS2.pl". 
Theme: Cybersecurity compliance testing.
Style: Corporate, clean, flat design. 
Colors: Dark navy (#1a365d) background, red accent (#c0392b), white text.
Elements: A shield icon with a checkmark, digital circuit pattern in background, 
text "Test NIS2" in bold white, subtitle "Sprawdź gotowość firmy" in lighter weight.
No gradients, no 3D effects. Modern, minimal, authoritative.
```

#### Hero background

```prompt
Create a wide hero image (1920x800px) for a cybersecurity compliance website.
Style: Abstract, corporate, minimal.
Colors: Deep navy (#1a365d) to dark blue gradient, subtle circuit board pattern.
Elements: Faint shield outlines, lock icons, connected nodes suggesting network security.
Very subtle — this will have white text overlaid on it.
No people, no text, no logos. Just atmospheric background.
```

#### Ikony filarów (4 sztuki)

```prompt
Create 4 flat icons (256x256px each) for a NIS2 compliance website. 
Style: Flat, minimal, monoline. Colors: Navy (#1a365d) on white background.
1. AUDIT — magnifying glass over a document with checkmarks
2. COMPLIANCE — balanced scale with a shield
3. IMPLEMENTATION — gear with an arrow showing process flow
4. TRAINING — graduation cap with a cyber lock
Clean lines, no shadows, no gradients. SVG-ready style.
```

#### Grafika do artykułu "Checklista NIS2"

```prompt
Create an infographic-style illustration (800x1200px) showing a checklist concept.
Style: Flat, corporate, clean.
Colors: Navy (#1a365d), red (#c0392b) for X marks, green (#27ae60) for checkmarks.
Elements: A clipboard with 6-8 checklist items, some checked (green), some X (red).
Title area at top for "Checklista NIS2". 
Professional, would fit on a compliance blog. No text except title placeholder.
```

#### Countdown / Deadline grafika

```prompt
Create a countdown-style graphic (1200x630px) for NIS2 deadline awareness.
Style: Urgent, corporate, clean.
Colors: Dark navy (#1a365d) background, red (#c0392b) for urgency, white text.
Elements: Digital clock/timer display showing "XX DNI", 
warning triangle icon, subtle ticking clock concept.
Text placeholder: "Do wdrożenia NIS2 zostało:" with large number area below.
Feeling: Time is running out, act now.
```

### DESIGN — PROMPTY DO CLAUDE (Artifacts / Cowork)

> Wklej do Claude z prośbą o wygenerowanie komponentów

#### Quiz NIS2 — interaktywny komponent React

```prompt
Stwórz interaktywny quiz "Czy Twoja firma jest gotowa na NIS2?" jako komponent React.
12 pytań tak/nie dotyczących wymogów NIS2 (zarządzanie ryzykiem, incydenty, łańcuch dostaw, szkolenia).
Kolorystyka: primary #1a365d, accent #c0392b, success #27ae60.
Funkcje:
- Progress bar na górze (1/12, 2/12...)
- Pytanie + dwa przyciski (Tak / Nie)
- Na końcu: gauge z wynikiem (0-12), 
  kolor: 0-4 czerwony, 5-8 pomarańczowy, 9-12 zielony
- Tekst interpretacji wyniku
- CTA button: "Zamów profesjonalny audyt" → link do archaios.ai
- Animacja przejść między pytaniami
Responsywny, mobile-first. Po polsku.
```

#### Countdown widget

```prompt
Stwórz widget odliczania do deadline NIS2 jako komponent HTML.
Data docelowa: 17 października 2026 (transpozycja krajowa PL — ustaw datę).
Wyświetla: DNI : GODZINY : MINUTY : SEKUNDY
Kolorystyka: tło #1a365d, cyfry białe, separatory #c0392b.
Pod licznikiem tekst: "Do obowiązkowego wdrożenia NIS2 w Polsce"
Responsywny, typografia: monospace dla cyfr, sans-serif dla tekstu.
Pulsująca kropka obok "LIVE" w prawym górnym rogu.
```

#### Gauge wyników testu

```prompt
Stwórz SVG gauge (półkole) pokazujący wynik testu NIS2 (0-100%).
Kolorystyka: 0-33% czerwony (#c0392b), 34-66% pomarańczowy (#e67e22), 67-100% zielony (#27ae60).
Pod gauge: duża liczba "45%" i tekst "Poziom gotowości".
Styl: czysty, flat, bez cieni. Tło przezroczyste.
Animacja: wskazówka gauge płynnie przesuwa się do wartości.
```

---

## SATELITA 2: karynis2.pl

### IDENTYFIKACJA

| Element | Wartość |
|---------|---------|
| **Domena** | karynis2.pl |
| **Rola** | Strach i motywacja — "co mi grozi jeśli nie wdrożę NIS2" |
| **Intencja SEO** | "kary NIS2", "grzywny NIS2", "konsekwencje NIS2", "ile wynosi kara NIS2" |
| **Emocja docelowa** | Strach → kalkulacja ryzyka → decyzja o działaniu |
| **CTA końcowe** | → archaios.ai/wdrozenie |

### KOLORYSTYKA

Taka sama paleta jak klaster NIS2, ale z **dominantą czerwieni** — strona operuje strachem.

| Rola | Kolor | Hex | Użycie |
|------|-------|-----|--------|
| Primary | Granatowy | `#1a365d` | Nagłówki, nawigacja — stabilność |
| Accent/Dominant | Czerwony | `#c0392b` | Kwoty kar, alerty, "UWAGA", wyróżnienia |
| Warning | Ciemny pomarańcz | `#d35400` | "Ryzyko", "Ostrzeżenie" |
| Trust | Niebieski | `#2980b9` | Źródła prawne, akty UE |
| Escape (CTA) | Zielony | `#27ae60` | "Uniknij kary" — jedyny zielony element = przycisk CTA |

**Psychologia kolorów**: Czerwień dominuje → pobudzenie, alarm. Jedyny "wyjście" to zielony CTA → archaios.ai. Kontrast czerwień/zieleń to klasyczny pattern "problem → rozwiązanie".

### TYPY NEWSÓW / ARTYKUŁÓW

| Typ | Częstotliwość | Cel psychologiczny | Przykładowy tytuł |
|-----|---------------|--------------------|--------------------|
| **Kalkulator kar** | 1 interaktywny tool | Personalizacja strachu — "TWOJA kara" | "Kalkulator kar NIS2: ile zapłaci Twoja firma?" |
| **Tabele kar per sektor** | 3-5 artykułów | Specificity — konkretne liczby = realne | "Kary NIS2 w sektorze energetycznym: od 7M do 10M EUR" |
| **Case study kary** | 1/mies. | Narrative transport — "to mogło być mnie" | "Pierwsza kara NIS2 w Europie: 2.3M EUR za brak planu incydentów" |
| **Porównanie kar NIS2 vs RODO** | 1 artykuł cornerstone | Anchoring — RODO jest znane, NIS2 = nowe + surowsze | "NIS2 vs RODO: która kara jest większa? [porównanie]" |
| **Odpowiedzialność zarządu** | 2 artykuły | Fear at decision-maker level | "NIS2: Zarząd odpowiada osobiście. Co to oznacza?" |
| **"Jak uniknąć kary"** | 2/mies. | Hope after fear — rozwiązanie po strachu | "5 kroków, które ochronią Cię przed karą NIS2" |

### TECHNIKI PERSWAZJI NA STRONIE

1. **"Kalkulator kar" na hero** — użytkownik wpisuje obrót firmy → wyświetla maksymalną karę. Personalizacja.
2. **Czerwone alerty inline** — bloki "⚠ UWAGA: Za ten brak grozi kara do X EUR" wewnątrz artykułów.
3. **Tabela porównawcza kar** — NIS2 vs RODO vs inne. Anchoring: NIS2 jest surowszy.
4. **Testimonial zarządu** — cytat fikcyjny: "Gdybym wiedział wcześniej, zaoszczędziłbym firmie 2M EUR".
5. **Zielony CTA jako jedyne wyjście** — cała strona czerwono-granatowa, jedyny zielony element = "Uniknij kary → archaios.ai".
6. **Efekt kontrastu** — artykuł o karze 10M EUR, a pod spodem CTA: "Audyt NIS2 od 5000 PLN" → anchoring cenowy.

### SCHEMAT INFORMACYJNY

```
STRONA GŁÓWNA
├── Hero: "Ile zapłaci Twoja firma?" + Kalkulator kar
├── 4 filary (Kary, Odpowiedzialność zarządu, Case studies, Jak uniknąć)
├── Tabela kar per sektor (skrót)
├── Najnowsze artykuły
└── CTA: "Uniknij kary — zamów audyt"

ARTYKUŁY (3 kategorie):
├── Kary → kwoty, sektory, mechanizm nakładania
├── Prawo → analiza aktów, interpretacje, nowelizacje
└── Case studies → realne/hipotetyczne scenariusze kar
```

### GRAFIKI — PROMPTY DO CHATGPT

#### OG Image

```prompt
Create a professional OG image (1200x630px) for "KaryNIS2.pl" — a website about NIS2 penalties.
Style: Corporate, alarming but professional.
Colors: Dark navy (#1a365d) background, bold red (#c0392b) accent, white text.
Elements: Euro sign (€) with warning triangle, cracked shield icon.
Text: "Kary NIS2" in large white bold, subtitle "Do 10 000 000 EUR" in red.
Feeling: Serious financial consequence. Clean, no gradients.
```

#### Infografika kar per sektor

```prompt
Create an infographic (800x1600px) showing NIS2 penalties by sector.
Style: Clean, data-driven, corporate.
Colors: Navy (#1a365d) background, red (#c0392b) for penalty amounts, white text.
Layout: Vertical list of 8 sectors (Energy, Transport, Health, Banking, Digital, Water, Space, Government) 
each with an icon and penalty range bar.
Bar chart style: horizontal bars showing "up to 10M EUR" or "up to 7M EUR".
Title: "Kary NIS2 wg sektora" at top.
Professional, would work as blog post header.
```

#### Ikona kalkulatora

```prompt
Create a flat icon (512x512px) of a penalty calculator concept.
Style: Flat, minimal, modern.
Colors: Navy (#1a365d), red (#c0392b).
Elements: Calculator with euro (€) sign on screen, 
small warning triangle in corner. 
Clean lines, no shadows. SVG-ready.
```

### DESIGN — PROMPTY DO CLAUDE

#### Kalkulator kar NIS2

```prompt
Stwórz interaktywny kalkulator kar NIS2 jako komponent React.
Pola wejściowe:
1. Roczny obrót firmy (slider: 1M - 500M PLN)
2. Typ podmiotu (dropdown: kluczowy / ważny)
3. Sektor (dropdown: energetyka, transport, zdrowie, bankowość, cyfrowy, woda, przestrzeń, administracja)
Wynik:
- Maksymalna kara (2% obrotu lub 10M EUR — wyższa kwota)
- Kara minimalna przewidywana
- Wizualizacja: duża czerwona kwota + porównanie "to tyle co X pensji / Y samochodów"
Kolorystyka: #1a365d, #c0392b, CTA zielony #27ae60.
CTA na dole: "Uniknij tej kary → Zamów audyt NIS2"
Responsywny, po polsku.
```

#### Tabela porównawcza NIS2 vs RODO

```prompt
Stwórz elegancką tabelę porównawczą HTML: NIS2 vs RODO.
Kolumny: Aspekt | NIS2 | RODO
Wiersze: Maksymalna kara, Kto podlega, Termin wdrożenia, Zgłaszanie incydentów, Odpowiedzialność zarządu, Audyty.
Kolorystyka: nagłówki #1a365d, wartości NIS2 podświetlone na #c0392b (surowsze), RODO na #2980b9.
Wiersz "Maksymalna kara" wyróżniony — bold, większa czcionka.
Responsywna, czytelna na mobile.
```

---

## SATELITA 3: skanujfirme.pl

### IDENTYFIKACJA

| Element | Wartość |
|---------|---------|
| **Domena** | skanujfirme.pl |
| **Rola** | Dual-scope: NIS2 + RODO — kompleksowy audyt bezpieczeństwa firmy |
| **Intencja SEO** | "audyt firmy", "skanowanie bezpieczeństwa", "sprawdź RODO", "audyt NIS2 i RODO" |
| **Emocja docelowa** | "Nie wiem, czy jestem bezpieczny" → diagnoza → plan działania |
| **CTA końcowe** | → archaios.ai/audyt |

### KOLORYSTYKA

| Rola | Kolor | Hex | Użycie |
|------|-------|-----|--------|
| Primary | Granatowy | `#1a365d` | Nagłówki, nawigacja — profesjonalizm |
| NIS2 accent | Czerwony | `#c0392b` | Sekcje NIS2, alerty cyber |
| RODO accent | Ciemny niebieski | `#2c3e50` | Sekcje RODO, ochrona danych |
| Scanner | Cyjan | `#00bcd4` | Elementy "skanowania", progress bary, animacje scan |
| Trust | Niebieski | `#2980b9` | Źródła prawne |

**Psychologia kolorów**: Cyjan dodaje element "technologii" i "skanowania" — kojarzy się z radarami, diagnostyką, interfejsami skanujących narzędzi. Dwa akcenty (czerwony NIS2 / ciemnoniebieski RODO) wizualnie rozdzielają dwa obszary compliance.

### TYPY NEWSÓW / ARTYKUŁÓW

| Typ | Częstotliwość | Cel psychologiczny | Przykładowy tytuł |
|-----|---------------|--------------------|--------------------|
| **Dual audit explainer** | 2/mies. | Framing — jeden audyt zamiast dwóch = oszczędność | "NIS2 + RODO: jeden audyt zamiast dwóch [przewodnik]" |
| **Checklista zbiorcza** | 1 cornerstone | Completeness — pełna lista buduje zaufanie | "Mega-checklista: 50 punktów NIS2 + RODO dla Twojej firmy" |
| **Porównanie wymogów** | 2 artykuły | Clarity — co się pokrywa, co jest osobne | "NIS2 vs RODO: co się pokrywa, a co musisz zrobić podwójnie" |
| **Narzędzie self-scan** | 1 interaktywny | Engagement — 5-minutowy scan daje wynik | "Skanuj swoją firmę: 5-minutowy test NIS2 + RODO" |
| **Branżowy explainer** | 4/mies. | Specificity — "to dotyczy MOJEJ branży" | "RODO + NIS2 w e-commerce: co musisz wiedzieć" |
| **Nowości prawne** | ad hoc | Recency | "UODO zmienia interpretację — co to znaczy dla NIS2" |

### TECHNIKI PERSWAZJI NA STRONIE

1. **"Skan" animacja na hero** — wizualna animacja skanowania (pasek przesuwający się po ekranie). Metafora diagnostyki.
2. **Dual-badge system** — każdy artykuł ma badge "NIS2" (czerwony) i/lub "RODO" (niebieski). Użytkownik widzi zakres.
3. **Venn diagram** — na stronie głównej: dwa nakładające się koła NIS2 + RODO. Środek = to co pokryjesz jednym audytem.
4. **"Twój wynik skanowania"** — po interaktywnym teście: dwa gauge'e (NIS2 score + RODO score).
5. **Anchoring cenowy** — "Dwa osobne audyty: ~30 000 PLN. Zintegrowany audyt w archaios.ai: od 8 000 PLN".
6. **Trust badges** — "Zgodne z wytycznymi ENISA" + "Zgodne z wytycznymi UODO".

### GRAFIKI — PROMPTY DO CHATGPT

#### OG Image

```prompt
Create a professional OG image (1200x630px) for "SkanujFirme.pl" — a website about NIS2 + GDPR compliance scanning.
Style: Corporate, tech-forward, clean.
Colors: Dark navy (#1a365d) background, cyan (#00bcd4) scan line, white text.
Elements: Abstract radar/scan visualization, two overlapping shields (one red for NIS2, one blue for GDPR/RODO).
Text: "Skanuj Firmę" in white bold, subtitle "NIS2 + RODO w jednym audycie".
Feeling: Diagnostic, technological, comprehensive. No gradients.
```

#### Venn Diagram NIS2 + RODO

```prompt
Create a Venn diagram infographic (1200x800px).
Two overlapping circles:
- Left circle: Red (#c0392b), labeled "NIS2" — contains: cyberbezpieczeństwo, incydenty 24h, CSIRT, supply chain
- Right circle: Blue (#2c3e50), labeled "RODO" — contains: dane osobowe, UODO, DPO, prawa podmiotów
- Overlap center: Purple blend — contains: analiza ryzyka, szkolenia, dokumentacja, audyty, kary finansowe
Style: Clean, flat, professional. White text on colored backgrounds.
Title at top: "Co łączy NIS2 i RODO?"
```

#### Animacja skanu (statyczna wersja)

```prompt
Create a tech-style illustration (1200x630px) of a business being "scanned".
Style: Flat, isometric-lite, modern.
Colors: Navy (#1a365d) base, cyan (#00bcd4) scan beam, white/light gray building.
Elements: An office building or server room with a horizontal cyan line sweeping across it (scanning effect), 
small checkmark and X icons appearing where the beam has passed.
Feeling: Diagnostic, technological, non-threatening.
```

### DESIGN — PROMPTY DO CLAUDE

#### Dual-scope self-scan quiz

```prompt
Stwórz interaktywny quiz "Skanuj swoją firmę" jako komponent React.
Dwie sekcje: NIS2 (8 pytań) i RODO (8 pytań), łącznie 16 pytań.
Każde pytanie: tak/nie, z ikoną kategorii.
Na końcu: DWA gauge'e obok siebie:
- Lewy: "Gotowość NIS2" (0-100%) z kolorem czerwonym/pomarańczowym/zielonym
- Prawy: "Zgodność RODO" (0-100%) z kolorem czerwonym/pomarańczowym/zielonym
Pod spodem: personalizowana rekomendacja na podstawie wyników.
CTA: "Zamów pełny audyt NIS2 + RODO → archaios.ai"
Kolorystyka: #1a365d, NIS2 badge #c0392b, RODO badge #2c3e50, scan elements #00bcd4.
Animacja: scan line effect przy przejściu między pytaniami.
Responsywny, po polsku.
```

---

## SATELITA 4: onpremiseai.pl

### IDENTYFIKACJA

| Element | Wartość |
|---------|---------|
| **Domena** | onpremiseai.pl |
| **Rola** | Niszowy ekspert — AI w lokalnej infrastrukturze, compliance-first |
| **Intencja SEO** | "AI on premise", "lokalne LLM", "AI bez chmury", "prywatne AI w firmie" |
| **Emocja docelowa** | "Chcę AI, ale boję się o dane" → bezpieczeństwo → zaufanie |
| **CTA końcowe** | → archaios.ai/ai-implementation |

### KOLORYSTYKA

| Rola | Kolor | Hex | Użycie |
|------|-------|-----|--------|
| Primary | Granatowy | `#1a365d` | Nagłówki — enterprise feel |
| Tech accent | Indygo | `#4a69bd` | Elementy AI, schematy, kod |
| Security | Zielony | `#27ae60` | "On-premise = bezpieczne", prywatność |
| Warning | Pomarańczowy | `#e67e22` | "Chmura = ryzyko" |
| Accent CTA | Czerwony | `#c0392b` | CTA, wyróżnienia |

**Psychologia kolorów**: Zielony = bezpieczeństwo danych. Indygo = technologia, innowacja. Pomarańczowy ostrzega przed chmurą publiczną. Kontrast "chmura (niebezpieczna/pomarańczowa)" vs "on-premise (bezpieczne/zielone)".

### TYPY NEWSÓW / ARTYKUŁÓW

| Typ | Częstotliwość | Cel psychologiczny | Przykładowy tytuł |
|-----|---------------|--------------------|--------------------|
| **Porównanie cloud vs on-prem** | 2 cornerstone | Framing — on-prem = jedyna bezpieczna opcja | "Dlaczego Twoje dane nie powinny opuszczać firmy" |
| **Tutorial wdrożenia** | 2/mies. | Authority — pokazujemy, że umiemy | "Jak postawić lokalne LLM w 30 minut [tutorial]" |
| **Compliance explainer** | 2/mies. | Fear-then-relief — AI w chmurze łamie RODO? | "AI + RODO: czy chmura publiczna łamie prawo?" |
| **Model reviews** | 1/mies. | Information — przegląd modeli open-source | "Top 5 modeli LLM do wdrożenia on-premise w 2026" |
| **Case study** | 1/mies. | Social proof — "firma X już to zrobiła" | "Bank Y wdrożył lokalne AI i zaoszczędził 40% na compliance" |
| **Koszty vs chmura** | 1 artykuł | Anchoring — on-prem droższy na start, tańszy long-term | "TCO: on-premise AI vs Azure/AWS — kalkulacja na 3 lata" |

### TECHNIKI PERSWAZJI NA STRONIE

1. **"Twoje dane nie opuszczają budynku"** — hero statement z ikoną zamkniętego zamka.
2. **Porównanie dwóch ścieżek** — wizualna infografika: "Chmura: dane lecą do USA ⚠" vs "On-premise: dane zostają u Ciebie ✓".
3. **Schematyczne diagramy** — architektura on-premise AI (serwer → model → API → użytkownicy). Buduje zaufanie techniczne.
4. **Trust badge "NIS2 Compliant"** — on-premise = automatycznie łatwiejszy compliance.
5. **TCO kalkulator** — "Oblicz, ile zaoszczędzisz w 3 lata" → archaios.ai.

### GRAFIKI — PROMPTY DO CHATGPT

#### OG Image

```prompt
Create a professional OG image (1200x630px) for "OnPremiseAI.pl".
Theme: AI running securely in local infrastructure.
Style: Corporate, tech, clean.
Colors: Navy (#1a365d) background, indigo (#4a69bd) tech accents, green (#27ae60) security.
Elements: Server rack icon with AI brain symbol inside, closed padlock, 
text "On-Premise AI" in white, subtitle "AI w Twojej infrastrukturze".
Feeling: Secure, innovative, enterprise-grade.
```

#### Diagram Cloud vs On-Premise

```prompt
Create a comparison infographic (1200x800px): Cloud AI vs On-Premise AI.
Left side (orange/warning): Cloud — data arrows going to external servers, 
warning icons, "Dane poza kontrolą", latency indicators.
Right side (green/safe): On-Premise — data stays inside building, 
lock icon, "Pełna kontrola", low latency.
Center: VS divider.
Style: Flat, isometric-lite. Colors: orange (#e67e22) for cloud risks, 
green (#27ae60) for on-premise benefits, navy (#1a365d) base.
```

### DESIGN — PROMPTY DO CLAUDE

#### TCO Calculator

```prompt
Stwórz kalkulator TCO (Total Cost of Ownership) jako komponent React.
Porównanie: On-Premise AI vs Cloud AI na 1/2/3 lata.
Pola:
- Liczba użytkowników (slider: 10-500)
- Średnie zapytania/dzień (slider: 100-10000)
- Model (dropdown: 7B / 13B / 70B parametrów)
Wynik: dwa słupki obok siebie (Cloud vs On-Prem) z kwotami PLN/rok.
Punkt break-even zaznaczony na osi czasu.
Kolorystyka: #1a365d, Cloud=#e67e22, On-Prem=#27ae60.
CTA: "Zamów wycenę wdrożenia → archaios.ai"
```

---

## SATELITA 5: aidzisiaj.pl

### IDENTYFIKACJA

| Element | Wartość |
|---------|---------|
| **Domena** | aidzisiaj.pl |
| **Rola** | Najszerszy zasięg — ogólne AI w polskim biznesie, trend-catching |
| **Intencja SEO** | "AI w firmie", "sztuczna inteligencja biznes", "narzędzia AI", "AI dla firm" |
| **Emocja docelowa** | Ciekawość → FOMO → "muszę to wdrożyć" |
| **CTA końcowe** | → archaios.ai (ogólne) |

### KOLORYSTYKA

| Rola | Kolor | Hex | Użycie |
|------|-------|-----|--------|
| Primary | Granatowy | `#1a365d` | Nagłówki |
| Tech/Innovation | Elektryczny niebieski | `#2196f3` | Elementy AI, ikony, wyróżnienia |
| Accent | Pomarańczowy | `#ff9800` | CTA, "Nowe!", trending |
| Trust | Granat jasny | `#4a7ab5` | Linki, źródła |
| Code | Szary ciemny | `#37474f` | Bloki kodu, terminale |

**Psychologia kolorów**: Elektryczny niebieski = innowacja, technologia, przyszłość. Pomarańczowy = energia, "nowe", "trending". To paleta "tech blogu" — szybka, energiczna, na czasie.

### TYPY NEWSÓW / ARTYKUŁÓW

| Typ | Częstotliwość | Cel psychologiczny | Przykładowy tytuł |
|-----|---------------|--------------------|--------------------|
| **Trend/News** | 3/mies. | FOMO — "wszyscy już to robią" | "GPT-5 w firmach: co zmieni się w 2026?" |
| **Narzędzie review** | 2/mies. | Practical value — oszczędzam czas na research | "10 narzędzi AI, które wdrożysz w firmie w 1 dzień" |
| **How-to / Tutorial** | 2/mies. | Self-efficacy — "ja też mogę" | "Jak zautomatyzować raporty w firmie z AI [krok po kroku]" |
| **ROI / Business case** | 1/mies. | Rational justification for emotional decision | "AI w obsłudze klienta: ROI 340% w 6 miesięcy [case study]" |
| **Regulacje AI** | 1/mies. | Fear + foresight — AI Act, compliance | "AI Act: co zmieni się dla polskich firm w 2026" |
| **Porównanie narzędzi** | 1/mies. | Decision support | "Claude vs GPT vs Gemini: które AI dla Twojej firmy?" |

### TECHNIKI PERSWAZJI NA STRONIE

1. **"Trending" badge na artykułach** — pomarańczowy badge "🔥 Trending" na popularnych. FOMO.
2. **Licznik "firm, które już wdrożyły AI"** — rosnący counter na hero. Social proof.
3. **Before/After sekcja** — "Przed AI: 4h na raport. Po AI: 12 minut." Wizualna redukcja.
4. **Newsletter z "AI Digest"** — cotygodniowe podsumowanie newsów AI. Lead magnet.
5. **Kalkulator oszczędności** — "Ile zaoszczędzisz z AI?" → wynik → "Wdrożymy to w archaios.ai".
6. **FOMO ticker** — pasek na górze: "Firma X wdrożyła AI asystenta. Firma Y zautomatyzowała raporty." Scroll.

### GRAFIKI — PROMPTY DO CHATGPT

#### OG Image

```prompt
Create a modern OG image (1200x630px) for "AIDzisiaj.pl" — AI business news portal.
Style: Tech-forward, energetic, modern.
Colors: Navy (#1a365d) background, electric blue (#2196f3) accents, orange (#ff9800) highlights.
Elements: Abstract AI brain/network visualization, trending arrow upward, 
text "AI Dzisiaj" in white bold, subtitle "Sztuczna inteligencja w polskim biznesie".
Feeling: Innovative, fast-paced, must-read. Clean, flat design.
```

#### Ikony kategorii

```prompt
Create 4 flat icons (256x256px each) for an AI business blog.
Style: Minimal, tech-modern. Colors: Electric blue (#2196f3) on white.
1. AI TOOLS — robot hand holding a wrench
2. BUSINESS — chart with AI sparkle
3. TUTORIALS — screen with code and play button
4. REGULATIONS — document with AI chip and gavel
Clean, no shadows, modern tech aesthetic.
```

### DESIGN — PROMPTY DO CLAUDE

#### AI Savings Calculator

```prompt
Stwórz kalkulator oszczędności AI jako komponent React.
Pola:
- Typ zadania (dropdown: Raporty, Obsługa klienta, Analiza danych, Content, Tłumaczenia)
- Obecny czas na zadanie (slider: 1-40h/tydzień)
- Stawka godzinowa pracownika (slider: 50-300 PLN)
Wynik:
- Czas zaoszczędzony/miesiąc z AI (założenie: 70% redukcji)
- Kwota oszczędności PLN/miesiąc i PLN/rok
- Wizualizacja: dwa słupki Before vs After
Kolorystyka: #1a365d, #2196f3, #ff9800 dla CTA.
CTA: "Wdrożymy to w Twojej firmie → archaios.ai"
Responsywny, po polsku.
```

#### Trending Ticker

```prompt
Stwórz animowany pasek "trending" jako komponent HTML.
Automatycznie przewijający się tekst od prawej do lewej:
"🔥 Firma X wdrożyła AI chatbota — obsługa +200% • 📊 AI w e-commerce: wzrost konwersji o 34% • 🤖 Nowy model Llama 4 dostępny on-premise •"
Kolorystyka: tło #1a365d, tekst biały, emoji kolorowe.
Prędkość: spokojna, czytelna. Pauza on hover.
Wysokość: 40px, width: 100%. Sticky top.
```

---

## WSPÓLNE ELEMENTY KLASTRA

### Spójność wizualna

Wszystkie 5 satelitów dzieli:
- **Font nagłówków**: Fraunces (serif) — buduje autorytet
- **Font body**: Inter (sans) — czytelność
- **Radius**: 14px — zaokrąglone, ale profesjonalne
- **Shadow warmth**: warm — nie zimne korporacyjne cienie
- **Footer disclaimer**: "Treści mają charakter informacyjny. Nie stanowią porady prawnej."
- **Newsletter sekcja**: ciemne tło (ink color), CTA accent

### Cross-linking między satelitami

```
testnis2.pl → "Przeczytaj też: Ile wynosi kara za brak NIS2?" (link do karynis2.pl)
karynis2.pl → "Sprawdź, czy Twoja firma podlega NIS2" (link do testnis2.pl)
skanujfirme.pl → "NIS2 + RODO: jeden audyt zamiast dwóch" (wewnętrzny)
               → "Wdrożenie AI bez ryzyka compliance" (link do onpremiseai.pl)
onpremiseai.pl → "AI w firmie: od czego zacząć?" (link do aidzisiaj.pl)
aidzisiaj.pl → "Czy Twoja firma jest gotowa na NIS2?" (link do testnis2.pl)
```

### UTM Convention

Każdy link satelita → archaios.ai:
```
https://archaios.ai/audyt?utm_source=testnis2.pl&utm_medium=article&utm_campaign={article-slug}
```

---

## NASTĘPNE KROKI

1. ✅ Strategia klastra NIS2 (ten dokument)
2. ⬜ Strategia klastra Psychologia (6 satelitów → nurio.pl + psychozdrowie.online)
3. ⬜ Strategia klastra Mediacja + Reszta
4. ⬜ Generowanie grafik w ChatGPT per domena
5. ⬜ Generowanie komponentów w Claude per domena
6. ⬜ Build all + deploy na Cyberfolks
