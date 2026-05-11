---
title: "Łańcuch dostaw w NIS2 — supply chain risk po polsku"
slug: "lancuch-dostaw-nis2-supply-chain-risk"
excerpt: "Twój dostawca SaaS to Twoje ryzyko regulacyjne. Mapowanie kluczowych dostawców, klauzule cyberbezpieczeństwa, audyty i plan reakcji na ich incydent."
category_slug: "wdrozenia-nis2"
tags: "NIS2, łańcuch dostaw, supply chain, dostawcy IT, kontrakty, średni"
reading_time: 11
is_published: true
is_featured: false
meta_title: "Łańcuch dostaw NIS2 — supply chain risk dla polskich firm"
meta_description: "Jak mapować kluczowych dostawców IT, jakie klauzule cyberbezpieczeństwa wstawić do umów, jak ocenić ryzyko dostawcy. Wzory dokumentów."
funnel: "MOFU"
author_slug: "marek-porycki"
related_slugs: "nis2-checklista-gotowosci-10-obszarow, nis2-vs-rodo-co-sie-naklada-co-rozni, raportowanie-incydentow-24-72h-protokol"
product_slugs: ""
---

W grudniu 2020 roku świat dowiedział się o ataku na SolarWinds. Atakujący wszedł nie do firm, które zaatakował — wszedł do dostawcy oprogramowania, którego używały te firmy. Złośliwy kod został wpisany do legalnej aktualizacji SolarWinds Orion, która następnie została zainstalowana przez 18 000 organizacji na całym świecie. Wśród ofiar — amerykańskie ministerstwa, korporacje technologiczne, agencje wywiadu. To był jeden z najpoważniejszych ataków na łańcuch dostaw IT w historii i punkt zwrotny w myśleniu o cyberbezpieczeństwie.

Komisja Europejska, projektując NIS2, wpisała wnioski z SolarWinds bezpośrednio do tekstu dyrektywy. Artykuł 21 ust. 2 lit. d wymienia "bezpieczeństwo łańcucha dostaw, w tym aspekty związane z bezpieczeństwem dotyczące relacji między każdym podmiotem a jego bezpośrednimi dostawcami lub usługodawcami" jako jeden z dziesięciu obszarów obowiązkowych. Artykuł 22 dyrektywy idzie dalej — wymaga skoordynowanej oceny ryzyka kluczowych łańcuchów dostaw na poziomie unijnym.

Ten tekst opisuje, jak polska firma podlegająca NIS2 powinna zorganizować zarządzanie ryzykiem łańcucha dostaw. Pokazuje metodologię mapowania dostawców, gradację ryzyka, klauzule kontraktowe, plan reakcji na incydent po stronie dostawcy oraz najczęstsze błędy.

## Czym jest łańcuch dostaw IT w sensie NIS2

Pojęcie szersze niż większość firm myśli intuicyjnie. Łańcuch dostaw IT obejmuje:

**Dostawcy infrastruktury** — hosting, kolokacja, chmura publiczna (AWS, Azure, GCP), chmura hybrydowa, dostawcy łączności (operatorzy telekomunikacyjni).

**Dostawcy oprogramowania** — wszystkie systemy biznesowe (ERP, CRM, BI, HR, finansowe), oprogramowanie biurowe (M365, Google Workspace), oprogramowanie specjalistyczne sektorowe, oprogramowanie open source z istotnym znaczeniem.

**Dostawcy usług IT** — outsourcing IT (administracja, helpdesk, monitoring), firmy wdrożeniowe, integratorzy, firmy bezpieczeństwa (SOC, MSSP, threat intelligence), audytorzy IT.

**Dostawcy sprzętu** — producenci serwerów, urządzeń sieciowych, end-pointów, firmy serwisujące sprzęt z dostępem do systemów.

**Dostawcy usług profesjonalnych z dostępem do systemów** — biura księgowe operujące w Twoim systemie ERP, doradcy biznesowi z dostępem do baz danych, audytorzy zewnętrzni.

W typowej firmie 100-osobowej taka mapa zawiera 25–60 podmiotów. W firmie 500-osobowej — 80–150 podmiotów. Większość z nich nie jest "dostawcami IT" w tradycyjnym rozumieniu, ale ma wpływ na bezpieczeństwo systemów krytycznych.

## Klasyfikacja dostawców według poziomu ryzyka

Nie wszyscy dostawcy wymagają tej samej głębi oceny. Praktyczne podejście wprowadza trzy poziomy:

**Poziom A — krytyczni dostawcy.** Awaria lub kompromitacja powoduje natychmiastowe lub poważne zakłócenie świadczenia usług. Przykłady: główny dostawca chmurowy, dostawca głównego ERP, główny dostawca łączności, firma utrzymująca infrastrukturę. Liczba w typowej firmie: 3–8.

**Poziom B — istotni dostawcy.** Awaria powoduje znaczące, ale obsługiwalne zakłócenie. Przykłady: dostawcy SaaS dla CRM, marketing automation, BI, firmy outsourcingowe IT poziomu drugiego, dostawcy oprogramowania finansowego. Liczba: 10–25.

**Poziom C — pozostali dostawcy.** Awaria powoduje niedogodność, ale nie zagraża ciągłości. Przykłady: dostawcy narzędzi pomocniczych, mniejsze SaaS-y, jednorazowe firmy doradcze. Liczba: pozostali z mapy.

Klasyfikacja decyduje o intensywności kontroli:

Poziom A — pełny audyt (zewnętrzne raporty SOC 2 lub równoważne, kontrakty z pełnymi klauzulami cyber, prawo do audytu, plan reakcji na incydent, regularny przegląd minimum raz w roku).

Poziom B — uproszczona ocena (kwestionariusz cyberbezpieczeństwa, klauzule kontraktowe, raport incydentów, przegląd raz w roku lub co 18 miesięcy).

Poziom C — minimalna ocena (klauzule kontraktowe podstawowe, oświadczenie dostawcy o poziomie bezpieczeństwa, weryfikacja co 24 miesiące).

Ta gradacja jest realistyczna dla średniej firmy. Próba audytowania wszystkich 60 dostawców na pełnym poziomie A jest niewykonalna i nieproporcjonalna.

## Co wstawić do umów — klauzule cyberbezpieczeństwa

Klauzule kontraktowe są podstawowym mechanizmem przeniesienia odpowiedzialności na dostawcę i zabezpieczenia praw audytu. Minimalny zestaw dla dostawcy poziomu A:

**Klauzula 1: standardy bezpieczeństwa.** Dostawca zobowiązuje się do utrzymania środków technicznych i organizacyjnych co najmniej na poziomie określonym w [Załączniku — Specyfikacja Bezpieczeństwa]. Specyfikacja powinna wymieniać konkretne kontrole: szyfrowanie, MFA, kontrola dostępu, segmentacja sieci, audyty wewnętrzne, certyfikacje (np. ISO 27001).

**Klauzula 2: powiadomienie o incydencie.** Dostawca zobowiązuje się do powiadomienia Zamawiającego o każdym incydencie cyberbezpieczeństwa mającym lub mogącym mieć wpływ na świadczenie usług, w terminie nie dłuższym niż [12/24] godziny od stwierdzenia. Powiadomienie zawiera: opis incydentu, ocenę wpływu, działania podjęte, plan dalszych działań.

**Klauzula 3: prawo do audytu.** Zamawiający ma prawo do audytu zgodności Dostawcy z postanowieniami niniejszej umowy w obszarze bezpieczeństwa, na własny koszt, z uprzednim powiadomieniem o [30] dni. Audyt może być przeprowadzony przez Zamawiającego lub wskazany przez niego niezależny podmiot.

**Klauzula 4: dokumentacja certyfikacji.** Dostawca zobowiązuje się do udostępniania Zamawiającemu, na żądanie, aktualnych raportów audytów zgodności (SOC 2, ISO 27001) oraz wyników testów penetracyjnych w zakresie usług objętych niniejszą umową.

**Klauzula 5: subdostawcy.** Dostawca informuje Zamawiającego o wszystkich subdostawcach mających dostęp do systemów lub danych Zamawiającego. Każda zmiana subdostawcy wymaga pisemnego powiadomienia z wyprzedzeniem [30] dni.

**Klauzula 6: zwrot/usunięcie danych.** Po zakończeniu umowy Dostawca w terminie [30/60] dni zwraca lub usuwa wszystkie dane Zamawiającego ze swoich systemów i systemów subdostawców. Dostawca przedstawia pisemne potwierdzenie usunięcia.

**Klauzula 7: odpowiedzialność.** Limit odpowiedzialności Dostawcy z tytułu naruszenia bezpieczeństwa wynosi [kwota lub % wartości kontraktu]. Limit nie obejmuje kar regulacyjnych i kosztów naprawienia szkód spowodowanych rażącym niedbalstwem.

**Klauzula 8: ubezpieczenie cyber.** Dostawca utrzymuje aktualną polisę ubezpieczenia cyberodpowiedzialności w wysokości minimum [kwota] EUR. Dostawca przedstawia kopię polisy na żądanie Zamawiającego.

Klauzule można negocjować. Duzi dostawcy chmurowi (AWS, Microsoft, Google) mają swoje standardowe DPA i Service Agreements, które rzadko podlegają negocjacji — ale zwykle pokrywają większość minimalnych wymagań NIS2. Średni i mali dostawcy częściej akceptują klauzule indywidualne.

## Kwestionariusz oceny dostawcy — minimalna treść

Dla dostawców poziomu B i wyżej standardową praktyką jest kwestionariusz wstępnej oceny. Minimum 25–40 pytań pokrywających:

**Sekcja 1: governance.** Czy posiada formalną politykę bezpieczeństwa? Czy ma dedykowaną osobę odpowiedzialną za cyberbezpieczeństwo? Czy posiada certyfikację ISO 27001 lub równoważną? Kiedy ostatnio przechodził audyt zewnętrzny?

**Sekcja 2: organizacja.** Ilu pracowników? Czy są szkoleni z cyberbezpieczeństwa minimum raz w roku? Czy MFA obowiązkowe dla wszystkich? Jaka procedura onboarding/offboarding?

**Sekcja 3: techniczne.** Jak szyfrują dane (w tranzycie, w spoczynku)? Jak zarządzają kluczami? Czy stosują segmentację sieci? Jak zarządzają patchami (czas reakcji na krytyczne podatności)?

**Sekcja 4: operacje.** Czy mają monitoring 24/7? Średni czas wykrycia incydentu? Czy mają incident response plan? Czy testują disaster recovery (kiedy ostatnio)?

**Sekcja 5: subdostawcy.** Lista subdostawców mających dostęp do systemów/danych. Jak ich oceniają? Jak monitorują?

**Sekcja 6: ostatnie incydenty.** Czy mieli incydent cyberbezpieczeństwa w ostatnich 24 miesiącach? Jeśli tak — opis, wpływ, lessons learned.

Kwestionariusz wypełniony przez dostawcę nie jest dowodem, jest deklaracją. Dla dostawców poziomu A trzeba weryfikować przez audyt lub przegląd raportów SOC 2.

## Audyty dostawców — kiedy i jak

Pełny audyt dostawcy IT to znaczący nakład. Proporcjonalne podejście:

**Dostawcy poziomu A:** raz w roku przegląd raportu SOC 2 Type II (lub równoważnego, np. ISAE 3402, ISO 27001 z ostatniego audytu zewnętrznego). Co 2–3 lata pełny audyt na miejscu (jeśli proporcjonalne i kontraktowo dopuszczalne) lub przez niezależnego audytora trzeciego.

**Dostawcy poziomu B:** weryfikacja kwestionariusza co 18 miesięcy, sprawdzenie certyfikacji, ewentualnie referencyjny audyt zewnętrzny.

**Dostawcy poziomu C:** kontrola minimalna — odnowienie kwestionariusza co 24 miesiące.

Praktycznie firma 100-osobowa może obsłużyć: 4–6 pełnych audytów dostawców rocznie (poziom A), 12–18 weryfikacji kwestionariuszy poziom B, 30–40 odnowień poziom C. Łączny nakład czasu Cybersecurity Officera: 200–350 godzin rocznie (10–15% etatu na obszar łańcucha dostaw).

Koszt zewnętrzny audytów: 5 000–25 000 zł na pojedynczy audyt dostawcy w zależności od skali.

## Plan reakcji na incydent po stronie dostawcy

Co robić, gdy dostawca zgłasza incydent? Procedura wewnętrzna powinna obejmować:

**Godzina 0–2:** odbiór zgłoszenia, wyznaczenie osoby koordynującej po Twojej stronie, wstępna ocena wpływu na Twoje systemy i dane.

**Godzina 2–6:** szczegółowa komunikacja z dostawcą (telefonicznie, nie tylko mailowo), zebranie informacji technicznych (jakie dane, jakie systemy, jaki wektor ataku), decyzja o izolacji integracji z dostawcą jeśli konieczna.

**Godzina 6–24:** ocena, czy incydent kwalifikuje się jako Twój incydent NIS2 (jeśli tak — uruchomienie protokołu trójstopniowego), ocena, czy są naruszone dane osobowe (jeśli tak — uruchomienie procedury RODO), komunikacja wewnętrzna w organizacji.

**Godzina 24–72:** koordynacja działań naprawczych z dostawcą, ocena, czy potrzebna komunikacja do klientów/partnerów, dokumentacja wszystkich działań.

**Po 30 dniach:** wspólny przegląd post-incydent z dostawcą, lessons learned, ewentualne renegocjacje umowy lub zmiana dostawcy.

Kluczowy element często pomijany: w umowie powinien być wskazany konkretny kanał komunikacji awaryjnej (telefon dyżurny dostawcy, kontakt 24/7), nie tylko ogólny adres email. W razie incydentu w nocy w niedzielę email może czekać 12 godzin na odpowiedź.

## Audyt łańcucha dostaw — case studies

**Case 1: średnia firma kurierska.** Mapa dostawców: 42 podmiotów. Po klasyfikacji: 5 poziomu A (chmura główna, ERP, system zarządzania flotą, dostawca łączności, biuro księgowe z dostępem do faktur), 14 poziomu B, 23 poziomu C. Pierwsza ocena ujawniła: 8 dostawców bez aktualnych klauzul cyberbezpieczeństwa w umowach, 3 dostawców używających kont współdzielonych zamiast indywidualnych, 1 krytyczny dostawca bez ubezpieczenia cyber. Plan naprawczy: renegocjacje z 8 dostawcami, zmiana procesu dla 3 dostawców, wymiana 1 dostawcy. Czas wdrożenia: 6 miesięcy. Koszt: 35 000 zł plus czas wewnętrzny.

**Case 2: producent artykułów gospodarstwa domowego.** Mapa: 58 dostawców. Niespodzianka: kluczowy dostawca SaaS używał 4 subdostawców (firmy chmurowe i dostawcy specjalistycznych komponentów), o czym firma nie wiedziała. Renegocjacja umowy z dostawcą wymusiła ujawnienie subdostawców i dodanie klauzul flow-down. Wykryto, że jeden subdostawca nie miał certyfikacji ISO 27001 mimo deklaracji dostawcy głównego.

**Case 3: średnia firma usług finansowych.** Mapa: 67 podmiotów. Złożoność dodatkowa — równolegle DORA (Digital Operational Resilience Act), która ma jeszcze ostrzejsze wymagania dla łańcucha dostaw IT w sektorze finansowym. Wdrożenie zintegrowane: NIS2 + DORA + RODO w jednym systemie. Koszt: 220 000 zł, czas: 9 miesięcy.

## Najczęstsze błędy zarządzania łańcuchem dostaw

**Błąd 1: pomijanie subdostawców.** Mapa zawiera dostawców bezpośrednich, ale ignoruje ich subdostawców, którzy często mają realny dostęp do systemów. SolarWinds był subdostawcą dla wielu firm — nikt z dotkniętych organizacji nie miał go formalnie w mapach swoich kluczowych dostawców.

**Błąd 2: kwestionariusze nigdy nie weryfikowane.** Dostawca wypełnia kwestionariusz raz, deklaruje wszystko najlepsze, dokument trafia do segregatora. Bez weryfikacji przez audyt lub raport zewnętrzny — kwestionariusz to tylko marketing.

**Błąd 3: klauzule kontraktowe w PDF, ale nie wdrożone operacyjnie.** Umowa zawiera świetne klauzule, ale w praktyce dostawca nie wie do kogo zgłaszać incydenty, a Zamawiający nigdy nie testował procesu eskalacji. Pierwsza realna sytuacja ujawnia, że proces nie istnieje.

**Błąd 4: brak wymogu informowania o zmianie subdostawców.** Dostawca zmienia podwykonawców i nie informuje. Zamawiający nie wie, że jego dane są przetwarzane w nowej lokalizacji.

**Błąd 5: lock-in bez planu wyjścia.** Dostawca poziomu A obsługuje krytyczny system, ale nie istnieje plan migracji do innego dostawcy. W razie problemów — nie ma alternatywy. NIS2 nie wymaga formalnego planu exit, ale wymaga zarządzania ryzykiem zależności od kluczowych dostawców.

## Lista kontrolna gotowości łańcucha dostaw

Dziewięć pytań, które każda firma podlegająca NIS2 powinna móc twierdząco odpowiedzieć:

1. Czy mamy aktualną mapę wszystkich dostawców IT i usług dotykających systemów krytycznych?
2. Czy każdy dostawca ma przypisany poziom ryzyka (A/B/C lub równoważny)?
3. Czy wszyscy dostawcy poziomu A mają w umowach klauzule cyberbezpieczeństwa minimum z [naszej listy 8 klauzul]?
4. Czy wszyscy dostawcy poziomu A mają aktualne raporty audytów (SOC 2, ISO 27001) lub przeszli audyt indywidualny?
5. Czy wszyscy dostawcy A i B wypełnili kwestionariusz cyberbezpieczeństwa w ostatnich 18 miesiącach?
6. Czy mamy procedurę reakcji na incydent po stronie dostawcy, z wyznaczonymi osobami i kontaktami awaryjnymi?
7. Czy wiemy, jakich subdostawców używają nasi kluczowi dostawcy?
8. Czy mamy plan reakcji na lock-in u kluczowych dostawców?
9. Czy roczny przegląd ryzyka łańcucha dostaw odbywa się jako odrębny punkt agendy zarządu?

Pełen kontekst NIS2 — [NIS2: kompletna checklista gotowości w 10 obszarach](/nis2-checklista-gotowosci-10-obszarow). Specyficznie procedura raportowania — [Raportowanie incydentów 24/72h](/raportowanie-incydentow-24-72h-protokol).

## Bibliografia

<ul>
<li>Komisja Europejska. (2022). <em>Dyrektywa Parlamentu Europejskiego i Rady (UE) 2022/2555 z dnia 14 grudnia 2022 r. (NIS2)</em> — art. 21 ust. 2 lit. d, art. 22. <a href="https://eur-lex.europa.eu/legal-content/PL/TXT/?uri=CELEX:32022L2555">https://eur-lex.europa.eu/legal-content/PL/TXT/?uri=CELEX:32022L2555</a></li>
<li>ENISA. (2024). <em>Supply Chain Risk Management for ICT Systems and Services</em>. European Union Agency for Cybersecurity. [DO WERYFIKACJI URL]</li>
<li>NIST. (2022). <em>Special Publication 800-161 Rev. 1: Cybersecurity Supply Chain Risk Management Practices</em>. National Institute of Standards and Technology. <a href="https://doi.org/10.6028/NIST.SP.800-161r1">https://doi.org/10.6028/NIST.SP.800-161r1</a></li>
<li>SolarWinds Corporation. (2021). <em>Investigation Update on Cyberattack</em>. SolarWinds. [DO WERYFIKACJI URL]</li>
<li>CISA. (2021). <em>Emergency Directive 21-01: Mitigate SolarWinds Orion Code Compromise</em>. Cybersecurity & Infrastructure Security Agency. <a href="https://www.cisa.gov/news-events/directives/ed-21-01-mitigate-solarwinds-orion-code-compromise">https://www.cisa.gov/news-events/directives/ed-21-01-mitigate-solarwinds-orion-code-compromise</a></li>
<li>AICPA. (2017). <em>SOC 2 Reports — Reporting on Controls at a Service Organization</em>. American Institute of CPAs. <a href="https://www.aicpa-cima.com/topic/audit-assurance/audit-and-assurance-greater-than-soc-2">https://www.aicpa-cima.com/topic/audit-assurance/audit-and-assurance-greater-than-soc-2</a></li>
<li>ISO. (2022). <em>ISO/IEC 27036-2:2022 — Cybersecurity — Supplier relationships</em>. International Organization for Standardization. <a href="https://www.iso.org/standard/82072.html">https://www.iso.org/standard/82072.html</a></li>
</ul>

---

**Łańcuch dostaw to obszar, w którym najwięcej firm ma luki.** W cotygodniowym newsletterze TestNIS2.pl publikujemy szablony umów, kwestionariuszy oceny dostawców i analiz konkretnych incydentów supply chain w polskich firmach. [Zapisz się — bezpłatnie](#newsletter-signup).
