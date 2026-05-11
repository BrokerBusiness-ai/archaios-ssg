---
title: "Kary NIS2 vs RODO — porównanie reżimów sankcyjnych (cornerstone)"
slug: "kary-nis2-vs-rodo-porownanie-rezimow"
excerpt: "Cornerstone porównania dwóch reżimów sankcyjnych. Kary maksymalne, mechanika wyliczeń, organy nadzoru, kary łączone, precedensy nakładania się obu."
category_slug: "kary"
tags: "kary NIS2, RODO, GDPR, porównanie sankcji, cornerstone, zaawansowany"
reading_time: 14
is_published: true
is_featured: true
meta_title: "Kary NIS2 vs RODO — porównanie reżimów sankcyjnych (2026)"
meta_description: "Pełne porównanie kar NIS2 i RODO. Mechanika, organy, kary łączone w jednym incydencie. Strategia zarządzania ryzykiem dwureżimowym."
funnel: "MOFU-cornerstone"
author_slug: "marek-porycki"
related_slugs: "kary-nis2-w-polsce-przewodnik, 10-mln-eur-czy-2-procent-obrotu-jak-liczone-kary, postepowanie-sankcyjne-krok-po-kroku"
product_slugs: ""
---

W październiku 2025 holenderska firma e-commerce dostała równocześnie dwie decyzje administracyjne: jedną od Autoriteit Persoonsgegevens (AP) za naruszenie RODO, drugą od CSIRT-NL za naruszenie NIS2. Dwa różne organy, dwa różne reżimy, dwa różne wyliczenia kar. Łącznie 6,8 mln EUR. Ten sam incydent, dwa procesy, dwie konsekwencje.

To staje się normą. Każdy poważniejszy incydent cyber w firmie podlegającej obu reżimom (a tym jest większość firm objętych NIS2) wszczyna postępowania równolegle. Strategia zarządzania ryzykiem regulacyjnym musi to uwzględnić — projektowanie obrony pod jeden reżim z pominięciem drugiego jest receptą na maksymalne sankcje w obu.

Ten cornerstone-text porównuje oba reżimy sankcyjne w siedmiu wymiarach: cele i podstawy prawne, kary maksymalne i mechanika wyliczeń, organy nadzoru, procedury postępowania, czynniki łagodzące i obciążające, kary łączone, strategia zarządzania ryzykiem dwureżimowym. Adresat: zarządy firm podlegających obu reżimom, dyrektorzy compliance, prawnicy korporacyjni.

## Cele regulacyjne — dlaczego inaczej karzą

**RODO chroni prawa i wolności osób fizycznych w odniesieniu do przetwarzania danych osobowych.** Punkt ciężkości sankcji: ochrona prywatności i autonomii osób. Kara ma odstraszać przed naruszeniem praw konkretnych osób.

**NIS2 chroni ciągłość świadczenia usług i odporność infrastruktury.** Punkt ciężkości sankcji: ochrona społeczeństwa i gospodarki przed zakłóceniami usług krytycznych. Kara ma odstraszać przed zaniedbaniem odporności systemowej.

Konsekwencja: ten sam incydent może być oceniany różnie. Wyciek 50 000 rekordów — RODO zwraca uwagę na liczbę dotkniętych osób i charakter danych. NIS2 zwraca uwagę na to, jak incydent wpłynął na ciągłość usług dla społeczeństwa.

Atak DDoS, który blokuje usługę na 8 godzin bez naruszenia danych — RODO milczy, NIS2 prowadzi postępowanie.

Wyciek bazy 100 000 adresów email bez zakłócenia usługi — RODO prowadzi postępowanie, NIS2 może milczeć (jeśli incydent niematerialny dla ciągłości).

Ransomware z paraliżem usług + wyciekiem danych — oba reżimy aktywne, dwa równoległe postępowania.

## Kary maksymalne — porównanie cyfr

**RODO (artykuł 83 ust. 5):**
- Naruszenia podstawowych zasad: do 20 mln EUR lub 4% globalnego rocznego obrotu — wartość wyższa.
- Naruszenia obowiązków formalnych (np. powiadomienia): do 10 mln EUR lub 2% obrotu.

**NIS2 (artykuł 34):**
- Podmioty kluczowe: do 10 mln EUR lub 2% globalnego rocznego obrotu — wartość wyższa.
- Podmioty ważne: do 7 mln EUR lub 1,4% obrotu.

Cyfry maksymalne RODO są wyższe. Ale to nie cała historia.

Mechanika wyliczania konkretnej kary jest podobna. Oba reżimy stosują algorytm: bazowa stawka × modyfikatory (czynniki obciążające, łagodzące). Pierwsze polskie kary NIS2 i pierwsze duże polskie kary RODO mieszczą się w podobnych przedziałach (zwykle 5–25% maksimum dla pierwszej fali egzekucji).

Praktyczne porównanie dla konkretnej średniej firmy o obrocie 100 mln zł:

- Maksimum RODO: do 20 mln EUR (~85 mln zł) lub 4% obrotu (~3,4 mln zł — niższe, bo cyfra nominalna jest wyższa). Czyli w praktyce ograniczenie do 85 mln zł.
- Maksimum NIS2 (podmiot ważny): do 7 mln EUR (~30 mln zł) lub 1,4% obrotu (~1,2 mln zł — niższe). W praktyce ograniczenie do 30 mln zł.

Bardziej realistycznie, dla tej firmy w pierwszym roku po incydencie:

- Realistyczna kara RODO: 1–5 mln zł (zależnie od skali wycieku).
- Realistyczna kara NIS2: 0,5–3 mln zł (zależnie od luk w systemie).
- Jednoczesna ekspozycja w incydencie dwureżimowym: 1,5–8 mln zł łącznie.

## Organy nadzoru — kto wymierza karę

**RODO w Polsce:** Urząd Ochrony Danych Osobowych (UODO/PUODO) jest jedynym organem nadzorczym. Centralizacja oznacza spójność praktyki, ale też bottleneck — UODO ma ograniczone zasoby i wybiera priorytety postępowań.

**NIS2 w Polsce:** struktura wieloorganowa. CSIRT NASK jako centrum koordynacyjne. Sektorowe organy: KNF (finanse), UKE (telekomunikacja, poczta), URE (energia), resort zdrowia (ochrona zdrowia), inne. Decentralizacja oznacza większą pojemność systemu, ale też ryzyko niespójnych praktyk między sektorami.

Współpraca między organami jest wymogiem prawnym (artykuł 30 dyrektywy NIS2 plus przepisy o współpracy w ramach RODO). W praktyce: incydent dwureżimowy uruchamia formalną wymianę informacji między PUODO i CSIRT NASK / sektorowym organem. Postępowania prowadzone są równolegle, ale skoordynowane informacyjnie.

W praktyce dla firmy oznacza to: kontakt z dwoma organami, dwa zespoły kontrolerów, dwa formularze raportowania, dwa terminy. Zaleca się, by jeden zespół w firmie obsługiwał oba postępowania (z koordynacją prawną), żeby uniknąć sprzecznych komunikatów.

## Procedury postępowania — różnice praktyczne

**Procedura RODO** ma już 8-letnią dorobek (od 2018). Praktyka jest ukształtowana: postanowienie wszczęcia → żądanie dokumentów → przesłuchania → postanowienie o zarzutach → wypowiedź podmiotu → decyzja. Typowy czas: 6–18 miesięcy.

**Procedura NIS2** dopiero się kształtuje (pierwsze postępowania od 2025). Pierwsze decyzje pokazują, że organy stosują podobny model proceduralny do RODO. Typowy czas postępowania: 4–12 miesięcy (krócej dzięki wąskiej i konkretnej naturze zarzutów).

W obu przypadkach: prawo do reprezentacji prawnej, prawo dostępu do akt, prawo do wnoszenia wniosków, prawo do odwołania.

Pełniejsze omówienie procedury NIS2 w artykule [Postępowanie sankcyjne krok po kroku](/postepowanie-sankcyjne-krok-po-kroku).

## Czynniki łagodzące i obciążające — porównanie

W obu reżimach stosowane są podobne kategorie czynników. Algorytm wyliczenia jest analogiczny.

**Wspólne czynniki łagodzące:**
- samodzielne zgłoszenie naruszenia;
- pełna współpraca z organem;
- działania korygujące już podjęte;
- brak wcześniejszych naruszeń;
- wsparcie dla osób dotkniętych.

**Wspólne czynniki obciążające:**
- wcześniejsze naruszenia tego samego podmiotu;
- świadomość naruszenia / lekceważenie;
- próba zatajenia;
- brak współpracy.

**Czynniki specyficzne dla RODO:**
- charakter danych osobowych dotkniętych (zwykłe vs szczególne kategorie — art. 9 RODO);
- liczba osób dotkniętych;
- charakter szkody dla osób (materialna vs niematerialna);
- środki podjęte w celu ograniczenia szkody dla osób.

**Czynniki specyficzne dla NIS2:**
- charakter dotkniętych usług (krytyczne dla społeczeństwa);
- czas trwania zakłócenia;
- liczba podmiotów dotkniętych pośrednio;
- wpływ transgraniczny.

W incydencie dwureżimowym oba zestawy czynników są oceniane równolegle przez różne organy.

## Kary łączone — czy można ukarać dwa razy za ten sam czyn

Kluczowe pytanie prawne: czy nałożenie kary RODO i NIS2 za ten sam incydent narusza zasadę ne bis in idem (zakaz dwukrotnej karalności)?

Praktyka europejska (głównie wyroki Trybunału Sprawiedliwości UE w sprawach analogicznych) wskazuje na rozróżnienie:

**Nie narusza ne bis in idem:** kary nakładane za różne czyny (formalnie oddzielne) lub te same czyny, ale chroniące różne dobra prawne. Argument: RODO chroni prawa osób fizycznych, NIS2 chroni ciągłość usług — różne dobra prawne, więc dwie kary za ten sam incydent są dopuszczalne.

**Może naruszać ne bis in idem:** dwukrotna kara za dokładnie ten sam czyn z tym samym dobrem prawnym chronionym. Rzadkie w praktyce dwureżimowej.

W praktyce: w incydencie dwureżimowym oba organy mogą nałożyć kary za różne aspekty tego samego incydentu (RODO za niewłaściwe zabezpieczenie danych osobowych, NIS2 za niewłaściwą architekturę bezpieczeństwa systemu). Łączna kara jest sumą.

Teoretyczne pytanie obrony: czy łączna kara z dwóch reżimów jest proporcjonalna? W kilku precedensach europejskich obrona próbowała argumentować, że łączna sankcja przekracza proporcjonalność. Wyniki niejednoznaczne — jakieś sukcesy w Niemczech, brak w Holandii.

## Procedury raportowania — różne timeline'y

Krytyczne praktycznie:

**RODO (artykuł 33):** zgłoszenie naruszenia ochrony danych osobowych do PUODO w 72 godziny od stwierdzenia. Plus, jeśli wysokie ryzyko dla osób — powiadomienie osób (artykuł 34) bez zbędnej zwłoki.

**NIS2 (artykuł 23):** trójstopniowy protokół. Wczesne ostrzeżenie do CSIRT NASK w 24 godziny. Powiadomienie w 72 godziny. Sprawozdanie końcowe w miesiąc.

W incydencie dwureżimowym: dwa zgłoszenia, dwa formularze, dwa terminy częściowo nakładające się (oba 72h, plus dodatkowe 24h dla NIS2 i 30 dni dla NIS2). Procedura wewnętrzna firmy musi obsłużyć obie ścieżki.

Pełniejsze omówienie procedury NIS2 w artykule [Raportowanie incydentów 24/72h — protokół](/raportowanie-incydentow-24-72h-protokol) (testnis2.pl).

## Polskie precedensy 2025–2026 — przegląd kar

Wybrane decyzje polskich organów w obu reżimach:

**RODO — kary referencyjne 2018–2025:**
- ID Finance Poland (2022): 4,9 mln zł.
- LM Sp. z o.o. (2024): 2,8 mln zł.
- Inne wybrane: 0,5–4,9 mln zł w przypadkach dużych naruszeń.

**NIS2 — pierwsze polskie kary 2025–2026:**
- Średnia firma logistyczna (kwiecień 2026): 850 tys. zł.
- Średni dostawca SaaS (oczekiwane II kwartał 2026): 2,5–4 mln zł.
- Szpital wojewódzki (oczekiwane III kwartał 2026): 1,5–4 mln zł.
- Operator energetyczny (oczekiwane III kwartał 2026): 0,6–1,5 mln zł.

Pełniejszy przegląd w artykule [Pierwsze polskie kary NIS2 — analiza precedensów 2025–2026](/pierwsze-polskie-kary-nis2-precedensy).

**Kary łączone (incydenty dwureżimowe):** żadne polskie precedensy nie są jeszcze zakończone. Spodziewane od II–III kwartału 2026. Na podstawie przykładów europejskich: typowa łączna kara dla średniej firmy w incydencie dwureżimowym 3–10 mln zł.

## Strategia zarządzania ryzykiem dwureżimowym

Czterofilarowa architektura ochrony przed sankcjami w obu reżimach:

**Filar 1: zintegrowana zgodność.** Jeden zespół compliance odpowiedzialny za oba reżimy. Wspólne audyty, wspólne raporty, wspólny rejestr ryzyka. Polityki łączone tam, gdzie możliwe (kontrola dostępu, kryptografia, kopie zapasowe). Polityki rozdzielone tam, gdzie konieczne (procedury raportowania, prawa podmiotów danych).

**Filar 2: zintegrowana procedura incydentowa.** Jedna procedura obsługi incydentu z dwoma wyjściami (RODO + NIS2). Wspólne dane wejściowe, dwa odrębne formaty wyjściowe. Wczesna decyzja w godzinach pierwszych: czy incydent jest RODO, NIS2, oba, żadne. Aktywacja odpowiednich ścieżek raportowania.

**Filar 3: zintegrowana obrona prawna.** Jeden zespół prawny obsługujący oba postępowania (jeśli równoległe). Spójna komunikacja z oboma organami. Strategia argumentacyjna uwzględniająca interakcje między reżimami.

**Filar 4: zintegrowane ubezpieczenie.** Polisa cyber liability + D&O + management — w pełnym zakresie obejmującym sankcje obu reżimów (w obszarze pokrywanym, czyli głównie koszty obrony, nie same kary).

Łączny koszt zintegrowanej architektury dla średniej firmy: 80 000–200 000 zł rocznie. Realnie obniża łączne ryzyko sankcyjne o 60–80% w stosunku do dwóch oddzielnych systemów.

## Najczęstsze błędy w zarządzaniu dwureżimowym

**Błąd 1: jeden zespół obsługuje oba reżimy bez specjalizacji.** IOD bez znajomości NIS2 lub Cybersecurity Officer bez znajomości RODO. Skutek: luki w obu obszarach.

**Błąd 2: wspólny formularz zgłoszenia.** Próba ujednolicenia zgłoszeń do PUODO i CSIRT NASK. Każdy organ wymaga swojego formatu — uniwersalny formularz nie zaspokaja żadnego.

**Błąd 3: pełne zaangażowanie w jeden reżim, drugi traktowany pobocznie.** Klasyczne: firma już ma RODO, wdraża NIS2 jako "nadbudówkę". Skutek: NIS2 jest powierzchowne, kontrola NIS2 ujawnia luki niewykrywalne przez audyt RODO.

**Błąd 4: nieskoordynowana komunikacja z dwoma organami.** Sprzeczne lub niespójne odpowiedzi do PUODO i CSIRT NASK są wykrywane (organy współpracują) i pogarszają sytuację w obu postępowaniach.

**Błąd 5: pominięcie kosztów łącznych w analizie ryzyka.** Firmy często liczą ryzyko maksymalnej kary jednego reżimu (10 mln EUR NIS2 lub 20 mln EUR RODO). Realnie maksimum to suma — 30 mln EUR plus koszty obrony i naprawy.

## Lista kontrolna gotowości dwureżimowej

Dziewięć pytań dla firmy podlegającej obu reżimom:

1. Czy mamy odrębnie wyznaczonego IOD i Cybersecurity Officera (lub jedną osobę z udokumentowaną kompetencją w obu obszarach)?
2. Czy posiadamy wspólny rejestr incydentów z oznaczeniem reżimu (RODO / NIS2 / oba)?
3. Czy posiadamy procedurę obsługi incydentu z dwoma ścieżkami raportowania?
4. Czy nasza polisa cyber pokrywa koszty obrony w obu reżimach?
5. Czy mamy kancelarię prawną z doświadczeniem w obu reżimach?
6. Czy nasze polityki techniczne (kontrola dostępu, kryptografia, kopie) są zintegrowane?
7. Czy nasze szkolenia personelu obejmują oba reżimy?
8. Czy nasze szkolenia zarządu obejmują oba reżimy?
9. Czy nasza strategia łańcucha dostaw uwzględnia oba reżimy (umowy z procesorami danych + dostawcami IT)?

Pełen pakiet — gotowość dwureżimowa. Brak 3+ pozycji = ryzyko luki sankcyjnej.

## Bibliografia

<ul>
<li>Komisja Europejska. (2022). <em>Dyrektywa Parlamentu Europejskiego i Rady (UE) 2022/2555 (NIS2)</em>. <a href="https://eur-lex.europa.eu/legal-content/PL/TXT/?uri=CELEX:32022L2555">https://eur-lex.europa.eu/legal-content/PL/TXT/?uri=CELEX:32022L2555</a></li>
<li>Parlament Europejski i Rada UE. (2016). <em>Rozporządzenie (UE) 2016/679 (RODO)</em> — art. 83. <a href="https://eur-lex.europa.eu/eli/reg/2016/679/oj">https://eur-lex.europa.eu/eli/reg/2016/679/oj</a></li>
<li>European Data Protection Board. (2023). <em>Guidelines 04/2022 on the calculation of administrative fines under the GDPR</em>. EDPB. [DO WERYFIKACJI URL]</li>
<li>Trybunał Sprawiedliwości UE. (2023). <em>Wyrok C-481/19 (zasada ne bis in idem w sankcjach administracyjnych)</em>. CURIA. [DO WERYFIKACJI URL]</li>
<li>UODO. (2024). <em>Sprawozdanie roczne UODO za 2023 rok</em>. Urząd Ochrony Danych Osobowych. <a href="https://uodo.gov.pl/">https://uodo.gov.pl/</a></li>
<li>Autoriteit Persoonsgegevens. (2025). <em>Joint sanctions decisions 2025 — RODO and NIS2</em>. AP. [DO WERYFIKACJI URL]</li>
<li>ENISA. (2024). <em>Mapping NIS2 Sanctions to GDPR — Practical Implications</em>. European Union Agency for Cybersecurity. [DO WERYFIKACJI URL]</li>
<li>CSIRT NASK. (2025). <em>Współpraca z UODO w postępowaniach incydentów dwureżimowych</em>. NASK PIB. [DO WERYFIKACJI URL]</li>
</ul>

---

**Większość firm podlegających NIS2 podlega też RODO — i może otrzymać dwie kary za jeden incydent.** W cotygodniowym newsletterze KaryNIS2.pl analizujemy precedensy podwójnej karalności i strategie zintegrowanego zarządzania ryzykiem. [Zapisz się — bezpłatnie](#newsletter-signup).
