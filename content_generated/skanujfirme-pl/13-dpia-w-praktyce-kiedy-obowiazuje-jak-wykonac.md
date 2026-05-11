---
title: "DPIA w praktyce — kiedy obowiązuje, jak wykonać, szablon oceny"
slug: "dpia-w-praktyce-kiedy-obowiazuje-jak-wykonac"
excerpt: "Ocena skutków dla ochrony danych (DPIA) wg art. 35 RODO. Kiedy musisz ją wykonać, kiedy nie, jaką metodykę zastosować, jak wygląda dobry raport DPIA."
category_slug: "rodo"
tags: "DPIA, art. 35 RODO, ocena skutków, IOD, EROD, metodyka, szablon, średniozaawansowany"
reading_time: 14
is_published: true
is_featured: false
meta_title: "DPIA w praktyce 2026 — kiedy, jak, szablon raportu (RODO art. 35)"
meta_description: "Pełna metodyka DPIA dla polskiej firmy. Kiedy obowiązuje, jak ocenić ryzyko, jak udokumentować, kiedy konsultować z UODO. Z gotową strukturą raportu."
funnel: "MOFU-BOFU"
author_slug: "marek-porycki"
related_slugs: "audyt-rodo-art-32-bezpieczenstwo-techniczne,audyt-rodo-krok-po-kroku,audyt-umow-powierzenia-art-28-rodo,audyt-transferow-do-krajow-trzecich-scc-tia,kompletny-audyt-firmy-2026"
product_slugs: ""
---

DPIA — Data Protection Impact Assessment, po polsku "ocena skutków dla ochrony danych" — jest jednym z najczęściej źle wykonywanych elementów wdrożenia RODO w polskich firmach. Częsta sytuacja: firma wpisuje DPIA do polityki, ma jeden szablon, wypełnia formalnie raz na pół roku z myślą "żeby było", ale nigdy nie służy on rzeczywistej decyzji o tym, czy operację przetwarzania w ogóle uruchomić, zmodyfikować, czy zaniechać. To jest DPIA-fasada.

DPIA wykonana właściwie jest narzędziem decyzyjnym. Jest analizą ryzyka skoncentrowaną na prawach i wolnościach osób fizycznych. Pokazuje zarządowi, że konkretna operacja przetwarzania (np. wdrożenie monitoringu wideo z analizą emocji, czy uruchomienie sklepu online z profilowaniem behawioralnym) ma takie a takie ryzyka, które są niwelowane przez takie a takie środki, a ryzyko rezydualne mieści się w akceptowanym progu (lub nie — i wtedy operacja nie powinna ruszyć bez konsultacji z UODO).

Ten tekst jest pełnym przewodnikiem operacyjnym po DPIA: kiedy jest obowiązkowa, jaką metodyką ją wykonać, jak wygląda raport, kiedy konsultować z UODO. Strukturę raportu DPIA podajemy w formie szablonu, którego można użyć w pracy zawodowej IOD. Adresat: IOD/DPO, dyrektorzy projektów wdrażających nowe operacje przetwarzania, członkowie zespołów compliance, kierownicy działów IT odpowiadający za nowe systemy.

## Podstawa prawna i kiedy DPIA jest obowiązkowa

Art. 35 ust. 1 RODO: "Jeżeli dany rodzaj przetwarzania — w szczególności z użyciem nowych technologii — ze względu na swój charakter, zakres, kontekst i cele z dużym prawdopodobieństwem może powodować wysokie ryzyko naruszenia praw lub wolności osób fizycznych, administrator przed rozpoczęciem przetwarzania dokonuje oceny skutków planowanych operacji przetwarzania dla ochrony danych osobowych".

Trzy elementy są kluczowe: (1) "z dużym prawdopodobieństwem" — czyli nie każde ryzyko, tylko prawdopodobne, (2) "wysokie ryzyko" — nie jakiekolwiek, tylko wysokie, (3) "przed rozpoczęciem" — DPIA jest narzędziem ex ante, nie ex post.

Art. 35 ust. 3 wymienia trzy obligatoryjne przypadki:
- (a) systematyczna, kompleksowa ocena czynników osobowych, oparta na zautomatyzowanym przetwarzaniu, w tym profilowaniu, mająca skutki prawne lub w podobny sposób istotnie wpływająca na osobę
- (b) przetwarzanie na dużą skalę szczególnych kategorii danych (art. 9) lub danych dotyczących wyroków skazujących (art. 10)
- (c) systematyczne monitorowanie na dużą skalę miejsc publicznych

Grupa Robocza Art. 29 (poprzednik EROD) w wytycznych WP248 z 2017 r. (aktualnych dzisiaj) wskazała dziewięć kryteriów. Operacja, która spełnia dwa lub więcej z nich, powinna być traktowana jako wymagająca DPIA:

1. ocenianie lub punktacja (scoring)
2. zautomatyzowane podejmowanie decyzji o skutkach prawnych
3. systematyczne monitorowanie
4. dane wrażliwe lub o szczególnym charakterze
5. przetwarzanie na dużą skalę
6. łączenie zbiorów danych
7. dane osób wrażliwych (dzieci, pracowników, osób chorych)
8. innowacyjne wykorzystanie technologii (AI, IoT, biometria)
9. uniemożliwianie korzystania z prawa lub usługi

UODO opublikował w 2018 r. (z aktualizacjami) listę rodzajów operacji bezwzględnie wymagających DPIA — m.in. monitoring pracowników, profilowanie konsumentów na dużą skalę, monitoring CCTV w przestrzeni publicznej, przetwarzanie danych biometrycznych do identyfikacji, AI w decyzjach personalnych. Tę listę audytor i IOD powinni znać dokładnie.

## Kiedy DPIA NIE jest obowiązkowa (i ważne uściślenia)

Częsta pułapka: zespoły wykonują DPIA dla operacji, które tego nie wymagają (marnując zasoby), lub odwrotnie — pomijają DPIA dla operacji, które wymagają (narażając firmę).

DPIA nie jest wymagana, gdy:
- operacja nie generuje wysokiego ryzyka (np. typowa korespondencja e-mailowa z klientami w kontekście pre-RODO ustalonego)
- operacja była już oceniona w ramach DPIA na poziomie kategorii (jeśli kontekst się nie zmienił)
- art. 35 ust. 10 — gdy podstawa prawna jest w prawie UE lub państwa członkowskiego i ocena skutków była przeprowadzona na poziomie legislacyjnym

Wyjątki nie zmieniają jednak ogólnej zasady, że formalna analiza ryzyka jest zawsze potrzebna (na podstawie art. 32 ust. 2 RODO). Granica jest taka: DPIA jest sformalizowaną, pogłębioną analizą ryzyka dla operacji wysokiego ryzyka. Dla pozostałych operacji wystarcza standardowa analiza ryzyka. Brak żadnej analizy = naruszenie RODO niezależnie od tego, czy DPIA była obowiązkowa.

## Metodyka DPIA — siedem etapów

Etapy DPIA wynikające z art. 35 ust. 7 RODO oraz wytycznych EROD. W praktyce można rozdzielić proces na siedem etapów wykonywanych sekwencyjnie.

**Etap 1: Identyfikacja potrzeby DPIA.** Konsultacja z IOD, ocena, czy operacja spełnia kryteria z art. 35 ust. 3 lub WP248. Output: notatka uzasadniająca decyzję o przeprowadzeniu DPIA (lub odmowie). Notatkę zachowuje się w dokumentacji — UODO przy kontroli pyta, czy decyzja "DPIA nie była wymagana" jest udokumentowana.

**Etap 2: Opis operacji przetwarzania.** Szczegółowy opis: cele, kategorie danych, kategorie podmiotów, źródła, odbiorcy, okresy przechowywania, technologia. Mapa przepływu danych (data flow diagram) jest tutaj wartościowa.

**Etap 3: Ocena konieczności i proporcjonalności.** Czy cel można osiągnąć mniej inwazyjnie? Czy zakres danych jest minimalny? Czy okres przechowywania jest adekwatny? Czy podmioty mają realne kanały realizacji praw?

**Etap 4: Identyfikacja ryzyk dla praw i wolności.** Konkretne ryzyka: utrata kontroli nad danymi, dyskryminacja, kradzież tożsamości, naruszenie tajemnicy zawodowej, dyskryminacja społeczna. Każde ryzyko z prawdopodobieństwem (niskie/średnie/wysokie) i wagą wpływu (niska/średnia/wysoka). Metodyka oceny — typowo macierz 3×3 lub 5×5.

**Etap 5: Środki techniczne i organizacyjne mitygujące ryzyko.** Dla każdego ryzyka — konkretne środki: szyfrowanie, pseudonimizacja, ograniczenie dostępu, audyt logów, szkolenie zespołu, polityka retencji, klauzula informacyjna. Środki muszą być proporcjonalne — DPIA pokazuje, jak.

**Etap 6: Ocena ryzyka rezydualnego.** Po zastosowaniu środków — jakie ryzyko pozostaje? Czy jest akceptowalne? Jeśli wysokie ryzyko nie zostało zniwelowane do średniego lub niskiego — wymagana konsultacja z UODO przed rozpoczęciem przetwarzania (art. 36).

**Etap 7: Dokumentacja i monitorowanie.** Pełny raport DPIA, zaakceptowany przez administratora (zarząd lub jego upoważniony przedstawiciel). Plan monitorowania — kiedy DPIA zostanie zaktualizowana (typowo: przy każdej istotnej zmianie operacji lub minimum co 24 miesiące).

## Struktura raportu DPIA

Raport DPIA to dokument, który audytor RODO (lub UODO w przypadku kontroli) traktuje jako dowód, że administrator wykonał obowiązek art. 35. Słaba struktura = słaba ochrona. Pełna struktura raportu, do bezpośredniego użycia jako szablon:

**Sekcja 1: Metryka dokumentu.**
- Tytuł operacji przetwarzania
- Numer i wersja DPIA
- Data utworzenia, data aktualizacji
- Autor (typowo IOD)
- Akceptujący (administrator danych — zarząd)
- Status: roboczy / zaakceptowany / wymagający konsultacji z UODO

**Sekcja 2: Opis operacji.**
- Cel(e) przetwarzania
- Kategorie danych
- Kategorie podmiotów
- Źródła danych
- Odbiorcy (wewnętrzni, zewnętrzni procesorzy)
- Transfery do krajów trzecich (jeśli dotyczy)
- Okresy przechowywania
- Technologia (systemy, narzędzia, dostawcy)
- Mapa przepływu danych (diagram)

**Sekcja 3: Analiza konieczności i proporcjonalności.**
- Podstawa prawna z uzasadnieniem
- Minimalizacja: czy cel można osiągnąć mniejszym zakresem danych?
- Klauzula informacyjna: czy podmiot ma pełną informację?
- Realizacja praw podmiotów: czy procedury istnieją i są wykonalne?

**Sekcja 4: Identyfikacja i ocena ryzyk.**
Tabela ryzyk:

| Lp. | Ryzyko | Prawdopodobieństwo | Wpływ | Ocena (P×W) |
|---|---|---|---|---|
| 1 | Nieuprawniony dostęp do bazy klientów | Średnie | Wysoki | Wysokie |
| 2 | Profilowanie skutkujące dyskryminacją | Niskie | Wysoki | Średnie |
| 3 | Utrata danych (brak backupu) | Niskie | Wysoki | Średnie |
| ... | | | | |

**Sekcja 5: Środki mitygujące.**
Dla każdego ryzyka — wykaz konkretnych środków technicznych i organizacyjnych.

**Sekcja 6: Ryzyko rezydualne.**
- Ocena po zastosowaniu środków
- Czy jest akceptowalne?
- Decyzja: kontynuować / konsultować z UODO / zmodyfikować operację / zaniechać

**Sekcja 7: Plan monitorowania.**
- Data następnej aktualizacji
- Sytuacje wyzwalające ad hoc aktualizację
- Osoba odpowiedzialna

**Sekcja 8: Załączniki.**
- Wyniki konsultacji z podmiotami danych lub ich przedstawicielami (jeśli przeprowadzono)
- Opinia IOD
- Decyzje administratora

Tak ustrukturyzowany raport DPIA jest jednocześnie dokumentem decyzyjnym i dowodem zgodności w razie kontroli. W audycie RODO audytor szuka tego formatu — jego brak skutkuje ustaleniem o niedostatecznej dokumentacji art. 35.

Jeśli pracujesz jako IOD i chcesz mieć gotowy szablon raportu DPIA w formacie DOCX z wszystkimi sekcjami, tabelami i przykładami wypełnienia dla typowych operacji (monitoring wideo, marketing behawioralny, profilowanie HR, biometria) — przygotowujemy taki pakiet jako część newslettera skanujfirme.pl. Zapis bez zobowiązań.

## Konsultacja z UODO (art. 36)

Art. 36 RODO: administrator przed rozpoczęciem przetwarzania konsultuje się z organem nadzorczym, jeżeli DPIA wskazuje, że przetwarzanie powodowałoby wysokie ryzyko, gdyby administrator nie zastosował środków w celu zminimalizowania tego ryzyka.

W praktyce: konsultacja jest wymagana, gdy ryzyko rezydualne po wdrożeniu środków pozostaje wysokie. UODO ocenia operację, może zaproponować dodatkowe środki, w skrajnych przypadkach zakazać.

Termin reakcji UODO: do 8 tygodni z możliwością wydłużenia o 6 tygodni. W tym czasie nie można rozpocząć przetwarzania. To istotne dla planowania projektu — operacja wymagająca konsultacji UODO ma minimum 8-tygodniowe opóźnienie w stosunku do planu pierwotnego.

Konsultacje są w Polsce rzadkością — UODO publikuje rocznie raport z liczby konsultacji, typowo kilkadziesiąt. To oznacza, że firmy albo dobrze projektują środki mitygujące (i ryzyko rezydualne nie jest wysokie), albo nie robią DPIA wcale (i nie wiedzą, że powinny konsultować). Drugi scenariusz jest częstszy.

## Częste błędy w wykonywaniu DPIA

**Błąd 1: DPIA wykonywana ex post.** Operacja już ruszyła, "trzeba dorobić DPIA". To narusza ducha i literę art. 35 — DPIA jest narzędziem ex ante.

**Błąd 2: Generyczność.** Szablon wypełniony ogólnikami ("ryzyko: utrata danych — środek: szyfrowanie"), bez konkretów. UODO odrzuca takie DPIA w kontrolach.

**Błąd 3: Brak udziału biznesu.** DPIA wykonana wyłącznie przez IOD bez konsultacji z właścicielem operacji. Wynik: środki nieadekwatne lub niewykonalne operacyjnie.

**Błąd 4: Brak udziału podmiotów danych.** Art. 35 ust. 9 wskazuje, że administrator powinien "w razie potrzeby zasięgnąć opinii osób, których dane dotyczą lub ich przedstawicieli". To nie jest często wykonywane, ale dla operacji wysokiego ryzyka (np. monitoring pracowników) — istotne.

**Błąd 5: Brak monitorowania.** DPIA wykonana raz, operacja się zmienia, DPIA nie jest aktualizowana. Po 12 miesiącach dokument jest oderwany od rzeczywistości.

**Błąd 6: Brak akceptacji administratora.** DPIA podpisana tylko przez IOD, bez akceptacji zarządu. To oznacza, że administrator danych nie wyraził formalnej decyzji o akceptacji ryzyka rezydualnego.

## Trzy pytania kontrolne dla IOD przed DPIA

**Pierwsze.** Czy mam pełną mapę operacji przetwarzania wymagających DPIA? Bez tego nie wiem, ile DPIA muszę przygotować. Klasyczne źródło: rejestr czynności przetwarzania (RCP) + analiza ryzyka per operacja + lista UODO operacji bezwzględnie wymagających.

**Drugie.** Czy proces DPIA jest zintegrowany z procesem wdrażania nowych projektów IT? Jeśli DPIA "doczepia się" po zakończeniu projektu, jest fasadą. Jeśli jest częścią gate'u w project management — jest narzędziem decyzyjnym.

**Trzecie.** Czy zarząd wie, że DPIA jest narzędziem decyzyjnym? Jeśli administrator danych traktuje DPIA jako formalność IOD, nie podejmuje świadomych decyzji o akceptacji ryzyka. To powracający temat w decyzjach UODO — zarząd ponosi odpowiedzialność za decyzje DPIA.

## Esencja

DPIA jest sformalizowaną, pogłębioną analizą ryzyka dla operacji wysokiego ryzyka przetwarzania danych osobowych. Obligatoryjna w trzech przypadkach z art. 35 ust. 3 oraz w operacjach spełniających minimum dwa z dziewięciu kryteriów WP248. Brak DPIA dla operacji wymagającej = naruszenie RODO niezależnie od pozostałych zabezpieczeń.

Metodyka siedmioetapowa: (1) identyfikacja potrzeby, (2) opis operacji, (3) konieczność i proporcjonalność, (4) identyfikacja ryzyk, (5) środki mitygujące, (6) ryzyko rezydualne, (7) monitorowanie. Każdy etap musi być udokumentowany. Output to raport DPIA w spójnej strukturze, akceptowany przez administratora.

Konsultacja z UODO (art. 36) wymagana, gdy ryzyko rezydualne po mitygacjach pozostaje wysokie. Termin reakcji UODO: do 8 tygodni, możliwość wydłużenia o 6 tygodni. Projekty wymagające konsultacji muszą uwzględnić ten bufor.

Klasyczne błędy: DPIA wykonywana ex post, generyczność szablonów, brak udziału biznesu, brak akceptacji administratora, brak aktualizacji. Każdy z tych błędów jest osobno punktowany w audycie i może skutkować ustaleniem o naruszeniu art. 35.

DPIA wykonana właściwie jest narzędziem zarządu, nie tylko IOD. Pokazuje decydentom, że konkretna operacja niesie konkretne ryzyko, które jest niwelowane lub akceptowane. Bez tej świadomości administrator nie pełni roli przewidzianej w RODO — pełni rolę formalnego sygnatariusza dokumentu, który nie rozumie.

W audycie RODO art. 35 jest jednym z najszybciej weryfikowanych obszarów — audytor patrzy na listę operacji wysokiego ryzyka i sprawdza, czy dla każdej istnieje aktualna DPIA. Luki są widoczne w 30 minut.

---

<ul>
<li>Rozporządzenie Parlamentu Europejskiego i Rady (UE) 2016/679 z dnia 27 kwietnia 2016 r. (RODO), art. 35 — Ocena skutków dla ochrony danych, art. 36 — Uprzednie konsultacje. https://eur-lex.europa.eu/eli/reg/2016/679/oj</li>
<li>Grupa Robocza Art. 29 (2017). <em>Wytyczne w sprawie oceny skutków dla ochrony danych (DPIA) WP248 rev.01</em>. (Aktualne dzisiaj jako wytyczne EROD). https://ec.europa.eu/newsroom/article29/items/611236</li>
<li>EROD/EDPB (2020). <em>Guidelines 05/2020 on consent under Regulation 2016/679</em>. https://www.edpb.europa.eu/our-work-tools/our-documents/guidelines/</li>
<li>UODO (2018, z aktualizacjami). <em>Komunikat Prezesa UODO w sprawie wykazu rodzajów operacji przetwarzania danych osobowych wymagających DPIA</em>. https://uodo.gov.pl/pl/138</li>
<li>UODO (2024). <em>Sprawozdanie roczne Prezesa UODO 2023 — sekcja DPIA i konsultacje uprzednie</em>. https://uodo.gov.pl/pl/sprawozdania-roczne</li>
<li>ENISA (2017). <em>Handbook on Security of Personal Data Processing</em>. https://www.enisa.europa.eu/publications/handbook-on-security-of-personal-data-processing</li>
<li>CNIL (2018). <em>PIA — Privacy Impact Assessment — Methodology</em>. Commission Nationale de l'Informatique et des Libertés. https://www.cnil.fr/en/privacy-impact-assessment-pia</li>
<li>ISO/IEC 29134:2017. <em>Guidelines for privacy impact assessment</em>. International Organization for Standardization.</li>
<li>ICO (UK). <em>Data protection impact assessments (DPIAs) — detailed guidance</em>. https://ico.org.uk/for-organisations/guide-to-data-protection/guide-to-the-general-data-protection-regulation-gdpr/data-protection-impact-assessments-dpias/</li>
<li>Polska Ustawa z dnia 10 maja 2018 r. o ochronie danych osobowych (Dz.U. 2018 poz. 1000 ze zm.)</li>
</ul>
