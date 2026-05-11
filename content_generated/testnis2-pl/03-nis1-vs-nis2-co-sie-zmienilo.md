---
title: "NIS1 vs NIS2 — co się zmieniło i dlaczego ma to znaczenie"
slug: "nis1-vs-nis2-co-sie-zmienilo"
excerpt: "Porównanie dyrektyw NIS i NIS2 — zakres podmiotowy, kary, raportowanie, odpowiedzialność zarządu. Konkretne różnice, które wymuszają nowe procedury."
category_slug: "regulacje"
tags: "NIS1, NIS2, dyrektywa UE, ENISA, krajowy system cyberbezpieczeństwa, porównanie, średni"
reading_time: 11
is_published: true
is_featured: false
meta_title: "NIS1 vs NIS2 — kompletne porównanie dyrektyw (2026)"
meta_description: "Czym różni się NIS2 od pierwotnej dyrektywy NIS? Zakres, kary do 10 mln EUR, raportowanie 24/72h, osobista odpowiedzialność członków zarządu."
funnel: "TOFU"
author_slug: "marek-porycki"
related_slugs: "nis2-checklista-gotowosci-10-obszarow, kogo-obowiazuje-nis2-w-polsce, raportowanie-incydentow-24-72h-protokol"
product_slugs: ""
---

Dyrektywa NIS z 2016 roku była pierwszą próbą uregulowania cyberbezpieczeństwa na poziomie unijnym. Po sześciu latach jej działania Komisja Europejska przyznała otwarcie: zawiodła. Zbyt wąski zakres, zbyt duża swoboda państw członkowskich w transpozycji, brak skutecznych sankcji. NIS2 — dyrektywa 2022/2555 — to odpowiedź na te niedociągnięcia. Nie jest to kosmetyczna nowelizacja; to przebudowa fundamentów.

W Polsce obie dyrektywy zostały transponowane przez ustawę o krajowym systemie cyberbezpieczeństwa. NIS — w wersji z 2018 roku, NIS2 — przez nowelizację, której pełne wdrożenie wszedł w życie po terminie 17 października 2024 roku. Większość polskich firm dopiero teraz orientuje się, że nie tylko mają nowe obowiązki, ale że stare procedury zbudowane pod NIS1 przestały być wystarczające.

W tym tekście porównuję obie dyrektywy w siedmiu kluczowych obszarach: zakres podmiotowy, klasyfikacja podmiotów, wymogi techniczne, raportowanie incydentów, sankcje, odpowiedzialność zarządu i nadzór.

## Zakres podmiotowy — z 7 sektorów do 18

Pierwotna dyrektywa NIS dotyczyła wąskiej grupy. Operatorzy usług kluczowych (OUK) z siedmiu sektorów: energia, transport, bankowość, infrastruktura rynków finansowych, służba zdrowia, dostawa wody pitnej, infrastruktura cyfrowa. Plus dostawcy usług cyfrowych (DSP): platformy handlu online, wyszukiwarki, usługi chmurowe.

W Polsce obowiązki NIS objęły około 400 podmiotów. Były to głównie duże firmy — operatorzy energetyczni, banki, szpitale wojewódzkie, lotniska, dostawcy wody w aglomeracjach. Reszta gospodarki — przemysł, przetwórstwo żywności, kurierzy, firmy chemiczne — pozostała poza zakresem regulacji.

NIS2 rozszerza zakres dramatycznie. Sektory wysokiej krytyczności (Załącznik I): energia, transport, bankowość, infrastruktura rynków finansowych, ochrona zdrowia, woda pitna i ścieki, infrastruktura cyfrowa, zarządzanie usługami ICT (B2B), administracja publiczna, przestrzeń kosmiczna. Sektory pozostałe krytyczne (Załącznik II): poczta i kurierzy, gospodarka odpadami, produkcja, dystrybucja i handel substancjami chemicznymi, produkcja, przetwarzanie i dystrybucja żywności, produkcja (urządzenia medyczne, komputerowe, elektroniczne, optyczne, elektryczne, maszynowe, pojazdy mechaniczne, inne środki transportu), dostawcy usług cyfrowych (platformy handlowe, wyszukiwarki, sieci społecznościowe), badania.

Razem 18 sektorów. Szacunki rządowe i analizy branżowe (CSIRT NASK, instytucje konsultingowe) mówią o 8 000–12 000 polskich podmiotów objętych NIS2 — czyli wzrost dwudziestokrotny w stosunku do NIS1. Skala jest taka, że administracja nie jest w stanie wszystkich aktywnie nadzorować; zakłada się model samorejestracji i kontroli następczych po incydencie.

Co to znaczy praktycznie? Średniej wielkości producent kosmetyków, który zatrudnia 60 osób i ma 12 mln euro obrotu, pod NIS1 nie miał żadnych obowiązków. Pod NIS2 — pełne wymagania zarządzania ryzykiem cybernetycznym, raportowanie incydentów, odpowiedzialność zarządu. Średnia firma kurierska z 80 pracownikami i 15 mln euro obrotu — to samo.

## Klasyfikacja — operatorzy usług kluczowych vs podmioty kluczowe i ważne

NIS1 wprowadzała dwie kategorie. Operatorzy usług kluczowych (OUK) — wyznaczani indywidualnie przez państwo członkowskie po analizie krytyczności konkretnej firmy. Dostawcy usług cyfrowych (DSP) — automatycznie, jeśli świadczyli określone usługi.

Mechanizm wyznaczania OUK był pracochłonny i nieefektywny. Państwa członkowskie miały dyskrecjonalność i interpretowały kryteria różnie. Polska wyznaczyła stosunkowo wąsko, Niemcy szeroko. Powstała nierówna sytuacja konkurencyjna i regulacyjna.

NIS2 wprowadza dwie nowe kategorie:

Podmioty kluczowe (essential entities) — duże podmioty z sektorów wysokiej krytyczności (Załącznik I). Próg: ≥250 pracowników LUB ≥50 mln EUR obrotu LUB ≥43 mln EUR sumy bilansowej. Ponadto wszystkie podmioty z administracji publicznej szczebla centralnego, świadczące usługi DNS na poziomie głównym, rejestratorzy nazw TLD, dostawcy publicznych sieci łączności.

Podmioty ważne (important entities) — wszystkie pozostałe podmioty z Załącznika I oraz wszystkie podmioty z Załącznika II spełniające próg średniego przedsiębiorstwa (≥50 pracowników LUB ≥10 mln EUR obrotu).

Klasyfikacja jest automatyczna — wynika z sektora i wielkości firmy. Nie ma już procesu wyznaczania, w którym państwo dyskretnie ocenia. Firma sama musi się sklasyfikować i zarejestrować w CSIRT NASK.

Różnica między klasyfikacją kluczową i ważną dotyczy głównie nadzoru. Podmioty kluczowe podlegają nadzorowi proaktywnemu — administracja może kontrolować bez powodu. Podmioty ważne — nadzorowi reaktywnemu, czyli kontrole po incydencie lub po zgłoszeniu nieprawidłowości.

Wymogi techniczne, kary i odpowiedzialność zarządu — w przeważającej mierze identyczne dla obu kategorii.

## Wymogi techniczne — z ogólników do dziesięciu konkretnych obszarów

NIS1 stawiała wymóg ogólny: podmioty mają wdrożyć "odpowiednie i proporcjonalne środki techniczne i organizacyjne" do zarządzania ryzykiem. Co to znaczy w praktyce — pozostawiono interpretacji. Wytyczne CSIRT GOV i CSIRT NASK starały się to konkretyzować, ale każdy podmiot mógł argumentować, że jego rozwiązania są "odpowiednie".

NIS2 (artykuł 21) wprowadza dziesięć konkretnych obszarów minimum. Każdy podmiot — kluczowy i ważny — musi wdrożyć środki w każdym z tych obszarów. Lista nie jest "best practices" — to wymóg prawny.

Te dziesięć obszarów to: polityki analizy ryzyka i bezpieczeństwa systemów informatycznych; obsługa incydentów; ciągłość działania (zarządzanie kopiami zapasowymi, odzyskiwanie po awarii, zarządzanie kryzysowe); bezpieczeństwo łańcucha dostaw; bezpieczeństwo w pozyskiwaniu, rozwoju i utrzymaniu sieci i systemów informatycznych; polityki i procedury oceny skuteczności środków zarządzania ryzykiem; podstawowe praktyki cyberhigieny i szkolenia; polityki i procedury kryptografii; bezpieczeństwo zasobów ludzkich, polityki kontroli dostępu i zarządzania aktywami; korzystanie z uwierzytelniania wieloskładnikowego.

Dla firmy, która pod NIS1 miała ogólny dokument "Polityka Bezpieczeństwa", to oznacza konieczność dekompozycji na dziesięć osobnych polityk i procedur, każdą operacyjną i mierzalną.

## Raportowanie incydentów — z 24 godzin do trójstopniowego protokołu

NIS1 wymagała zgłoszenia incydentu "bez zbędnej zwłoki". Konkretne ramy czasowe pozostawiała państwom członkowskim. Polska transpozycja mówiła o 24 godzinach od wykrycia.

NIS2 (artykuł 23) wprowadza precyzyjny trójstopniowy protokół. Wczesne ostrzeżenie — w ciągu 24 godzin od stwierdzenia istotności incydentu. Powiadomienie właściwe — w ciągu 72 godzin, z oceną wstępną i znaną już naturą zdarzenia. Sprawozdanie końcowe — w ciągu jednego miesiąca od powiadomienia, z pełną analizą przyczyn źródłowych i wpływem.

Definicja incydentu istotnego również się zmieniła. NIS1 mówiła o incydentach "mających istotny wpływ na dostępność, autentyczność, integralność lub poufność". NIS2 dodaje kryteria: powodujące lub mogące powodować poważne zakłócenia operacyjne lub straty finansowe; wpływające lub mogące wpływać na inne osoby fizyczne lub prawne, powodując znaczne szkody materialne lub niematerialne. Próg "istotności" jest niższy — więcej incydentów wymaga raportowania.

Praktyczna konsekwencja: zespół IT, który pod NIS1 raportował dwa–trzy incydenty rocznie, pod NIS2 może raportować dziesięć–piętnaście. Wymaga to procesu, nie ad hoc decyzji.

## Sankcje — z symbolicznych grzywien do 10 milionów euro

NIS1 zobowiązywała państwa członkowskie do wprowadzenia "skutecznych, proporcjonalnych i odstraszających" kar. Polska transpozycja przewidywała kary do 200 000 zł — symbolicznie dla dużej korporacji, dla SME już dotkliwie, ale nie wymuszała compliance.

NIS2 standaryzuje sankcje na poziomie unijnym. Dla podmiotów kluczowych: do 10 milionów euro lub 2% globalnego rocznego obrotu — wartość wyższa. Dla podmiotów ważnych: do 7 milionów euro lub 1,4% obrotu — wartość wyższa.

Wzór jest analogiczny do RODO i nie jest przypadkowy. Komisja Europejska przyznała otwarcie, że NIS1 nie wymuszała compliance, bo kary były nieadekwatne. RODO pokazało, że sankcje proporcjonalne do obrotu globalnego firmy działają — koncerny technologiczne zaczęły traktować ochronę danych poważnie dopiero, gdy kara mogła sięgnąć kilku procent ich rocznego obrotu.

Polskie kary za naruszenie RODO sięgnęły rekordowo 4,9 mln zł (ID Finance Poland, 2022). Pierwsze kary NIS2 są spodziewane od 2026 roku, kiedy administracja zakończy fazę "miękkiego" wdrożenia i przejdzie do egzekucji.

## Odpowiedzialność zarządu — od reputacji do osobistej odpowiedzialności

To zmiana, którą zarządy często ignorowały podczas wdrożeń pierwotnej NIS1, traktując cyberbezpieczeństwo jako problem działu IT. NIS2 zamyka tę furtkę.

Artykuł 20 NIS2 stanowi wprost: organy zarządzające podmiotów kluczowych i ważnych zatwierdzają środki zarządzania ryzykiem cybernetycznym, nadzorują ich wdrożenie, mogą ponosić odpowiedzialność za naruszenia. Państwa członkowskie zapewniają, że osoby pełniące funkcje zarządzające mogą być ukarane lub czasowo odsunięte od pełnienia funkcji.

W polskiej transpozycji oznacza to: członek zarządu, który zatwierdził budżet 50 000 zł na cyberbezpieczeństwo dla firmy o obrotach 200 mln zł i nie kwestionował ewidentnie nieadekwatnego poziomu inwestycji, może zostać uznany za współodpowiedzialnego za incydent. Ubezpieczenie D&O nie pokryje kar administracyjnych nakładanych personalnie.

Dodatkowo: szkolenie zarządu z cyberbezpieczeństwa jest wymogiem prawnym, nie rekomendacją. Zarząd musi wykazać, że rozumie ryzyka, którymi kieruje. Brak szkoleń — naruszenie obowiązków członka zarządu, które może być podstawą roszczeń odszkodowawczych ze strony spółki.

Pełniejsze omówienie w artykule [Odpowiedzialność osobista zarządu w NIS2](/odpowiedzialnosc-zarzadu-nis2-osobista).

## Nadzór — kto, jak i kiedy

NIS1 powierzała nadzór państwom członkowskim z dużą swobodą organizacyjną. W Polsce odpowiedzialne były sektorowe zespoły CSIRT (CSIRT GOV dla administracji, CSIRT NASK dla podmiotów cywilnych, CSIRT MON dla obronności) plus ministerstwa właściwe dla sektorów. Mechanizm był rozdrobniony.

NIS2 utrzymuje strukturę zespołów CSIRT, ale wzmacnia uprawnienia nadzorcze. Dla podmiotów kluczowych przewidziano nadzór proaktywny: kontrole na miejscu, audyty bezpieczeństwa, żądania dostępu do dokumentacji i systemów, badania ad hoc. Dla podmiotów ważnych — nadzór reaktywny, ale ze zwiększonymi uprawnieniami w przypadku stwierdzenia naruszeń.

Na poziomie unijnym powstała sieć krajów członkowskich (Cooperation Group) i ENISA otrzymała wzmocnione kompetencje koordynacyjne. To ważne dla firm działających w wielu krajach UE — naruszenie wykryte w jednym państwie może być przedmiotem koordynowanego dochodzenia w innych.

## Tabela porównawcza — NIS1 kontra NIS2

| Obszar | NIS1 (2016) | NIS2 (2022/2024) |
|---|---|---|
| Liczba sektorów | 7 + DSP | 11 + 7 (Załącznik I + II) |
| Polskie podmioty objęte | ~400 | ~8 000–12 000 |
| Klasyfikacja | OUK (wyznaczani) + DSP | Kluczowe + ważne (automatycznie) |
| Wymogi techniczne | Ogólne ("odpowiednie środki") | 10 konkretnych obszarów |
| Termin raportowania | "Bez zbędnej zwłoki" (PL: 24h) | Trzy etapy: 24h / 72h / 30 dni |
| Maksymalne kary (PL) | 200 000 zł | 10 mln EUR lub 2% obrotu |
| Odpowiedzialność zarządu | Brak osobistej | Osobista, możliwe odsunięcie |
| Nadzór | Reaktywny, sektorowy | Proaktywny (kluczowe), reaktywny (ważne) |
| Łańcuch dostaw | Nie regulowany | Wymóg oceny ryzyka dostawców |
| Szkolenia | Nie wymagane | Obowiązkowe (zarząd + personel) |

## Co to znaczy dla firm, które już były pod NIS1

Podmioty, które wdrożyły NIS1 i teraz przechodzą na NIS2, mają punkt startowy lepszy niż firmy zaczynające od zera. Mają jakąś dokumentację, jakieś procesy, świadomość organizacyjną. Ale błąd polega na założeniu, że "skoro mieliśmy NIS1, to NIS2 to drobna modyfikacja".

Rzeczywistość: dla typowego operatora usług kluczowych pod NIS1, dostosowanie do NIS2 wymaga: rozbudowy polityk z jednej ogólnej do dziesięciu szczegółowych, dodania procedury raportowania trójetapowego (większość miała tylko procedurę 24h), wdrożenia oceny ryzyka łańcucha dostaw (NIS1 tego nie wymagała), uruchomienia programu szkoleń dla zarządu, wprowadzenia uwierzytelniania wieloskładnikowego dla wszystkich krytycznych dostępów, formalnej oceny ryzyka kryptograficznego.

Średni nakład czasowy: trzy do sześciu miesięcy pracy zespołu compliance/IT. Średni nakład finansowy dla firmy, która już była pod NIS1: 80 000–250 000 zł na konsultacje, narzędzia, szkolenia. Dla firmy zaczynającej od zera (typowy nowy podmiot ważny): 150 000–500 000 zł.

## Co to znaczy dla firm, które dopiero teraz wchodzą w zakres regulacji

Większość polskich średnich i większych firm produkcyjnych, kurierskich, chemicznych, spożywczych, dostawców usług IT B2B — to firmy, które pod NIS1 nie miały żadnych obowiązków cyberbezpieczeństwa wynikających z prawa. RODO regulowało dane osobowe. Sektorowe regulacje (np. KNF dla finansowych, URE dla energetycznych) pokrywały wąskie obszary. Cyberbezpieczeństwo jako takie — pozostawało dobrowolnym wyborem.

Pod NIS2 to się zmienia. Firma, która rozumie, że NIS2 jej dotyczy, ma 12–18 miesięcy realnego okna na wdrożenie pełnego systemu. Nie warto czekać na pierwszy audyt — administracja będzie ekstremalnie wymagająca wobec podmiotów, które się "nie spodziewały".

Pierwszy krok: kwalifikacja. Sprawdź, czy Twoja firma jest podmiotem kluczowym, ważnym, czy nie podlega NIS2 wcale. Drugi krok: rejestracja w CSIRT NASK. Trzeci krok: gap analysis — porównanie obecnego stanu z dziesięcioma obszarami artykułu 21. Czwarty krok: plan wdrożenia z konkretnymi terminami i odpowiedzialnościami.

Szczegółowa procedura kwalifikacyjna w artykule [Kogo dokładnie obowiązuje NIS2 w Polsce](/kogo-obowiazuje-nis2-w-polsce). Pełna lista obszarów do audytu — [NIS2: kompletna checklista gotowości](/nis2-checklista-gotowosci-10-obszarow).

## Czy NIS3 jest już planowana?

Komisja Europejska konsekwentnie pracuje nad spójnym ekosystemem regulacji cyfrowych. Po NIS2 weszły w życie: DORA (Digital Operational Resilience Act, 2025) — sektor finansowy. CRA (Cyber Resilience Act, 2024) — produkty z elementami cyfrowymi. AI Act (2024) — sztuczna inteligencja. CER (Critical Entities Resilience Directive, 2024) — odporność fizyczna podmiotów krytycznych.

Wszystkie te regulacje wzajemnie się przeplatają. Firma podlega często kilku jednocześnie. NIS3 nie jest ogłoszona, ale ENISA już mówi o "NIS2.5" — doprecyzowaniach implementacyjnych spodziewanych w 2027 roku po pierwszej fali kar.

Inwestycja w solidny system zarządzania ryzykiem cybernetycznym pod NIS2 to nie wydatek na "jedną dyrektywę". To budowa fundamentu pod cały ekosystem regulacyjny, który będzie się rozwijał.

## Bibliografia

<ul>
<li>Komisja Europejska. (2022). <em>Dyrektywa Parlamentu Europejskiego i Rady (UE) 2022/2555 z dnia 14 grudnia 2022 r. (NIS2)</em>. Dziennik Urzędowy UE L 333/80. <a href="https://eur-lex.europa.eu/legal-content/PL/TXT/?uri=CELEX:32022L2555">https://eur-lex.europa.eu/legal-content/PL/TXT/?uri=CELEX:32022L2555</a></li>
<li>Parlament Europejski i Rada UE. (2016). <em>Dyrektywa (UE) 2016/1148 z dnia 6 lipca 2016 r. (NIS)</em>. Dziennik Urzędowy UE L 194/1. <a href="https://eur-lex.europa.eu/eli/dir/2016/1148/oj">https://eur-lex.europa.eu/eli/dir/2016/1148/oj</a></li>
<li>ENISA. (2024). <em>NIS2 Directive: Implementation Guidance for Member States</em>. European Union Agency for Cybersecurity. [DO WERYFIKACJI dokładny URL]</li>
<li>Sejm RP. (2018). <em>Ustawa z dnia 5 lipca 2018 r. o krajowym systemie cyberbezpieczeństwa</em>. Dz.U. 2018 poz. 1560. <a href="https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WDU20180001560">https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WDU20180001560</a></li>
<li>Komisja Europejska. (2020). <em>Impact Assessment Report accompanying the proposal for NIS2 Directive</em>. SWD(2020) 345 final. [DO WERYFIKACJI URL]</li>
<li>Urząd Ochrony Danych Osobowych. (2022). <em>Decyzja administracyjna nakładająca karę na ID Finance Poland Sp. z o.o.</em> [DO WERYFIKACJI numer decyzji]</li>
<li>CSIRT NASK. (2024). <em>Wytyczne dla podmiotów objętych nowelizacją ustawy o krajowym systemie cyberbezpieczeństwa</em>. NASK PIB. [DO WERYFIKACJI URL]</li>
</ul>

---

**Jeśli zarządzasz średnią lub dużą firmą i masz wątpliwość, czy NIS2 Cię dotyczy** — co tydzień analizujemy w newsletterze konkretne przypadki polskich podmiotów, decyzje organów nadzoru i praktyczne pytania compliance. [Zapisz się na cotygodniowy biuletyn TestNIS2.pl](#newsletter-signup). Zero spamu, możesz wypisać się jednym kliknięciem.
