# PROMPT WYKONAWCZY — Implementacja strategii klastra Psychologia w Archaios SSG

> **Jak użyć**: Wklej CAŁĄ zawartość tego promptu do Claude Code (lub DeepSeek Code).
> Potem wklej plik `STRATEGIA_KLASTER_PSYCHOLOGIA.md` jako kontekst.
> Code przeczyta strategię i zaimplementuje wszystkie zmiany w jednym przebiegu.

---

## PROMPT DO WKLEJENIA:

```
Przeczytaj dokument STRATEGIA_KLASTER_PSYCHOLOGIA.md (wklejony poniżej) i zaimplementuj 5 brakujących feature'ów w silniku Archaios SSG. Projekt jest w bieżącym katalogu roboczym.

WAŻNE: Nie ruszaj istniejącego kodu, który już działa. Dodawaj nowe feature'y bez łamania kompatybilności wstecznej. Wszystkie zmiany muszą być warunkowe ({% if %}, opcjonalne pola).

## KONTEKST TECHNICZNY

- Generator: build.py (Jinja2 + Pillow, multi-domain)
- Szablony: src/templates/ (base.html, article.html, _article_card.html, _product_cta.html)
- CSS: src/static/css/style.css (vanilla CSS, zmienne CSS w :root)
- JS: src/static/js/main.js (vanilla JS, IIFE pattern)
- Domeny: domains/*.yaml (config per domena, ładowane przez domain_config.py)
- Model Article: title, slug, excerpt, content, category_id, author_id, tags, reading_time, bibliography, is_published, is_featured
- Theme system: domains/YAML.theme → domain_config.py:get_full_css_variables() → css/domain-colors.css

## ZADANIE 1: Dark mode per domena (psychosen.pl)

Strategia wymaga: psychosen.pl domyślnie w dark mode ("Dark mode default — strona domyślnie w ciemnym motywie").

1. W `src/templates/base.html`:
   - Na tagu `<html>` dodaj warunek: `class="{% if theme.dark_mode %}dark-auto{% endif %}"` 
   - W `<head>` dodaj: `{% if theme.dark_mode %}<meta name="color-scheme" content="dark light">{% else %}<meta name="color-scheme" content="light dark">{% endif %}`

2. W `src/static/css/style.css`:
   - Znajdź istniejący blok `@media (prefers-color-scheme: dark) { :root.dark-auto {` 
   - Dodaj DRUGI blok tuż pod nim, który wymusza dark niezależnie od preferencji systemu:
   ```css
   :root.dark-auto {
       --color-bg: #1a1815;
       --color-bg-alt: #232019;
       --color-surface: #2d2a23;
       --color-text: #e8e1d4;
       --color-text-muted: #a8a195;
       --color-text-light: #8a857d;
       --color-ink: #f6f0e6;
       --color-border: #3d3a33;
       --color-border-strong: #4d4a43;
   }
   ```

3. W `build.py` funkcja `make_env()` lub tam gdzie tworzysz kontekst Jinja2:
   - Upewnij się, że `theme` dict z CONFIG trafia do kontekstu szablonu.
   - Jeśli już tam jest — OK. Jeśli nie, dodaj: `"theme": CONFIG.get("theme", {})`

4. W `domains/psychosen-pl.yaml` dodaj:
   ```yaml
   theme:
     dark_mode: true
   ```

## ZADANIE 2: Sticky CTA po 60% scroll

Strategia wymaga: "po przescrollowaniu 60% artykułu pojawia się delikatny pasek" z CTA.

1. W `src/templates/article.html`, przed `{% block scripts %}`, dodaj:
   ```html
   {% if products_end %}
   <div class="sticky-cta" id="sticky-cta" hidden aria-hidden="true">
       <div class="container sticky-cta__inner">
           <p>{{ products_end[0].tagline_short }}</p>
           <a href="{{ products_end[0].target_url }}" class="btn btn--primary btn--sm" target="_blank" rel="noopener">{{ products_end[0].cta_text }}</a>
           <button type="button" class="sticky-cta__close" aria-label="Zamknij">&times;</button>
       </div>
   </div>
   {% endif %}
   ```

2. W `src/static/css/style.css`, dodaj:
   ```css
   /* Sticky CTA */
   .sticky-cta {
       position: fixed;
       bottom: 0;
       left: 0;
       right: 0;
       z-index: 50;
       background: var(--color-surface);
       border-top: 2px solid var(--color-accent);
       box-shadow: var(--shadow-lg);
       padding: 0.75rem 0;
       transform: translateY(100%);
       transition: transform var(--t-base) var(--ease);
   }
   .sticky-cta[data-visible] {
       transform: translateY(0);
   }
   .sticky-cta__inner {
       display: flex;
       align-items: center;
       justify-content: center;
       gap: 1rem;
   }
   .sticky-cta__inner p {
       font-size: 0.9rem;
       font-weight: 500;
       margin: 0;
   }
   .sticky-cta__close {
       font-size: 1.2rem;
       opacity: 0.6;
       padding: 0.25rem;
   }
   .sticky-cta__close:hover { opacity: 1; }
   .btn--sm { padding: 0.5rem 1rem; font-size: 0.85rem; }
   @media (max-width: 768px) {
       .sticky-cta__inner { flex-wrap: wrap; text-align: center; }
       .sticky-cta { bottom: 56px; } /* nad mobile-bottom-nav */
   }
   ```

3. W `src/static/js/main.js`, dodaj w głównym IIFE:
   ```javascript
   // Sticky CTA — pokazuj po 60% scroll
   (function initStickyCta() {
       var cta = document.getElementById('sticky-cta');
       if (!cta) return;
       var dismissed = false;
       var closeBtn = cta.querySelector('.sticky-cta__close');
       if (closeBtn) {
           closeBtn.addEventListener('click', function() {
               cta.removeAttribute('data-visible');
               cta.setAttribute('hidden', '');
               dismissed = true;
           });
       }
       window.addEventListener('scroll', function() {
           if (dismissed) return;
           var scrollPercent = window.scrollY / (document.documentElement.scrollHeight - window.innerHeight);
           if (scrollPercent > 0.6) {
               cta.removeAttribute('hidden');
               cta.setAttribute('aria-hidden', 'false');
               requestAnimationFrame(function() { cta.setAttribute('data-visible', ''); });
           }
       }, { passive: true });
   })();
   ```

## ZADANIE 3: "Badania mówią" sidebar blok

Strategia wymaga: "w każdym artykule blok z cytowaniem badania: Autor (rok), N=, główny wynik".

To już częściowo istnieje (article.bibliography + sidebar), ale dodaj dedykowany blok wizualny.

1. W `src/templates/article.html`, wewnątrz `<aside class="article__sidebar">`, po bloku `sticky-box` z udostępnianiem, dodaj:
   ```html
   {% if article.bibliography %}
   <div class="research-badge">
       <h4><span class="research-badge__icon" aria-hidden="true">🔬</span> Badania mówią</h4>
       <div class="research-badge__content" data-nosnippet>
           {{ article.bibliography | safe | truncate(300, true) }}
       </div>
       <a href="#bibliography-title" class="research-badge__link">Pełna bibliografia →</a>
   </div>
   {% endif %}
   ```

2. W `src/static/css/style.css`:
   ```css
   /* Research Badge */
   .research-badge {
       background: var(--color-bg-alt);
       border-left: 3px solid var(--color-trust, #5b8def);
       border-radius: var(--radius-sm);
       padding: 1rem;
       margin-top: 1.5rem;
       font-size: 0.85rem;
   }
   .research-badge h4 {
       font-size: 0.9rem;
       color: var(--color-trust);
       margin-bottom: 0.5rem;
       font-family: var(--font-sans);
   }
   .research-badge__icon { margin-right: 0.25rem; }
   .research-badge__content {
       color: var(--color-text-muted);
       line-height: 1.5;
   }
   .research-badge__link {
       display: block;
       margin-top: 0.5rem;
       color: var(--color-trust);
       font-weight: 500;
       font-size: 0.8rem;
   }
   ```

## ZADANIE 4: Difficulty badge (psycho.edu.pl)

Strategia wymaga: artykuły oznaczone "Podstawowy / Średniozaawansowany / Zaawansowany".

Rozwiązanie: użyj istniejącego pola `tags` — jeśli artykuł ma tag "zaawansowany", "średniozaawansowany" lub "podstawowy", wyświetl badge.

1. W `src/templates/_article_card.html`, tuż po otwarciu karty (po `<article class="article-card"`), dodaj:
   ```html
   {% set diff_tags = {'podstawowy': '🟢', 'średniozaawansowany': '🟡', 'zaawansowany': '🔴'} %}
   {% for dt, icon in diff_tags.items() %}
       {% if article_tags and dt in article_tags.lower() %}
       <span class="difficulty-badge difficulty-badge--{{ dt }}">{{ icon }} {{ dt | capitalize }}</span>
       {% endif %}
   {% endfor %}
   ```
   Gdzie `article_tags` = `a.tags` lub `article.tags` (sprawdź jak się odwołujesz do tagów w karcie — może być `a.tags`).

2. W `src/templates/article.html`, w sekcji `article__meta` (koło reading_time), dodaj:
   ```html
   {% set diff_levels = ['podstawowy', 'średniozaawansowany', 'zaawansowany'] %}
   {% set diff_icons = {'podstawowy': '🟢', 'średniozaawansowany': '🟡', 'zaawansowany': '🔴'} %}
   {% for level in diff_levels %}
       {% if article.tags and level in article.tags.lower() %}
       <span class="difficulty-badge difficulty-badge--{{ level }}">{{ diff_icons[level] }} {{ level | capitalize }}</span>
       {% endif %}
   {% endfor %}
   ```

3. W CSS:
   ```css
   /* Difficulty Badge */
   .difficulty-badge {
       display: inline-flex;
       align-items: center;
       gap: 0.25rem;
       font-size: 0.7rem;
       font-weight: 600;
       text-transform: uppercase;
       letter-spacing: 0.05em;
       padding: 0.2rem 0.6rem;
       border-radius: var(--radius-pill);
       background: var(--color-bg-alt);
       color: var(--color-text-muted);
   }
   .difficulty-badge--podstawowy { color: #2a7f62; background: #e8f5e9; }
   .difficulty-badge--średniozaawansowany { color: #b58b36; background: #fff8e1; }
   .difficulty-badge--zaawansowany { color: #c44745; background: #fce4ec; }
   ```

## ZADANIE 5: "Cytuj ten artykuł" przycisk (psycho.edu.pl)

1. W `src/templates/article.html`, po sekcji bibliography, dodaj:
   ```html
   <div class="cite-block">
       <button type="button" class="btn btn--ghost btn--sm" data-cite
               data-author="{{ article.author }}"
               data-title="{{ article.title | striptags }}"
               data-site="{{ site.name }}"
               data-url="{{ site.url }}/artykuly/{{ article.slug }}.html"
               data-date="{{ article.published_at }}">
           📋 Cytuj ten artykuł (APA 7)
       </button>
       <div class="cite-block__output" hidden></div>
   </div>
   ```

2. W `src/static/js/main.js`:
   ```javascript
   // Cite button — APA 7 format
   (function initCite() {
       document.addEventListener('click', function(e) {
           var btn = e.target.closest('[data-cite]');
           if (!btn) return;
           var author = btn.dataset.author;
           var title = btn.dataset.title;
           var site = btn.dataset.site;
           var url = btn.dataset.url;
           var date = btn.dataset.date;
           var year = date ? date.substring(0, 4) : new Date().getFullYear();
           var months = ['styczeń','luty','marzec','kwiecień','maj','czerwiec','lipiec','sierpień','wrzesień','październik','listopad','grudzień'];
           var monthNum = date ? parseInt(date.substring(5, 7), 10) : 0;
           var day = date ? parseInt(date.substring(8, 10), 10) : 0;
           var dateStr = day && monthNum ? day + ' ' + months[monthNum - 1] + ' ' + year : year;
           // APA 7: Autor. (rok, data). Tytuł artykułu. Nazwa Serwisu. URL
           var citation = author + '. (' + dateStr + '). ' + title + '. ' + site + '. ' + url;
           var output = btn.nextElementSibling;
           if (output) {
               output.hidden = false;
               output.textContent = citation;
               output.style.userSelect = 'all';
           }
           navigator.clipboard.writeText(citation).catch(function() {});
       });
   })();
   ```

3. W CSS:
   ```css
   .cite-block { margin: 1.5rem 0; }
   .cite-block__output {
       margin-top: 0.75rem;
       padding: 0.75rem 1rem;
       background: var(--color-bg-alt);
       border-left: 3px solid var(--color-trust);
       border-radius: var(--radius-sm);
       font-size: 0.85rem;
       font-family: var(--font-mono);
       line-height: 1.6;
       color: var(--color-text-muted);
   }
   ```

## PO ZAKOŃCZENIU

1. Zrób `python build.py --domain psychosen.pl --clean` i sprawdź czy dark mode działa
2. Zrób `python build.py --domain psycho-edu.pl --clean` i sprawdź difficulty badges
3. Zrób `python build.py --domain zdrowie.fit --clean` i sprawdź sticky CTA + research badge + cite button
4. Uruchom `python scripts/audit_aeo.py --domain zdrowie.fit` i sprawdź czy JSON-LD jest poprawny

Commituj: `git add -A && git commit -m "feat: dark mode, sticky CTA, research badge, difficulty badge, cite button (strategia klastra psychologia)"`
```

---

## INSTRUKCJA UŻYCIA

1. Otwórz Claude Code w folderze `C:\PYTHON\ARCHAIOS Demand Engine\zdrowie-fit-generator` (lub `archaios-ssg` jeśli zmieniłeś nazwę)
2. Wklej CAŁY tekst z sekcji "PROMPT DO WKLEJENIA" powyżej
3. Pod spodem wklej CAŁY plik `STRATEGIA_KLASTER_PSYCHOLOGIA.md` jako kontekst
4. Wyślij — Code zaimplementuje 5 feature'ów w jednym przebiegu
5. Po zakończeniu: sprawdź build i commituj

**Nie musisz dodawać nic od siebie** — prompt jest samodzielny i kompletny. Strategia jest kontekstem, prompt jest instrukcją.
