# aidzisiaj.pl — prompty AI do zdjęć hero (10 artykułów)

Gotowy zestaw do **ChatGPT (DALL·E 3 / GPT-Image)**, **Midjourney v7 (2026)**, **fal.ai Flux Pro 1.1** lub **Imagen 4**. Każdy prompt unikalny, anti-cliché, dark cyber vibe spójny z resztą strony.

---

## Universal style suffix dla aidzisiaj.pl

**Skopiuj na końcu KAŻDEGO promptu hero:**

```
Style: cinematic editorial photography, dark moody atmosphere, premium
tech magazine aesthetic (think Wired x The Verge x MIT Technology Review).
Color palette: deep black #0a0a0a base, electric cyan #00d9ff highlights,
neon magenta #ff2d92 accent details, AI violet #a78bfa ambient glow.
Strong directional lighting, volumetric haze, subtle film grain,
high detail, shallow depth of field, magazine-quality composition.
No text overlays, no watermarks, no logos, no UI mockups.
16:9 aspect ratio, photorealistic with painterly mood.

Avoid: typical AI clichés (glowing brain, hand touching robot, neural
network spheres, binary code rain, blue gradient backgrounds, generic
robotic faces, holographic dashboards), stock photo aesthetic, cheesy
cyberpunk Tokyo, rainbow gradients, cartoonish 3D renders.
```

**Midjourney v7 parametry:**
```
--ar 16:9 --style raw --v 7 --s 250
```

**DALL·E 3 / GPT-Image (ChatGPT):** parametry niepotrzebne, proporcje wymuszaj w samym prompcie ("16:9 aspect ratio, wide landscape composition").

---

## Workflow

1. **Pierwszy wybór 2026:** ChatGPT z GPT-Image (najlepsza spójność stylu, dobra obsługa polskich kontekstów). 4 warianty, wybór 1.
2. **Backup:** Midjourney v7 (najwyższa jakość fotograficzna, --s 250 = artystyczna interpretacja).
3. **Po wygenerowaniu:**
   - zapisz jako `.webp` (`squoosh.app`, q=78, target ~180 KB)
   - dodatkowo `.jpg` fallback
   - nazwa: `<slug>-hero.webp`
4. **Wrzuć do:** `src/static/img/articles/`
5. **W CMS:** pole `image_url` = `/img/articles/<slug>-hero.webp` (build.py auto-generuje OG image z hero przez Pillow).

---

## Artykuł #1 — AI w polskim biznesie 2026 (PILLAR)

**Slug:** `ai-w-polskim-biznesie-2026-przewodnik`
**Plik:** `ai-w-polskim-biznesie-2026-hero.webp`
**Vibe:** strategiczna mapa decyzyjna dla zarządów, panorama polskiego biznesu w punkcie zwrotnym

### Prompt

```
Cinematic wide-angle aerial view of a modern Warsaw business district at
blue hour, photographed from a low-flying drone. Glass office towers in
the foreground (Warsaw Spire, Varso Tower silhouettes), dusty cyan
volumetric haze rolling between buildings. Above the skyline, faint
luminous network of magenta and cyan lines connecting building to
building like an invisible nervous system — barely visible, ambient,
not dominant. The city feels alive, computational, on the cusp of
transformation. Single warm window glow in one tower (one CEO making a
decision). Dark sky with subtle violet gradient. Polish twilight mood.

[+ universal suffix]
```

---

## Artykuł #2 — 12 use cases AI z ROI dla MŚP

**Slug:** `12-use-cases-ai-z-roi-dla-msp`
**Plik:** `12-use-cases-roi-hero.webp`
**Vibe:** macierz / portfolio decyzji, konkrety vs hype, ROI calculation

### Prompt

```
Cinematic close-up of a wooden conference table from above (top-down
shot, 30 degree tilt), illuminated by single dramatic overhead spotlight.
On the table: 12 small dark cards arranged in a 3x4 grid, each card
glowing with different intensity of cyan and magenta light from within,
suggesting different ROI levels. One card in the corner pulses bright
magenta (top performer), three cards barely glow (low ROI). A sleek
black pen rests beside the grid. Single ceramic espresso cup, half-empty,
casts long shadow. Polished concrete floor visible at edges, deep
shadows, executive decision-making atmosphere. No text on cards, just
luminous patterns.

[+ universal suffix]
```

---

## Artykuł #3 — Pierwszy projekt AI od zera do produkcji

**Slug:** `pierwszy-projekt-ai-od-zera-do-produkcji`
**Plik:** `pierwszy-projekt-ai-hero.webp`
**Vibe:** pierwsze kroki, droga, transformacja od pomysłu do działania

### Prompt

```
Cinematic side-profile shot of a single sneaker mid-step on a wet
asphalt path at twilight, captured ankle-level perspective, sharp focus
on the shoe. The path stretches forward into a dimly lit corridor lined
on both sides by translucent panels glowing softly with cyan and magenta
data patterns (like server racks reimagined as a runway). Each panel
slightly different — first ones simple grids, later ones complex
patterns — visualizing progression from idea to production. Volumetric
mist hovers above the path. The far end disappears into magenta glow
suggesting destination. Polish industrial architecture vibe (think
Praga district lofts), grounded in reality, not sci-fi.

[+ universal suffix]
```

---

## Artykuł #4 — Customer service z AI

**Slug:** `customer-service-z-ai-przyklady-wdrozen`
**Plik:** `customer-service-ai-hero.webp`
**Vibe:** ludzki kontakt + AI, dialog, support 24/7, empatyczna technologia

### Prompt

```
Cinematic medium shot of a young woman customer service agent (Slavic
features, mid-30s, professional but warm, no smile) wearing a wireless
headset, illuminated only by the cyan-magenta glow of multiple monitors
in front of her, faces obscured. The screens display abstract flowing
data streams (NOT text or UI mockups), suggesting incoming customer
queries being processed. Behind her: empty open-plan office at night,
deep shadows, single distant window. Her expression is focused,
attentive — listening. Subtle reflection of magenta highlight on her
glasses. Composition has cinematic 21:9 widescreen feel cropped to 16:9.
Real human warmth meeting machine speed.

[+ universal suffix]
```

---

## Artykuł #5 — AI w sprzedaży B2B (lead scoring)

**Slug:** `ai-w-sprzedazy-b2b-lead-scoring`
**Plik:** `ai-sprzedaz-b2b-hero.webp`
**Vibe:** segregacja, priorytetyzacja, scoring, hot vs cold leads

### Prompt

```
Cinematic close-up of dozens of small glass marbles scattered across a
dark marble desk, photographed at eye level with sharp tilt-shift effect.
Most marbles are dim, cool gray. A handful glow intensely — three or
four pulse hot magenta (qualified leads), several warmer cyan (warm
leads), the rest cold and dark. A single executive hand (man's wrist
with simple watch, no face) gently touches one of the magenta marbles.
Strong rim lighting from the left, deep shadows on the right.
Photographic feel like a chess close-up shot in National Geographic.
Conveys triage, prioritization, decision under data.

[+ universal suffix]
```

---

## Artykuł #6 — Automatyzacja backoffice z AI

**Slug:** `automatyzacja-backoffice-z-ai`
**Plik:** `automatyzacja-backoffice-hero.webp`
**Vibe:** dokumenty, papier → cyfra, biurokracja → przepływ

### Prompt

```
Cinematic wide shot of a dark office archive room at night, rows of
metal filing cabinets stretching into vanishing point. From one cabinet
drawer in the center, paper documents are mid-air, hovering, dissolving
into streams of cyan and magenta luminous particles that flow upward
and rightward, transforming into clean abstract data ribbons disappearing
into the ceiling. The transformation is precise, surgical, not chaotic.
Volumetric haze, single architectural spotlight on the dissolving
papers. Vintage filing cabinets contrast with the futuristic light flow
— old bureaucracy literally becoming new. Photographic, not 3D rendered.

[+ universal suffix]
```

---

## Artykuł #7 — ROI AI w polskiej firmie (CORNERSTONE)

**Slug:** `roi-ai-w-polskiej-firmie-jak-liczyc`
**Plik:** `roi-ai-cornerstone-hero.webp`
**Vibe:** kalkulacja, finanse, twarde liczby, mathematical precision

### Prompt

```
Cinematic top-down shot of an executive desk in deep shadow,
illuminated only by the cyan glow of a financial spreadsheet projection
floating just above the surface (like holographic display, but
photographic — slight blur, real reflection on glass desk). The
projection shows abstract bar charts and curves rising sharply, ROI
visualization, but no readable numbers. A vintage calculator (1980s
Casio aesthetic) sits beside, its display glowing magenta. A single
fountain pen across a leather notebook with dark cyan ink stain — old
math meeting new math. The composition feels weighty, decisive,
analytical. Shadow gradient from deep black to softer gray edges.
Wall Street Journal x Bloomberg Businessweek aesthetic.

[+ universal suffix]
```

---

## Artykuł #8 — AI w produkcji (predictive maintenance)

**Slug:** `ai-w-produkcji-predictive-maintenance`
**Plik:** `predictive-maintenance-hero.webp`
**Vibe:** fabryka, czujniki, maszyna z "intuicją", przewidywanie awarii

### Prompt

```
Cinematic medium shot of a single massive industrial machine (CNC mill
or production line component) in a dark factory hall, photographed at
3/4 angle with slight worm's-eye view to emphasize scale. The machine
itself is hyper-realistic, oily metal, scratched paint. Across its
surface, subtle constellations of tiny cyan sensor lights — clusters
suggesting a "neural map" of the machine. From one specific spot on the
machine, a faint magenta glow pulses outward (the predicted failure
point). Cold blue twilight from windows above, ambient violet haze in
the background. Industrial gravity, not sci-fi. Look feels like a
Werner Herzog documentary frame about modern industry.

[+ universal suffix]
```

---

## Artykuł #9 — Niebezpieczeństwa AI w biznesie (etyka, ryzyka)

**Slug:** `niebezpieczenstwa-ai-w-biznesie-etyka-ryzyka`
**Plik:** `etyka-ryzyka-ai-hero.webp`
**Vibe:** ostrzeżenie, ryzyko, ludzka kontrola vs autonomia AI

### Prompt

```
Cinematic high-contrast portrait shot from behind a single executive
chair (back of leather chair fills lower half of frame, occupant
unseen). The chair faces a vast dark window. In the window's reflection
(slightly distorted), a complex constellation of cyan and magenta data
patterns swirls — alive, autonomous, not human-controlled. The reflection
is too perfect, too fast, too organized — uncanny. A single hand grips
the chair's armrest, knuckles slightly tense. The room is empty
otherwise. Single dim desk lamp casts amber-orange counter-light (the
only warm color, suggesting human presence threatened). Atmospheric
tension, not horror. Like the opening shot of a thriller about
corporate AI gone wrong, before anything bad happens.

[+ universal suffix]
```

---

## Artykuł #10 — Audyt dojrzałości AI firmy (checklist, BOFU)

**Slug:** `audyt-dojrzalosci-ai-firmy-checklist`
**Plik:** `audyt-dojrzalosci-ai-hero.webp`
**Vibe:** ocena, dashboard, gauges, kompas dojrzałości

### Prompt

```
Cinematic close-up of a precision analog dashboard with five circular
gauges arranged horizontally, photographed at slight 15-degree tilt,
extreme shallow focus. Each gauge has a different needle position —
some at low (dim cyan glow), one at mid (bright magenta), one at near-
max (intense violet glow). The gauges are physical, aerospace-grade,
not digital — like a 1960s NASA control panel reimagined for AI
maturity assessment. Brushed metal housing, gentle reflections.
Background: deep dark surface with hints of architectural lines (like
edge of a polished granite executive desk). Atmosphere: precise,
measured, professional, not gimmicky. Hasselblad medium-format depth
of field. Conveys diagnostic rigor.

[+ universal suffix]
```

---

## Tips do generowania

1. **Po pierwszej generacji** — jeśli wynik jest za "stockowy", dodaj na początku promptu: `"Editorial cover photograph for premium tech publication, NOT stock photo, NOT corporate website hero, NOT generic AI illustration."`

2. **Jeśli DALL-E/ChatGPT odmawia** (czasem dla "executive in dark office"): podmień na `"single CEO silhouette"` lub przeformułuj. Etyka/Ryzyka prompt może wymagać 2-3 prób.

3. **Spójność per-strona:** wszystkie 10 hero powinny dzielić te same accent kolory + ten sam mood (dark editorial). Jeśli któryś wygenerowany wynik jest za jasny lub za kolorowy — odrzuć i regeneruj.

4. **Test przed deployem:** zestaw 10 obok siebie powinien wyglądać jak okładki spójnej serii w jednym czasopiśmie tech, NIE jak zbiór losowych stocków.

5. **Backup stockowy** (jak nic nie wyjdzie):
   - Unsplash: szukaj `editorial dark cyan magenta`, `cinematic warsaw business`, `industrial close-up moody`
   - Pexels: szukaj `tech editorial dark`
   - Czasem Unsplash + lekki tint w Photoshop daje lepszy efekt niż AI gen.

6. **Po wygenerowaniu obrazów** zostaje ostatni krok: wrzucenie ścieżek do bazy SQLite (pole `image_url` per artykuł). Mogę dorobić skrypt `update_hero_images.py` jak będziesz mieć pliki gotowe.
