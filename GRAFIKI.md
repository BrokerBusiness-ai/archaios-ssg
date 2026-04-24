# Grafiki dla Zdrowie.fit — prompty do ChatGPT (DALL-E 3)

> Gotowa lista 18 najważniejszych grafik dla strony i artykułów.
> Każdy prompt = jeden obraz. Wklejasz do ChatGPT, dostajesz grafikę, robisz crop.

## Jak używać

ChatGPT (DALL-E 3) generuje **tylko 1 obraz na prompt**, w jednym z 3 formatów:

| Format | Wymiary DALL-E | Kiedy |
|---|---|---|
| **Square** | 1024×1024 | ikony kategorii, post IG, zdjęcia autorów |
| **Landscape** (wide) | 1792×1024 | OG default, hero, featured artykułu, FB cover |
| **Portrait** (tall) | 1024×1792 | infografika, IG story, Pinterest pin |

**Flow roboczy:**
1. Wklej prompt do ChatGPT → dostaniesz grafikę w najbliższym formacie DALL-E
2. Pobierz → otwórz w Canva / Photoshop / squoosh.app
3. Crop + resize do docelowych wymiarów z kolumny "Target size"
4. Konwersja na WebP dla front-endu: `cwebp -q 85 plik.png -o plik.webp`
5. Wrzuć do `src/static/img/` w odpowiedni podfolder

**Design system (trzymaj spójność):**
- sage green `#4a7c59` (primary)
- terracotta `#d9724a` (accent)
- ivory `#fdfcf9` (background)
- **Zero tekstu na obrazach** — tytuły nakłada Pillow w `build.py`

---

## A. Site-wide (6 grafik)

### 1. OG default — `src/static/img/og-default.png`
**Format:** landscape · **Target size:** 1200×630

```
Minimalist hero illustration for a Polish holistic health & fitness blog.
Abstract composition: a soft sage green (#4a7c59) organic curve blending into
a warm terracotta (#d9724a) circle, on ivory background (#fdfcf9).
Subtle botanical line-art (leaf, wave). Flat design, clean, editorial style.
No text. Centered composition with breathing space on the left third for title
overlay. Soft grain texture. Modern Nordic minimalism. Format: wide landscape.
```

---

### 2. Logo — `src/static/img/logo.png`
**Format:** square · **Target size:** 512×512 (PNG + SVG)

```
Minimalist monogram logo combining a stylized human silhouette with a half-moon
shape symbolizing body-mind harmony. Sage green (#4a7c59) primary color,
terracotta (#d9724a) accent. Flat geometric design, rounded strokes, no gradients,
no text. Professional wellness brand aesthetic. Centered on transparent or ivory
background. Clean padding around the mark. Format: square.
```

---

### 3. Hero homepage — `src/static/img/hero-home.webp`
**Format:** landscape · **Target size:** 1920×960

```
Wide cinematic editorial illustration for a wellness blog homepage. Two figures
(one female, one male) in yoga or meditation pose, simplified flat style, sage
green (#4a7c59) and terracotta (#d9724a) palette on ivory (#fdfcf9) background.
Natural elements around them: eucalyptus leaves, smooth stones, a warm sun.
Calm, scientific-yet-warm mood. Left third of the composition empty for
headline text overlay. No text. Pastel shadows, soft natural light.
Format: wide landscape.
```

---

### 4. Sekcja "O projekcie" — `src/static/img/about-section.webp`
**Format:** landscape · **Target size:** 1200×800

```
Editorial flat illustration, top-down view of a wooden desk. On the desk:
an open notebook, a steaming cup of herbal tea, a stethoscope, fresh eucalyptus
leaves, and a pair of running shoes. Palette: sage green (#4a7c59), terracotta
(#d9724a), ivory (#fdfcf9). Scientific and wellness atmosphere combined.
Warm soft shadows. No text. Format: landscape.
```

---

### 5. Strona 404 / empty state — `src/static/img/404.webp`
**Format:** landscape · **Target size:** 1200×800

```
Friendly minimalist illustration of a lost winding path through abstract leaves
and smooth stones, with a tiny compass in the center. Sage green (#4a7c59)
and terracotta (#d9724a) palette, ivory (#fdfcf9) background. Hopeful,
reassuring mood. Flat editorial style. No text. Format: landscape.
```

---

### 6. Tło sekcji newsletter — `src/static/img/newsletter-bg.webp`
**Format:** landscape · **Target size:** 1920×600 (user crop)

```
Very subtle abstract decorative banner: overlapping translucent sage green
(#4a7c59) and terracotta (#d9724a) circles on ivory (#fdfcf9) background,
with delicate botanical line-art crossing horizontally. Purely decorative
background — will be overlaid with a form in the center. No focal point.
Low saturation, plenty of negative space. No text. Format: wide landscape.
```

---

## B. Ikony kategorii (5 szt.) · `src/static/img/categories/`

Wszystkie w stylu: **flat icon, single-line illustration, sage green + terracotta accent, ivory background, circular framed composition**. Format: **square** · Target size: 400×400.

### 7. Zdrowie psychiczne — `categories/psychika.webp`

```
Flat minimalist icon: simplified human head silhouette in profile with a small
plant growing inside from the brain area. Sage green (#4a7c59) strokes,
terracotta (#d9724a) leaves, ivory (#fdfcf9) background. Circular framed
composition, consistent stroke weight. No text. Format: square.
```

### 8. Ruch / aktywność fizyczna — `categories/ruch.webp`

```
Flat minimalist icon: simplified running human silhouette with motion lines
flowing behind. Sage green (#4a7c59) strokes, terracotta (#d9724a) accent on
shoes. Ivory (#fdfcf9) background. Circular framed composition, consistent
stroke weight. No text. Format: square.
```

### 9. Odżywianie — `categories/odzywianie.webp`

```
Flat minimalist icon: bowl seen from top-down view with abstract vegetables,
leafy greens, and one avocado half inside. Sage green (#4a7c59) strokes,
terracotta (#d9724a) bowl. Ivory (#fdfcf9) background. Circular framed
composition, consistent stroke weight. No text. Format: square.
```

### 10. Sen / regeneracja — `categories/sen.webp`

```
Flat minimalist icon: crescent moon with a small sprig of leaves underneath
and two tiny stars. Sage green (#4a7c59) moon and stars, terracotta (#d9724a)
leaves. Ivory (#fdfcf9) background. Circular framed composition, consistent
stroke weight. No text. Format: square.
```

### 11. Profilaktyka / zdrowie prewencyjne — `categories/profilaktyka.webp`

```
Flat minimalist icon: a rounded shield with a heart shape inside and a subtle
stethoscope curve wrapping around. Sage green (#4a7c59) shield outline,
terracotta (#d9724a) heart. Ivory (#fdfcf9) background. Circular framed
composition, consistent stroke weight. No text. Format: square.
```

---

## C. Artykuły (szablony — podmień `{TEMAT}` w prompcie)

### 12. Featured image artykułu — `src/static/img/articles/{slug}.webp`
**Format:** landscape · **Target size:** 1600×900

```
Editorial flat illustration for a Polish wellness blog article about {TEMAT}.
Conceptual composition visualizing the topic metaphorically rather than
literally. Palette: sage green (#4a7c59) and terracotta (#d9724a) on ivory
(#fdfcf9) background. Soft natural elements (leaves, water droplets, smooth
stones) as decorative accents. Clean, scientific yet approachable mood.
Centered composition with breathing space. Subtle grain texture. No text,
no logos, no watermarks. Format: wide landscape.
```

**Przykład podstawienia** — artykuł "Jak ruch wpływa na nastrój":

```
Editorial flat illustration for a Polish wellness blog article about how
physical movement affects mood. Conceptual composition: a running silhouette
blending into a rising sun made of abstract dopamine molecules floating in
the air. Palette: sage green (#4a7c59) and terracotta (#d9724a) on ivory
(#fdfcf9) background. Soft natural elements as decorative accents. Clean,
scientific yet approachable mood. Subtle grain texture. No text. Format:
wide landscape.
```

---

### 13. Infografika pionowa (Pinterest) — `src/static/img/articles/{slug}-infographic.webp`
**Format:** portrait · **Target size:** 1000×1500

```
Vertical infographic illustration for an article about {TEMAT}. Three
horizontal sections stacked vertically, each section with one symbolic flat
icon (sage green #4a7c59 and terracotta #d9724a accents on ivory #fdfcf9).
Sections connected by thin dotted lines. Clear empty space between sections
for text to be added later in post-production. Pinterest-ready aesthetic.
No text. Format: tall portrait.
```

---

### 14. Ilustracja inline (środek artykułu) — `src/static/img/articles/{slug}-inline.webp`
**Format:** landscape · **Target size:** 800×450

```
Small supporting inline illustration for a wellness blog article about
{TEMAT}, specifically visualizing the concept of {SUBTEMAT}. Minimalist flat
style, single focal concept, sage green (#4a7c59) and terracotta (#d9724a)
palette on ivory (#fdfcf9) background. Clean and unobtrusive — decorative
support for text. No text. Format: landscape.
```

---

## D. Autorzy · `src/static/img/authors/`

### 15. Portret autora (ilustrowany) — `authors/{slug}.webp`
**Format:** square · **Target size:** 600×600

```
Stylized flat illustrated portrait of a person, head and shoulders, for a
wellness blog author page. Warm and professional expression, looking slightly
off-camera. Sage green (#4a7c59) and terracotta (#d9724a) palette with soft
warm skin tones, on ivory (#fdfcf9) background. Circular-crop-friendly
composition with mark centered. Editorial illustration style similar to
The New Yorker magazine. No text. Format: square.
```

### 15b. Wariant — prawdziwe zdjęcie autora
**Format:** square · **Target size:** 600×600

```
Professional headshot photograph of a person in their 30s-40s, natural daylight,
warm and confident smile, looking directly at camera. Soft neutral background
in warm beige or sage green tones. Medium shot: head and shoulders. Shallow
depth of field. Editorial wellness and health publication style. Natural,
authentic, approachable. Format: square.
```

---

## E. Social media · `src/static/img/social/`

### 16. Facebook cover — `social/fb-cover.png`
**Format:** landscape · **Target size:** 820×312

```
Horizontal banner for a Facebook page cover. Minimalist composition: an abstract
sage green (#4a7c59) wavy shape on the left side, a terracotta (#d9724a) circle
on the right side, ivory (#fdfcf9) background throughout. Generous safe-zone
of negative space in the center (where the profile picture will overlay).
Modern wellness brand aesthetic. No text. Format: wide landscape.
```

---

### 17. Instagram post template — `social/ig-post-template.png`
**Format:** square · **Target size:** 1080×1080

```
Instagram post background template. Soft vertical gradient from ivory (#fdfcf9)
at the top to very pale sage green (lightened #4a7c59) at the bottom.
Decorative botanical line-art (eucalyptus branches) in two opposite corners,
very subtle, low opacity. Large empty area in the center for a quote or title
text overlay added later. Minimal, editorial, Pinterest aesthetic. No text.
Format: square.
```

---

### 18. Instagram Story / Pinterest pin — `social/ig-story-template.png`
**Format:** portrait · **Target size:** 1080×1920

```
Vertical 9:16 template for Instagram Story or Pinterest Pin. Ivory (#fdfcf9)
background with a single organic terracotta (#d9724a) blob shape in the upper
third and a sage green (#4a7c59) curved line dividing the composition at the
two-thirds height mark. Generous breathing space for title and CTA text
overlay to be added later. Clean modern wellness aesthetic. No text.
Format: tall portrait.
```

---

## Workflow: jak zrobić wszystkie 18 w 1 sesji (30–45 min)

1. **Utwórz strukturę folderów:**
   ```bash
   cd C:/MEV-1/zdrowie-fit-generator
   mkdir -p src/static/img/{og,categories,articles,authors,social}
   ```

2. **Otwórz nową rozmowę w ChatGPT** (model GPT-4o / GPT-5 z image gen).

3. **Generuj po 3–4 prompty naraz** — ChatGPT zrobi po kolei, nie naraz (limit). Po każdej partii pobierz wszystko.

4. **Konwersja i crop** w Canva / squoosh.app:
   - square 1024×1024 → downscale do docelowego (400, 512, 600, 1080)
   - landscape 1792×1024 → crop do 16:9 (1920×1080, 1600×900, 1200×675, 820×312)
   - portrait 1024×1792 → crop do 9:16 (1080×1920, 1000×1500)

5. **Batch-konwersja do WebP** (dla front-endu, oprócz OG):
   ```bash
   cd src/static/img
   for f in $(find . -name "*.png" -not -name "og-default*"); do
     cwebp -q 85 "$f" -o "${f%.png}.webp"
   done
   ```

6. **Podepnij w templates** — ścieżki `/img/categories/psychika.webp` itd. już są w kodzie (model Category ma pole `icon`). Uzupełnij w admin panelu albo bezpośrednio SQL.

7. **Rebuild + deploy:**
   ```bash
   python build.py --clean
   git add src/static/img/ && git commit -m "chore: add wellness graphic set"
   git push  # GitHub Actions wyśle przez SFTP
   ```

---

## Uwagi końcowe

- **Ten sam zestaw dla satelit** — podmieniasz tylko paletę w każdym prompcie (np. dla archaios: `#0F1B2D` background, `#00B4D8` accent, reszta stylistyki bez zmian).
- **DALL-E nie trzyma perfekcyjnej spójności** między generacjami — jeśli chcesz identyczny styl dla 5 ikon kategorii, wygeneruj je w **jednej rozmowie**, dodając "in the same style as the previous icon".
- **Jeśli coś wyjdzie nie tak** — ChatGPT przyjmuje poprawki typu "zrób jaśniejsze tło" albo "usuń ten element". Nie trzeba od zera.
- **Alternatywa dla DALL-E:** Midjourney (`--style raw --ar 16:9`), Flux, Leonardo — lepsze kontrolowanie stylu, ale płatne subskrypcje.
