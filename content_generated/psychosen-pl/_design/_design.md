# psychosen.pl — pakiet design

Zestaw assetów wizualnych dla `psychosen.pl` (klaster NURIO, sub-temat: nauka o śnie, chronobiologia, zaburzenia snu).

## Tożsamość marki

**Nazwa:** PsychoSen
**Tagline:** Nauka o śnie — jak spać lepiej i zdrowiej
**Pozycjonowanie:** Specjalistyczna nisza wokół snu i chronobiologii, ton spokojny i wieczorny
**Charakter wizualny:** noc, kontemplacja, science magazine z nutą poezji — nie new age, nie wellness pop

## Paleta kolorów (dark mode default)

| Rola | HEX | Użycie |
|---|---|---|
| Primary (głęboki granat) | `#2d3a7c` | nagłówki, linki, wnętrze CTA |
| Primary dark | `#1e2854` | tła kart, footer, znak |
| Primary light | `#6a7bc4` | hover, akcenty drugorzędne |
| Accent (złoto-musztardowe) | `#d4a843` | ".Sen" w wordmarku, księżyc, akcenty |
| Accent dark | `#b58b36` | hover na akcent |
| Trust (jasny niebieski) | `#6b9fd4` | linki do źródeł, drobne gwiazdy |
| Background dark | `#0a1130` | tło strony (dark mode) |
| Background medium | `#1e2854` | sekcje |
| Text primary (silver) | `#e8ecf4` | nagłówki, czytelny tekst |
| Text body | `#c0c8d0` | akapity |
| Text muted | `#8a96b0` | meta, daty, autor |

**Logika kolorów:** granat = noc, sen, głębia. Złoto = księżyc, świadomość mimo snu (lucid dreaming, REM). Srebro = gwiazdy, dystans poznawczy.

## Typografia

**Heading:** Cormorant Garamond (humanistyczny serif z italic) — ton kontemplacyjny, czytelny w dark mode
**Body:** Inter (jak w zdrowie.fit, dla spójności inżynieryjnej)

```css
--font-heading: 'Cormorant Garamond', 'EB Garamond', Georgia, 'Times New Roman', serif;
--font-body: 'Inter', system-ui, sans-serif;
```

Italic w nagłówkach H1/H2 dla wyróżnień (np. ".Sen" w logo, akcenty słowne).

## Asetty wizualne

Pliki w `_design/`:
- `logo.svg` — pełny lockup (znak księżyca + wordmark)
- `favicon.svg` — sam księżyc na granatowym kwadracie
- `og-default.svg` — 1200×630 z wielkim księżycem i gwiezdnym tłem
- `hero-illustration.svg` — śpiąca osoba pod gwiazdami i księżycem
- `article-divider.svg` — separator z mini-księżycem

## Galeria artykułowa — zdjęcia i grafiki dla 10 artykułów

### Konwencja stylu wizualnego dla psychosen.pl

Wszystkie zdjęcia muszą trzymać estetykę **"contemplative night photography / clinical neuroscience"**:
- **Paleta zdjęć:** dominanta granat-noc-srebro, akcenty ciepłe (świeca, bedside lamp, księżyc).
- **Światło:** miękkie, nocne, low-key. Cienie głębokie, brak fluorescencji. Naturalne źródła (świeca, lampa nocna, księżyc).
- **Ludzie:** zawsze w pozycji odpoczynku/snu, twarze odprężone, brak pozowania, brak make-upu reklamowego.
- **Format:** `.webp` (główny) + `.jpg` (fallback). SVG dla diagramów (wykresy hipnogramów, chronotypów, faz snu).
- **Wyklucz:** stockowe modelki w pidżamach z perfekcyjnym uśmiechem, fluorescencyjne sypialnie, sleep masks z napisami "BEAUTY SLEEP".

### Universal AI prompt suffix dla psychosen.pl

```
... contemplative night photography style, low-key lighting, deep navy
and silver palette with warm gold accents (#d4a843), shallow depth of
field, cinematic composition, magazine-quality, no text overlays, no
watermarks, 16:9 aspect ratio --ar 16:9 --style raw
```

Negative prompt: `--no neon, oversaturated, fake smile, plastic, instagram filter, hdr, daylight bedroom, perfect makeup, text, watermark, logo, beauty influencer`

---

### Artykuł #1 — Chronotypy: skowronki, sowy, kolibry (PILLAR)

**Slug:** `chronotypy-skowronki-sowy-kolibry`

**Hero (1200×675)** — `01-chronotypy-hero.webp`

*Prompt:* `Editorial split photograph: left half showing person walking energetically at sunrise through misty forest path (cool morning light, blue/lavender tones), right half showing same kind of person reading at midnight by warm desk lamp in dark room (warm amber tones). Both calm, focused, neither tired nor wired. Magazine-cover quality, contemplative, balanced. [+ suffix]`

*Stock alt:* Unsplash `early morning runner mist`, `late night reading lamp`. Łączyć dwa zdjęcia w grafiku.

*Alt text:* `Dwie osoby w naturalnych dla siebie porach: skowronek o świcie i sowa o północy — chronotypy w obrazie`

**Inline graphic (SVG, 800×450)** — `01-chronotypy-curve.svg`

Krzywa rozkładu chronotypów w populacji (~25% poranni / ~50% pośredni / ~25% wieczorni). Trzy strefy w kolorach: poranni granatowy, pośredni srebrny, wieczorni złoty. Etykiety z procentami i przybliżonymi godzinami pików aktywności.

---

### Artykuł #2 — Bezsenność: pierwotna vs wtórna

**Slug:** `bezsennosc-pierwotna-wtorna`

**Hero (1200×675)** — `02-bezsennosc-hero.webp`

*Prompt:* `Editorial photograph: person lying awake in bed at 3 AM, only the dim glow of a phone screen illuminating face from below, expression of frustrated exhaustion not theatrical, dark blue bedroom, alarm clock visible showing late hour, blanket twisted. Authentic insomnia photography, not a lifestyle pose. [+ suffix]`

*Alt text:* `Osoba leżąca bezsennie w łóżku o trzeciej w nocy — autentyczny obraz bezsenności`

**Inline graphic (SVG, 700×400)** — `02-bezsennosc-decision-tree.svg`

Drzewo decyzyjne: czy bezsenność trwa <3 mies (ostra) / ≥3 mies (przewlekła) → kolejne pytania (czy z innym schorzeniem? czy z lekami?) → kategorie: pierwotna idiopatyczna / paradoksalna / wtórna do depresji / OSA / leków.

---

### Artykuł #3 — CBTI: gold standard leczenia bezsenności

**Slug:** `cbti-terapia-poznawczo-behawioralna-bezsennosci`

**Hero (1200×675)** — `03-cbti-hero.webp`

*Prompt:* `Documentary photograph: cozy therapy room at evening hour, one armchair occupied by person mid-conversation (visible from behind only), warm amber lamp, sleep diary on small table, calendar on wall with sleep tracking marks, framed art subtle. Therapeutic mood, not corporate. [+ suffix]`

*Alt text:* `Gabinet terapeutyczny wieczorem z zapisem snu na stole — terapia CBT-I w praktyce`

**Inline graphic (SVG, 800×500)** — `03-cbti-techniki.svg`

Pięć kafelków: Sleep Restriction / Stimulus Control / Cognitive Restructuring / Relaxation / Sleep Hygiene. Każdy z ikoną i krótkim opisem mechanizmu.

---

### Artykuł #4 — Melatonina: co naprawdę robi

**Slug:** `melatonina-co-robi-blędy-w-dawkowaniu`

**Hero (1200×675)** — `04-melatonina-hero.webp`

*Prompt:* `Macro photograph: small amber pharmacy bottle of melatonin tablets next to a fresh sprig of montmorency cherry on dark slate surface, single moonbeam-like light from above, scientific yet poetic, very minimal composition. Editorial science photography. [+ suffix]`

*Alt text:* `Buteleczka melatoniny i wiśnia montmorency w świetle księżyca — melatonina w nauce i naturze`

**Inline graphic (SVG, 800×400)** — `04-melatonina-rhythm.svg`

Wykres: krzywa endogennej melatoniny w ciągu 24h (peak ok 2–4 nad ranem). Naniesione: optymalne okno suplementacji 30–90 min przed snem (mała dawka 0,3 mg). Wskazane "blue light suppression" zone wieczorem.

---

### Artykuł #5 — Sen a konsolidacja pamięci

**Slug:** `sen-a-pamiec-konsolidacja-rem-nrem`

**Hero (1200×675)** — `05-sen-pamiec-hero.webp`

*Prompt:* `Conceptual editorial photograph: open book lying on pillow, soft moonlight illuminating pages, ghostly translucent overlay of brain neural network pattern projected onto book and pillow, dark mood, single bedside lamp creating warm halo. Like a National Geographic cover on neuroscience. [+ suffix]`

*Alt text:* `Otwarta książka na poduszce w nocnym świetle z subtelną siatką połączeń neuronalnych — sen jako konsolidacja pamięci`

**Inline graphic (SVG, 900×450)** — `05-hipnogram.svg`

Hipnogram nocy: 8h, oś Y = stadium snu (Awake / REM / N1 / N2 / N3), oś X = czas. Pokazane cykle 90-min, dominacja NREM3 w pierwszej połowie nocy, REM przedłużający się rano. Etykiety: "konsolidacja proceduralna" w REM, "konsolidacja deklaratywna" w NREM.

---

### Artykuł #6 — Niebieskie światło: prawda o blue light

**Slug:** `niebieskie-swiatlo-ekrany-przed-snem`

**Hero (1200×675)** — `06-blue-light-hero.webp`

*Prompt:* `Cinematic close-up: face of person illuminated only by cold blue glow of smartphone screen in dark bedroom, eyes slightly squinted, expression neutral not negative, ambient room dark navy, very shallow DOF on the eyes. Documentary mood, no judgment. [+ suffix]`

*Alt text:* `Twarz osoby w niebieskim świetle ekranu telefonu w zaciemnionym pokoju nocnym`

**Inline graphic (SVG, 800×450)** — `06-spektrum-swiatla.svg`

Wykres widma światła: porównanie spektrum LED (pik niebieski 460nm) vs żarówka tradycyjna (ciepły) vs świeca. Naniesiona krzywa wrażliwości fotoreceptorów ipRGC (czułych na niebieski) i ich wpływ na supresję melatoniny.

---

### Artykuł #7 — Polifazowy sen: dlaczego nie działa

**Slug:** `sen-polifazowy-uberman-dlaczego-nie-dziala`

**Hero (1200×675)** — `07-polifazowy-hero.webp`

*Prompt:* `Editorial photograph: cluttered desk at 4 AM with multiple alarm clocks set to different times, half-empty cups of coffee, scattered papers, small couch pillow indicating attempted nap, single dim lamp, person not visible (chair empty), atmosphere of unsustainable schedule. Anti-biohacking aesthetic. [+ suffix]`

*Alt text:* `Biurko o czwartej rano z wieloma budzikami i pustymi kubkami kawy — porażka snu polifazowego`

**Inline graphic (SVG, 800×400)** — `07-polifazowy-vs-monofazowy.svg`

Porównanie: cykl monofazowy 8h (jeden blok snu, prawidłowe REM/NREM) vs Uberman (6×20min drzemki — fragmentaryczne, bez głębokiego SWS). Czerwona flaga przy Uberman: "brak SWS".

---

### Artykuł #8 — Po co śnimy: neurobiologia snów

**Slug:** `po-co-snimy-neurobiologia-snow`

**Hero (1200×675)** — `08-sny-hero.webp`

*Prompt:* `Surreal editorial photograph: silhouette of sleeping person seen from above, with translucent dreamlike imagery rising from head area — abstract shapes, soft color washes, partial faces and landscapes barely visible, like a Magritte painting in photography. Dark navy background. Mysterious, contemplative. [+ suffix]`

*Alt text:* `Sylwetka śpiącej osoby z onirycznymi obrazami unoszącymi się nad głową — neurobiologia snów`

**Inline graphic (SVG, 800×450)** — `08-aktywacja-rem.svg`

Mapa aktywacji mózgu w fazie REM: ciało migdałowate (silnie aktywne, emocje), kora wzrokowa (aktywna mimo zamkniętych oczu), kora przedczołowa (wyciszona = brak racjonalnej kontroli). Strzałka do kategorii snów.

---

### Artykuł #9 — Sen a depresja (CORNERSTONE)

**Slug:** `sen-a-depresja-dwukierunkowa-relacja`

**Hero (1200×675)** — `09-sen-depresja-hero.webp`

*Prompt:* `Diptych editorial photograph: left side person curled in bed in dim morning light, blanket pulled up, face partially visible showing exhaustion not despair; right side same person at therapist office, soft lamp light, talking with mild relief on face. Subtle hope without sentimentality. [+ suffix]`

*Alt text:* `Dwa obrazy: osoba wyczerpana w łóżku rano i ta sama osoba w gabinecie terapeuty — sen, depresja, wyjście`

**Inline graphic (SVG, 800×500)** — `09-petla-sen-depresja.svg`

Pętla przyczynowa: zaburzony sen → wzrost cytokin prozapalnych → spadek BDNF → objawy depresyjne → dalsze zaburzenia snu. Każda strzałka opatrzona konkretnym mediator. Punkty interwencji oznaczone.

---

### Artykuł #10 — Higiena snu evidence-based (BOFU)

**Slug:** `higiena-snu-evidence-based-12-zasad`

**Hero (1200×675)** — `10-higiena-snu-hero.webp`

*Prompt:* `Top-down flat lay photograph: minimal bedside table with elements of perfect sleep hygiene — closed book (paper, no screen), warm low lamp, glass of water, simple analog alarm clock at 22:00, herbal tea cup, soft linen napkin, all in warm amber/dark blue palette. Magazine quality, no clutter. [+ suffix]`

*Alt text:* `Przy łóżku: książka, ciepła lampka, herbata ziołowa, analogowy budzik — elementy zdrowej higieny snu`

**Inline graphic (tabela SVG, 900×600)** — `10-12-zasad-higieny-snu.svg`

Lista 12 zasad z poziomem dowodów dla każdej (RCT/meta / kohortowe / mechanistyczne): stała pora wstawania, pokój 18–19°C, zaciemnienie, brak ekranów 60 min przed snem, kofeina <14:00, alkohol max 2×/tydzień, ekspozycja na światło dzienne rano, drzemka <30 min do 15:00, ruch fizyczny >5h przed snem, lekka kolacja, brak jedzenia 3h przed snem, sleep restriction therapy w razie bezsenności.

---

## Skrypt batch generowania OG per artykuł

Ten sam wzorzec co dla zdrowie.fit (`generate_og_per_article.py`). Skopiowany do `psychosen-pl/_design/`, używa tego `og-default.svg` jako template.

## Reguły użycia

1. **Dark mode default** dla psychosen.pl — strona ma `<html class="dark">` na starcie. Light mode jest opcjonalny dla użytkowników z silną preferencją (toggle w nagłówku).
2. **Logo na ciemnym tle** zachowuje pełną czytelność dzięki granatowemu tłu znaku. Wersja na białym — odwrócić tła znaku na #f4f1ea.
3. **Akcent złoty** rzadko — tylko ".Sen" w wordmarku, księżyc, jeden CTA. Nie powielać.
4. **Hero illustration animacja:** subtelne migotanie gwiazd przez CSS `@keyframes twinkle { 50% { opacity: 0.3 } }` z różnym `animation-delay`.
5. **Body text** w kolorze `#c0c8d0` (silver) — nie czysta biel, nie męczy oczu nocą.

## Integracja z `src/templates/base.html`

Per domena, dynamicznie z domain YAML. Dla psychosen.pl:

```html
<html lang="pl" class="dark">
<head>
  <link rel="icon" type="image/svg+xml" href="/static/img/favicon.svg">
  <meta property="og:image" content="{{ SITE_URL }}/static/img/og-default.png">
  <meta name="theme-color" content="#0a1130">
</head>
```

CSS zmienne dla dark mode:

```css
:root.dark {
  --bg: #0a1130;
  --bg-card: #1e2854;
  --text-primary: #e8ecf4;
  --text-body: #c0c8d0;
  --text-muted: #8a96b0;
  --accent: #d4a843;
  --primary: #2d3a7c;
  --primary-light: #6a7bc4;
  --trust: #6b9fd4;
}
```
