# HANDOFF — Archaios SSG, 130 artykułów × 13 domen

> Ten dokument jest **jedynym wymaganym promptem** w nowym chacie. Wczytaj go i kontynuuj.
>
> **Komenda startowa w nowym chacie:**
> > Przeczytaj `C:\PYTHON\ARCHAIOS Demand Engine\zdrowie-fit-generator\content_generated\HANDOFF.md` i kontynuuj realizację projektu z miejsca, w którym poprzedni chat skończył.

---

## 1. CEL PROJEKTU

Generowanie **130 artykułów** dla **13 domen satelitarnych** systemu **Archaios SSG** (zdrowie.fit, psychosen.pl, psychodzisiaj.pl, jaksobieradzic.pl, sprawdzwypalenie.pl, testpredyspozycje.pl, testnis2.pl, karynis2.pl, skanujfirme.pl, audytzespolu.pl, onpremiseai.pl, aidzisiaj.pl, ragpolska.pl).

Każdy artykuł: **2000–4000 słów**, jakość **10/10**, prawdziwe DOI, **zero artefaktów AI**, mistrzowskie subtelne techniki przekierowania psychologicznego.

Architektura biznesowa: **dwa klastry SEO**, każdy artykuł prowadzi naturalny ruch do produktu końcowego.

- **Klaster NURIO** (6 domen) → produkty: `nurio.pl` (konwersacyjna apka AI), `psychozdrowie.online` (testy psychologiczne), `psycho.edu.pl` (edukacja)
- **Klaster ARCHAIOS** (7 domen) → produkty: `archaios.ai` (platforma AI dla firm), `twojamediacja.pl` (mediacje)

---

## 2. STATUS — gdzie jesteśmy

### Zrobione: 41 artykułów (~131 000 słów, 320+ źródeł z DOI)

| Domena | Klaster | Artykuły | Design pack | Import script | ZIP |
|---|---|---|---|---|---|
| **zdrowie.fit** | NURIO | 10/10 ✅ | 5 SVG + `_design.md` ✅ | `_import.py` ✅ | (skrypt `make_zip.py` w `content_generated/`) |
| **psychosen.pl** | NURIO | 10/10 ✅ | 5 SVG + `_design.md` ✅ | (przez universal `import_articles.py`) | — |
| **psychodzisiaj.pl** | NURIO | 10/10 ✅ | 5 SVG + `_design.md` ✅ | (universal) | — |
| **jaksobieradzic.pl** | NURIO | 10/10 ✅ | 5 SVG + `_design.md` ✅ | (universal) | — |
| **sprawdzwypalenie.pl** | NURIO | **8/10** 🟡 | 5 SVG + `_design.md` ✅ | (universal) | — |

### Do zrobienia: 62 artykuły + 8 design packów

| Domena | Klaster | Artykuły do zrobienia | Design pack | Notatki |
|---|---|---|---|---|
| **sprawdzwypalenie.pl** | NURIO | **#9 cornerstone, #10 IT** | gotowy | `_README.md` zawiera plan tematów |
| **testpredyspozycje.pl** | NURIO | 10/10 (BOFU testów) | brak | charakter: kompas/labirynt, granat + złoto akademicki |
| **testnis2.pl** | ARCHAIOS | 10/10 (gotowość NIS2) | brak | tarcza/zamek, granat + neon green bezpieczeństwa |
| **karynis2.pl** | ARCHAIOS | 10/10 (kary NIS2) | brak | waga sprawiedliwości, czerń + bordo + złoto sądowy |
| **skanujfirme.pl** | ARCHAIOS | 10/10 (audyt RODO+NIS2) | brak | radar/skan, cyan + ciemny granat |
| **audytzespolu.pl** | ARCHAIOS | 10/10 (audyt zespołu) | brak | mozaika/kółka, ciepły profesjonalny |
| **onpremiseai.pl** | ARCHAIOS | 10/10 (AI on-prem) | brak | serwer/box, grafit + zielony LED |
| **aidzisiaj.pl** | ARCHAIOS | 10/10 (AI w biznesie) | brak | neuron/sieć, electric blue + magenta |
| **ragpolska.pl** | ARCHAIOS | 10/10 (RAG/LLM tech) | brak | graf wiedzy, dark + cyan |

### Plus do zrobienia (zdrowie.fit live deployment — w toku)

- [x] `IMAGE_PROMPTS.md` — 10 promptów AI do hero (gotowy)
- [x] `SSH_AUDIT.md` — komendy do audytu serwera (gotowy)
- [ ] **STRATEGY.md** — operacyjna strategia serwisu (publikacja, SEO, social, KPI, roadmap)
- [ ] **NEWSLETTER_STRATEGY.md** — strategia + welcome series 5 maili + 3 pierwsze numery
- [ ] **HTML templates newsletterowe** — welcome + weekly
- [ ] **Wdrożenie na serwer** — lokalny build → SFTP → live test
- [ ] **CI/CD secrets** — sprawdzenie GitHub Actions
- [ ] **DNS / SSL audit** — czy zdrowie.fit żyje publicznie

---

## 3. LOKALIZACJE — gdzie wszystko jest

```
C:\PYTHON\ARCHAIOS Demand Engine\zdrowie-fit-generator\
├── CLAUDE.md                    # instrukcje projektu (ZAWSZE czytane przez Claude)
├── build.py                     # generator stron (AKTYWNY, 584 linie)
├── domains/
│   ├── _schema.yaml             # schema YAML dla domen
│   ├── zdrowie-fit.yaml         # konfiguracja zdrowie.fit
│   ├── psychosen-pl.yaml
│   ├── psychodzisiaj-pl.yaml
│   ├── jaksobieradzic-pl.yaml
│   ├── sprawdzwypalenie-pl.yaml
│   ├── testpredyspozycje-pl.yaml
│   ├── testnis2-pl.yaml
│   ├── karynis2-pl.yaml
│   ├── skanujfirme-pl.yaml
│   ├── audytzespolu-pl.yaml
│   ├── onpremiseai-pl.yaml
│   ├── aidzisiaj-pl.yaml
│   └── ragpolska-pl.yaml
├── backend/                     # FastAPI CMS (port 8765)
├── src/templates/               # Jinja2 HTML templates (NIE edytuj output/)
├── src/static/css/style.css     # główny CSS, system designu
├── output/                      # auto-generowany przez build.py
└── content_generated/           # ⭐ TWÓJ FOLDER ROBOCZY
    ├── HANDOFF.md               # ⭐ TEN PLIK
    ├── _topic_registry.json     # rejestr wszystkich tematów (anty-duplikacja)
    ├── make_zip.py              # universal pakowacz ZIP
    ├── import_articles.py       # universal import md → SQLite/API
    ├── zdrowie-fit/
    │   ├── _README.md           # plan 10 tematów
    │   ├── _design/
    │   │   ├── favicon.svg
    │   │   ├── logo.svg
    │   │   ├── og-default.svg
    │   │   ├── hero-illustration.svg
    │   │   ├── article-divider.svg
    │   │   └── _design.md       # paleta + galeria zdjęć
    │   ├── _deployment/         # ⭐ pakiet wdrożeniowy live
    │   │   ├── IMAGE_PROMPTS.md # prompty AI do hero
    │   │   ├── SSH_AUDIT.md     # komendy audytu serwera
    │   │   ├── STRATEGY.md      # ⏳ TODO operacyjna strategia
    │   │   └── NEWSLETTER_*.md  # ⏳ TODO newsletter
    │   ├── 01-mikrobiom-os-jelita-mozg-depresja.md   ✅
    │   ├── 02-trening-silowy-antydepresant-metaanaliza.md  ✅
    │   ├── 03-uklad-glimfatyczny-sen-mozg.md  ✅
    │   ├── 04-dieta-mind-vs-srodziemnomorska-mozg.md  ✅
    │   ├── 05-polywagal-theory-nerw-bledny-emocje.md  ✅
    │   ├── 06-cold-exposure-zimne-prysznice-nauka.md  ✅
    │   ├── 07-kortyzol-a-serce-stres-chroniczny.md  ✅
    │   ├── 08-cztery-filary-odpornosci-psychicznej.md  ✅ (cornerstone)
    │   ├── 09-kawa-a-zdrowie-metaanaliza-2024.md  ✅
    │   └── 10-audyt-zdrowia-5-testow-z-domu.md  ✅ (BOFU)
    ├── psychosen-pl/            # 10 art ✅ + design ✅
    ├── psychodzisiaj-pl/        # 10 art ✅ + design ✅
    ├── jaksobieradzic-pl/       # 10 art ✅ + design ✅
    └── sprawdzwypalenie-pl/     # 8 art ✅ + design ✅ (zostały #9, #10)
```

---

## 4. STANDARD JAKOŚCI 10/10 — non-negotiable

Każdy artykuł musi spełniać:

### Bibliografia
- **Minimum 5 prawdziwych źródeł** (zwykle 7-12) z **realnymi DOI**
- **Cytuj tylko badania, których jesteś 100% pewny** (autor + tytuł + czasopismo + rok)
- Tam gdzie nie znasz dokładnego DOI: dopisek `[DOI DO WERYFIKACJI]`
- **Nigdy nie halucynuj** autorów, czasopism, DOI
- Format APA 7 w `<ul><li>` (HTML, bo trafia do pola `bibliography` w bazie)

### Struktura artykułu (HTML markdown)
1. **Hook (1 akapit)** — zaskakujący fakt, statystyka lub konkretne badanie. Bez "W dzisiejszych czasach"
2. **Problem (2-3 akapity)** — dlaczego to ważne, kogo dotyczy, skala zjawiska
3. **Rozwinięcie merytoryczne (5-8 sekcji H2/H3)** — badania, mechanizmy, dane
4. **Praktyka (2-3 sekcji)** — co czytelnik może ZROBIĆ, konkretne kroki
5. **Trzy pytania kontrolne** — pytania refleksyjne dla czytelnika
6. **Inline CTA** w środku (po empatycznym fragmencie)
7. **Esencja** — 4-6 akapitów, esencja a nie powtórka
8. **Bibliografia HTML** w `<ul><li>` po separatorze `---`

### YAML frontmatter (wszystkie pola wymagane)
```yaml
---
title: "Tytuł SEO (50-65 znaków, keyword na początku)"
slug: "tytuł-z-myślnikami"
excerpt: "Lead 150-160 znaków — co czytelnik zyska"
category_slug: "slug-kategorii-z-yamla-domeny"
tags: "tag1, tag2, tag3, poziom-trudności"
reading_time: 12
is_published: true
is_featured: false  # true dla 2 najlepszych per domena
meta_title: "Tytuł | Nazwa Serwisu"
meta_description: "Opis SEO 150-160 znaków"
funnel: "TOFU" / "MOFU" / "BOFU" / "TOFU-pillar" / "MOFU-cornerstone"
author_slug: "marek-porycki"
related_slugs: "slug1,slug2,slug3"  # 3-5 cross-linków wewnątrz domeny
product_slugs: "nurio,psychozdrowie"  # CTA produkty
---
```

### Zero AI-mowy — czarna lista

NIE używaj:
- "warto zauważyć", "nie ulega wątpliwości", "kluczowe jest", "podsumowując"
- "w dzisiejszych czasach", "obecnie", "współczesny", "dynamicznie zmieniający się świat"
- "z jednej strony / z drugiej strony" (jako pusty zwrot)
- "warto pamiętać"
- Listy bez konkretnej treści ("krótko", "jasno", "konkretnie" jako bullety)
- Schematyczne podsumowania w stylu "Podsumowując, kluczowe jest aby..."
- Emoji w tekście (chyba że specyficznie ironicznie)

### Subtelne techniki przekierowania psychologicznego

CTA nigdy nie sprzedażowe, zawsze:
1. **Empathic anchor PRZED CTA** — minimum 1-2 zdania uznające stan czytelnika
2. **Self-determination preserved** — "jeśli...", "może być pierwszym krokiem", nigdy "musisz"
3. **Implementation intention** — frazujemy jako warunkowe instrukcje
4. **Authority through specificity** — wymieniaj walidowane testy (BDI-II, NEO-FFI, ECR-R, MBI, PSQI, ECR-R) jako klinicystyczny język
5. **Cross-linking jako budowanie autorytetu domeny** — 3-5 linków wewnętrznych

Maksymalnie **2 CTA** per artykuł:
- 1 inline (wpięty w naturalny moment narracji, po empatycznej walidacji)
- 1 na końcu (po sekcji "Trzy pytania", jako "co dalej")

UTM template: `?utm_source={domain-slug}&utm_medium=article&utm_campaign={article-slug}`

### Numery alarmowe (etyczny obowiązek)

W artykułach z komponentem kryzysowym (samobójstwo, przemoc, ostry kryzys) ZAWSZE w stopce:
- **Telefon Zaufania 116 123** (dorośli, 24/7, bezpłatnie)
- **Niebieska Linia 800 120 002** (ofiary przemocy)
- **Telefon dla Dzieci i Młodzieży 116 111**

---

## 5. CHARAKTER WIZUALNY DOMEN

Każda domena ma osobny charakter (paleta + ton + symbol logo). Konfiguracja w `domains/<slug>.yaml` + design pack w `content_generated/<slug>/_design/`.

### NURIO cluster (klimat: psychologia, zdrowie, empatia)

| Domena | Paleta | Mark | Ton |
|---|---|---|---|
| **zdrowie.fit** | sage `#4a7c59` + terracotta `#d9724a` + ivory | ◐ półokrąg ciało/umysł | dziennikarz naukowy, holistycznie |
| **psychosen.pl** | granat `#2d3a7c` + złoto `#d4a843` + srebro | księżyc + gwiazdy | dark mode, kontemplacyjnie, "nocno" |
| **psychodzisiaj.pl** | ocean `#2c6e8a` + coral `#e07b4f` + violet | uśmiechnięta twarz w okręgu | ciepły rozmowny, "psycholog przy kawie" |
| **jaksobieradzic.pl** | forest `#2a7f62` + terracotta + lavender | drabinka 3 stopnie | empatyczny kliniczny dla osób w kryzysie |
| **sprawdzwypalenie.pl** | brąz `#7c5b3c` + orange flame `#e8922d` + sage | trzy świece (energia/wypalenie/regeneracja) | konkretny, kliniczny BOFU |
| **testpredyspozycje.pl** | granat akademicki + złoto | kompas/labirynt | (DO ZROBIENIA) BOFU testów psychometrycznych |

### ARCHAIOS cluster (klimat: tech, compliance, biznes)

| Domena | Paleta (planowana) | Mark | Ton |
|---|---|---|---|
| **testnis2.pl** | granat + neon green | tarcza/zamek | techniczny audytowy |
| **karynis2.pl** | czerń + bordo + złoto | waga sprawiedliwości | sądowy, wagi konsekwencji |
| **skanujfirme.pl** | cyan + ciemny granat | radar/skan | techniczny security |
| **audytzespolu.pl** | ciepły profesjonalny | mozaika/kółka | corporate empatyczny |
| **onpremiseai.pl** | grafit + zielony LED | serwer/box | hardware'owy, dla decydentów IT |
| **aidzisiaj.pl** | electric blue + magenta | neuron/sieć | nowoczesny AI ogólnie |
| **ragpolska.pl** | dark + cyan | graf wiedzy/węzły | techniczny dark dla deweloperów |

---

## 6. ANTI-DUPLIKACJA TEMATÓW

`content_generated/_topic_registry.json` zawiera pełną listę tematów per domena. Reguły:

- **Wypalenie zawodowe** — TYLKO sprawdzwypalenie.pl. Inne domeny mogą o nim wspominać, ale nie poświęcać artykułu (chyba że *inny kąt*: jaksobieradzic.pl ma "wypalenie rodzicielskie", to inny konstrukt).
- **Sen** (główny temat) — TYLKO psychosen.pl. zdrowie.fit ma jeden artykuł o układzie glimfatycznym (neurobiologia), nie o higienie snu.
- **Testy psychologiczne** (NEO-FFI, MBTI, Big Five jako temat główny) — TYLKO testpredyspozycje.pl.
- **NIS2** — TYLKO testnis2.pl, karynis2.pl, skanujfirme.pl. Każda z innym kątem (gotowość vs kary vs audyt).
- **RAG/LLM techniczne** — TYLKO ragpolska.pl. onpremiseai.pl tylko o wdrożeniach lokalnych, aidzisiaj.pl tylko biznes/regulacje.

Przy każdym nowym artykule **najpierw sprawdź `_topic_registry.json`**, czy temat nie koliduje.

---

## 7. PLAN TEMATÓW DLA POZOSTAŁYCH DOMEN

### sprawdzwypalenie.pl (zostały 2)

- **#9** — Fizjologia stresu chronicznego (CORNERSTONE, 3500 słów). Bibliografia: McEwen allostatic load, Steptoe & Kivimäki Nat Rev Cardiol 2012, oś HPA, cytokiny IL-6/TNF-α/CRP, BDNF.
- **#10** — Wypalenie w IT (specyfika branży, 2600 słów). Bibliografia: Westgaard 2014 IT workers, Verdonk 2018 ICT burnout, crunch culture, deadline-driven cycles.

### testpredyspozycje.pl (10 do zrobienia)

Tematy z prompta Marka:
1. Big Five a kariera (PILLAR) — McCrae & Costa NEO-PI-R, predyktory zawodowe
2. CliftonStrengths w praktyce — Gallup, Buckingham
3. MBTI vs Big Five — porównanie naukowe (debunking MBTI)
4. Inteligencja emocjonalna w pracy — Goleman, Bar-On EQ-i
5. Neuroplastyczność a rozwój talentów — Doidge, Dweck growth mindset
6. Testy predyspozycji — co naprawdę mierzą (psychometria)
7. Introwersja w świecie ekstrawertyków — Cain Quiet
8. Flow state — Csíkszentmihályi (cornerstone)
9. Mocne strony w zespole — Lencioni, Patrick Lencioni
10. Talenty wrodzone vs wyuczone (BOFU — bezpośrednio do testów)

### testnis2.pl (10 do zrobienia)

Tematy: checklist gotowości, kogo obowiązuje (PL), NIS1 vs NIS2, MŚP, raportowanie 24/72h, odpowiedzialność zarządu, NIS2 vs RODO (cornerstone), łańcuch dostaw, certyfikacje, test online (BOFU).

### karynis2.pl (10 do zrobienia)

Tematy: wysokość kar (€10M / 2% obrotu) (PILLAR), odpowiedzialność osobista zarządu, case studies europejskie, timeline PL, NIS2 vs RODO porównanie kar, ubezpieczenie cyber, koszty braku compliance, audyt vs kara — ROI (cornerstone), sektory ryzyka, jak przygotować firmę (BOFU).

### skanujfirme.pl (10 do zrobienia)

Tematy: co to audyt cyberbezpieczeństwa (PILLAR), RODO 2026, phishing MŚP statystyki, ransomware PL, polityka haseł evidence-based, backup 3-2-1, szkolenia cyberhigieny (cornerstone), IOD - kto musi mieć, audyt NIS2 krok po kroku, monitoring 24/7 (BOFU).

### audytzespolu.pl (10 do zrobienia)

Tematy: skala dysfunkcji zespołu Lencioniego (PILLAR), mobbing - obowiązki pracodawcy, mediacja pracownicza, NVC w zespole, audyt kultury, wypalenie zespołowe, onboarding a retencja (cornerstone), feedback 360°, różnorodność, compliance pracowniczy a NIS2 (BOFU).

### onpremiseai.pl (10 do zrobienia)

Tematy: chmura vs on-premise (PILLAR), RODO a dane w AI, llama.cpp - LLM na serwerze, koszt wdrożenia, TCO cloud vs local, RAG na danych firmowych, fine-tuning (cornerstone), AI Act a lokalne modele, bezpieczeństwo LLM, case study PL (BOFU).

### aidzisiaj.pl (10 do zrobienia)

Tematy: AI Act dla polskiej firmy (PILLAR), ChatGPT vs Claude vs Gemini, automatyzacja - od czego zacząć, AI w obsłudze klienta, AI w HR, ROI z AI (cornerstone), etyka AI, AI w marketingu PL, low-code AI, polska strategia AI 2026 (BOFU).

### ragpolska.pl (10 do zrobienia)

Tematy: RAG game-changer (PILLAR), chunking strategies, vector databases (Chroma/Qdrant/Pinecone), embedding models PL benchmark, hallucynacje LLM (cornerstone), RAG vs fine-tuning, bezpieczeństwo RAG pipeline, RAG na dokumentacji firmowej, ewaluacja RAG metryki, case study kancelaria PL (BOFU).

---

## 8. CHECKLIST KONTYNUACJI W NOWYM CHACIE

W nowym chacie wykonaj po kolei:

1. **Wczytaj kontekst:**
   - CLAUDE.md (automatycznie czytane przez Claude)
   - HANDOFF.md (ten plik)
   - `_topic_registry.json` — zobacz co jest, co nie

2. **Sprawdź pierwszy gotowy artykuł** — np. `zdrowie-fit/01-mikrobiom-os-jelita-mozg-depresja.md` jako wzorzec jakości.

3. **Sprawdź design pack zdrowie.fit** — `_design/_design.md` jako wzorzec dla pozostałych domen.

4. **Decyzja na start nowego chatu:**
   - Najpierw priorytet: **wdrożenie zdrowie.fit live** (jeśli nieukończone — patrz sekcja 11)
   - LUB: **kontynuacja artykułów** od sprawdzwypalenie.pl #9, #10

5. **Dla każdej kolejnej domeny** powtórz cykl:
   - Stwórz design pack (5 SVG + `_design.md`)
   - Stwórz `_README.md` + zaktualizuj `_topic_registry.json`
   - Napisz 10 artykułów (3-4 per tura)
   - Sprawdź anty-duplikację
   - Maksymalnie 2 CTA per artykuł
   - Bibliografia 7+ źródeł z DOI

---

## 9. KOMENDA STARTOWA W NOWYM CHACIE

Wklej w nowym chacie:

```
Przeczytaj C:\PYTHON\ARCHAIOS Demand Engine\zdrowie-fit-generator\content_generated\HANDOFF.md i kontynuuj realizację projektu Archaios SSG.

Status: 41/130 artykułów ukończonych. Kontynuuj od sprawdzwypalenie.pl #9 (cornerstone fizjologia stresu chronicznego), potem #10 (wypalenie w IT), potem testpredyspozycje.pl (design + 10 art), potem 7 domen klastra ARCHAIOS.

Standard jakości 10/10 zgodnie z HANDOFF.md sekcja 4. Bez raportów pośrednich — produkcja w każdej turze.

Zacznij od najszybszego potwierdzenia że masz cały kontekst (przeczytałeś jeden gotowy artykuł i wiesz, jaki jest standard), potem leć.
```

---

## 10. NAJWAŻNIEJSZE BADANIA — bibliografia podstawowa

Te źródła powtarzają się w wielu artykułach. **Wszystkie zweryfikowane**, prawdziwe DOI.

### Wypalenie zawodowe
- Maslach, C., & Jackson, S. E. (1981). The measurement of experienced burnout. *Journal of Occupational Behavior*, 2(2), 99-113. https://doi.org/10.1002/job.4030020205
- Maslach, C., Schaufeli, W. B., & Leiter, M. P. (2001). Job burnout. *Annual Review of Psychology*, 52, 397-422. https://doi.org/10.1146/annurev.psych.52.1.397
- Bakker, A. B., & Demerouti, E. (2007). The Job Demands-Resources model. *Journal of Managerial Psychology*, 22(3), 309-328. https://doi.org/10.1108/02683940710733115
- WHO (2019). ICD-11: Burn-out QD85. https://icd.who.int/

### Depresja & nastrój
- Cipriani, A., et al. (2018). 21 antidepressants meta-analysis. *Lancet*, 391(10128), 1357-1366. https://doi.org/10.1016/S0140-6736(17)32802-7
- Singh, B., et al. (2023). Physical activity for depression umbrella review. *British Journal of Sports Medicine*, 57(18), 1203-1209. https://doi.org/10.1136/bjsports-2022-106195
- Jacka, F. N., et al. (2017). SMILES trial dietary improvement for depression. *BMC Medicine*, 15(1), 23. https://doi.org/10.1186/s12916-017-0791-y

### Stres & serce
- Steptoe, A., & Kivimäki, M. (2012). Stress and cardiovascular disease. *Nature Reviews Cardiology*, 9(6), 360-370. https://doi.org/10.1038/nrcardio.2012.45
- Tawakol, A., et al. (2017). Resting amygdalar activity and cardiovascular events. *Lancet*, 389(10071), 834-845. https://doi.org/10.1016/S0140-6736(16)31714-7
- McEwen, B. S. (1998). Stress, adaptation, and disease: Allostasis. *Annals NYAS*, 840(1), 33-44. https://doi.org/10.1111/j.1749-6632.1998.tb09546.x

### Sen
- Walker, M. P. (2017). *Why We Sleep*. Scribner.
- Xie, L., et al. (2013). Sleep drives metabolite clearance. *Science*, 342(6156), 373-377. https://doi.org/10.1126/science.1241224
- Trauer, J. M., et al. (2015). CBT-I meta-analysis. *Annals of Internal Medicine*, 163(3), 191-204. https://doi.org/10.7326/M14-2841

### Mikrobiom & oś jelita-mózg
- Cryan, J. F., et al. (2019). Microbiota-Gut-Brain Axis. *Physiological Reviews*, 99(4), 1877-2013. https://doi.org/10.1152/physrev.00018.2018
- Valles-Colomer, M., et al. (2019). Neuroactive potential of human gut microbiota. *Nature Microbiology*, 4(4), 623-632. https://doi.org/10.1038/s41564-018-0337-x

### Relacje & samotność
- Holt-Lunstad, J., et al. (2010). Social relationships and mortality. *PLoS Medicine*, 7(7), e1000316. https://doi.org/10.1371/journal.pmed.1000316
- Holt-Lunstad, J., et al. (2015). Loneliness and mortality. *Perspectives on Psychological Science*, 10(2), 227-237. https://doi.org/10.1177/1745691614568352

### Przywiązanie
- Hazan, C., & Shaver, P. (1987). Romantic love as attachment. *J Personality and Social Psychology*, 52(3), 511-524. https://doi.org/10.1037/0022-3514.52.3.511
- Mikulincer, M., & Shaver, P. R. (2007). *Attachment in Adulthood*. Guilford.

### Decyzje & emocje
- Bechara, A., Damasio, H., Tranel, D., & Damasio, A. R. (1997). Iowa Gambling Task. *Science*, 275(5304), 1293-1295. https://doi.org/10.1126/science.275.5304.1293
- Damasio, A. R. (1996). Somatic marker hypothesis. *Phil Trans Royal Society B*, 351(1346), 1413-1420. https://doi.org/10.1098/rstb.1996.0125
- Lerner, J. S., et al. (2015). Emotion and decision making. *Annual Review of Psychology*, 66, 799-823. https://doi.org/10.1146/annurev-psych-010213-115043

### Procrastinacja
- Steel, P. (2007). Nature of procrastination meta-analysis. *Psychological Bulletin*, 133(1), 65-94. https://doi.org/10.1037/0033-2909.133.1.65
- Sirois, F. M., & Pychyl, T. A. (2013). Procrastination and emotion regulation. *Social and Personality Psychology Compass*, 7(2), 115-127. https://doi.org/10.1111/spc3.12011

### Lęk & emocje
- Gross, J. J. (1998). Emotion regulation review. *Review of General Psychology*, 2(3), 271-299. https://doi.org/10.1037/1089-2680.2.3.271
- Bushman, B. J. (2002). Catharsis myth debunked. *PSPB*, 28(6), 724-731. https://doi.org/10.1177/0146167202289002

### Żałoba
- Bonanno, G. A. (2009). *The Other Side of Sadness*. Basic Books.
- Maciejewski, P. K., et al. (2007). Stage theory of grief examination. *JAMA*, 297(7), 716-723. https://doi.org/10.1001/jama.297.7.716

---

## 11. ZDROWIE.FIT LIVE — co zostało

Status w momencie handoff:

- ✅ Audyt SSH wykonany — serwer s159.cyber-folks.pl, port 222, user bestios, dostęp OK
- ✅ public_html zdrowie.fit zawiera build z 19 IV (struktura: artykuly/, autor/, css/, etc.)
- ⏳ **Pełen audyt zawartości** — do uruchomienia (komenda w SSH_AUDIT.md krok 2)
- ⏳ **DNS / SSL check** — `curl -sI https://zdrowie.fit` + `nslookup zdrowie.fit`
- ⏳ **Decyzja override vs uzupełnienie**: stary build prawdopodobnie z domyślnym seed (5 art z `seed_service`). Najczystsze: świeży build z 10 nowymi artykułami → SFTP overwrite.

### Następne kroki konkretne (w nowym chacie)

1. **Lokalny build:**
   ```bash
   cd C:\PYTHON\ARCHAIOS Demand Engine\zdrowie-fit-generator
   python content_generated/import_articles.py zdrowie-fit
   python build.py --domain zdrowie.fit --clean
   ```

2. **Test lokalnie:**
   ```bash
   cd output/zdrowie-fit && python -m http.server 8766
   # otworzyć http://127.0.0.1:8766
   ```

3. **Deploy SFTP** — albo:
   - **GitHub Actions** (push do main → automatyczny deploy, wymaga ustawienia secrets)
   - **Ręcznie** (lftp / WinSCP / FileZilla na port 222 do `/home/bestios/domains/zdrowie.fit/public_html/`)

4. **Po deployu:**
   ```powershell
   curl.exe -sI https://zdrowie.fit
   ```
   Powinno zwrócić HTTP 200, sprawdzić poprawność stron przez przeglądarkę.

5. **Pakiet zostały do zrobienia (`_deployment/`):**
   - `STRATEGY.md` — operacyjna strategia (publikacja co tydzień, SEO, social, KPI)
   - `NEWSLETTER_STRATEGY.md` — welcome series 5 maili + 3 pierwsze numery + welcome HTML template
   - Szczegóły: ton newslettera = identyczny jak artykuły (dziennikarz naukowy z empatią), CTA do nurio.pl + psychozdrowie.online subtelne, 1 numer/tydzień, formaty: top story (długi pillar) + 2 quick reads + 1 "myśl tygodnia"

---

## 12. INFORMACJE OPERACYJNE — Cyber_Folks

```
Host SSH/SFTP:    s159.cyber-folks.pl
Port:             222
User:             bestios
Hasło:            (GitHub Secrets: FTP_PASS, NIE w repo)
Fingerprint ED25519 SHA256: l/jfbMOzZibqe/kD2WHuhdbpRiVIg/YcG8M9mt67lHM
Path zdrowie.fit: /home/bestios/domains/zdrowie.fit/public_html
```

⚠️ **Fail2ban aktywny** — 3-5 błędnych prób → ban IP na 30-60 min, czasem długo. Ostrożnie z hasłami.
⚠️ **`~/public_html` to symlink** do `bestios.pl/public_html` — NIE deployować tam zdrowie.fit.
⚠️ **Inne domeny na koncie**: archaios.ai, brokerbusiness.eu, psychozdrowie.online, spine.fit, yerbata.eu — uważaj przy listowaniu, żeby nie pomylić katalogów.

---

## 13. POMYSŁY OPTYMALIZACYJNE (jeśli zostanie czas)

- **Skrypt batch generowania OG images** per artykuł (już zaprojektowany w `_design.md`, do uruchomienia)
- **Skrypt eksportu PNG/ICO** z SVG (cairosvg + Pillow)
- **Universal `import_articles.py`** już istnieje — może obsłużyć wszystkie 13 domen
- **Universal `make_zip.py`** już istnieje
- **Audyt jakości artykułów** przed deployem przez `academic-quality-agent` skill (jeśli chcesz)
- **Topic registry update** przy każdej nowej domenie — anty-duplikacja

---

## 14. KTO JEST UŻYTKOWNIKIEM (kontekst projektu)

**Marek Porycki**:
- Psycholog kliniczny, biegły sądowy, mediator
- CEO Archaios.ai (FENG.05.01 finalista, ~14,8M PLN)
- Prorektor uczelni
- Autor thrillerów psychologicznych pod własnym nazwiskiem (NIE Silas Vaughn — pseudonim porzucony XI.2025)
- Developer (Python/PHP/CodeIgniter/React/FastAPI/llama.cpp/RAG/fine-tuning)
- Producent muzyki AI (Orion Valen)
- Pisze pod własnym nazwiskiem akademicko, klinicznie, fictional

**Skill `marek-core` (w `.claude/skills/`):**
- Domyślnie aktywny w każdej sesji
- Tryb operacyjny: prędkość + jakość, gęstość > objętość
- Zero zbędnego moralizowania
- Bez "świetne pytanie", bez disclaimerów typu "skonsultuj się ze specjalistą"
- Polski informalny (mirror Marka)
- Toleruj literówki / voice-to-text

**Skill `marek-writing`:**
- Comprehensive writing assistant
- Psychologia, statystyki SPSS, APA 7
- Thrillery psychologiczne
- WordPress content
- Use przy pisaniu długich treści

---

**Koniec HANDOFF.md.**

Powodzenia w nowym chacie. Wszystkie dane są zachowane. Standard 10/10. Lecisz dalej.
