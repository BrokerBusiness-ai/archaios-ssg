# jaksobieradzic.pl — pakiet design

Domena: strategie radzenia sobie w kryzysie życiowym (klaster NURIO, MOFU). Charakter: ciepły ale konkretny, dla osoby aktywnie szukającej pomocy w trudnym momencie. Nie poradnikowy. Empatyczny, kliniczny, oparty na dowodach.

## Tożsamość marki

**Nazwa:** Jak Sobie Radzić
**Tagline:** Strategie radzenia sobie w trudnych sytuacjach
**Pozycjonowanie:** Sprawdzone klinicznie techniki dla osób w kryzysach: żałobie, rozwodzie, utracie pracy, samotności, syndromie oszusta, opiece nad chorą osobą.

## Paleta kolorów

| Rola | HEX | Użycie |
|---|---|---|
| Primary (forest green) | `#2a7f62` | nagłówki, znak, CTA podstawowe |
| Primary dark | `#1d5c46` | hover, ramki, ciemniejsze tła |
| Primary light | `#6bbf9e` | tła sekcji |
| Accent (terracotta) | `#e08c4f` | "Radzić", stopnie drabiny, akcenty |
| Accent dark | `#c0703a` | hover na akcent |
| Trust (lavender) | `#8b7bb8` | linki źródeł, najwyższe stopnie drabiny (cel/spokój) |
| Background ivory | `#fdfcf9` | tło |
| Text primary | `#1d2a26` | nagłówki |
| Text body | `#4a4a4a` | akapity |
| Text muted | `#7a7a7a` | meta |

**Logika kolorów:** zielony forest = stabilność, ziemiste osadzenie. Terracotta = ciepło wsparcia, codzienność. Lavender = nadzieja, transcendencja, "tam dokąd zmierzamy".

## Typografia

**Heading:** Source Serif Pro (humanistyczny, czytelny)
**Body:** Inter

```css
--font-heading: 'Source Serif Pro', 'EB Garamond', Georgia, serif;
--font-body: 'Inter', system-ui, sans-serif;
```

## Asetty wizualne

`_design/`: `logo.svg` (drabina + wordmark), `favicon.svg` (drabina), `og-default.svg` (1200×630 z drabiną), `hero-illustration.svg` (postać wchodząca po szczeblach drabiny — symbol przejścia), `article-divider.svg` (3 stopnie różnokolorowe).

## Galeria artykułowa — 10 artykułów

### Konwencja stylu zdjęć

**Estetyka:** "documentary support photography" — autentyczne ludzkie momenty w kryzysie, ale bez voyeryzmu. Środowiska codzienne (mieszkania, parki, gabinety, kawiarnie), naturalne światło, prawdziwi ludzie różnego wieku, bez dramatyzacji.

**Paleta zdjęć:** ziemiste tony — terracotta, oliwka, kremowy, akcenty głębokiego zielonego. Wyklucz: nagrane słoneczne uśmiechy reklamowe, fluorescencyjne klisze "wszystko zaraz będzie dobrze", melodramat.

### Universal AI prompt suffix

```
... documentary support photography, natural daylight, real people in
quiet contemplative moments (not staged), European urban/home context,
warm earth palette (terracotta #e08c4f, forest green #2a7f62, ivory
#fdfcf9 with lavender #8b7bb8 accents), shallow depth of field,
respectful intimate scale, no theatrical drama, no fake smiles,
magazine-quality, 16:9 aspect ratio --ar 16:9 --style raw
```

Negative: `--no neon, fake smile, melodrama, plastic, instagram filter, hdr, beauty influencer, american suburb, oversaturated`

---

### Artykuł #1 — Żałoba (PILLAR)

**Slug:** `zaloba-fazy-trwanie-kiedy-szukac-pomocy`

**Hero (1200×675)** — `01-zaloba-hero.webp`

*Prompt:* `Editorial documentary photo: person sitting alone on edge of bed in soft morning light, hands clasped together, looking down quietly, photo of loved one barely visible on bedside table out of focus, no tears - just quiet contemplation. Real grief, not theatrical. [+ suffix]`

*Alt:* `Osoba siedząca cicho na łóżku w porannym świetle, ze zdjęciem bliskiej osoby na nocnej szafce — żałoba w codzienności`

**Inline graphic (SVG, 800×450)** — `01-zaloba-fazy-vs-zadania.svg`: porównanie modeli — Kübler-Ross (5 faz: zaprzeczenie/gniew/targowanie/depresja/akceptacja) vs Worden (4 zadania: uznanie straty / przeżycie bólu / adaptacja / przeniesienie więzi). Tabela.

---

### Artykuł #2 — Rozwód (psychologiczna mapa)

**Slug:** `rozwod-psychologiczna-mapa-przejscia`

**Hero** — `02-rozwod-hero.webp`

*Prompt:* `Documentary photo: empty side of king bed in morning light, single half-cup of coffee on bedside table, second pillow slightly disturbed, soft warm light through curtain. Symbol of transition without explicit drama. [+ suffix]`

**Inline graphic** — `02-rozwod-mapa-emocjonalna.svg`: oś czasu 24 miesięcy z krzywą emocjonalną — szok → ulga → smutek → gniew → akceptacja → integracja. Punkty kryzysowe w 6, 12, 18 miesiącu (typowe).

---

### Artykuł #3 — Utrata pracy

**Slug:** `utrata-pracy-kryzys-tozsamosci`

**Hero** — `03-utrata-pracy-hero.webp`

*Prompt:* `Editorial photo: person at home midday wearing comfortable but not pajamas clothes, looking at laptop with calm focus, half-empty cup of tea, papers around — NOT despair, but transition phase between identity, calm uncertainty. [+ suffix]`

**Inline graphic** — `03-faza-przejscia.svg`: 4-fazowy model Bridges'a: zakończenie → strefa neutralna → nowy początek + integracja. Każda faza z czasem, emocjami, zadaniami.

---

### Artykuł #4 — Lęk przed przyszłością

**Slug:** `lek-przed-przyszloscia-jak-zyc`

**Hero** — `04-lek-przyszlosc-hero.webp`

*Prompt:* `Conceptual photo: person standing on balcony at twilight, looking at distant horizon with calm uncertainty, mug of tea in hands, soft urban dusk light, not anxious face but contemplative. [+ suffix]`

**Inline graphic** — `04-pole-kontroli.svg`: trzy koncentryczne kręgi — kontrola, wpływ, zainteresowanie. Pomocne narzędzie redukcji lęku przed niekontrolowalnym.

---

### Artykuł #5 — Syndrom oszusta

**Slug:** `syndrom-oszusta-sukces-bez-radosci`

**Hero** — `05-syndrom-oszusta-hero.webp`

*Prompt:* `Documentary photo: person at office desk holding professional certificate or award, looking at it with strange dissociated expression — not pride, not sadness, just disconnect. Soft office light. [+ suffix]`

**Inline graphic** — `05-cykl-syndromu.svg`: pętla: nowe wyzwanie → lęk → over-prep → sukces → przypisanie szczęściu → ↑ pętla. Z wyjściami po linkach (terapia, walidacja, redefinicja sukcesu).

---

### Artykuł #6 — Wypalenie rodzicielskie

**Slug:** `wypalenie-rodzicielskie-ukryta-epidemia`

**Hero** — `06-wypalenie-rodzic-hero.webp`

*Prompt:* `Editorial photo: parent sitting on edge of children's bed late evening after putting kid to sleep, expression of exhaustion not joy, soft nightlight, scattered toys around — capturing the unspoken cost. [+ suffix]`

**Inline graphic** — `06-3-wymiary-wypalenia.svg`: 3 wymiary Maslach: wyczerpanie / cynizm wobec roli rodzica / poczucie niemożności. Skala PBA (Parental Burnout Assessment) Roskam.

---

### Artykuł #7 — Samotność

**Slug:** `samotnosc-od-izolacji-do-kontaktu`

**Hero** — `07-samotnosc-hero.webp`

*Prompt:* `Documentary photo: older woman at small apartment kitchen at evening, single setting at table, looking out window with dignity not despair, warm lamp light. Not stereotyped lonely senior — just quiet evening. [+ suffix]`

**Inline graphic** — `07-samotnosc-vs-izolacja.svg`: 2x2 matryca: subiektywna samotność (oś Y) × obiektywna izolacja (oś X). 4 ćwiartki: społecznie aktywny ale samotny / odosobniony bez cierpienia / w kontakcie i syty / izolacja + samotność.

---

### Artykuł #8 — Trudne rozmowy

**Slug:** `trudne-rozmowy-jak-mowic-czego-sie-boisz`

**Hero** — `08-trudne-rozmowy-hero.webp`

*Prompt:* `Editorial photo: two people sitting at small kitchen table, one mid-sentence with tense but non-aggressive expression, other listening attentively, soft afternoon light. Real moment of difficult conversation. [+ suffix]`

**Inline graphic** — `08-formula-trudnej-rozmowy.svg`: 5-step framework: kontekst → fakt → uczucie → potrzeba → prośba. Z przykładami.

---

### Artykuł #9 — Kryzys wartości w połowie życia (CORNERSTONE)

**Slug:** `kryzys-wartosci-polowa-zycia-nie-kryzys-wieku`

**Hero** — `09-kryzys-polowa-hero.webp`

*Prompt:* `Conceptual editorial photo: person mid-40s standing at window looking out, holding coffee, contemplative not anxious, surrounded by familiar life elements (books, family photos out of focus) — moment of internal review, not external crisis. [+ suffix]`

**Inline graphic** — `09-trzy-poziomy-wartosci.svg`: piramida wartości — głębokie (egzystencjalne) / pośrednie (relacyjne, zawodowe) / powierzchowne (cele zewnętrzne). Pytania do każdego poziomu.

---

### Artykuł #10 — Opieka nad osobą chorą (BOFU)

**Slug:** `opieka-nad-osoba-chora-jak-nie-zatracic-siebie`

**Hero** — `10-opieka-hero.webp`

*Prompt:* `Documentary photo: caregiver at home holding mug, looking through window at garden, expression of quiet strength mixed with weariness, no patient in frame. The moment between caring tasks. [+ suffix]`

**Inline graphic** — `10-cykl-opiekuna.svg`: cykl wyczerpania opiekuna + 5 punktów interwencji (respite care, grupy wsparcia, granice, terapia, profesjonalna pomoc).

---

## Reguły użycia

- **Light mode default** z opcjonalnym ciemnym (jaksobieradzic.pl jest "wschodem słońca po nocy" — paleta jasna, ale nie ostro biała).
- **CTA do nurio.pl** w 8/10 artykułów (charakter pomocowy idealnie pasuje do AI companion).
- **Telefon Zaufania 116 123** w stopce każdego artykułu w sekcji "kryzysowej" (samobójstwo, ciężka żałoba, rozwód z konfliktem) — to obowiązek etyczny.
- **Numery kryzysowe** w artykule #10: Opieka nad osobą chorą — telefon dla opiekunów, fundacje wsparcia.
- **Hero illustration**: drabina to centralny motyw - "kolejny krok" zawsze możliwy, mimo że trudny.

## Subtelne techniki przekierowania (krytyczne dla MOFU)

W jaksobieradzic.pl czytelnik jest *aktywnie* w trudnym momencie. CTA muszą być:

1. **Maksymalnie empatyczne** — *najpierw* uznanie trudności, *potem* możliwość pomocy.
2. **Bez frazy "kup/zarejestruj"** — zawsze "może być pierwszym krokiem", "może dać przestrzeń".
3. **Z numerem kryzysowym** ZAWSZE w sytuacji wyraźnego zagrożenia (samobójstwo, przemoc, akut).
4. **Frame pomocniczy** — narzędzie, nie zastępstwo bliskich/terapeuty.
5. **Specificity** — wymieniaj walidowane testy (BDI-II, PCL-5, Maslach, etc.) jako konkretne narzędzia diagnostyczne.

CTA do nurio.pl w tej domenie jest najbardziej naturalne — bo Nuria jest *zaprojektowana* dla osób w trudnych emocjach. Frame: "miejsce, gdzie można po cichu nazwać, co się dzieje, kiedy bliscy są nieobecni lub niewystarczający".
