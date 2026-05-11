# psychodzisiaj.pl — pakiet design

Domena: codzienna psychologia (klaster NURIO). Charakter: ciepły, dostępny, jak rozmowa z mądrym przyjacielem-psychologiem przy kawie. Nie kontemplacyjny jak psychosen. Nie naukowo-rygorystyczny jak zdrowie.fit. Bardziej *engaged & accessible*.

## Tożsamość marki

**Nazwa:** PsychoDzisiaj
**Tagline:** Psychologia na co dzień — zrozum siebie
**Pozycjonowanie:** Codzienna psychologia, emocje, relacje, stres, rozwój — wiedza akademicka w przystępnym ujęciu

## Paleta kolorów

| Rola | HEX | Użycie |
|---|---|---|
| Primary (ocean teal) | `#2c6e8a` | nagłówki, linki, znak twarzy lewej |
| Primary dark | `#1d4e66` | hover, ramki |
| Primary light | `#6aafc9` | tła sekcji |
| Accent (terracotta/coral) | `#e07b4f` | "Dzisiaj", uśmiechy, druga twarz |
| Accent dark | `#c0623a` | hover na akcent |
| Trust (violet) | `#7b68ee` | linie komunikacji, akcenty psychologiczne |
| Background ivory | `#fdfcf9` | tło |
| Text primary | `#2a2a2a` | nagłówki |
| Text body | `#5a5a5a` | akapity |
| Text muted | `#7a7a7a` | meta |

**Logika kolorów:** teal = "ja", spokój, refleksja. Coral = "ty", kontakt, emocja. Violet = przestrzeń między ludźmi (relacje, komunikacja).

## Typografia

**Heading:** Source Serif Pro (humanistyczny serif, czytelny w długich tekstach)
**Body:** Inter

```css
--font-heading: 'Source Serif Pro', 'EB Garamond', Georgia, serif;
--font-body: 'Inter', system-ui, sans-serif;
```

## Asetty wizualne

`_design/` zawiera: `logo.svg`, `favicon.svg`, `og-default.svg`, `hero-illustration.svg` (dwie sylwetki w komunikacji), `article-divider.svg` (trzy kolorowe kropki).

## Galeria artykułowa — 10 artykułów

### Konwencja stylu zdjęć

**Estetyka:** "warm editorial documentary" — codzienne sytuacje, prawdziwi ludzie (nie modele), ciepłe naturalne światło, autentyczne emocje (nie pozowane uśmiechy reklamowe). Polskie/europejskie konteksty kulturowe (mieszkania, kawiarnie, ulice, biura — nie LA/Manhattan).

**Paleta:** ciepłe ziemiste tony (oliwka, terracotta, kremowy), akcenty teal i violet w detalach. Nie cold-blue, nie HDR.

### Universal AI prompt suffix

```
... warm editorial documentary photography, natural daylight, real
unposed people (not models), authentic candid emotions, European
urban context, palette of warm earth tones (terracotta #e07b4f,
ocean teal #2c6e8a, ivory #fdfcf9 with violet #7b68ee accents),
shallow depth of field, magazine-quality, no text overlays,
16:9 aspect ratio --ar 16:9 --style raw
```

Negative: `--no neon, oversaturated, fake smile, plastic, instagram filter, hdr, model headshots, beauty influencer, american suburb`

---

### Artykuł #1 — Prokrastynacja (PILLAR)

**Slug:** `prokrastynacja-dlaczego-odkladamy-wazne-sprawy`

**Hero (1200×675)** — `01-prokrastynacja-hero.webp`

*Prompt:* `Editorial documentary photo: 30-something person at kitchen table mid-morning, half-finished cup of coffee, open laptop showing blank document, hand on chin staring distractedly out window at neutral middle-distance, warm soft window light, organic objects around (notebook, plant), expression contemplative not distressed. Real candid moment, not staged. [+ suffix]`

*Stock:* Unsplash `procrastination work from home`, `staring out window laptop`. *Alt:* `Osoba przy biurku z pustym dokumentem patrząca przez okno — moment prokrastynacji`

**Inline graphic (SVG, 700×400)** — `01-petla-prokrastynacji.svg`

Diagram pętli: Zadanie → Lęk/dyskomfort → Unikanie → Krótkotrwała ulga → Wzrost lęku z czasem → Zadanie pilniejsze → ↑ pętla. Każdy etap z mini-ikoną.

---

### Artykuł #2 — Gaslighting w relacjach

**Slug:** `gaslighting-w-relacjach-jak-rozpoznac`

**Hero** — `02-gaslighting-hero.webp`

*Prompt:* `Editorial documentary photo: two people sitting in living room, one (back of head visible, blurred) gesturing animatedly while explaining, second person (in focus) showing expression of self-doubt and confusion - touching forehead, looking down. Soft afternoon light, real intimate scale of intimate space, no exaggerated drama. [+ suffix]`

*Alt:* `Osoba z gestem niepokoju i samokrytycznej refleksji — wzorzec relacyjny gaslightingu`

**Inline graphic** — `02-flagi-gaslightingu.svg`: 7 sygnałów ostrzegawczych (DARVO, "to twoja wina", izolacja od bliskich, etc.) jako kafelki.

---

### Artykuł #3 — Lęk społeczny vs niechęć

**Slug:** `lek-spoleczny-vs-introwertyzm-roznice`

**Hero** — `03-lek-spoleczny-hero.webp`

*Prompt:* `Editorial photo: person at edge of small social gathering (3-4 people in soft focus background), holding wine glass, eyes scanning room with mild apprehension, body slightly turned away from group. Warm cafe light. Captures the difference between someone overwhelmed (anxiety) vs someone simply preferring solitude. [+ suffix]`

**Inline graphic** — `03-spektrum-lek-introwertyzm.svg`: spektrum z punktami: introwertyzm (preferuje samotność, czuje się dobrze sam) → nieśmiałość → lęk społeczny (cierpi w sytuacjach społecznych mimo chęci kontaktu) → SAD (zaburzenie). Granice oznaczone.

---

### Artykuł #4 — Gniew jako informacja

**Slug:** `gniew-regulacja-emocji-co-mowi`

**Hero** — `04-gniew-hero.webp`

*Prompt:* `Documentary photo: person standing alone in apartment hallway after argument (out of frame), pressing palm against wall, breathing visibly, expression of contained intensity not explosion, eyes downcast. Low warm hallway light. The moment between feeling and reaction. [+ suffix]`

**Inline graphic** — `04-piramida-gniewu.svg`: warstwy gniewu — powierzchowne (irytacja) → emocje pierwotne pod nim (lęk, smutek, krzywda, wyczerpanie). Ikony w warstwach.

---

### Artykuł #5 — People-pleasing

**Slug:** `people-pleasing-koszty-bycia-mily`

**Hero** — `05-people-pleasing-hero.webp`

*Prompt:* `Editorial photo: person at office desk smiling pleasantly while typing, but eyes show exhaustion not joy. Multiple sticky notes on monitor with "tasks for others", phone with messages waiting. Soft fluorescent office light. The disconnect between performed happiness and inner state. [+ suffix]`

**Inline graphic** — `05-cykl-people-pleasing.svg`: koło zachowań: zgoda → krótkotrwała ulga → narastający resentment → wyczerpanie → wybuch lub depresja → cykl wraca po próbie naprawy.

---

### Artykuł #6 — Granice psychologiczne

**Slug:** `granice-psychologiczne-w-praktyce`

**Hero** — `06-granice-hero.webp`

*Prompt:* `Editorial documentary photo: hand gently raised in "stop/wait" gesture in foreground, blurred figure of another person in soft focus background, calm not aggressive expression visible, warm wood interior. Communicating boundary without hostility. [+ suffix]`

**Inline graphic** — `06-typy-granic.svg`: 5 typów granic — fizyczne, emocjonalne, czasowe, materialne, intelektualne. Każdy z przykładem komunikatu.

---

### Artykuł #7 — Style przywiązania w dorosłości

**Slug:** `style-przywiazania-doroslosc-relacje`

**Hero** — `07-przywiazanie-hero.webp`

*Prompt:* `Editorial photo: couple sitting on park bench at golden hour, neither too close nor distant, one looking at other with quiet attention, second looking thoughtfully forward. Real connection without theatrical romance. [+ suffix]`

**Inline graphic** — `07-cztery-style-przywiazania.svg`: 4 style (bezpieczny, lękowo-ambiwalentny, unikający, zdezorganizowany) jako 2x2 matryca z osiami "lęk" i "unikanie", z opisami zachowań w każdej ćwiartce.

---

### Artykuł #8 — Efekt Dunninga-Krugera

**Slug:** `efekt-dunninga-krugera-niekompetencja`

**Hero** — `08-dunning-kruger-hero.webp`

*Prompt:* `Editorial photo: confident person in business meeting gesturing emphatically, two colleagues in background showing politely skeptical expressions, neutral conference room. Captures the gap between confidence and competence without mockery. [+ suffix]`

**Inline graphic** — `08-krzywa-dunninga.svg`: klasyczna krzywa Dunninga-Krugera (kompetencja na X, pewność siebie na Y) z punktami: "Mt. Stupid", "Valley of Despair", "Slope of Enlightenment", "Plateau of Sustainability".

---

### Artykuł #9 — Emocje w decyzjach (CORNERSTONE)

**Slug:** `emocje-w-podejmowaniu-decyzji-damasio`

**Hero** — `09-emocje-decyzje-hero.webp`

*Prompt:* `Conceptual editorial photo: person at fork in path (literal forest path or metaphorical urban junction at twilight), looking thoughtfully in two directions, hand on chest area suggesting body awareness, contemplative not anxious. Warm dusk light. [+ suffix]`

**Inline graphic** — `09-somatic-markers.svg`: model markerów somatycznych Damasio: bodziec → ciało (pobudzenie autonomiczne) → korowa interpretacja → decyzja. Ścieżka przez wyspę i korę przedczołową.

---

### Artykuł #10 — Toxic positivity (BOFU)

**Slug:** `toxic-positivity-kiedy-pozytywne-szkodzi`

**Hero** — `10-toxic-positivity-hero.webp`

*Prompt:* `Documentary photo: person crying quietly while looking at phone screen showing "It will all work out!" type message, half-empty cup nearby, soft daytime light through curtain. The hollow feeling of being told positivity instead of being heard. [+ suffix]`

**Inline graphic** — `10-zamiast-tego.svg`: tabela porównawcza — toxic positivity ("nie smucisz się") vs valid emotional support ("widzę, że ci ciężko"). 8 par sformułowań.

---

## Reguły użycia

- **Light mode default** (psychodzisiaj.pl jest "dziennym" odpowiednikiem psychosen.pl).
- **Akcent terracotta** rzadko — głównie dla "Dzisiaj" w wordmarku, uśmiechów w znakach, jednego CTA.
- **Hero z parami sylwetek** odzwierciedla relacyjny charakter domeny.
- **Animacja**: subtelne falowanie krzywej "uśmiechu" w hero przez CSS, ożywiając twarz.

## Skrypt batch OG

Ten sam wzorzec co dla zdrowie.fit — `generate_og_per_article.py` używa `og-default.svg` jako template, podstawia tytuły artykułów.
