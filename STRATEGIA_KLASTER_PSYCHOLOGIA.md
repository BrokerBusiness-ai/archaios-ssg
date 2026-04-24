# STRATEGIA KLASTRA PSYCHOLOGIA — 7 SATELITÓW → nurio.pl + psychozdrowie.online

> Dokument operacyjny. Każda domena ma kartę strategiczną z gotowymi promptami do wklejenia w ChatGPT (grafiki) i Claude (design/content). Wygenerowane materiały trafiają do `src/static/img/` danej domeny.

---

## ARCHITEKTURA KLASTRA

```
psychodzisiaj.pl ─────┐
psychosen.pl ─────────┤
jaksobieradzic.pl ────┤
sprawdzwypalenie.pl ──┤──→ nurio.pl (AI companion do dobrostanu)
testpredyspozycje.pl ─┤    + psychozdrowie.online (testy, diagnozy, usługi)
zdrowie.fit ──────────┤
psycho.edu.pl ────────┘
```

**Mechanizm orbity**: Każdy satelita przechwytuje ruch z innego kąta intencji psychologicznej. Użytkownik trafia przez SEO, konsumuje wartościowy content oparty na badaniach, a CTA kieruje go do:
- **nurio.pl** — AI companion, codzienny dobrostan, self-help
- **psychozdrowie.online** — profesjonalne testy, diagnozy, konsultacje

**Podwójny cel konwersji** — w odróżnieniu od klastra NIS2 (single target: archaios.ai), tu mamy dwa produkty. Routing zależy od intencji:
- Intencja "chcę się lepiej poczuć" → nurio.pl
- Intencja "chcę się zbadać / zdiagnozować" → psychozdrowie.online
- Artykuły zawierają OBA CTA, ale z różnym priorytetem per kategoria

**Techniki perswazji wspólne dla klastra**:
- **Self-reference effect** — "Czy to dotyczy Ciebie?" — treści pisane w 2. osobie, z pytaniami aktywującymi identyfikację
- **Mere exposure effect** — powtarzalne pojawienie się marek nurio/psychozdrowie w kontekście "pomagania" buduje pozytywne skojarzenie
- **Barnum effect** — opisy psychologiczne trafnie "pasujące do każdego" → zachęcają do testów
- **Curiosity gap** — tytuły z luką informacyjną: "5 sygnałów, które ignorujesz — a nie powinieneś"
- **Authority bias** — cytowanie badań APA, WHO, metaanaliz. Format: Autor (rok), N=, efekt
- **Reciprocity** — darmowa wartość (artykuły, mini-testy) → chęć odwzajemnienia (zapisy, zakupy)

**Wspólny disclaimer klastra**: "Treści mają charakter edukacyjny i nie zastępują profesjonalnej pomocy psychologicznej ani psychoterapii."

---

## SATELITA 1: psychodzisiaj.pl

### IDENTYFIKACJA

| Element | Wartość |
|---------|---------|
| **Domena** | psychodzisiaj.pl |
| **Rola** | Hub klastra — psychologia codzienna, najszerszy zasięg SEO |
| **Intencja SEO** | "psychologia codzienna", "dlaczego czuję", "jak radzić sobie z emocjami", "psychologia relacji" |
| **Emocja docelowa** | Ciekawość → identyfikacja → "to mówi o mnie" → chęć zmiany |
| **CTA główne** | → nurio.pl (primary) / psychozdrowie.online (secondary) |

### KOLORYSTYKA

| Rola | Kolor | Hex | Użycie |
|------|-------|-----|--------|
| Primary | Morski teal | `#2c6e8a` | Nagłówki, nawigacja — spokój, profesjonalizm, zaufanie |
| Primary dark | Ciemny teal | `#1d4e66` | Hover, footer, aktywne stany |
| Accent | Ciepły coral | `#e07b4f` | CTA, wyróżnienia, "Przeczytaj", notyfikacje |
| Accent dark | Głęboki coral | `#c0623a` | Hover na CTA |
| Trust | Fiolet | `#7b68ee` | Cytaty badań, źródła naukowe, "zbadano" badge |
| Warm | Złoty ciepły | `#d4a843` | Ikony emocji, highlight w treści |

**Psychologia kolorów**: Morski teal = spokój + kompetencja (jak gabinet psychologa). Coral = ciepło, empatia, zachęta do działania. Fiolet = introspekcja, głębia, nauka. Złoty = wartość, pozytywna zmiana.

### TYPY NEWSÓW / ARTYKUŁÓW

| Typ | Częstotliwość | Cel psychologiczny | Przykładowy tytuł |
|-----|---------------|--------------------|--------------------|
| **"Czy to normalne?"** | 3/mies. | Self-reference — "to o mnie!" → identyfikacja | "Ciągle się martwisz? 7 oznak, że to może być GAD" |
| **Explainer emocji** | 2/mies. | Naming effect — nazwanie emocji zmniejsza jej siłę | "Czym różni się smutek od depresji — i kiedy szukać pomocy" |
| **Technika CBT/DBT** | 2/mies. | Self-efficacy — "mogę to zrobić sam" | "Technika 5-4-3-2-1: Jak zatrzymać atak paniki w 60 sekund" |
| **Psychologia relacji** | 2/mies. | Social identity — relacje to fundament | "4 style przywiązania: który jest Twój i co to zmienia?" |
| **Mini-quiz** | 1/mies. | Commitment — inwestujesz czas → chcesz wynik | "Test: Jaki jest Twój dominujący styl radzenia sobie?" |
| **Badanie tygodnia** | 1/mies. | Authority + novelty — "nauka mówi, że..." | "Nowe badanie: 15 min dziennie tej aktywności obniża lęk o 30%" |

### TECHNIKI PERSWAZJI NA STRONIE

1. **"Czy to o Tobie?" hero** — pytanie otwierające na głównej stronie z opisem uniwersalnym (Barnum): "Czujesz, że coś jest nie tak, ale nie wiesz co? Nie jesteś sam/sama."
2. **Emotion wheel** — interaktywne koło emocji na stronie głównej. Kliknij emocję → artykuły. Engagement + nawigacja.
3. **"Badania mówią" sidebar** — w każdym artykule blok z cytowaniem badania: Autor (rok), N=, główny wynik. Authority bias.
4. **Progressive disclosure** — artykuły zaczynają od objawów (identyfikacja), potem mechanizm (edukacja), potem rozwiązanie (CTA do nurio.pl).
5. **Social proof** — "Ponad 5000 osób przeczytało ten artykuł w tym miesiącu".
6. **Sticky CTA** — po przescrollowaniu 60% artykułu pojawia się delikatny pasek: "Potrzebujesz wsparcia? → Wypróbuj Nurio".

### SCHEMAT INFORMACYJNY (ARCHITEKTURA TREŚCI)

```
STRONA GŁÓWNA
├── Hero: "Czy to o Tobie?" + Emotion Wheel CTA
├── 4 filary (Emocje, Relacje, Stres, Rozwój osobisty)
├── Najnowsze artykuły (3 karty)
├── Sekcja "Badanie tygodnia" (wyróżniony blok)
├── Mini-quiz embed (1 pytanie → "kontynuuj na psychozdrowie.online")
└── Newsletter signup

ARTYKUŁY (4 kategorie):
├── Psychologia codzienna → explainer, "czy to normalne?", nawyki
├── Emocje → naming, regulacja, techniki CBT/DBT
├── Relacje → style przywiązania, komunikacja, granice
└── Stres & Rozwój → radzenie sobie, motywacja, zmiana

KAŻDY ARTYKUŁ:
├── Breadcrumb (SEO)
├── H1 + excerpt (z pytaniem "Czy to o Tobie?")
├── TOC (automatyczny)
├── Treść z H2/H3 (min. 1500 słów)
├── "Badania mówią" sidebar (cytowania)
├── CTA nurio.pl (end: pełny blok) + psychozdrowie.online (sidebar: mini-test)
├── Related articles (3)
└── Newsletter inline
```

### GRAFIKI — PROMPTY DO CHATGPT (DALL-E / GPT-4o)

#### OG Image (1200×630)

```prompt
Create a professional OG image (1200x630px) for "PsychoDzisiaj.pl" — a psychology self-help website.
Style: Warm, approachable, professional. Soft gradients, organic shapes.
Colors: Teal (#2c6e8a) as dominant, warm coral (#e07b4f) accent, light ivory (#fdfcf9) background areas.
Elements: Abstract human head silhouette with gentle flowing lines representing thoughts/emotions, 
a soft brain outline, text "Psycho Dzisiaj" in a clean serif font, subtitle "Psychologia na co dzień".
Feeling: Calm, trustworthy, empathetic. No clinical/cold feel — warm and inviting.
No stock photo style. Modern, editorial illustration aesthetic.
```

#### Hero background

```prompt
Create a wide hero image (1920x800px) for a psychology self-help website.
Style: Abstract, warm, organic. Watercolor-meets-digital.
Colors: Soft teal (#2c6e8a) flowing into warm coral (#e07b4f), with ivory (#fdfcf9) spaces.
Elements: Abstract flowing shapes suggesting emotions, gentle curves, 
subtle neuron-like connections in teal. Very atmospheric and calming.
This will have dark text overlaid — keep it light enough for readability.
No people, no text, no logos. Just atmospheric background.
```

#### Ikony filarów (4 sztuki)

```prompt
Create 4 flat icons (256x256px each) for a psychology website about daily emotional wellbeing.
Style: Warm, rounded, friendly. Thick outlines, soft fill. Colors: Teal (#2c6e8a) outline, coral (#e07b4f) accents.
1. EMOTIONS — heart with gentle EKG wave line through it
2. RELATIONSHIPS — two overlapping circles forming a vesica piscis
3. STRESS — tangled line that straightens out (left messy → right smooth)
4. PERSONAL GROWTH — seedling growing from an open book
Clean, no shadows. Warm and approachable, not clinical.
```

#### Emotion Wheel (grafika bazowa)

```prompt
Create a circular emotion wheel diagram (800x800px) with 8 basic emotions arranged in a circle.
Style: Clean, modern infographic. Pastel/muted tones.
Segments: Joy (golden), Sadness (blue), Anger (red-coral), Fear (purple), 
Surprise (orange), Disgust (green), Trust (teal), Anticipation (amber).
Each segment labeled in Polish: Radość, Smutek, Złość, Lęk, Zaskoczenie, Wstręt, Zaufanie, Oczekiwanie.
Center: brain icon. Outer ring: lighter shade of each color.
White background. Modern, Plutchik-inspired but simplified.
```

### DESIGN — PROMPTY DO CLAUDE (Artifacts / Cowork)

#### Interaktywne Koło Emocji — React

```prompt
Stwórz interaktywne koło emocji jako komponent React.
8 segmentów: Radość, Smutek, Złość, Lęk, Zaskoczenie, Wstręt, Zaufanie, Oczekiwanie.
Każdy segment to klikalny SVG arc w odpowiednim kolorze (pastelowe, ciepłe).
Po kliknięciu segmentu:
- Segment się powiększa (animacja)
- Pod kołem pojawia się opis emocji (2-3 zdania)
- Lista 3 artykułów powiązanych z tą emocją (linki placeholder)
- CTA: "Chcesz lepiej rozumieć swoje emocje? → nurio.pl"
Kolorystyka bazowa: #2c6e8a (teal), #e07b4f (coral), #7b68ee (trust).
Responsywny — na mobile koło zmniejsza się, opisy pod spodem.
Smooth animations (CSS transitions). Po polsku.
```

#### Mini-quiz "Styl radzenia sobie" — React

```prompt
Stwórz mini-quiz "Jaki jest Twój styl radzenia sobie ze stresem?" jako komponent React.
8 pytań, każde z 4 opcjami odpowiedzi (A/B/C/D) odpowiadającymi stylom:
- A: Problemowy (task-focused coping)
- B: Emocjonalny (emotion-focused coping)
- C: Unikowy (avoidant coping)
- D: Społeczny (social support seeking)
Interface:
- Postęp: 1/8, 2/8... z progress barem
- Każde pytanie to sytuacja + 4 reakcje
- Na końcu: wynik główny styl + rozkład % na pie chart
- Interpretacja stylu (3-4 zdania)
- "Twój dominujący styl to... To oznacza, że..."
- CTA: "Pogłębiony test osobowości → psychozdrowie.online" + "Wsparcie w radzeniu sobie → nurio.pl"
Kolorystyka: primary #2c6e8a, accent #e07b4f, trust #7b68ee.
Animacje przejść. Responsywny. Po polsku.
```

---

## SATELITA 2: psychosen.pl

### IDENTYFIKACJA

| Element | Wartość |
|---------|---------|
| **Domena** | psychosen.pl |
| **Rola** | Niszowy ekspert — nauka o śnie, higiena snu, zaburzenia snu |
| **Intencja SEO** | "jak zasnąć", "bezsenność co robić", "higiena snu", "chronotyp", "zaburzenia snu" |
| **Emocja docelowa** | Frustracja (nie mogę spać) → zrozumienie → ulga → nawyk |
| **CTA główne** | → psychozdrowie.online/test-snu (primary) / nurio.pl (secondary) |

### KOLORYSTYKA

| Rola | Kolor | Hex | Użycie |
|------|-------|-----|--------|
| Primary | Nocny indygo | `#2d3a7c` | Nagłówki, nawigacja — nocne niebo, sen, głębia |
| Primary dark | Granat nocny | `#1e2854` | Footer, hover, dark sections |
| Primary light | Niebiesko-lawendowy | `#6a7bc4` | Tła sekcji, karty |
| Accent | Księżycowy złoty | `#d4a843` | CTA, wyróżnienia, "Noc" badge, melatonina |
| Accent dark | Ciepły bursztyn | `#b58b36` | Hover na CTA |
| Trust | Spokojny błękit | `#6b9fd4` | Linki, cytaty badań, barometry snu |

**Psychologia kolorów**: Indygo = noc, sen, spokój, głębia. Złoty/księżycowy = ciepło nocne, melatonina, gwiazdki — podświadome skojarzenie z "dobrą nocą". Błękit = spokój, wyciszenie. Paleta celowo CIEMNA — użytkownik przeglądający stronę wieczorem nie jest oślepiany.

### TYPY NEWSÓW / ARTYKUŁÓW

| Typ | Częstotliwość | Cel psychologiczny | Przykładowy tytuł |
|-----|---------------|--------------------|--------------------|
| **Rytuał wieczorny** | 2/mies. | Implementation intention — konkretny plan na wieczór | "7-dniowy rytuał wieczorny, który zmieni Twój sen [plan krok po kroku]" |
| **"Dlaczego nie śpię?"** | 2/mies. | Naming — nazwa problemu = kontrola nad nim | "5 powodów, dla których budzisz się o 3 w nocy" |
| **Chronotyp / nauka** | 1/mies. | Curiosity + self-discovery — "jaki jestem?" | "Sowa czy skowronek? Twój chronotyp decyduje o produktywności" |
| **Zaburzenia snu** | 1/mies. | Fear-then-relief — "to może być poważne, ale jest rozwiązanie" | "Bezdech senny: niewidoczny problem, który niszczy Twoje zdrowie" |
| **Sen a zdrowie psychiczne** | 2/mies. | Cross-selling wewnętrzny (linki do psychodzisiaj.pl) | "Dlaczego bezsenność i depresja chodzą parami" |
| **Gadżety / środowisko snu** | 1/mies. | Practical value | "Temperatura, światło, dźwięk: 3 zmienne, które kontrolują Twój sen" |

### TECHNIKI PERSWAZJI NA STRONIE

1. **Dark mode default** — strona domyślnie w ciemnym motywie (nocnym). Użytkownik czytający wieczorem = natychmiastowe dopasowanie kontekstu.
2. **"Ile teraz powinieneś spać?" widget** — podaj swój wiek → ile godzin snu rekomenduje nauka. Personalizacja.
3. **Sleep score mini-test** — 5 pytań na hero → wynik jakości snu 1-10 → "Zrób pełny test → psychozdrowie.online".
4. **Countdown do snu** — na stronie wyświetla się: "Do zalecanej pory snu zostało: X godzin" (na podstawie czasu użytkownika). Urgency + personalizacja.
5. **"Przeczytaj przed snem" sekcja** — artykuły oznaczone jako "spokojne", formatowane do czytania wieczorem (dark, duża czcionka, mało bodźców wizualnych).
6. **Blue light warning** — delikatny banner: "Pamiętaj, że ekran emituje niebieskie światło. Po przeczytaniu — odłóż telefon."

### SCHEMAT INFORMACYJNY

```
STRONA GŁÓWNA
├── Hero: "Jak spałeś dzisiejszej nocy?" + Sleep Score mini-test (5 pytań)
├── 4 filary (Higiena snu, Zaburzenia, Chronobiologia, Sen a zdrowie psychiczne)
├── "Przeczytaj przed snem" — 3 spokojne artykuły
├── "Twój chronotyp" — quiz teaser (1 pytanie + "kontynuuj")
└── Newsletter: "Cotygodniowy przegląd badań o śnie"

ARTYKUŁY (3 kategorie):
├── Higiena snu → rytuały, środowisko, nawyki
├── Zaburzenia → bezsenność, bezdech, parasomnie
└── Badania → chronobiologia, neurobiologia snu, melatonina

KAŻDY ARTYKUŁ:
├── Breadcrumb
├── H1 + excerpt
├── TOC
├── Treść (min. 1500 słów)
├── "Badanie" sidebar (cytowanie)
├── CTA psychozdrowie.online (end: test snu) + nurio.pl (sidebar: wsparcie)
├── Related articles (3)
└── Newsletter inline
```

### GRAFIKI — PROMPTY DO CHATGPT

#### OG Image (1200×630)

```prompt
Create a professional OG image (1200x630px) for "PsychoSen.pl" — a sleep science website.
Style: Calming, nocturnal, elegant. Soft gradients.
Colors: Deep indigo (#2d3a7c) background, golden moon accent (#d4a843), soft blue (#6b9fd4) highlights.
Elements: Crescent moon with subtle brain outline inside it, soft stars/dots, 
gentle wave pattern suggesting sleep cycles.
Text "Psycho Sen" in white serif font, subtitle "Nauka o zdrowym śnie".
Feeling: Peaceful, scientific, night-time. Like a calm night sky.
No stock photos. Modern editorial illustration.
```

#### Hero background (Dark mode)

```prompt
Create a wide dark hero image (1920x800px) for a sleep science website.
Style: Nocturnal, abstract, calming.
Colors: Deep indigo (#2d3a7c) gradients, subtle golden (#d4a843) star dots, 
dark navy (#1e2854) shadows.
Elements: Abstract sleep wave patterns (like EEG sine waves), 
very faint constellation-like connections, soft circular moon glow in upper area.
Very dark overall — this is for a dark-mode website. White text will overlay.
No people, no text. Atmospheric night sky feel.
```

#### Ikony filarów (4 sztuki)

```prompt
Create 4 flat icons (256x256px each) for a sleep science website.
Style: Minimal, calming. Light lines on dark background (#2d3a7c).
Colors: Golden (#d4a843) line art on indigo (#2d3a7c) circles.
1. SLEEP HYGIENE — pillow with moon and checkmark
2. SLEEP DISORDERS — EEG wave with warning marker
3. CHRONOBIOLOGY — clock face with sun and moon halves
4. SLEEP & MIND — brain with ZZZ coming from it
Clean, minimal, monoline. Rounded style.
```

### DESIGN — PROMPTY DO CLAUDE

#### Sleep Score Quiz — React

```prompt
Stwórz mini-quiz "Jak oceniasz swój sen?" jako komponent React z dark mode.
6 pytań o jakość snu (czas zasypiania, budzenie się, senność dzienna, rytuał wieczorny, ekrany, regularność).
Każde pytanie: skala 1-5 (od "bardzo źle" do "doskonale") z emoji.
Kolorystyka: tło #1e2854, tekst biały, akcent #d4a843, trust #6b9fd4.
Na końcu: Sleep Score 1-10 z kolorowym gauge:
- 1-3: czerwony — "Twój sen wymaga uwagi" 
- 4-6: złoty — "Jest pole do poprawy"
- 7-10: niebieski — "Śpisz dobrze!"
Pod wynikiem: 3 spersonalizowane wskazówki na podstawie odpowiedzi.
CTA: "Profesjonalny test snu → psychozdrowie.online" + "Wsparcie wieczornych rytuałów → nurio.pl"
Animacje: płynne przejścia, efekt "fade in" jak zasypianie.
Responsywny. Po polsku.
```

#### Kalkulator godzin snu — React

```prompt
Stwórz kalkulator "Kiedy powinienem iść spać?" jako komponent React.
Dane wejściowe:
- O której musisz wstać (time picker)
- Twój wiek (dropdown: dziecko / nastolatek / dorosły / senior)
Algorytm: oblicz cykle snu (90 min każdy), dodaj 15 min na zaśnięcie.
Wynik: 3 sugerowane pory pójścia spać (4/5/6 cykli).
Wizualizacja: oś czasu nocy z zaznaczonymi cyklami snu (NREM → REM → NREM...).
Kolorystyka: tło ciemne #1e2854, cykle w gradiencie indygo-niebieski, 
REM fazy podświetlone złotym #d4a843.
Responsywny, po polsku. Dark mode native.
```

---

## SATELITA 3: jaksobieradzic.pl

### IDENTYFIKACJA

| Element | Wartość |
|---------|---------|
| **Domena** | jaksobieradzic.pl |
| **Rola** | Pomost kryzysowy — strategie radzenia sobie w trudnych sytuacjach |
| **Intencja SEO** | "jak sobie radzić ze stresem", "jak poradzić sobie z", "techniki relaksacji", "pomoc w kryzysie" |
| **Emocja docelowa** | Ból / bezradność → "ktoś rozumie" → "jest wyjście" → konkretne kroki |
| **CTA główne** | → nurio.pl (primary — wsparcie codzienne) / psychozdrowie.online (secondary — diagnostyka) |

### KOLORYSTYKA

| Rola | Kolor | Hex | Użycie |
|------|-------|-----|--------|
| Primary | Szmaragdowy teal | `#2a7f62` | Nagłówki — resilience, wzrost, nadzieja |
| Primary dark | Głęboki szmaragd | `#1d5c46` | Footer, hover |
| Primary light | Miętowy | `#6bbf9e` | Tła kart, sekcje |
| Accent | Ciepły pomarańcz | `#e08c4f` | CTA, wyróżnienia, "Pierwsza pomoc" badge |
| Accent dark | Miedziany | `#c0703a` | Hover na CTA |
| Trust | Spokojny fiolet | `#8b7bb8` | Cytaty, źródła, "Eksperci mówią" |
| Emergency | Ciepły czerwony | `#d35f5f` | Baner kryzysowy, telefon zaufania |

**Psychologia kolorów**: Szmaragdowy = regeneracja, wzrost, nadzieja (kolor roślin odradzających się). Pomarańczowy = ciepło, energia do działania, wsparcie. Fiolet = empatia, głębia. Czerwony wyłącznie dla sytuacji kryzysowych (telefon zaufania). NIE dominuje na stronie — ma być ostatnią deską ratunku, nie straszakiem.

### TYPY NEWSÓW / ARTYKUŁÓW

| Typ | Częstotliwość | Cel psychologiczny | Przykładowy tytuł |
|-----|---------------|--------------------|--------------------|
| **"Krok po kroku"** | 3/mies. | Self-efficacy — "mogę to zrobić" | "Atak paniki: 5 kroków, które zatrzymają go w 2 minuty" |
| **"Przetrwałem/am"** | 1/mies. | Narrative transportation + social proof | "Jak przetrwałam rozwód z narcyzem — i czego nauczyła mnie terapia" |
| **Technika terapeutyczna** | 2/mies. | Practical value — narzędzia do ręki | "Technika RAIN: 4 kroki mindfulness na trudne emocje" |
| **"Kiedy szukać pomocy"** | 1/mies. | Permission giving — "to OK prosić o pomoc" | "7 sygnałów, że potrzebujesz psychologa — i dlaczego to odwaga" |
| **Kryzys życiowy** | 1/mies. | Normalizacja — "nie jesteś sam/sama" | "Żałoba po rozstaniu: dlaczego boli jak śmierć i co z tym zrobić" |
| **Psychoedukacja** | 2/mies. | Naming + demystification | "Co to jest dysregulacja emocji — i dlaczego wybuchasz 'bez powodu'" |

### TECHNIKI PERSWAZJI NA STRONIE

1. **"Teraz czuję..." selektor** — na hero: 6 przycisków z emocjami (Lęk, Złość, Smutek, Bezradność, Samotność, Przytłoczenie) → kliknięcie = artykuły dopasowane. Natychmiastowa personalizacja.
2. **Warm language** — cała strona w tonie terapeuty: "To, co czujesz, jest normalne. Oto, co możesz zrobić." Zerowa patologizacja.
3. **"Pierwsza pomoc psychologiczna" — sticky panel** — na dole każdej strony: Telefon Zaufania 116 123, przycisk "Porozmawiaj z kimś". Odpowiedzialność + zaufanie.
4. **Progress tracking** — po przeczytaniu artykułu: "Zrobione. To był pierwszy krok. Oto następny →" (link do kolejnego artykułu w ścieżce).
5. **Gentle CTA** — zamiast "KUP TERAZ": "Kiedy będziesz gotowy/a, Nurio może pomóc Ci w codziennym radzeniu sobie." Zero presji.
6. **"Ścieżki" — guided journeys** — 3-5 artykułów w sekwencji tematycznej: "Ścieżka radzenia sobie z lękiem (1/5)". Commitment & consistency.

### SCHEMAT INFORMACYJNY

```
STRONA GŁÓWNA
├── Hero: "Teraz czuję..." — 6 przycisków emocji → filtrowane artykuły
├── 4 filary (Stres, Lęk, Kryzysy, Wsparcie)
├── "Ścieżki" — 3 guided journeys (Lęk, Rozwód, Wypalenie)
├── Najnowsze artykuły (3 karty)
├── "Pierwsza pomoc" — stały panel z kontaktami kryzysowymi
└── Newsletter: "Cotygodniowy przegląd strategii radzenia sobie"

ARTYKUŁY (3 kategorie):
├── Radzenie sobie → techniki, kroki, strategie
├── Techniki → CBT, DBT, mindfulness, grounding
└── Wsparcie → kiedy szukać pomocy, gdzie, jak

KAŻDY ARTYKUŁ:
├── Breadcrumb
├── H1 + "Jeśli to czujesz — ten artykuł jest dla Ciebie"
├── TOC
├── Treść (min. 1500 słów, ciepły ton)
├── "Co mówią badania" sidebar
├── Gentle CTA nurio.pl (end) + psychozdrowie.online (sidebar)
├── "Następny krok w ścieżce" (jeśli jest w journey)
├── Related articles (3)
└── "Pierwsza pomoc" panel (footer stały)
```

### GRAFIKI — PROMPTY DO CHATGPT

#### OG Image (1200×630)

```prompt
Create a warm, empathetic OG image (1200x630px) for "JakSobieRadzić.pl" — a mental health coping strategies website.
Style: Warm, hopeful, supportive. Organic shapes, soft edges.
Colors: Emerald teal (#2a7f62) as base, warm orange (#e08c4f) accent, soft ivory background.
Elements: An abstract path/road going from tangled/dark on left to open/bright on right,
gentle human silhouette walking the path, small sprouts/growth along the path.
Text "Jak Sobie Radzić" in warm serif font, subtitle "Strategie na trudne chwile".
Feeling: "Jest wyjście. Nie jesteś sam/sama." Hopeful, never clinical.
```

#### Ikony emocji (6 sztuk)

```prompt
Create 6 emotion icons (256x256px each) for a mental health website.
Style: Soft, rounded, warm watercolor-digital hybrid. Each on white/transparent background.
Colors: Each in a muted, warm version of its emotion color.
1. ANXIETY — gentle tangled circle in lavender (#8b7bb8)
2. ANGER — soft flame shape in warm coral (#e08c4f)
3. SADNESS — gentle raindrop in soft blue (#6b9fd4)
4. HELPLESSNESS — open hands reaching up in muted teal (#6bbf9e)
5. LONELINESS — single figure in a soft circle, warm gray
6. OVERWHELM — overlapping gentle waves in mixed pastels
Feeling: empathetic, non-threatening. Would feel safe on a therapy office wall.
```

### DESIGN — PROMPTY DO CLAUDE

#### "Teraz czuję..." Emotion Router — React

```prompt
Stwórz komponent "Teraz czuję..." jako React.
6 przycisków-kart z emocjami: Lęk, Złość, Smutek, Bezradność, Samotność, Przytłoczenie.
Każdy przycisk: ikona emoji + nazwa + krótki opis (1 zdanie walidujące: "To normalne, że...").
Po kliknięciu:
- Karta się rozszerza (animacja)
- Pojawia się: "Kiedy czujesz [emocja], spróbuj:" — 3 szybkie techniki (1 zdanie każda)
- Lista 3 artykułów z tej kategorii (linki placeholder)
- CTA: "Chcesz codziennego wsparcia? → nurio.pl" (delikatny, nie agresywny)
Kolorystyka: #2a7f62 primary, #e08c4f akcent, #8b7bb8 fiolet dla introspekcji.
Ton: ciepły, walidujący, zero patologizacji.
Responsywny. Po polsku.
```

#### Ścieżka radzenia sobie — Step Tracker

```prompt
Stwórz komponent "Ścieżka radzenia sobie z lękiem" jako React.
5 kroków/etapów wyświetlonych jako ścieżka (timeline/stepper):
1. Zrozum swój lęk (psychoedukacja)
2. Naucz się oddychać (techniki oddechowe)
3. Kwestionuj myśli (restrukturyzacja poznawcza)
4. Ekspozycja (stopniowe konfrontowanie)
5. Buduj nawyki (codzienna praktyka)
Każdy krok: ikona + tytuł + krótki opis + link do artykułu.
Wizualnie: ścieżka z checkpointami. Ukończone kroki = zielone (#2a7f62), 
bieżący = pomarańczowy (#e08c4f), przyszłe = szare.
Na dole: "Ukończono 2/5 kroków. Następny: Kwestionuj myśli →"
Kolorystyka: #2a7f62, #e08c4f, #8b7bb8.
Responsywny. Po polsku. Animacja postępu.
```

---

## SATELITA 4: sprawdzwypalenie.pl

### IDENTYFIKACJA

| Element | Wartość |
|---------|---------|
| **Domena** | sprawdzwypalenie.pl |
| **Rola** | Niszowy ekspert — wypalenie zawodowe, diagnoza, profilaktyka |
| **Intencja SEO** | "wypalenie zawodowe test", "objawy wypalenia", "burnout", "jak zapobiec wypaleniu" |
| **Emocja docelowa** | Wyczerpanie → "czy to wypalenie?" → diagnoza → "mogę coś z tym zrobić" |
| **CTA główne** | → psychozdrowie.online/test-wypalenia (primary) / nurio.pl (secondary) |

### KOLORYSTYKA

| Rola | Kolor | Hex | Użycie |
|------|-------|-----|--------|
| Primary | Ciepły umber | `#7c5b3c` | Nagłówki — ziemia, wypalony, ale ciepły |
| Primary dark | Głęboki brąz | `#5a4129` | Footer, hover |
| Primary light | Piaskowy | `#c4a882` | Tła sekcji, karty |
| Accent | Amber energetyczny | `#e8922d` | CTA, wyróżnienia, "Test" badge, energia |
| Accent dark | Ciemny amber | `#c07824` | Hover na CTA |
| Trust | Spokojny oliwkowy | `#7a9a6d` | Regeneracja, "powrót do równowagi", badania |
| Warning | Tlący pomarańcz | `#d47b3e` | Fazy wypalenia, skala Maslach |

**Psychologia kolorów**: Umber/brązowy = "wypalona ziemia" — metafora wypalenia, ale ciepła (nie ponura). Amber = energia, iskra, "jeszcze się tlisz". Oliwkowy = regeneracja, powrót do natury/równowagi. Paleta celowo przechodzi od ciepłych brązów (wypalenie) do zieleni (regeneracja) — wizualna narracja "od wypalenia do odnowy".

### TYPY NEWSÓW / ARTYKUŁÓW

| Typ | Częstotliwość | Cel psychologiczny | Przykładowy tytuł |
|-----|---------------|--------------------|--------------------|
| **Test / autodiagnoza** | 1 główny + warianty | Commitment → wynik → chęć zmiany | "Test Maslach: Sprawdź poziom wypalenia zawodowego [12 pytań]" |
| **"Czy to wypalenie?"** | 2/mies. | Naming — identyfikacja = pierwszy krok | "Zmęczenie czy wypalenie? 8 różnic, które musisz znać" |
| **Profilaktyka** | 2/mies. | Prevention focus — zapobiegaj zanim będzie za późno | "5 nawyków, które chronią przed wypaleniem — codziennie" |
| **Case study / historia** | 1/mies. | Narrative transportation — "to mógłbym być ja" | "Menedżerka IT, 35 lat: 'Myślałam, że jestem leniwa. To było wypalenie'" |
| **Regeneracja** | 2/mies. | Hope + practical steps | "Powrót po wypaleniu: plan 90 dni krok po kroku" |
| **Pracodawca / HR** | 1/mies. | B2B angle — pracodawcy też szukają | "Wypalenie w zespole: 5 sygnałów, które lider musi znać" |

### TECHNIKI PERSWAZJI NA STRONIE

1. **"Burnout Meter" na hero** — wizualny termometr/gauge: "Gdzie jesteś teraz?" z 5 strefami (Energiczny → Zmęczony → Wyczerpany → Cyniczny → Wypalony). Użytkownik klika swoją strefę → dopasowane artykuły.
2. **Fazy wypalenia — timeline** — infografika: 5 faz wypalenia (honeymoon → stagnation → frustration → apathy → burnout) z opisem objawów. Użytkownik identyfikuje swoją fazę.
3. **"Dziennik energii" download** — PDF do pobrania: 7-dniowy dziennik poziomu energii → email capture → nurturing.
4. **Before/After sekcja** — "Przed: budzisz się zmęczony, nie chce Ci się... Po: wstajesz z energią, praca ma sens." Wizualizacja zmiany.
5. **Statystyki szokujące** — "W Polsce 60% pracowników doświadcza objawów wypalenia (CIOP, 2025)." Social proof + urgency.
6. **"Nie dla szefa" disclaimer** — "Ten artykuł jest dla Ciebie, nie dla Twojego pracodawcy. Twoje odpowiedzi są anonimowe." → buduje zaufanie przy testach.

### SCHEMAT INFORMACYJNY

```
STRONA GŁÓWNA
├── Hero: "Burnout Meter" — kliknij swoją strefę
├── 4 filary (Diagnoza, Profilaktyka, Regeneracja, Work-life balance)
├── "Fazy wypalenia" — interaktywna timeline
├── Test teaser: "Odpowiedz na 3 pytania → Twój wynik"
├── Najnowsze artykuły (3 karty)
└── Newsletter: "Cotygodniowy przegląd profilaktyki wypalenia"

ARTYKUŁY (3 kategorie):
├── Wypalenie → diagnoza, objawy, fazy, testy
├── Profilaktyka → granice, nawyki, zarządzanie energią
└── Regeneracja → powrót, terapia, zmiana

KAŻDY ARTYKUŁ:
├── Breadcrumb
├── H1 + excerpt
├── TOC
├── Treść (min. 1500 słów)
├── "Badania" sidebar
├── CTA psychozdrowie.online (end: test wypalenia) + nurio.pl (sidebar)
├── Related articles (3)
└── Newsletter inline
```

### GRAFIKI — PROMPTY DO CHATGPT

#### OG Image (1200×630)

```prompt
Create a professional OG image (1200x630px) for "SprawdźWypalenie.pl" — a burnout awareness website.
Style: Warm, honest, supportive. Not depressing — hopeful.
Colors: Warm umber (#7c5b3c) base, amber (#e8922d) energy accent, olive green (#7a9a6d) hope.
Elements: A match metaphor — left side: burnt match (brown/gray), 
right side: fresh match with warm flame (amber). 
Subtle transition from dark to bright.
Text "Sprawdź Wypalenie" in clean font, subtitle "Rozpoznaj. Zapobiegaj. Odnawiaj się."
Feeling: "Wypalenie nie musi być końcem." Honest but hopeful.
```

#### Burnout Phases Timeline

```prompt
Create an infographic timeline (1200x600px) showing 5 phases of burnout.
Style: Clean, horizontal flow, left to right progression.
Colors: Phase gradient from green (#7a9a6d) through amber (#e8922d) to deep brown (#5a4129).
Phases (left to right):
1. "Miesiąc miodowy" (green) — star icon, high energy
2. "Stagnacja" (yellow-green) — flat line icon
3. "Frustracja" (amber) — tangled line icon
4. "Apatia" (brown) — drooping line icon
5. "Wypalenie" (dark brown) — burnt match icon
Each phase: icon + Polish label + 2-word descriptor.
Arrow connecting phases. Clean, professional. White background.
```

### DESIGN — PROMPTY DO CLAUDE

#### Burnout Meter Quiz — React

```prompt
Stwórz "Burnout Meter" jako komponent React.
10 pytań opartych na Maslach Burnout Inventory (wyczerpanie, cynizm, skuteczność).
Każde pytanie: skala 1-5 (Nigdy → Zawsze) z emotikon.
Progress bar na górze.
Na końcu: gauge/termometr z 5 strefami:
- Zielona (#7a9a6d): "Energiczny — profilaktyka to klucz"
- Żółto-zielona: "Zmęczony — zacznij dbać o granice"
- Amber (#e8922d): "Wyczerpany — czas na zmiany"
- Pomarańczowa (#d47b3e): "Cyniczny — potrzebujesz wsparcia"
- Brązowa (#7c5b3c): "Wypalony — szukaj pomocy"
Pod wynikiem: 3 personalizowane rekomendacje.
CTA: "Profesjonalny test wypalenia → psychozdrowie.online" + "Codzienne wsparcie → nurio.pl"
Kolorystyka: #7c5b3c primary, #e8922d accent.
Responsywny. Po polsku. Anonimowy — "Twoje odpowiedzi nie są nigdzie zapisywane."
```

#### Energy Tracker — React

```prompt
Stwórz "Dziennik Energii" jako komponent React — 7-dniowy tracker.
Dla każdego dnia: slider 1-10 z etykietami (Wyczerpany → Pełen energii).
Wizualizacja: wykres liniowy pokazujący trend 7 dni.
Pod wykresem: automatyczna analiza:
- Średni poziom energii
- Trend (rosnący/spadający/stabilny)
- "Twoje najtrudniejsze dni to: [poniedziałek, środa]"
- Jeśli średnia < 4: "Twój poziom energii jest niepokojąco niski. Rozważ test wypalenia."
CTA: "Zrób pełny test → psychozdrowie.online"
Kolorystyka: #7c5b3c, #e8922d, #7a9a6d.
Responsywny. Po polsku. Dane w pamięci — nic nie jest wysyłane.
```

---

## SATELITA 5: testpredyspozycje.pl

### IDENTYFIKACJA

| Element | Wartość |
|---------|---------|
| **Domena** | testpredyspozycje.pl |
| **Rola** | Brama testowa — testy osobowości, predyspozycje, diagnostyka |
| **Intencja SEO** | "test osobowości", "jaki mam typ osobowości", "test predyspozycji zawodowych", "MBTI test" |
| **Emocja docelowa** | Ciekawość → "kim jestem?" → fascynacja wynikiem → chęć pogłębienia |
| **CTA główne** | → psychozdrowie.online (primary — pełne testy) / nurio.pl (secondary) |

### KOLORYSTYKA

| Rola | Kolor | Hex | Użycie |
|------|-------|-----|--------|
| Primary | Królewski fiolet | `#6b5b95` | Nagłówki — introspekcja, głębia, analiza |
| Primary dark | Ciemny fiolet | `#4e4270` | Footer, hover |
| Primary light | Lawendowy | `#9b8ec4` | Tła sekcji, karty |
| Accent | Turkusowy | `#3cb4a0` | CTA, wyróżnienia, "Zrób test" badge, odkrywanie |
| Accent dark | Ciemny turkus | `#2d8f7d` | Hover na CTA |
| Trust | Złoty ciepły | `#d4a843` | Wyniki testów, osiągnięcia, "Twój profil" |
| Neutral | Szary ciepły | `#6b7b8d` | Skale, wykresy, dane |

**Psychologia kolorów**: Fiolet = introspekcja, tajemnica, "odkrywanie siebie" (kojarzony z psychologią Junga, duchowością, głębią). Turkus = odkrywanie, otwartość, "nowa wiedza o sobie". Złoty = wartość wyniku ("to jest Twój unikalny profil"). Paleta zaprasza do samoeksploracji.

### TYPY NEWSÓW / ARTYKUŁÓW

| Typ | Częstotliwość | Cel psychologiczny | Przykładowy tytuł |
|-----|---------------|--------------------|--------------------|
| **Mini-test** | 2/mies. | Commitment → curiosity gap → wynik | "Test: Jaki jest Twój typ osobowości? [5 minut]" |
| **Explainer modelu** | 2/mies. | Authority — "to nie buzzfeed, to nauka" | "Big Five vs MBTI: który test osobowości jest bardziej naukowy?" |
| **"Co mówi o Tobie..."** | 2/mies. | Self-reference + Barnum | "Co Twój styl pracy mówi o Twojej osobowości" |
| **Kariera + osobowość** | 1/mies. | Practical value — "który zawód do mnie pasuje?" | "Holland RIASEC: znajdź karierę dopasowaną do Twojej osobowości" |
| **Inteligencja** | 1/mies. | Curiosity + self-validation | "IQ, EQ, SQ: 3 rodzaje inteligencji — i dlaczego liczy się każdy" |
| **Mity o testach** | 1/mies. | Demystification + authority | "'Jestem INTJ' — dlaczego MBTI kłamie (i co lepszego oferuje nauka)" |

### TECHNIKI PERSWAZJI NA STRONIE

1. **"Poznaj siebie" hero quiz** — 1 pytanie na hero: "Gdy masz wolny wieczór, najchętniej: A) Czytasz B) Spotykasz się z ludźmi C) Planujesz projekt D) Eksperymentujesz z czymś nowym" → wynik → "Chcesz więcej? Zrób pełny test."
2. **Personality cards** — 16 kart MBTI / 5 wymiarów Big Five jako wizualne, klikalne karty. Engagement.
3. **Barnum effect** — celowo uniwersalne opisy ("Bywasz towarzyski, ale potrzebujesz czasu sam/sama") → "to tak trafne!" → chęć głębszego testu.
4. **Gamification** — "Odkryłeś 2 z 5 wymiarów swojej osobowości. Kontynuuj →" Progress tracking.
5. **Compare with friends** — "Podziel się wynikiem. Sprawdź, jaki typ ma Twój partner/przyjaciel." Viralność.
6. **"Naukowy vs pop" badge** — artykuły oznaczone: "Naukowy" (recenzowane narzędzie) vs "Pop" (rozrywkowy, niewalidowany). Buduje autorytet.

### SCHEMAT INFORMACYJNY

```
STRONA GŁÓWNA
├── Hero: "Poznaj siebie" — 1 pytanie quick quiz
├── 4 filary (Osobowość, Predyspozycje zawodowe, Inteligencja, Talenty)
├── "Popularne testy" — 4 karty z mini-testami
├── "Naukowy vs Pop" — porównanie podejść
├── Najnowsze artykuły (3 karty)
└── Newsletter: "Cotygodniowy przegląd psychometrii"

ARTYKUŁY (3 kategorie):
├── Testy → mini-testy, explainer narzędzi, walidacje
├── Kariera → predyspozycje, Holland, RIASEC
└── Rozwój → talenty, mocne strony, inteligencje

KAŻDY ARTYKUŁ:
├── Breadcrumb
├── H1 + "Poznaj siebie głębiej"
├── TOC
├── Treść (min. 1500 słów)
├── "Naukowy badge" sidebar (trafność, rzetelność narzędzia)
├── CTA psychozdrowie.online (end: pełny test) + nurio.pl (sidebar)
├── Related articles (3)
└── Newsletter inline
```

### GRAFIKI — PROMPTY DO CHATGPT

#### OG Image (1200×630)

```prompt
Create a professional OG image (1200x630px) for "TestPredyspozycje.pl" — a personality tests website.
Style: Intriguing, scientific, inviting. Clean modern design.
Colors: Royal purple (#6b5b95) background, turquoise (#3cb4a0) accents, golden (#d4a843) highlights.
Elements: Abstract human head silhouette filled with puzzle pieces in different colors,
one piece floating outward (representing self-discovery).
Text "Test Predyspozycje" in clean font, subtitle "Poznaj swoje mocne strony".
Feeling: "Kim jesteś naprawdę?" Intriguing, scientific, empowering.
```

#### Personality dimension cards (5 sztuk Big Five)

```prompt
Create 5 personality dimension cards (400x300px each) for the Big Five personality model.
Style: Clean, modern, gradient fills. Each card unique color.
1. OPENNESS — purple (#6b5b95), telescope icon, "Otwartość na doświadczenia"
2. CONSCIENTIOUSNESS — turquoise (#3cb4a0), checklist icon, "Sumienność"
3. EXTRAVERSION — golden (#d4a843), sun/people icon, "Ekstrawersja"
4. AGREEABLENESS — soft green (#7a9a6d), handshake icon, "Ugodowość"
5. NEUROTICISM — warm coral (#e08c4f), wave icon, "Neurotyczność"
Each card: icon + Polish name + English name below in smaller text + scale bar (low-high).
White text on colored background. Rounded corners (14px).
```

### DESIGN — PROMPTY DO CLAUDE

#### Big Five Quick Test — React

```prompt
Stwórz szybki test Big Five jako komponent React.
10 pytań (po 2 na wymiar), każde na skali 1-5 (Zdecydowanie nie → Zdecydowanie tak).
Wymiary: Otwartość, Sumienność, Ekstrawersja, Ugodowość, Neurotyczność.
Progress bar. Jedno pytanie na ekran z animacją przejścia.
Na końcu: radar/pentagon chart z 5 wymiarami.
Każdy wymiar: wartość 1-10 + krótki opis (2 zdania).
"Twój dominujący wymiar: [X] — oznacza to, że..."
Kolorystyka per wymiar:
- Otwartość: #6b5b95
- Sumienność: #3cb4a0
- Ekstrawersja: #d4a843
- Ugodowość: #7a9a6d
- Neurotyczność: #e08c4f
CTA: "Pełny test Big Five (60 pytań) → psychozdrowie.online" + "Rozwiń swoje mocne strony → nurio.pl"
Responsywny. Po polsku.
```

#### Career Match Explorer — React

```prompt
Stwórz "Jaka kariera do Ciebie pasuje?" jako komponent React.
6 typów Hollanda (RIASEC): Realistyczny, Badawczy, Artystyczny, Społeczny, Przedsiębiorczy, Konwencjonalny.
Krok 1: 12 par aktywności (forced choice) — wybierz A lub B.
Krok 2: Wynik — top 3 typy na bar chart.
Krok 3: Lista 5 sugerowanych zawodów dla Twojej kombinacji.
Wizualizacja: heksagonalny diagram RIASEC z zaznaczonym profilem użytkownika.
Kolorystyka: #6b5b95 primary, #3cb4a0 akcent, #d4a843 highlights.
CTA: "Pełna diagnostyka zawodowa → psychozdrowie.online"
Responsywny. Po polsku. Animacje smooth.
```

---

## SATELITA 6: zdrowie.fit

### IDENTYFIKACJA

| Element | Wartość |
|---------|---------|
| **Domena** | zdrowie.fit |
| **Rola** | Most między ciałem a psychiką — holistyczne zdrowie, najszerszy funnel |
| **Intencja SEO** | "zdrowy styl życia", "jak być zdrowym", "dieta a nastrój", "ćwiczenia na stres" |
| **Emocja docelowa** | "Chcę być zdrowszy" → zrozumienie połączeń ciało-umysł → nawyki |
| **CTA główne** | → nurio.pl (primary — wellbeing) / psychozdrowie.online (secondary — testy) |

### KOLORYSTYKA

| Rola | Kolor | Hex | Użycie |
|------|-------|-----|--------|
| Primary | Zdrowy zielony | `#4a7c59` | Nagłówki — natura, zdrowie, równowaga |
| Primary dark | Leśny | `#3a6347` | Footer, hover |
| Primary light | Miętowy jasny | `#7fb3a3` | Tła sekcji |
| Accent | Energetyczny coral | `#d9724a` | CTA, wyróżnienia, "Nowe!", aktywność |
| Accent dark | Ciemny coral | `#b85a38` | Hover |
| Trust | Niebieski spokojny | `#5b8def` | Badania, linki, cytaty naukowe |
| Nature | Złoto-oliwkowy | `#a8b53c` | Natura, outdoor, sekcja "Natura leczy" |

**Psychologia kolorów**: Zielony = zdrowie, natura, równowaga, wzrost (najbardziej "zdrowotny" kolor). Coral = energia, aktywność fizyczna, witalność. Niebieski = nauka, spokój, zaufanie. Oliwkowy = natura, outdoor, "wyjdź na dwór". Paleta jest NAJCIEPLEJSZA w klastrze — zdrowie to pozytywna aspiracja, nie strach.

### TYPY NEWSÓW / ARTYKUŁÓW

| Typ | Częstotliwość | Cel psychologiczny | Przykładowy tytuł |
|-----|---------------|--------------------|--------------------|
| **Ciało-umysł connection** | 3/mies. | Cross-reference — łączenie tematów | "Dlaczego 30 min spaceru działa jak lekki antydepresant [badanie]" |
| **Nawyk tygodnia** | 2/mies. | Implementation intention — 1 konkretna zmiana | "Nawyk tygodnia: 10 min rozciągania rano zmienia cały dzień" |
| **Dieta a nastrój** | 2/mies. | Practical + surprising | "Jelita to drugi mózg: 5 produktów, które poprawią nastrój" |
| **Trening + psychologia** | 1/mies. | Motivation — ćwiczenia = zdrowie psychiczne | "BDNF: białko, które ćwiczenia uwalniają w mózgu [i dlaczego to ważne]" |
| **Sen (cross-link)** | 1/mies. | Cross-selling → psychosen.pl | "Jak trening wpływa na jakość snu — i odwrotnie" |
| **Natura leczy** | 1/mies. | Novelty + biophilia | "Shinrin-yoku: japońska terapia lasem z potwierdzoną skutecznością" |

### TECHNIKI PERSWAZJI NA STRONIE

1. **"Wheel of Health" na hero** — koło zdrowia holistycznego: 6 segmentów (Ruch, Umysł, Dieta, Sen, Natura, Relacje). Kliknij → artykuły. Wizualizacja "wszystko się łączy".
2. **Daily challenge** — codzienne mikro-wyzwanie: "Dzisiejsze wyzwanie: 5 min świadomego oddychania po obiedzie." → buduje nawyk wracania na stronę.
3. **"Nauka mówi" badge** — każdy artykuł z cytowaniem: "Metaanaliza 47 badań (N=15,000) potwierdza..." Authority.
4. **Before/After wizualizacje** — "Osoba A: siedzący tryb życia, fast food, 5h snu → cortyzol, lęk, otyłość. Osoba B: ruch, dieta, 7h snu → energia, spokój, zdrowie."
5. **Cross-linking** — silne linkowanie do psychosen.pl (sen), psychodzisiaj.pl (emocje), sprawdzwypalenie.pl (stres). Zdrowie.fit = hub łączący.
6. **Seasonal content** — artykuły sezonowe: "Wiosenne zmęczenie: mit czy fakt?" — recency, relevance.

### SCHEMAT INFORMACYJNY

```
STRONA GŁÓWNA
├── Hero: "Wheel of Health" — 6-segmentowe koło + "Zacznij od jednego"
├── 6 filarów (Ruch, Umysł, Odżywianie, Sen, Natura, Relacje)
├── "Dzisiejsze wyzwanie" — daily micro-challenge
├── Najnowsze artykuły (3 karty)
├── "Nauka tygodnia" — wyróżnione badanie
└── Newsletter: "Cotygodniowy przegląd zdrowia"

ARTYKUŁY (3 kategorie):
├── Zdrowie fizyczne → ruch, trening, ergonomia
├── Zdrowie psychiczne → stres, nastrój, mindfulness
└── Dieta i odżywianie → mikrobiom, suplementy, posiłki

KAŻDY ARTYKUŁ:
├── Breadcrumb
├── H1 + excerpt
├── TOC
├── Treść (min. 1500 słów)
├── "Nauka mówi" sidebar
├── CTA nurio.pl (end) + psychozdrowie.online (sidebar)
├── Cross-linki do innych satelitów klastra
├── Related articles (3)
└── Newsletter inline
```

### GRAFIKI — PROMPTY DO CHATGPT

#### OG Image (1200×630)

```prompt
Create a vibrant OG image (1200x630px) for "Zdrowie.fit" — a holistic health website.
Style: Fresh, energetic, natural. Modern illustration.
Colors: Green (#4a7c59) base, coral (#d9724a) energy accent, blue (#5b8def) calm accent.
Elements: Abstract human figure in motion (running/stretching), surrounded by 
nature elements (leaves, water drops) and subtle brain/neuron connections.
Text "Zdrowie.fit" in clean font, subtitle "Ciało i umysł w harmonii".
Feeling: Energetic, positive, holistic. "Health is everything connected."
```

#### Wheel of Health (grafika)

```prompt
Create a circular "Wheel of Health" diagram (800x800px) with 6 equal segments.
Style: Modern infographic, clean, colorful but harmonious.
Segments (clockwise):
1. RUCH (green #4a7c59) — running shoe icon
2. UMYSŁ (blue #5b8def) — brain icon
3. ODŻYWIANIE (coral #d9724a) — bowl/spoon icon
4. SEN (indigo #2d3a7c) — moon icon
5. NATURA (olive #a8b53c) — leaf icon
6. RELACJE (purple #7b68ee) — two people icon
Center: heart with pulse line. Polish labels.
White background. Clean, modern, would work as hero element.
```

### DESIGN — PROMPTY DO CLAUDE

#### Wheel of Health Interactive — React

```prompt
Stwórz interaktywne "Koło Zdrowia" jako komponent React.
6 segmentów SVG: Ruch, Umysł, Odżywianie, Sen, Natura, Relacje.
Każdy segment: kolor + ikona emoji + nazwa.
Po kliknięciu segmentu:
- Segment podświetla się (animacja pulse)
- Obok koła pojawia się panel z: 
  - Krótki opis filaru (2 zdania)
  - "Szybka wskazówka" (1 actionable tip)
  - 3 artykuły z tej kategorii (linki placeholder)
  - Micro CTA: "Pogłęb temat → [link do odpowiedniego satelity]"
    np. Sen → psychosen.pl, Umysł → psychodzisiaj.pl
Kolory segmentów: Ruch=#4a7c59, Umysł=#5b8def, Odżywianie=#d9724a, 
Sen=#2d3a7c, Natura=#a8b53c, Relacje=#7b68ee.
Na mobile: koło nad panelem (stacking). Responsywny. Po polsku.
```

#### Daily Challenge Widget — React

```prompt
Stwórz "Wyzwanie Dnia" jako komponent React.
Wyświetla losowe mikro-wyzwanie zdrowotne z kategorią (ikona + kolor).
Przykłady:
- 🏃 Ruch: "Zrób 20 przysiadów po obiedzie"
- 🧠 Umysł: "5 min oddychania 4-7-8 przed snem"
- 🥗 Dieta: "Dodaj jedną garść orzechów do posiłku"
- 😴 Sen: "Odłóż telefon 30 min przed snem"
Funkcje:
- Przycisk "Zrobione ✓" (zmienia kolor na zielony, confetti animacja)
- Przycisk "Inne wyzwanie" (losuje nowe)
- Counter: "Ukończone wyzwania: X" (w pamięci sesji)
Kolorystyka: #4a7c59, #d9724a accent. Ciepły, motywujący ton.
Responsywny. Po polsku.
```

---

## SATELITA 7: psycho.edu.pl

### IDENTYFIKACJA

| Element | Wartość |
|---------|---------|
| **Domena** | psycho.edu.pl |
| **Rola** | Baza wiedzy — edukacja psychologiczna, suplement akademicki |
| **Intencja SEO** | "psychologia ogólna", "czym jest terapia CBT", "neuropsychologia", "zaburzenia psychiczne lista" |
| **Emocja docelowa** | Ciekawość akademicka → "to fascynujące" → pogłębienie → praktyczne zastosowanie |
| **CTA główne** | → nurio.pl (primary) / psychozdrowie.online (secondary) |

### KOLORYSTYKA

| Rola | Kolor | Hex | Użycie |
|------|-------|-----|--------|
| Primary | Akademicki granat | `#34568b` | Nagłówki — edukacja, uniwersytet, powaga |
| Primary dark | Ciemny granat | `#243d66` | Footer, hover |
| Primary light | Jasny niebieski | `#6b8cc4` | Tła sekcji, karty |
| Accent | Złoty akademicki | `#c49b3a` | CTA, wyróżnienia, "Nowy artykuł", osiągnięcia |
| Accent dark | Ciemne złoto | `#a37e2d` | Hover na CTA |
| Trust | Teal wiedzy | `#2c8e8a` | Cytaty, źródła, "Peer-reviewed" badge |
| Neutral | Ciepły szary | `#5d6d7e` | Opisy, meta, skale |

**Psychologia kolorów**: Granat akademicki = powaga, wiedza, instytucja (kolory uniwersytetów: Oxford, Harvard). Złoty = osiągnięcie, wartość edukacji, "złota wiedza". Teal = wiarygodność naukowa. Paleta jest NAJPOWAŻNIEJSZA w klastrze — tu nie gramy na emocjach, tu budujemy autorytet.

### TYPY NEWSÓW / ARTYKUŁÓW

| Typ | Częstotliwość | Cel psychologiczny | Przykładowy tytuł |
|-----|---------------|--------------------|--------------------|
| **Explainer** | 3/mies. | Authority — "tu się uczysz od eksperta" | "Terapia poznawczo-behawioralna (CBT): jak działa i dla kogo" |
| **Porównanie podejść** | 1/mies. | Decision support — "która terapia dla mnie?" | "CBT vs psychodynamika: 5 kluczowych różnic [i co wybrać]" |
| **Neuropsychologia** | 2/mies. | Fascination — "mózg jest niesamowity" | "Jak mózg przetwarza traumę — neurobiologia PTSD" |
| **Zaburzenia — demystification** | 1/mies. | Naming + destigmatization | "Zaburzenie osobowości borderline: co to naprawdę znaczy [i czym NIE jest]" |
| **Historia psychologii** | 1/mies. | Narrative — "skąd to się wzięło" | "Od Freuda do CBT: 120 lat psychoterapii w 10 minutach" |
| **Narzędzia diagnostyczne** | 1/mies. | Cross-selling → psychozdrowie.online | "MMPI-2: najbardziej badany test osobowości na świecie" |

### TECHNIKI PERSWAZJI NA STRONIE

1. **"Encyklopedia psychologii" nawigacja** — alfabetyczny indeks haseł. Użytkownik przegląda jak słownik. Engagement + SEO long-tail.
2. **"Peer-reviewed" badge** — artykuły z tagiem "Recenzowany naukowo" → autorytet. Wyróżnione wizualnie (teal badge z ikoną mikroskop).
3. **Difficulty level** — artykuły oznaczone: Podstawowy / Średniozaawansowany / Zaawansowany. Pozwala użytkownikowi dobrać poziom.
4. **"Czytaj dalej" ścieżki** — po artykule o CBT: "Następny krok: Jak wygląda sesja CBT?" → "Czy CBT działa na depresję?" → pipeline.
5. **Cytowanie w formacie APA** — przy każdym artykule: przycisk "Cytuj ten artykuł" → gotowy tekst w APA 7. Buduje prestiż + przydatność dla studentów.
6. **Infografiki naukowe** — każdy artykuł z co najmniej 1 infografiką (schemat, diagram, model). Sharing + SEO images.

### SCHEMAT INFORMACYJNY

```
STRONA GŁÓWNA
├── Hero: "Psychologia — wiedza dla każdego" + searchbar
├── 4 filary (Psychologia ogólna, Neuropsychologia, Psychopatologia, Metody terapii)
├── "Encyklopedia" — A-Z index (top 20 haseł)
├── Najnowsze artykuły (3 karty z difficulty badge)
├── "Popularne tematy" — tag cloud
└── Newsletter: "Cotygodniowy przegląd artykułów z psychologii"

ARTYKUŁY (3 kategorie):
├── Edukacja → podstawy, encyklopedia, history
├── Neuropsychologia → mózg, neuro, biologia
└── Terapia → CBT, psychodynamika, EMDR, schematy

KAŻDY ARTYKUŁ:
├── Breadcrumb
├── H1 + difficulty badge + reading time
├── TOC
├── Treść (min. 2000 słów — dłuższe niż inne satelity)
├── Infografika (min. 1 na artykuł)
├── "Źródła" — pełna bibliografia APA 7
├── "Cytuj ten artykuł" button
├── CTA nurio.pl (end, delikatny) + psychozdrowie.online (sidebar: testy)
├── "Czytaj dalej" pipeline (3 artykuły w kolejności)
└── Newsletter inline
```

### GRAFIKI — PROMPTY DO CHATGPT

#### OG Image (1200×630)

```prompt
Create a professional, academic OG image (1200x630px) for "Psycho.edu.pl" — a psychology education portal.
Style: Academic, prestigious, clean. Think university textbook cover.
Colors: Academic navy (#34568b) background, golden (#c49b3a) accents, white text.
Elements: Open book with subtle brain/neuron illustration emerging from pages,
graduation cap icon, subtle dotted connection lines (neural network feel).
Text "Psycho.edu.pl" in elegant serif font, subtitle "Edukacja psychologiczna".
Feeling: Prestigious, trustworthy, "here you learn from experts."
```

#### Terapie — porównanie (infografika)

```prompt
Create a comparison infographic (1200x800px) of 4 major therapy approaches.
Style: Academic, clean, tabular with icons.
Colors: Navy (#34568b) headers, golden (#c49b3a) highlights, teal (#2c8e8a) for data.
Four columns:
1. CBT — brain with gear icon — "Myśli → Zachowania"
2. Psychodynamic — iceberg icon — "Nieświadome procesy"
3. Humanistic — sun/person icon — "Samorealizacja"
4. Systemic — connected circles icon — "Relacje i systemy"
Rows: Założenia, Metody, Dla kogo, Czas trwania, Dowody naukowe.
Polish labels. Clean, would work in a textbook.
```

### DESIGN — PROMPTY DO CLAUDE

#### Psychology Encyclopedia Browser — React

```prompt
Stwórz przeglądarkę "Encyklopedia Psychologii" jako komponent React.
Litery A-Z na górze jako klikalne tabs.
Po kliknięciu litery: lista haseł zaczynających się na tę literę.
Hasła: 5-10 per litera (łącznie ~100), np.:
- A: Afekt, Agorafobia, Amnezja, Anoreksja, Attachment theory
- B: BDI, Big Five, Borderline, Burnout
- C: CBT, Chronotyp, Coping, Cortyzol
Każde hasło: nazwa + 1-zdaniowa definicja + link do artykułu (placeholder).
Searchbar na górze — filtruje hasła na żywo.
Kolorystyka: #34568b primary, #c49b3a accent, #2c8e8a trust.
Responsywny. Po polsku. Clean, academic feel.
```

#### Therapy Comparison Tool — React

```prompt
Stwórz narzędzie "Którą terapię wybrać?" jako komponent React.
5 pytań o problem użytkownika:
1. Główny problem (dropdown: lęk, depresja, relacje, trauma, osobowość, uzależnienie)
2. Preferencja stylu (dropdown: praktyczne ćwiczenia / rozmowa / praca z ciałem / kreatywne)
3. Czas (dropdown: krótkoterminowo / długoterminowo)
4. Cel (dropdown: usunąć objaw / zrozumieć przyczynę / oba)
5. Doświadczenie z terapią (tak/nie)
Na podstawie odpowiedzi: ranking 4 podejść (CBT, psychodynamika, humanistyczna, systemowa) 
z % dopasowania i krótkim uzasadnieniem.
Top rekomendacja wyróżniona złotym (#c49b3a) obramowaniem.
CTA: "Znajdź terapeutę → psychozdrowie.online"
Kolorystyka: #34568b, #c49b3a, #2c8e8a.
Responsywny. Po polsku. Profesjonalny, akademicki ton.
```

---

## WSPÓLNE ELEMENTY KLASTRA

### Spójność wizualna

Wszystkie 7 satelitów dzieli:
- **Font nagłówków**: Fraunces (serif) — buduje autorytet, ciepłe serify
- **Font body**: Inter (sans) — czytelność, neutralność
- **Radius**: 14px — zaokrąglone, ale profesjonalne
- **Shadow warmth**: warm — ciepłe cienie, nie korporacyjne
- **Newsletter sekcja**: ciemne tło, CTA w kolorze accent domeny
- **"Badania mówią" sidebar** — format wspólny: Autor (rok), N=, wynik. Kolor trust danej domeny.
- **Disclaimer**: "Treści mają charakter edukacyjny i nie zastępują profesjonalnej pomocy psychologicznej ani psychoterapii."

### Różnicowanie kolorystyczne — podsumowanie

| Satelita | Primary | Accent | Motyw |
|----------|---------|--------|-------|
| psychodzisiaj.pl | Morski teal `#2c6e8a` | Coral `#e07b4f` | Psychologia codzienna |
| psychosen.pl | Nocny indygo `#2d3a7c` | Księżycowy złoty `#d4a843` | Noc, sen |
| jaksobieradzic.pl | Szmaragdowy `#2a7f62` | Ciepły pomarańcz `#e08c4f` | Nadzieja, wzrost |
| sprawdzwypalenie.pl | Ciepły umber `#7c5b3c` | Amber `#e8922d` | Wypalenie → odnowa |
| testpredyspozycje.pl | Królewski fiolet `#6b5b95` | Turkusowy `#3cb4a0` | Introspekcja, odkrywanie |
| zdrowie.fit | Zdrowy zielony `#4a7c59` | Coral `#d9724a` | Natura, witalność |
| psycho.edu.pl | Akademicki granat `#34568b` | Złoty `#c49b3a` | Edukacja, prestiż |

### Cross-linking między satelitami

```
psychodzisiaj.pl → "Nie śpisz? Sprawdź dlaczego" (→ psychosen.pl)
                 → "Jaki masz styl radzenia sobie?" (→ jaksobieradzic.pl)
                 → "Poznaj swój typ osobowości" (→ testpredyspozycje.pl)

psychosen.pl → "Bezsenność a depresja — jak to się łączy" (→ psychodzisiaj.pl)
             → "Sen a wypalenie zawodowe" (→ sprawdzwypalenie.pl)
             → "Jak ruch poprawia sen" (→ zdrowie.fit)

jaksobieradzic.pl → "Sprawdź poziom wypalenia" (→ sprawdzwypalenie.pl)
                  → "Techniki oddechowe na lepszy sen" (→ psychosen.pl)
                  → "Ruch jako terapia stresu" (→ zdrowie.fit)

sprawdzwypalenie.pl → "Wypalenie a depresja — różnice" (→ psychodzisiaj.pl)
                    → "Jaki typ osobowości jest narażony na burnout?" (→ testpredyspozycje.pl)
                    → "Ćwiczenia, które regenerują po wypaleniu" (→ zdrowie.fit)

testpredyspozycje.pl → "Osobowość a styl radzenia sobie" (→ jaksobieradzic.pl)
                     → "Który chronotyp to Ty?" (→ psychosen.pl)
                     → "Czym jest neurotyczność?" (→ psycho.edu.pl)

zdrowie.fit → "Stres a kortyzol — co mówi nauka" (→ psycho.edu.pl)
            → "Ćwiczenia na lęk: co działa?" (→ jaksobieradzic.pl)
            → "Dieta a sen — co jeść wieczorem" (→ psychosen.pl)

psycho.edu.pl → "CBT w praktyce — jak sobie radzić" (→ jaksobieradzic.pl)
              → "Test Big Five — zrób szybki quiz" (→ testpredyspozycje.pl)
              → "Neurobiologia snu" (→ psychosen.pl)
```

### UTM Convention

Każdy link satelita → nurio.pl:
```
https://nurio.pl?utm_source=psychodzisiaj.pl&utm_medium=article&utm_campaign={article-slug}
```

Każdy link satelita → psychozdrowie.online:
```
https://psychozdrowie.online/test?utm_source=sprawdzwypalenie.pl&utm_medium=article&utm_campaign={article-slug}
```

---

## NASTĘPNE KROKI

1. ✅ Strategia klastra NIS2 (STRATEGIA_KLASTER_NIS2.md)
2. ✅ Strategia klastra Psychologia (ten dokument)
3. ⬜ Strategia klastra Mediacja + Reszta (twojamediacja.pl, audytzespolu.pl, analizastatystyczna.me, ragpolska.pl, wppage.pl, creativebrandpro.com, marekporycki.pl)
4. ⬜ Aktualizacja YAML domen — nowe kolory z tego dokumentu
5. ⬜ Generowanie grafik w ChatGPT per domena
6. ⬜ Generowanie komponentów w Claude per domena
7. ⬜ Build all + deploy na Cyberfolks
