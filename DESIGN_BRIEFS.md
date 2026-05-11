# Design Briefs — Archaios SSG (18 domen)

Briefy do wklejania w Claude Design / Canvas / dowolny generator obrazów. Każda domena ma komplet zasobów: **favicon (32×32, SVG + PNG), apple-touch-icon (180×180), logo poziome (SVG), og-default.png (1200×630)**.

## Globalne zasady (dla wszystkich domen)

**Pliki do dostarczenia per domena** (do wgrania w `output/<domain-slug>/static/img/`):
- `favicon.ico` — 32×32, fallback dla starych przeglądarek
- `favicon.svg` — wektor, monogram + kolor brand, działa w dark/light
- `favicon-16.png`, `favicon-32.png` — rastry
- `apple-touch-icon.png` — 180×180, pełne wypełnienie tłem brand, monogram biały, **bez przezroczystości** (iOS dodaje cień)
- `og-default.png` — 1200×630, fallback dla artykułów bez własnej OG (build.py i tak generuje OG per artykuł, ale ten jest dla strony głównej i kategorii)
- `logo.svg` — wersja pozioma (monogram + nazwa) do nagłówka

**Zasady projektowe (wspólne)**:

1. **Favicon = monogram, nie scena.** Maksymalna prostota — jedna litera/symbol, jeden kolor tła, kontrastujący znak. Czytelność w 16×16 to priorytet. Nigdy nie używaj cienkich linii, gradientów ani drobnych detali.
2. **Safe area na apple-touch-icon**: znak w środkowych 60% płótna (108×108 z 180), reszta to padding tłem.
3. **OG image (1200×630)**: lewy górny róg = monogram + nazwa domeny, środek = tagline (max 6 słów, font Fraunces 64–80px), dół = `nazwadomeny.pl` w mniejszym ścisłym tekście. Kolor tła = `primary`, akcent w jednym elemencie (linia, kropka, kropka nad i).
4. **Typografia**: Fraunces (display, nagłówki), Inter (body). W favicon/logo używaj Fraunces dla cyfr i nazw z charakterem, Inter dla bardziej technicznych domen.
5. **Brand-spójność wewnątrz brand-grupy**: domeny `archaios` używają tej samej tarczy 🛡 + paleta granat/czerwień; domeny `nurio` mają warianty mózg-symbol w odmiennych paletach; domeny `marek` mają personal-feel.
6. **Czego unikać**: stockowych ikonek (lupa, koło zębate), neonów, gradientów tęczowych, AI-generated mid-journey-looku z cieniami, emoji jako finalnego favicon (emoji to placeholder w `logo_mark` w YAML — finalny favicon to ZAWSZE wektor narysowany pod konkretną literą/symbol).
7. **Plik favicon.svg powinien działać w dark mode** — albo neutralne tło, albo użycie `prefers-color-scheme` w SVG `<style>`.

---

## BRAND GROUP: ARCHAIOS (cybersec / AI B2B) — 7 domen

**Wspólna paleta brand-grupy**:
- Primary: `#1a365d` (granat — autorytet, korporacja)
- Accent: `#c0392b` (czerwień — alarm, compliance)
- Trust: `#2980b9` (niebieski — technologia)
- Tło neutralne: `#fdfcf9` (ivory)

**Wspólny język wizualny**: tarcza, linie geometryczne, monospace dla kodu/tagów, brak organicznych kształtów. Estetyka: enterprise, serious, audytorska. Inspiracja: NATO STANAG, ENISA, ISO 27001 wizualizacje.

---

### 1. testnis2.pl

**Pozycjonowanie**: Audyt gotowości firm na dyrektywę NIS2.
**Target**: CISO, IT managerowie, compliance officers.

**Favicon (32×32 SVG)**:
- Tło: `#1a365d`
- Symbol: stylizowane „N2" w białym (Inter Bold), gdzie „2" lekko nachodzi na „N" — sugeruje wersję 2 dyrektywy
- Alternatywa: tarcza minimalistyczna z wpisanym „N2" w środku
- Padding wewnętrzny: 4px

**Apple-touch-icon (180×180)**:
- Tło: pełny `#1a365d`
- Centralnie: „N2" w białym, font Inter Black, 88pt
- Mała czerwona kropka (`#c0392b`, 8px) nad „2" jako kropka nad i — sygnał compliance/ostrzeżenia

**Logo poziome (SVG)**:
- Monogram tarczowy (16×16 w SVG): granat z białym „N2"
- Tekst: „TestNIS2" (Inter Semibold, granat) + „.pl" (Inter Regular, czerwień `#c0392b`)
- Spacing: 8px między monogramem a tekstem

**OG image (1200×630)**:
- Tło: `#1a365d`
- Lewy górny: monogram + „TestNIS2.pl" (Inter Semibold 28pt, ivory)
- Środek (waga wizualna): „Sprawdź gotowość firmy na NIS2" (Fraunces SemiBold 72pt, ivory)
- Dół: cienka linia czerwona 2px, pod nią „Audyt zgodności · Checklisty · Plan wdrożenia" (Inter 20pt, `#7fb3d4`)
- Prawy dolny: dyskretny ornament — 12 kropek w siatce 3×4 (`#c0392b`, 6px każda) jako abstrakcja punktów audytu

---

### 2. karynis2.pl

**Pozycjonowanie**: Sankcje finansowe i odpowiedzialność zarządu w NIS2.
**Target**: Zarządy, compliance officers, prawnicy korporacyjni.

**Favicon (32×32 SVG)**:
- Tło: `#1a365d`
- Symbol: stylizowany znak `€` lub `§` w czerwieni `#c0392b` na białym kwadracie wewnętrznym (24×24, radius 4px) — sugeruje karę
- Alternatywa: cyfra „2" w białym z czerwoną pieczęcią/przekreśleniem

**Apple-touch-icon (180×180)**:
- Tło: pełny `#1a365d`
- Centralnie: „§" (paragraf, Fraunces 120pt) w czerwieni `#c0392b`
- Pod spodem mikro-tekst „NIS2" (Inter Bold 18pt, biały)

**Logo poziome**:
- Monogram: kwadrat `#1a365d` z „§" `#c0392b`
- Tekst: „KaryNIS2" (Inter Semibold, granat) + „.pl" (czerwień)

**OG image (1200×630)**:
- Tło: gradient od `#1a365d` (lewo) do `#0f2340` (prawo) — minimalny
- Lewy górny: monogram + „KaryNIS2.pl"
- Środek: „Sankcje i konsekwencje prawne NIS2" (Fraunces 68pt, ivory)
- Pod tytułem: czerwona linia 4px szerokości 80px (akcent)
- Dół: „do 10 mln € · 2% obrotu · odpowiedzialność osobista zarządu" (Inter Mono 18pt, `#e8b4ad`)

---

### 3. skanujfirme.pl

**Pozycjonowanie**: Audyt bezpieczeństwa + RODO + NIS2 dla SMB.
**Target**: IT, DPO, compliance w SMB.

**Favicon (32×32 SVG)**:
- Tło: `#1a365d`
- Symbol: stylizowana lupa minimalistyczna — koło 14px obwód 2px biały, rączka 6px pod kątem 45°, **w środku koła kropka czerwona 4px** (sugeruje wykryty problem)
- Tu lupa jest OK bo jest centralna do brandu „skanowania"

**Apple-touch-icon (180×180)**:
- Tło: `#1a365d`
- Lupa biała 100×100 w centrum, w środku koła czerwona kropka 18px

**Logo poziome**:
- Monogram lupy (jak favicon)
- Tekst: „Skanuj" (Inter Semibold granat) + „Firmę" (Inter Semibold, czerwień)

**OG image**:
- Tło: `#1a365d` z subtelnym pattern siatki (linie `#234070` co 40px, opacity 0.3)
- Lewy górny: lupa + „SkanujFirmę.pl"
- Środek: „Audyt bezpieczeństwa i zgodności" (Fraunces 70pt)
- Dół: trzy ikonki w rzędzie (NIS2 🇪🇺, RODO 🔒, IT 🛡️) — narysowane jako proste białe outline, każda z labelem pod spodem

---

### 4. audytzespolu.pl

**Pozycjonowanie**: Audyt zespołów + mediacja w firmie + compliance.
**Target**: HR, liderzy zespołów, CEO.

**Favicon (32×32 SVG)**:
- Tło: `#1a365d`
- Symbol: trzy okręgi 8px ułożone w trójkąt równoboczny (dwa na dole, jeden na górze), białe, połączone cienkimi liniami 1px — sugeruje zespół/relacje
- Alternatywa: stylizowany ludzik 👥 narysowany jako geometria (dwa półokręgi = głowy)

**Apple-touch-icon**:
- Tło: `#1a365d`
- Trzy okręgi 40px białe w trójkącie, połączone liniami 3px

**Logo poziome**:
- Monogram trzy okręgi
- Tekst: „Audyt" (Inter Semibold granat) + „Zespołu" (Inter Semibold, `#c0392b`)

**OG image**:
- Tło: `#1a365d`
- Lewy górny: monogram + nazwa
- Środek: „Audyt zespołu — od diagnozy do działania" (Fraunces 64pt)
- Prawa strona: ilustracja — sześć okręgów w sieci (jak graf relacji) w odcieniach niebieskich, jeden czerwony (problem do diagnozy)

---

### 5. onpremiseai.pl

**Pozycjonowanie**: AI on-premise + suwerenność danych.
**Target**: CTO, AI engineers, security architects.

**Favicon (32×32 SVG)**:
- Tło: `#1a365d`
- Symbol: kwadrat-serwer (rack) — prostokąt 18×24 biały z trzema poziomymi liniami `#1a365d` w środku (sloty serwera) + mała kropka zielona `#27ae60` w prawym górnym rogu (status: on)
- Alternatywa: litera „Ω" (omega — on-premise jako lokalna stała) w białym

**Apple-touch-icon**:
- Tło: `#1a365d`
- Rack-server biały 100×130 w centrum, status-dot zielona 14px

**Logo poziome**:
- Monogram rack-server
- Tekst: „OnPremise" (Inter Semibold granat) + „AI" (Inter Black, `#c0392b`)

**OG image**:
- Tło: `#1a365d`
- Lewy górny: monogram + nazwa
- Środek: „AI w Twojej infrastrukturze" (Fraunces 72pt)
- Pod tytułem: „bezpiecznie · zgodnie · suwerennie" (Inter Mono 22pt, `#7fb3d4`)
- Tło — subtelny pattern z heksów (jak NVIDIA branding) opacity 0.1

---

### 6. aidzisiaj.pl

**Pozycjonowanie**: AI w polskim biznesie — praktycznie.
**Target**: Polscy przedsiębiorcy, decydenci SMB.

**Favicon (32×32 SVG)**:
- Tło: `#1a365d`
- Symbol: „AI" w białym (Inter Black 16pt), pod nim mały orzeł stylizowany 6×6 (skrzydła rozłożone jako trzy kreski) — odniesienie do polskości, ale subtelne
- Wersja prostsza: tylko „AI" białe + czerwona kropka pod (akcent narodowy)

**Apple-touch-icon**:
- Tło: `#1a365d`
- „AI" w centrum (Fraunces 110pt), pod spodem cienka czerwona linia 60×3px

**Logo poziome**:
- Monogram „AI"
- Tekst: „AI" (Inter Black granat) + „Dzisiaj" (Inter Regular, czerwień)

**OG image**:
- Tło: `#1a365d`
- Lewy górny: „AIDzisiaj.pl"
- Środek: „Sztuczna inteligencja w polskim biznesie" (Fraunces 60pt) + na drugiej linii kursywa „— praktycznie" (Fraunces Italic 56pt, `#c0392b`)
- Dół: trzy biało-czerwone akcenty (małe paski 40×4px) jako delikatne odniesienie narodowe

---

### 7. ragpolska.pl

**Pozycjonowanie**: Retrieval-Augmented Generation w polskim biznesie.
**Target**: AI engineers, data engineers, CTO.

**Favicon (32×32 SVG)**:
- Tło: `#1a365d`
- Symbol: dwa okręgi nakładające się (jak Venn diagram) — lewy biały, prawy `#e74c3c`, część wspólna jaśniejsza (sugeruje retrieval + generation)
- Alternatywa: „R" (Fraunces Bold) z subskryptem „AG" w mniejszym

**Apple-touch-icon**:
- Tło: `#1a365d`
- Venn-diagram 130×80 w centrum

**Logo poziome**:
- Monogram Venn
- Tekst: „RAG" (Inter Black granat) + „Polska" (Inter Semibold, `#e74c3c`)

**OG image**:
- Tło: `#1a365d`
- Lewy górny: monogram + nazwa
- Środek: „RAG — inteligentne wyszukiwanie dla Twojej firmy" (Fraunces 56pt, ivory)
- Wizualka z prawej: schemat strzałka „query → vector DB → LLM → answer" w monoline icons (białe outline)

---

## BRAND GROUP: NURIO (mental health B2C) — 8 domen

**Wspólny język wizualny**: organiczne kształty, miękkie radiusy (14–20px), kolory ziemi i natury, ilustracje zamiast ikon, ludzkie i ciepłe. Inspiracja: Headspace, Calm, ale bardziej dorosłe i edytorialne.

---

### 8. zdrowie.fit

**Pozycjonowanie**: Holistyczne zdrowie (ruch, umysł, dieta, regeneracja).
**Target**: B2C, evidence-based wellness.

**Paleta**: primary `#4a7c59` (sage green) / accent `#d9724a` (terracotta) / trust `#5b8def` / tło `#fdfcf9`.

**Favicon (32×32 SVG)**:
- Tło: `#fdfcf9` (ivory) z radiusem 6px
- Symbol: „◐" (półksiężyc) w `#4a7c59` 22×22, **kropka terracotta** 4px w pustej części półksiężyca — równowaga ciało/umysł
- Wersja dark-mode: tło `#4a7c59`, półksiężyc ivory

**Apple-touch-icon**:
- Tło: `#4a7c59` (sage)
- Półksiężyc ivory 110×110 w centrum, terracotta kropka 16px

**Logo poziome**:
- Monogram półksiężyca
- Tekst: „Zdrowie" (Fraunces Semibold sage) + „.fit" (Inter Semibold terracotta)

**OG image (1200×630)**:
- Tło: `#fdfcf9` (ivory) z subtelną teksturą papieru
- Lewy górny: monogram + „Zdrowie.fit" (Inter Semibold 28pt sage)
- Środek: „Ciało i umysł w harmonii" (Fraunces Italic 80pt sage)
- Pod tytułem: półksiężyc 80×80 obrócony, jako element graficzny
- Dół: „badania · praktyka · równowaga" (Inter 20pt terracotta) cienka linia 1px sage pod
- **Charakter editorialny, jak okładka magazynu lifestyle**

---

### 9. psychodzisiaj.pl

**Pozycjonowanie**: Psychologia codzienna — emocje, relacje, stres.
**Target**: B2C, dorośli zainteresowani self-development.

**Paleta**: primary `#2c6e8a` (teal-blue) / accent `#e07b4f` (coral) / trust `#7b68ee` (lawenda).

**Favicon (32×32 SVG)**:
- Tło: `#fdfcf9`
- Symbol: stylizowana spirala 18×18 (jak fala/myśl) w `#2c6e8a`, koniec zakończony małym okręgiem coral
- Alternatywa: litera „ψ" (psi) w `#2c6e8a` Fraunces

**Apple-touch-icon**:
- Tło: `#2c6e8a`
- „ψ" 140pt w ivory w centrum

**Logo poziome**:
- Monogram „ψ"
- Tekst: „Psycho" (Fraunces Semibold teal) + „Dzisiaj" (Fraunces Italic coral)

**OG image**:
- Tło: gradient `#2c6e8a` → `#3d8aab` (subtelny)
- Lewy górny: monogram + nazwa (ivory)
- Środek: „Zrozum siebie — żyj świadomie" (Fraunces Italic 76pt, ivory)
- Prawa strona: subtelna ilustracja — twarz w profilu narysowana jednym ciągłym konturem (1 line art) w `#e07b4f`

---

### 10. jaksobieradzic.pl

**Pozycjonowanie**: Strategie radzenia sobie ze stresem, lękiem, kryzysami.
**Target**: B2C, coping skills.

**Paleta**: primary `#2a7f62` / accent `#e08c4f` / trust `#8b7bb8`.

**Favicon (32×32 SVG)**:
- Tło: `#fdfcf9`
- Symbol: ścieżka — krzywa S-line w `#2a7f62`, na końcu mały trójkąt (strzałka) w `#e08c4f` — sugeruje drogę przez trudność
- Alternatywa: górka/szczyt (trójkąt z zaokrąglonym wierzchołkiem) w `#2a7f62` z małym słońcem `#e08c4f` nad

**Apple-touch-icon**:
- Tło: `#2a7f62`
- Stylizowana ścieżka biała przez całe pole, kończąca się szczytem ze słońcem `#e08c4f`

**Logo poziome**:
- Monogram (S-line + strzałka)
- Tekst: „JakSobie" (Fraunces Semibold zielony) + „Radzić" (Fraunces Italic, `#e08c4f`)

**OG image**:
- Tło: jasne ivory `#fdfcf9` z teksturą
- Lewy górny: monogram + nazwa
- Środek: „Trudne sytuacje — konkretne rozwiązania" (Fraunces 64pt, `#2a7f62`)
- Prawa strona dolna: ilustracja krętej drogi pod górę (1 line, `#e08c4f`)
- **Ton: empatyczny, ale konkretny — nie sentymentalny**

---

### 11. sprawdzwypalenie.pl

**Pozycjonowanie**: Wypalenie zawodowe — diagnoza, profilaktyka, regeneracja.
**Target**: Pracownicy korporacji, HR.

**Paleta**: primary `#7c5b3c` (warm brown) / accent `#e8922d` (amber) / trust `#7a9a6d` (sage).

**Favicon (32×32 SVG)**:
- Tło: `#fdfcf9`
- Symbol: świeca lub płomień stylizowany — owalna płomień 12×18 w `#e8922d`, „knot" 2px brązowy
- Alternatywa: bateria z niskim poziomem (prostokąt 22×12 obwód brąz, wypełnienie tylko 25% w amber)

**Apple-touch-icon**:
- Tło: `#7c5b3c`
- Płomień ivory 110×140 w centrum, z amber „rdzeniem"

**Logo poziome**:
- Monogram płomień
- Tekst: „Sprawdź" (Fraunces Semibold brąz) + „Wypalenie" (Fraunces Italic, `#e8922d`)

**OG image**:
- Tło: `#fdfcf9` z subtelnym vignette w rogach `#7c5b3c` (10% opacity)
- Lewy górny: monogram + nazwa
- Środek: „Rozpoznaj i pokonaj wypalenie" (Fraunces 70pt, `#7c5b3c`)
- Prawa: dwie świece — jedna płonąca jasno (amber), druga zgaszona (szara) — wizualizacja stanu

---

### 12. testpredyspozycje.pl

**Pozycjonowanie**: Testy predyspozycji zawodowych, osobowości, talentów.
**Target**: Osoby na rozdrożu zawodowym, doradcy kariery.

**Paleta**: primary `#6b5b95` (lawenda) / accent `#3cb4a0` (turkus) / trust `#d4a843` (gold).

**Favicon (32×32 SVG)**:
- Tło: `#fdfcf9`
- Symbol: stylizowany „kompas" — okrąg 22×22 obwód `#6b5b95` 2px, w środku igła (cienki trójkąt) skierowana w prawo-górę, jedna połowa lawendowa, druga turkusowa
- Alternatywa: cztery puzzle-piece układające się w mały kwadrat 20×20 (4 kolory: lawenda, turkus, gold, ivory)

**Apple-touch-icon**:
- Tło: `#6b5b95`
- Kompas ivory 130×130 w centrum, igła turkus/gold

**Logo poziome**:
- Monogram kompas
- Tekst: „Test" (Fraunces Semibold lawenda) + „Predyspozycje" (Fraunces Regular turkus)

**OG image**:
- Tło: `#fdfcf9`
- Lewy górny: monogram + nazwa
- Środek: „Poznaj swoje mocne strony" (Fraunces Italic 76pt, `#6b5b95`)
- Prawa: kompas-róża 4 kierunki, każde ramię w innym brand-color, eleganckie linie

---

### 13. psychosen.pl

**Pozycjonowanie**: Nauka o śnie, higiena snu, chronobiologia.
**Target**: Osoby z problemami ze snem.

**Paleta**: primary `#2d3a7c` (deep night blue) / accent `#d4a843` (gold/moon) / trust `#6b9fd4` (dawn blue).

**WYJĄTEK: dark_mode = true** — favicon i OG mają ciemne tło naturalnie.

**Favicon (32×32 SVG)**:
- Tło: `#2d3a7c`
- Symbol: półksiężyc gold `#d4a843` 18×22, mały gwiazdki obok (3 kropki gold 2px każda)
- **Bardzo dobrze rozpoznawalne nawet w 16×16** — księżyc to klasyk dla snu

**Apple-touch-icon**:
- Tło: pełny `#2d3a7c`
- Półksiężyc gold 130×130 w centrum, 5 gwiazdek wokół (rozsiane)

**Logo poziome**:
- Monogram księżyc
- Tekst: „Psycho" (Fraunces Semibold ivory) + „Sen" (Fraunces Italic gold)
- Logo na nagłówku — używaj jasnej wersji (ivory tekst), bo dark mode default

**OG image**:
- Tło: `#2d3a7c` z subtelnym gradientem nocnego nieba (ciemniejszy w prawym dolnym rogu)
- Punktowe „gwiazdki" rozsiane (małe białe kropki 1–2px, 30 sztuk, low opacity)
- Lewy górny: monogram + nazwa (ivory)
- Środek: „Jak spać lepiej i zdrowiej" (Fraunces Italic 80pt, ivory)
- Pod: cienka linia gold + „Higiena snu · Chronobiologia · Zaburzenia snu" (Inter 20pt `#6b9fd4`)
- **Klimat: spokojny, nocny, edytorialny — jak okładka książki o astronomii**

---

### 14. psycho.edu.pl

**Pozycjonowanie**: Edukacja psychologiczna — ogólna, neuropsy, terapia.
**Target**: Studenci psychologii, terapeuci, dociekliwi pacjenci.

**Paleta**: primary `#34568b` (academic blue) / accent `#c49b3a` (academic gold) / trust `#2c8e8a` (teal).

**WYJĄTEK: heading_weight 700, radius 6px** — bardziej akademicki, kanciasty look.

**Favicon (32×32 SVG)**:
- Tło: `#fdfcf9`
- Symbol: stylizowany czepek absolwenta + „ψ" — uproszczony do trójkąta-kapelusza `#34568b` 22×8 + pod nim „ψ" w gold
- Alternatywa (prostsza): tylko „Ψ" (psi duże) w `#34568b` Fraunces Bold

**Apple-touch-icon**:
- Tło: `#34568b`
- „Ψ" Fraunces Bold 140pt ivory w centrum, mała pozioma linia gold pod (jak signature)

**Logo poziome**:
- Monogram „Ψ"
- Tekst: „Psycho" (Fraunces Bold blue) + „.edu.pl" (Inter Semibold gold)

**OG image**:
- Tło: `#fdfcf9` z teksturą starego papieru/manuskryptu (subtle)
- Górna belka pozioma: „Ψ" gold + „Psycho.edu.pl" (Inter Bold 28pt blue)
- Środek: „Psychologia — wiedza dla każdego" (Fraunces Bold 76pt, `#34568b`)
- Dół: znaki książkowe — trzy poziome linie różnej długości (jak listy w spisie treści)
- **Akademicki, klasyczny, jak okładka podręcznika Wiley**

---

## BRAND GROUP: MAREK (personal/creative) — 2 domeny

---

### 15. creativebrandpro.com

**Pozycjonowanie**: AI Music + Creative Branding (EN, międzynarodowy).
**Target**: Cyfrowi twórcy, muzycy, brand professionals.

**Paleta**: primary `#6c3483` (electric purple) / accent `#f39c12` (gold) / trust `#5b8def`.

**Favicon (32×32 SVG)**:
- Tło: `#6c3483`
- Symbol: nuta stylizowana ♪ w `#f39c12`, wokół subtelne „pulse" — okrąg obwód 1px gold, jakby fala dźwięku
- Alternatywa: „CB" splecione (ligature) jak monogram couture

**Apple-touch-icon**:
- Tło: `#6c3483`
- Stylizowana fala dźwięku — 5 pionowych słupków różnej wysokości (40–120px) gold w centrum, jak equalizer

**Logo poziome**:
- Monogram (nuta lub equalizer)
- Tekst: „Creative" (Fraunces Italic purple) + „BrandPro" (Inter Black gold)

**OG image (EN!)**:
- Tło: gradient `#6c3483` → `#3d1b50` (deep purple)
- Lewy górny: monogram + „CreativeBrandPro.com"
- Środek: „Create. Brand. Amplify." (Fraunces Bold Italic 90pt, ivory) — trzy słowa, każde w nowej linii, kropki gold między
- Prawa: equalizer wizualka — 7 słupków gold różnej wysokości, animacja w SVG opcjonalnie
- **Charakter: bold, kreatywny, music-industry feel, premium**

---

### 16. analizastatystyczna.me

**Pozycjonowanie**: SPSS, statystyka, metodologia naukowa.
**Target**: Studenci, doktoranci, naukowcy.

**Paleta**: primary `#34495e` (slate) / accent `#e67e22` (warm orange) / trust `#7b68ee` (lavender).

**Favicon (32×32 SVG)**:
- Tło: `#fdfcf9`
- Symbol: krzywa Gaussa stylizowana — łuk (półokrąg dolny przesunięty) `#34495e` 24×14, pod nim oś pozioma 1px
- Alternatywa: „σ" (sigma — symbol odchylenia) w `#34495e` Fraunces

**Apple-touch-icon**:
- Tło: `#34495e`
- Krzywa Gaussa biała + „σ" pomarańczowy w środku pola

**Logo poziome**:
- Monogram krzywa
- Tekst: „Analiza" (Fraunces Semibold slate) + „Statystyczna" (Inter Light, `#e67e22`)

**OG image**:
- Tło: `#fdfcf9` z dyskretną siatką kratkową (graph paper, opacity 0.15)
- Lewy górny: monogram + nazwa
- Środek: „SPSS, statystyka i badania naukowe" (Fraunces 64pt slate)
- Prawa: ilustracja — krzywa rozkładu normalnego z zaznaczonymi obszarami σ (pomarańczowe wypełnienie 1σ, jaśniejsze 2σ)
- **Charakter: precyzyjny, akademicki, ale przyjazny — jak okładka książki R for Data Science**

---

## BRAND GROUP: MEDIACJA — 1 domena

---

### 17. twojamediacja.pl

**Pozycjonowanie**: Mediacja rodzinna, gospodarcza, pracownicza (Białystok + online).
**Target**: Strony konfliktów szukające alternatywy dla sądu.

**Paleta**: primary `#27ae60` (peace green) / accent `#2c3e50` (slate dark) / trust `#5b8def`.

**Favicon (32×32 SVG)**:
- Tło: `#fdfcf9`
- Symbol: waga sprawiedliwości stylizowana ⚖ — pionowa kreska (słup) 2×20 `#27ae60`, na górze poziomy belka 16×2, na końcach belki dwa małe okręgi 4px (szalki) wypełnione `#2c3e50`
- Alternatywa: dwie ręce uścisk (ale to trudne w 32px) — uścisk dłoni jako dwa „L" stykające się

**Apple-touch-icon**:
- Tło: `#27ae60`
- Waga ivory 100×140 w centrum, szalki w `#2c3e50`

**Logo poziome**:
- Monogram waga
- Tekst: „Twoja" (Fraunces Italic green) + „Mediacja" (Fraunces Semibold, `#2c3e50`)

**OG image**:
- Tło: `#fdfcf9` z subtelnym gradientem zielonkawym w lewym górnym rogu
- Lewy górny: monogram + nazwa
- Środek: „Rozwiąż konflikt — szybko, poufnie, skutecznie" (Fraunces Italic 60pt, `#2c3e50`)
- Prawa: ilustracja dwóch dłoni stykających się palcem (bardzo subtelna line art zielona)
- Dół: „Białystok · online · cała Polska" (Inter 20pt green)
- **Charakter: ciepły, profesjonalny, godny zaufania, NIE prawniczy-sztywny**

---

## BRAND GROUP: BROKER — 1 domena

---

### 18. wppage.pl

**Pozycjonowanie**: WordPress — strony, SEO, wtyczki, bezpieczeństwo.
**Target**: Właściciele stron WP, freelancerzy, agencje.

**Paleta**: primary `#21759b` (WP blue) / accent `#d54e21` (WP orange) / trust `#5b8def`.

**Favicon (32×32 SVG)**:
- Tło: `#fdfcf9`
- Symbol: NIE używaj oficjalnego logo WordPress (znak handlowy). Zamiast tego — stylizowane „WP" w `#21759b` Inter Black, „W" lekko nakłada się na „P", kropka pomarańczowa nad „P" (jak focus dot)
- Alternatywa: nawias `< >` w `#21759b` z „WP" w środku

**Apple-touch-icon**:
- Tło: `#21759b`
- „WP" w ivory Inter Black 130pt w centrum, kropka `#d54e21` 16px nad „P"

**Logo poziome**:
- Monogram „WP"
- Tekst: „WP" (Inter Black `#21759b`) + „Page" (Inter Semibold `#d54e21`)

**OG image**:
- Tło: `#21759b`
- Lewy górny: monogram + nazwa (ivory)
- Środek: „WordPress — twórz, optymalizuj, zabezpieczaj" (Fraunces 56pt ivory)
- Prawa: stylizowana „strona" — biały prostokąt z liniami tekstu (3 linie) i pomarańczowym przyciskiem CTA na dole
- **Charakter: technical, ale przyjazny, web-dev focused**

---

## Workflow generowania w Claude Design

**Sugerowany prompt-template** (wklej dla każdej domeny osobno):

```
Wygeneruj komplet brandingu dla domeny [DOMAIN.PL]:

KONTEKST:
[skopiuj sekcję domeny z DESIGN_BRIEFS.md]

DOSTARCZ:
1. favicon.svg — 32×32, wektor, czytelny w 16×16
2. favicon-32.png i favicon-16.png — rastry z SVG
3. apple-touch-icon.png — 180×180, pełne tło, monogram biały
4. logo.svg — wersja pozioma (monogram + tekst)
5. og-default.png — 1200×630, kompozycja jak w briefie

ZASADY:
- Użyj DOKŁADNIE kolorów z briefu (hex)
- Fraunces dla nagłówków, Inter dla body
- Bez gradientów tęczowych, bez stockowych ikon
- Każdy plik gotowy do `output/<slug>/static/img/`
```

**Lokalizacja docelowa** (ważne dla buildu):
```
src/static/img/
├── favicon.ico
├── favicon.svg
├── favicon-16.png
├── favicon-32.png
├── apple-touch-icon.png
├── og-default.png
└── logo.svg
```

Build kopiuje `src/static/` do `output/<domain-slug>/static/`. Jeśli chcesz różne assety per-domena, rozważ rozszerzenie `build.py` o sekcję `assets:` w YAML domeny — obecnie wszystkie domeny dzielą jeden katalog `src/static/img/`, więc trzeba albo (a) generować assety per-build-step (build.py kopiuje dla każdej domeny inny zestaw), albo (b) trzymać assety osobno w `src/static/img/<domain-slug>/` i dostosować szablon.

**Rekomendacja**: dodaj do `build.py` sekcję która kopiuje `src/static/img/<domain-slug>/` do `output/<domain-slug>/static/img/` zamiast globalnego `src/static/img/`. Wtedy 18 domen = 18 osobnych folderów z assetami, każdy z własnym faviconem.

---

## Spójność wizualna — checklist po wygenerowaniu

- [ ] Favicon czytelny w 16×16 w pasku zakładek (test: zminimalizuj okno)
- [ ] Apple-touch-icon nie ma przezroczystości (iOS doda cień)
- [ ] OG image ma czytelny tekst gdy zmniejszony do 600×315 (preview FB/LinkedIn)
- [ ] Logo SVG działa w jednym kolorze (test: konwersja na grayscale)
- [ ] Wszystkie pliki w SVG mają `viewBox` (responsywność)
- [ ] PNG-i mają kompresję (TinyPNG/oxipng)
- [ ] OG-default ma `alt`-friendly kompozycję — tekst czytelny bez kontekstu

---

# CZĘŚĆ II — POZOSTAŁE ASSETY (PWA, social, email, error pages)

Brief uzupełniający — to co poza podstawowym kompletem (favicon/og/logo). Wszystko trzymaj spójne z wcześniej zdefiniowaną paletą i typografią danej domeny.

## A. PWA / Manifest icons (per domena)

Pliki do dostarczenia (do `static/img/icons/`):

| Plik | Rozmiar | Cel |
|------|---------|-----|
| `icon-192.png` | 192×192 | Android Chrome home screen |
| `icon-512.png` | 512×512 | Splash screen, app drawer |
| `icon-maskable-192.png` | 192×192 | Adaptive icons (Android) |
| `icon-maskable-512.png` | 512×512 | jak wyżej |
| `mstile-144.png` | 144×144 | Windows live tile |
| `mstile-150.png` | 150×150 | Windows pinned site |
| `safari-pinned-tab.svg` | wektor mono | Safari pinned tab (jeden kolor!) |

**Zasada maskable**: znak musi być w **wewnętrznych 80%** płótna (centralne 153×153 z 192). Reszta to bezpieczny padding tłem brand. Bez tego Android utnie znak okrągłą maską.

**Safari pinned tab** = SVG monochromatyczny, jedna ścieżka, kolor zostanie nadpisany przez user agent. Najprostsza wersja monogramu z brief.

**Manifest webmanifest** (do `output/<slug>/site.webmanifest` — dodaj do build.py jeśli nie ma):
```json
{
  "name": "[Pełna nazwa z YAML.name]",
  "short_name": "[max 12 znaków, najczęściej pierwsze słowo]",
  "icons": [
    {"src": "/static/img/icons/icon-192.png", "sizes": "192x192", "type": "image/png"},
    {"src": "/static/img/icons/icon-512.png", "sizes": "512x512", "type": "image/png"},
    {"src": "/static/img/icons/icon-maskable-192.png", "sizes": "192x192", "type": "image/png", "purpose": "maskable"},
    {"src": "/static/img/icons/icon-maskable-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"}
  ],
  "theme_color": "[primary z YAML]",
  "background_color": "[#fdfcf9 lub primary jeśli dark_mode]",
  "display": "standalone",
  "start_url": "/"
}
```

## B. Social media — kanały

Per domena potrzebujesz min. dwa pakiety: **Facebook + Instagram** (wszystkie B2C) lub **LinkedIn + Twitter/X** (wszystkie B2B archaios).

### B.1 Facebook

| Plik | Rozmiar | Uwagi |
|------|---------|-------|
| `fb-profile.png` | 360×360 (wyświetla się 170×170) | = apple-touch-icon, ten sam plik |
| `fb-cover.png` | 820×312 (mobile crop: 640×360, safe zone: 820×312 środkowo) | tagline + CTA + URL |
| `fb-shared-post.png` | 1200×630 | = og-default |

**FB cover (820×312) — kompozycja**:
- Tło: `primary`
- Lewa 1/3: monogram + nazwa domeny (białe, duże)
- Środek: tagline (Fraunces 36pt, ivory, max 8 słów)
- Prawa: URL `domena.pl` (Inter Mono 22pt, accent color)
- Mobile safe zone: krytyczne elementy w środkowych 640×360 — boki mogą być przycięte

### B.2 Instagram

| Plik | Rozmiar | Cel |
|------|---------|-----|
| `ig-profile.png` | 320×320 | apple-touch-icon equivalent |
| `ig-post-template.png` | 1080×1080 | szablon do postów (z miejscem na tekst) |
| `ig-story-template.png` | 1080×1920 | szablon Story |
| `ig-reels-cover.png` | 1080×1920 | thumbnail Reels |

**IG post template (1080×1080) — kompozycja stała**:
- Górny pasek (200px): primary color, monogram + nazwa biało
- Środek (680px): biała przestrzeń na nagłówek artykułu (placeholder „Tytuł artykułu" Fraunces 80pt, primary)
- Dolny pasek (200px): accent color, „domena.pl" + CTA „czytaj więcej →" (ivory)
- W każdym poście podmieniasz tylko tekst środkowy

**IG story (1080×1920)**: pionowy wariant — nazwa na górze, tytuł w środku z dużą przestrzenią, na dole "swipe up" / link sticker placeholder.

### B.3 LinkedIn

| Plik | Rozmiar | Cel |
|------|---------|-----|
| `li-profile.png` | 400×400 | profile picture (firma/osobisty) |
| `li-banner.png` | 1584×396 | cover banner |
| `li-shared-post.png` | 1200×627 | shared link preview |

**LinkedIn banner (1584×396)** — szczególnie dla archaios + marek:
- Tło: `primary`
- Lewa strona: monogram (duży, 200×200) + nazwa + tagline
- Prawa strona: 3 kluczowe propozycje wartości jako bullety lub ikony (np. dla TestNIS2: "Audyt · Checklisty · Wdrożenie")
- Mobile crop: środkowe 80% widoczne, brzegi mogą zniknąć

### B.4 Twitter / X

| Plik | Rozmiar | Cel |
|------|---------|-----|
| `tw-profile.png` | 400×400 | = LinkedIn profile |
| `tw-header.png` | 1500×500 | banner |
| `tw-card.png` | 1200×675 | summary_large_image card |

**Twitter card (1200×675)** — różni się od OG (1200×630) wysokością 45px. Najprościej: zaprojektuj w 1200×675, OG to crop top 1200×630. Albo dwa osobne pliki.

### B.5 YouTube (jeśli kanał)

| Plik | Rozmiar | Cel |
|------|---------|-----|
| `yt-channel-art.png` | 2560×1440 (TV safe: 1546×423 środkowo) | banner |
| `yt-thumbnail-template.png` | 1280×720 | thumbnail dla wideo |

## C. Email — podpis i newsletter

### C.1 Email signature banner

Format: 600×150 PNG (skala 2× = 1200×300 dla Retina).
Kompozycja:
- Lewa: monogram 100×100
- Środek: nazwa + tagline + email + URL (Inter, smallish)
- Prawa: maks 3 ikonki social (24×24 monochrome w kolorze primary)
- Bez animacji, bez CSS-only — czysty PNG do wklejenia w Outlook/Gmail

### C.2 Newsletter header

Format: 600×200 PNG (responsywny w klientach pocztowych).
- Tło primary, monogram + nazwa biała na lewo, slogan tygodniowy po prawej
- **Statyczny, bez webfontów** — fonty rasteryzuj do PNG, klienci pocztowi nie ładują custom fonts wiarygodnie

### C.3 Newsletter article thumbnail

Format: 600×300 (2:1).
- Placeholder dla zdjęcia wpisu w newsletterze. Jeśli nie ma własnego — generuj z og-default skrojony do 600×300.

## D. Error pages — 404 i 500

Per domena lub jeden uniwersalny set z brand-grupy. Format: ilustracja inline w HTML lub `404.png` (1200×600).

**404 brief — wariant per brand-grupa**:

- **Archaios** (B2B): poważna estetyka — duże „404" w `primary` Fraunces Black 200pt, pod spodem „Nie znaleziono zasobu — sprawdź ścieżkę audytu" (ironia compliance), CTA „wróć do strony głównej"
- **Nurio** (B2C wellness): łagodna ilustracja — zagubiona postać line-art na ścieżce, „Wygląda na to że ta strona zboczyła z trasy", CTA z ciepłym tonem
- **Marek** (creative): minimalizm — 404 jako equalizer (creativebrandpro) albo wykres z brakującymi danymi (analizastatystyczna)
- **Mediacja**: spokojny ton — „Konflikt URL. Mediator został wezwany. Wróćmy do startu" + CTA do strony głównej
- **Broker (wppage)**: techniczny — kod HTTP wyświetlony jak DevTools console, „Strona nie istnieje — sprawdź permalink"

**500 page**: jednolity dla wszystkich — krótki tekst, monogram, link do strony głównej, mailto do supportu (`email` z YAML).

## E. Author placeholder + product placeholder

Build.py używa `author.photo_url` i nie zawsze ma swoją grafikę. Potrzebny placeholder:

- `author-placeholder.png` — 400×400, kolisty crop, sylwetka neutralna w kolorach brand-grupy
- `author-default-bg.png` — 1200×400, header ścieżki autora (`/autorzy/jan-kowalski/`)

**Sylwetka neutralna**: prosty kontur głowy + ramion w `primary`, na tle ivory. Bez konkretnych cech (brak fryzury, gender-neutral). Inspiracja: GitHub identicon, ale spójny z brandem.

**Product placeholder (do CTA-cards w artykułach)**:
- 800×450 (16:9), tło `primary`, w środku duża nazwa produktu + cena/CTA (jeśli jest), na dole mała linia accent
- Generowany dynamicznie w build.py przez Pillow (jak og_image), jeśli `product.image_url` puste

## F. Default article hero (fallback)

Gdy artykuł nie ma `image_url`, OG-image generuje się z tytułu. Ale dla samego artykułu (sekcja hero) potrzebny jest fallback:

- `article-hero-fallback.png` — 1200×500, abstrakcyjna kompozycja brand-grupy (bez tekstu — sam brand-pattern)
- Per brand-grupa:
  - **Archaios**: siatka geometryczna, heksagony, monoline tarcza w prawym dolnym rogu
  - **Nurio**: organiczne kształty (krzywe Béziera), gradienty primary→primary_light, ilustracja botaniczna jednej linii
  - **Marek-creative**: equalizer-fala
  - **Marek-academic**: krzywa Gaussa + siatka kratkowa
  - **Mediacja**: dwie krzywe spotykające się w punkcie (symbolika spotkania)
  - **Broker (wppage)**: stylizowana siatka HTML/CSS

## G. Skróty per domena — co realnie potrzebujesz najpierw

Priorytetyzacja (jeśli ograniczony czas):

**P0 — bez tego strona nie zadziała poprawnie**:
1. `favicon.svg` + `favicon-32.png` + `favicon-16.png`
2. `apple-touch-icon.png`
3. `og-default.png`

**P1 — istotne dla SEO i social sharing**:
4. `icon-192.png` + `icon-512.png` + `site.webmanifest`
5. `safari-pinned-tab.svg`
6. `logo.svg` (dla nagłówka)

**P2 — dla aktywnej promocji**:
7. FB cover + IG profile (jeśli prowadzisz konta)
8. LinkedIn banner (dla archaios + marek)
9. Email signature banner

**P3 — dopieszczenie**:
10. 404 illustration
11. Author placeholder
12. Article hero fallback
13. Newsletter header
14. Maskable icons

## H. Tabela szybkich kolorów per domena (do copy-paste)

| Domena | Primary | Accent | Trust | Charakter |
|--------|---------|--------|-------|-----------|
| zdrowie.fit | `#4a7c59` | `#d9724a` | `#5b8def` | sage/terracotta editorial |
| testnis2.pl | `#1a365d` | `#c0392b` | `#2980b9` | granat compliance |
| karynis2.pl | `#1a365d` | `#c0392b` | `#2980b9` | granat compliance + alarm |
| skanujfirme.pl | `#1a365d` | `#c0392b` | `#2980b9` | granat audyt |
| audytzespolu.pl | `#1a365d` | `#c0392b` | `#5b8def` | granat HR |
| onpremiseai.pl | `#1a365d` | `#c0392b` | `#2980b9` | enterprise AI |
| aidzisiaj.pl | `#1a365d` | `#c0392b` | `#2980b9` | granat + akcent narodowy |
| ragpolska.pl | `#1a365d` | `#e74c3c` | `#5b8def` | granat tech |
| psychodzisiaj.pl | `#2c6e8a` | `#e07b4f` | `#7b68ee` | teal + coral |
| jaksobieradzic.pl | `#2a7f62` | `#e08c4f` | `#8b7bb8` | green + amber |
| sprawdzwypalenie.pl | `#7c5b3c` | `#e8922d` | `#7a9a6d` | brown + amber |
| testpredyspozycje.pl | `#6b5b95` | `#3cb4a0` | `#d4a843` | lawenda + turkus + gold |
| psychosen.pl | `#2d3a7c` | `#d4a843` | `#6b9fd4` | night blue + moon gold (DARK) |
| psycho.edu.pl | `#34568b` | `#c49b3a` | `#2c8e8a` | academic blue + gold |
| creativebrandpro.com | `#6c3483` | `#f39c12` | `#5b8def` | electric purple + gold |
| analizastatystyczna.me | `#34495e` | `#e67e22` | `#7b68ee` | slate + warm orange |
| twojamediacja.pl | `#27ae60` | `#2c3e50` | `#5b8def` | peace green + slate |
| wppage.pl | `#21759b` | `#d54e21` | `#5b8def` | WP blue + WP orange |

## I. Naming convention dla wygenerowanych plików

Niezależnie od narzędzia, trzymaj się tej struktury w outputach:

```
brand-assets/<domain-slug>/
├── favicon/
│   ├── favicon.svg
│   ├── favicon.ico
│   ├── favicon-16.png
│   ├── favicon-32.png
│   ├── apple-touch-icon.png
│   └── safari-pinned-tab.svg
├── pwa/
│   ├── icon-192.png
│   ├── icon-512.png
│   ├── icon-maskable-192.png
│   ├── icon-maskable-512.png
│   ├── mstile-144.png
│   ├── mstile-150.png
│   └── site.webmanifest
├── social/
│   ├── og-default.png
│   ├── tw-card.png
│   ├── fb-cover.png
│   ├── ig-profile.png
│   ├── ig-post-template.png
│   ├── ig-story-template.png
│   ├── li-banner.png
│   └── li-shared-post.png
├── email/
│   ├── signature-banner.png
│   └── newsletter-header.png
├── errors/
│   ├── 404.png
│   └── 500.png
├── fallbacks/
│   ├── author-placeholder.png
│   ├── article-hero-fallback.png
│   └── product-placeholder.png
└── logo/
    ├── logo.svg              (poziomy, kolorowy)
    ├── logo-mono.svg         (poziomy, jeden kolor)
    ├── logo-stacked.svg      (pionowy, monogram nad tekstem)
    └── logo-mark-only.svg    (sam monogram)
```

Po wygenerowaniu kopiujesz to do `src/static/img/<domain-slug>/` i build.py używa per-domain.

## J. Master prompt — pełny pakiet (do wklejenia w Claude Design)

```
Wygeneruj KOMPLET BRANDINGU dla domeny [DOMAIN].

KONTEKST DOMENY:
[wklej sekcję z DESIGN_BRIEFS.md część I — domena]

PALETA:
Primary: [hex]
Accent: [hex]
Trust: [hex]
Tło neutralne: #fdfcf9 (chyba że dark_mode)

TYPOGRAFIA:
Heading: Fraunces (semibold/bold)
Body: Inter (regular/semibold)

DOSTARCZ KOMPLET (zgodnie ze strukturą brand-assets/<slug>/):

FAVICON & PWA:
- favicon.svg (32×32, czytelny w 16×16)
- favicon-16.png, favicon-32.png
- apple-touch-icon.png (180×180, pełne tło)
- icon-192.png, icon-512.png
- icon-maskable-192.png, icon-maskable-512.png (znak w 80% środka)
- safari-pinned-tab.svg (mono, jedna ścieżka)
- mstile-144.png, mstile-150.png

LOGO:
- logo.svg (poziomy)
- logo-mono.svg (jeden kolor)
- logo-stacked.svg (pionowy)
- logo-mark-only.svg (monogram)

SOCIAL:
- og-default.png (1200×630)
- tw-card.png (1200×675)
- fb-cover.png (820×312, safe zone 640×360)
- ig-profile.png (320×320)
- ig-post-template.png (1080×1080)
- ig-story-template.png (1080×1920)
- li-banner.png (1584×396)
- li-shared-post.png (1200×627)

EMAIL:
- signature-banner.png (600×150)
- newsletter-header.png (600×200)

ERRORS:
- 404.png (1200×600)
- 500.png (1200×600)

FALLBACKS:
- author-placeholder.png (400×400)
- article-hero-fallback.png (1200×500)
- product-placeholder.png (800×450)

ZASADY:
- Wszystkie SVG mają viewBox
- PNG-i zoptymalizowane (max kompresja bez artefaktów)
- Maskable icons: znak w wewnętrznych 80%
- Apple-touch-icon: 0% przezroczystości
- OG czytelny po skompresowaniu do 600×315
- Spójność: wszystkie pliki używają DOKŁADNIE tej samej palety i tego samego monogramu
```

## K. Co dalej w build.py (wymagane zmiany techniczne)

Żeby pełny pakiet trafił do produkcji, trzeba w `build.py`:

1. **Per-domain assets**: kopiować `src/static/img/<domain-slug>/` zamiast globalnego `src/static/img/`
2. **Manifest**: generować `site.webmanifest` per domena z `theme_color = colors.primary` z YAML
3. **`<link>` tags w base.html**: dorzucić `apple-touch-icon`, `manifest`, `mask-icon` (Safari), `msapplication-TileColor`, `msapplication-TileImage`
4. **404/500 templates**: dodać `src/templates/404.html` i `500.html` z fallback ilustracją

Mogę to zrobić w osobnej iteracji — daj znak.

