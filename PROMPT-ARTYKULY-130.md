# PROMPT: Generowanie 130 artykułów do 13 domen satelitarnych Archaios SSG

## Kontekst systemu

Buduję ekosystem 13 stron satelitarnych (content sites), które prowadzą ruch organiczny do moich produktów końcowych. Każda strona ma 3-4 kategorie tematyczne, newsletter i CTA do produktu. Artykuły muszą być **rzeczowe, oparte na badaniach, z prawdziwymi źródłami** — zero clickbaitu, zero bzdur. Każdy artykuł ma jasne miejsce w lejku sprzedażowym.

Jestem psychologiem, biegłym sądowym, mediatorem, CEO firmy AI (Archaios.ai), developerem (Python/React/FastAPI), prorektorem uczelni i autorem thrillerów psychologicznych. Nie potrzebuję upraszczania ani moralizowania — potrzebuję treści na poziomie eksperta, które jednocześnie są przystępne dla czytelnika.

---

## Architektura lejków

### KLASTER NURIO (zdrowie, psychologia) → 6 satelitów → 60 artykułów

**Produkty docelowe:**
- **nurio.pl** — konwersacyjna apka AI (Nuria), wsparcie emocjonalne 24/7
- **psychozdrowie.online** — profesjonalne testy psychologiczne online (NEO-FFI, PCL-5, ECR-R, BDI-II, BAI, STAI, SWLS, SES, Gallup CliftonStrengths)
- **psycho.edu.pl** — platforma edukacyjna z egzaminami (EduExam Pro)

**Satelity i ich role w lejku:**

| Satelita | Tematyka | Główny produkt docelowy | Rola w lejku |
|----------|----------|------------------------|--------------|
| **zdrowie.fit** | Psychosomatyka, dietetyka, neuronauka, wellbeing | nurio.pl + psychozdrowie.online | TOFU — szerokie wejście, zdrowie holistyczne |
| **psychosen.pl** | Sen, higiena snu, chronobiologia, zaburzenia snu | psychozdrowie.online (test snu) + nurio.pl | TOFU/MOFU — specjalistyczna nisza snu |
| **psychodzisiaj.pl** | Codzienne emocje, relacje, stres, psychologia stosowana | nurio.pl (rozmowa z AI) + psychozdrowie.online | TOFU — masowy ruch na codzienne problemy |
| **jaksobieradzic.pl** | Techniki radzenia sobie, kryzysy życiowe, wsparcie | nurio.pl (natychmiastowe wsparcie) | MOFU — ludzie w konkretnym problemie |
| **sprawdzwypalenie.pl** | Wypalenie zawodowe: diagnoza, profilaktyka, regeneracja | psychozdrowie.online (test wypalenia) | MOFU/BOFU — test → diagnoza → pomoc |
| **testpredyspozycje.pl** | Testy osobowości, predyspozycje zawodowe, talenty | psychozdrowie.online (NEO-FFI, Gallup) | MOFU/BOFU — bezpośrednie CTA do testów |

### KLASTER ARCHAIOS (cyberbezpieczeństwo, AI, compliance) → 7 satelitów → 70 artykułów

**Produkty docelowe:**
- **archaios.ai** — platforma AI dla firm (Writer Pro, Redaktor, RAG, agenci)
- **twojamediacja.pl** — mediacje biznesowe i pracownicze (dla audytzespolu.pl)
- **analizastatystyczna.me** — usługi statystyczne (dla kontekstu akademickiego)

**Satelity i ich role w lejku:**

| Satelita | Tematyka | Główny produkt docelowy | Rola w lejku |
|----------|----------|------------------------|--------------|
| **testnis2.pl** | Testy gotowości NIS2, audyty compliance | archaios.ai (cybersecurity) | MOFU/BOFU — test → audyt → wdrożenie |
| **karynis2.pl** | Kary NIS2, odpowiedzialność zarządu, case studies | archaios.ai (unikanie kar) | TOFU/MOFU — strach jako motywator |
| **skanujfirme.pl** | Audyt NIS2 + RODO, skan bezpieczeństwa firmy | archaios.ai (pełny audyt) | MOFU — praktyczny scan → oferta |
| **audytzespolu.pl** | Diagnostyka zespołu, komunikacja, mediacje workplace | twojamediacja.pl + archaios.ai | MOFU — audyt zespołu → mediacja/AI |
| **onpremiseai.pl** | AI on-premise, dane lokalne, bezpieczeństwo wdrożeń | archaios.ai (wdrożenia lokalne) | MOFU/BOFU — decydenci IT szukający rozwiązań |
| **aidzisiaj.pl** | AI w polskim biznesie: narzędzia, case studies, regulacje | archaios.ai (pełna platforma) | TOFU — szerokie wejście AI w firmach |
| **ragpolska.pl** | RAG, LLM, wdrożenia AI enterprise, fine-tuning | archaios.ai (RAG/LLM) | MOFU/BOFU — technicy i decydenci |

---

## Wymagania dla KAŻDEGO artykułu

### Struktura techniczna (pola w CMS):
```yaml
title: "Tytuł SEO (50-65 znaków, keyword na początku)"
slug: "tytuł-z-myslnikami"
excerpt: "Lead 150-160 znaków — co czytelnik zyska"
content: "Pełna treść HTML (2000-4000 słów)"
category_slug: "slug-kategorii-z-yamla-domeny"
tags: "tag1, tag2, tag3, tag4, poziom-trudności"
reading_time: 12  # minuty
bibliography: "<ul><li>Autor, A. (2023). Tytuł. <em>Czasopismo</em>, vol(nr), ss. DOI</li></ul>"
is_published: true
is_featured: false  # true dla 2 najlepszych per domena
meta_title: "Tytuł | Nazwa Serwisu"
meta_description: "Opis SEO 150-160 znaków"
```

### Struktura treści artykułu:
1. **Hook** (1 akapit) — zaskakujący fakt, statystyka lub pytanie. Bez "W dzisiejszych czasach..."
2. **Problem** (2-3 akapity) — dlaczego to ważne, kogo dotyczy, skala zjawiska
3. **Rozwinięcie merytoryczne** (5-8 sekcji z H2/H3) — badania, mechanizmy, dane
4. **Praktyka** (2-3 sekcji) — co czytelnik może ZROBIĆ, konkretne kroki
5. **Podsumowanie** (1 akapit) — esencja, nie powtórka
6. **Bibliografia** — minimum 5 źródeł naukowych (prawdziwe DOI, prawdziwe czasopisma)

### Wymagania jakościowe:
- **Prawdziwe źródła** — cytuj istniejące badania z DOI. Nie wymyślaj autorów ani czasopism. Jeśli nie znasz dokładnego DOI — napisz "[DO WERYFIKACJI]" przy źródle.
- **Dane liczbowe** — statystyki, procenty, wielkości efektu. "Badania pokazują" to za mało — KTÓRE badania, JAKI wynik.
- **Poziom trudności** — każdy artykuł oznacz w tagach: `podstawowy`, `średniozaawansowany` lub `zaawansowany`
- **Brak AI-mowy** — zero "w dzisiejszym dynamicznie zmieniającym się świecie", "warto zauważyć że", "nie ulega wątpliwości". Pisz jak dziennikarz naukowy.
- **Engagement** — pytania do czytelnika, analogie, case studies, mini-scenariusze
- **Wewnętrzne linkowanie** — w 3-4 artykułach per domenę dodaj linki do innych artykułów tej samej domeny

### CTA (Call to Action) — naturalne, nie nachalne:
- **Inline CTA** (w treści): "Sprawdź swój poziom wypalenia testem Maslach w psychozdrowie.online" — osadzony w kontekście, nie banner
- **End CTA** (na końcu): "Jeśli rozpoznajesz u siebie te objawy, rozmowa z Nurią (nurio.pl) może być pierwszym krokiem" — empatyczne, nie sprzedażowe
- **Sidebar CTA** (automatyczny z YAML): product matching po tagach — nie pisz tego w treści, silnik dopasuje

### Proporcja typów w lejku (per domena, 10 artykułów):
- **4 × TOFU** (Top of Funnel) — edukacja, świadomość, szerokie tematy SEO
- **3 × MOFU** (Middle of Funnel) — porównania, "jak wybrać", poradniki zaawansowane
- **2 × BOFU** (Bottom of Funnel) — case studies, "jak zaczać", bezpośrednie CTA do produktu
- **1 × Pillar/Cornerstone** — obszerny artykuł 4000+ słów, linkowany z pozostałych

---

## ARTYKUŁY PER DOMENA — tematy do wygenerowania

### 1. zdrowie.fit (NURIO cluster — zdrowie holistyczne)
Kategorie: `zdrowie`, `psychiczne`, `odzywianie`, `fitness`, `wellbeing`

Generuj 10 artykułów na tematy łączące ciało z umysłem. Każdy musi mieć aspekt psychosomatyczny. Zadbaj o mix: odżywianie × mózg, ruch × nastrój, sen × regeneracja, stres × ciało, mikrobiom × psychika. Produkt docelowy: nurio.pl (wsparcie emocjonalne), psychozdrowie.online (testy).

### 2. psychosen.pl (NURIO cluster — nauka o śnie)
Kategorie: `higiena-snu`, `zaburzenia-snu`, `badania`

Generuj 10 artykułów o śnie. Mix: chronotypy, bezsenność, CBTI, melatonina, sen a pamięć, ekrany × sen, polifazowy sen, sny i podświadomość, sen a depresja, higiena snu evidence-based. Dark mode na stronie — ton spokojny, "nocny". Produkt: psychozdrowie.online (test snu).

### 3. psychodzisiaj.pl (NURIO cluster — codzienna psychologia)
Kategorie: `psychologia-dnia`, `emocje`, `relacje`

Generuj 10 artykułów o codziennych problemach emocjonalnych. Mix: prokrastynacja, gaslighting w relacjach, lęk społeczny, radzenie sobie z gniewem, people-pleasing, granice psychologiczne, attachment styles w dorosłości, efekt Dunninga-Krugera w pracy, emocje w podejmowaniu decyzji, toxic positivity. Produkt: nurio.pl (codzienna rozmowa z AI).

### 4. jaksobieradzic.pl (NURIO cluster — radzenie sobie)
Kategorie: `radzenie-sobie`, `techniki`, `wsparcie`

Generuj 10 artykułów typu "jak sobie radzić z X". Mix: żałoba, rozwód, utrata pracy, lęk przed przyszłością, syndrom oszusta, wypalenie rodzicielskie, samotność, trudne rozmowy, kryzys wartości, opieka nad osobą chorą. MOFU — ludzie aktywnie szukający pomocy. Produkt: nurio.pl (natychmiastowe wsparcie).

### 5. sprawdzwypalenie.pl (NURIO cluster — wypalenie zawodowe)
Kategorie: `wypalenie`, `profilaktyka`, `regeneracja`

Generuj 10 artykułów o wypaleniu zawodowym. Mix: test Maslach (BOFU), fazy wypalenia, wypalenie w zawodach pomocowych, wypalenie a depresja (różnice), quiet quitting, powrót po wypaleniu, rola przełożonego, work-life balance evidence-based, wypalenie w IT, fizjologia stresu chronicznego. Produkt: psychozdrowie.online (test wypalenia).

### 6. testpredyspozycje.pl (NURIO cluster — testy i predyspozycje)
Kategorie: `testy`, `kariera`, `rozwoj`

Generuj 10 artykułów o testach psychologicznych i predyspozycjach. Mix: Big Five a kariera, CliftonStrengths w praktyce, MBTI vs Big Five (porównanie naukowe), inteligencja emocjonalna w pracy, neuroplastyczność a rozwój talentów, testy predyspozycji — co naprawdę mierzą, introwersja w świecie ekstrawertyków, flow state, mocne strony w zespole, talenty wrodzone vs wyuczone. BOFU — bezpośrednie CTA do testów. Produkt: psychozdrowie.online.

### 7. testnis2.pl (ARCHAIOS cluster — gotowość NIS2)
Kategorie: `audyt`, `regulacje`, `wdrozenia`

Generuj 10 artykułów o dyrektywie NIS2. Mix: checklist gotowości NIS2, kogo obowiązuje NIS2 w Polsce, różnice NIS1 vs NIS2, wymagania dla MŚP, raportowanie incydentów 24/72h, zarząd a odpowiedzialność NIS2, NIS2 vs RODO — co się nakłada, łańcuch dostaw w NIS2, certyfikacje wymagane, test gotowości online. Produkt: archaios.ai (audyt cybersecurity).

### 8. karynis2.pl (ARCHAIOS cluster — kary i sankcje NIS2)
Kategorie: `kary`, `prawo`, `case-studies`

Generuj 10 artykułów o karach i odpowiedzialności za NIS2. Mix: wysokość kar (€10M / 2% obrotu), odpowiedzialność osobista zarządu, case studies z Europy (pierwsze kary), timeline wdrożenia w Polsce, porównanie kar NIS2 vs RODO, ubezpieczenie cyber, koszty braku compliance, audyt vs kara — ROI, sektory najwyższego ryzyka, jak przygotować firmę. TOFU/MOFU — strach jako motywator, ale z rozwiązaniem. Produkt: archaios.ai.

### 9. skanujfirme.pl (ARCHAIOS cluster — audyty bezpieczeństwa)
Kategorie: `nis2`, `rodo`, `cyberbezpieczenstwo`

Generuj 10 artykułów o audytach bezpieczeństwa firm. Mix: co to jest audyt cyberbezpieczeństwa, RODO w 2026 — co się zmieniło, phishing w MŚP — statystyki, ransomware w polskich firmach, polityka haseł evidence-based, backup 3-2-1, szkolenia pracowników z cyberhigieny, IOD — kto musi mieć, audyt NIS2 krok po kroku, monitoring bezpieczeństwa 24/7. Produkt: archaios.ai (pełny skan bezpieczeństwa).

### 10. audytzespolu.pl (ARCHAIOS cluster — diagnostyka zespołów)
Kategorie: `audyt-zespolu`, `mediacje`, `compliance`

Generuj 10 artykułów o diagnostyce i usprawnianiu zespołów. Mix: skala dysfunkcji zespołu Lencioniego, mobbing — obowiązki pracodawcy, mediacja pracownicza krok po kroku, komunikacja NVC w zespole, audyt kultury organizacyjnej, wypalenie zespołowe, onboarding a retencja, feedback 360° — jak robić dobrze, różnorodność w zespole, compliance pracowniczy a NIS2. Produkty: twojamediacja.pl + archaios.ai.

### 11. onpremiseai.pl (ARCHAIOS cluster — AI on-premise)
Kategorie: `ai-on-premise`, `bezpieczenstwo`, `compliance`

Generuj 10 artykułów o wdrożeniach AI na serwerach klienta. Mix: chmura vs on-premise — kiedy co, RODO a dane w AI (gdzie trzymać), llama.cpp — LLM na własnym serwerze, koszt wdrożenia AI on-premise, TCO cloud vs local, RAG na danych firmowych, fine-tuning na danych wewnętrznych, AI Act a lokalne modele, bezpieczeństwo danych w LLM, case study: wdrożenie AI w polskiej firmie. Produkt: archaios.ai (wdrożenia lokalne).

### 12. aidzisiaj.pl (ARCHAIOS cluster — AI w polskim biznesie)
Kategorie: `ai-w-biznesie`, `narzedzia`, `regulacje`

Generuj 10 artykułów o AI w polskim kontekście biznesowym. Mix: AI Act — co musi wiedzieć polska firma, ChatGPT vs Claude vs Gemini — porównanie dla firm, automatyzacja procesów AI — od czego zacząć, AI w obsłudze klienta, AI w HR — rekrutacja i ocena, ROI z wdrożenia AI, etyka AI w firmie, AI w marketingu — case studies PL, low-code AI tools, polska strategia AI 2026. TOFU — szerokie wejście. Produkt: archaios.ai.

### 13. ragpolska.pl (ARCHAIOS cluster — RAG i LLM enterprise)
Kategorie: `rag`, `ai-w-biznesie`, `wdrozenia`

Generuj 10 artykułów technicznych o RAG i LLM. Mix: co to jest RAG i dlaczego to game-changer, chunking strategies — porównanie, vector databases — Chroma vs Qdrant vs Pinecone, embedding models — benchmark PL, hallucynacje LLM — jak RAG pomaga, RAG vs fine-tuning — kiedy co, bezpieczeństwo danych w RAG pipeline, wdrożenie RAG na dokumentacji firmowej, ewaluacja RAG — metryki jakości, case study: RAG w polskiej kancelarii. MOFU/BOFU — techniczna publiczność. Produkt: archaios.ai.

---

## Format wyjściowy

Dla KAŻDEJ domeny generuj output w formacie:

```markdown
## [NAZWA DOMENY] — [domena.tld]

### Artykuł 1/10: [TYTUŁ]
- **Slug:** tytuł-z-myślnikami
- **Kategoria:** [slug]
- **Tagi:** tag1, tag2, tag3, poziom-trudności
- **Typ lejka:** TOFU/MOFU/BOFU
- **CTA docelowe:** [produkt + kontekst]
- **Czas czytania:** X min
- **Featured:** tak/nie

#### Treść:
[PEŁNA TREŚĆ ARTYKUŁU W HTML — z <h2>, <h3>, <p>, <ul>, <blockquote>]

#### Bibliografia:
[MIN. 5 ŹRÓDEŁ APA 7 z DOI lub [DO WERYFIKACJI]]

---
```

## Zasady końcowe

1. **Generuj po jednej domenie** — zapytaj mnie "generuję [nazwa domeny], OK?" przed każdą
2. **Nie skracaj treści** — każdy artykuł 2000-4000 słów, pełna treść, nie streszczenie
3. **Nie powtarzaj tematów** między domenami — jeśli wypalenie jest w sprawdzwypalenie.pl, nie pisz o wypaleniu w jaksobieradzic.pl (chyba że z innego kąta, np. "jak pomóc wypalonemupartnerowi")
4. **SEO-first tytuly** — keyword na początku, max 65 znaków, click-worthy ale nie clickbait
5. **Każdy artykuł to samodzielna wartość** — czytelnik ma wynieść wiedzę NAWET jeśli nie kliknie CTA
6. **Ton:** dziennikarz naukowy z empatią, nie wykładowca akademicki
7. **CTA max 2 per artykuł** — jeden inline, jeden na końcu. Naturalne, nie nachalne.
