---
title: "Audyt RODO art. 32 — bezpieczeństwo techniczne i organizacyjne w praktyce"
slug: "audyt-rodo-art-32-bezpieczenstwo-techniczne"
excerpt: "Art. 32 RODO wymaga 'odpowiednich środków technicznych i organizacyjnych'. Co to znaczy w audycie? Pełna metodologia weryfikacji bezpieczeństwa danych osobowych."
category_slug: "rodo"
tags: "RODO, art. 32, audyt, bezpieczeństwo techniczne, środki organizacyjne, GDPR, średniozaawansowany"
reading_time: 14
is_published: true
is_featured: false
meta_title: "Audyt RODO art. 32 — bezpieczeństwo techniczne i organizacyjne (2026)"
meta_description: "Jak audytować zgodność z art. 32 RODO. Konkretne pytania, dowody do zebrania, testy techniczne, kryteria oceny. Dla IOD, audytorów i compliance."
funnel: "MOFU"
author_slug: "marek-porycki"
related_slugs: "audyt-nis2-art-21-krok-po-kroku-metodologia-audytora,audyt-rodo-krok-po-kroku,dpia-w-praktyce-kiedy-obowiazuje-jak-wykonac,audyt-umow-powierzenia-art-28-rodo,audyt-kryptografii-nis2-rodo"
product_slugs: ""
---

Artykuł 32 RODO jest najbardziej cytowanym i najtrudniej audytowalnym przepisem rozporządzenia. Wymaga, by administrator i procesor wdrożyli "odpowiednie środki techniczne i organizacyjne, aby zapewnić stopień bezpieczeństwa odpowiadający ryzyku". W tekście rozporządzenia są tylko cztery konkretne przykłady — pseudonimizacja i szyfrowanie, zdolność do zapewnienia poufności, integralności, dostępności i odporności systemów, zdolność do szybkiego przywrócenia dostępności, regularne testowanie skuteczności środków. Resztę zostawia kontrolerom danych.

Ta otwartość art. 32 jest jednocześnie jego siłą (skalowalność do różnych firm) i słabością (niejednoznaczność audytowa). UODO w decyzjach z lat 2020–2025 sukcesywnie precyzuje, co dla średniej polskiej firmy oznacza "odpowiednie środki". Audytor RODO musi znać te decyzje, znać standardy techniczne (ISO 27001, NIST SP 800-53), znać typową architekturę IT polskiej firmy i połączyć to w spójną metodologię.

Ten tekst jest pełną metodologią audytu zgodności z art. 32. Strukturuje się wokół czterech kategorii środków (kryptografia, ciągłość, monitoring, organizacja), dla każdej podaje pytania, dowody, testy techniczne i kryteria oceny. Adresat: IOD/DPO, audytorzy wewnętrzni i zewnętrzni RODO, dyrektorzy bezpieczeństwa odpowiedzialni za wdrożenie środków.

## Co dokładnie wymaga art. 32

Tekst art. 32 ust. 1 RODO: "Uwzględniając stan wiedzy technicznej, koszt wdrażania oraz charakter, zakres, kontekst i cele przetwarzania oraz ryzyko naruszenia praw lub wolności osób fizycznych o różnym prawdopodobieństwie wystąpienia i wadze zagrożenia, administrator i podmiot przetwarzający wdrażają odpowiednie środki techniczne i organizacyjne".

Cztery przykłady w ust. 1 lit. a–d:
- (a) pseudonimizacja i szyfrowanie danych osobowych
- (b) zdolność do ciągłego zapewnienia poufności, integralności, dostępności i odporności systemów i usług przetwarzania
- (c) zdolność do szybkiego przywrócenia dostępności danych osobowych i dostępu do nich w razie incydentu fizycznego lub technicznego
- (d) regularne testowanie, mierzenie i ocenianie skuteczności środków technicznych i organizacyjnych mających zapewnić bezpieczeństwo przetwarzania

Art. 32 ust. 2 dodaje: "Oceniając, czy stopień bezpieczeństwa jest odpowiedni, uwzględnia się w szczególności ryzyko wiążące się z przetwarzaniem, w szczególności wynikające z przypadkowego lub niezgodnego z prawem zniszczenia, utraty, modyfikacji, nieuprawnionego ujawnienia lub nieuprawnionego dostępu".

Audyt zgodności z art. 32 oznacza więc weryfikację: czy firma przeprowadziła analizę ryzyka, czy na jej podstawie wybrała środki, czy wdrożyła je technicznie, czy regularnie testuje skuteczność. Wszystkie cztery elementy muszą występować. Brak analizy ryzyka = automatycznie niezgodność, nawet jeśli wdrożone środki są zaawansowane.

## Kategoria 1: Środki kryptograficzne (pseudonimizacja i szyfrowanie)

**Dokumenty do zebrania.** Polityka kryptograficzna firmy, lista systemów z włączonym szyfrowaniem (w spoczynku i w tranzycie), polityka zarządzania kluczami kryptograficznymi, dokumentacja KMS (Key Management System) jeśli używany, raporty z audytów konfiguracji TLS.

**Pytania do wywiadu z IT/CISO.** Które bazy danych z danymi osobowymi są szyfrowane w spoczynku (encryption at rest)? Jaką wersję TLS wymuszacie? Jak zarządzacie kluczami kryptograficznymi — gdzie są przechowywane, kto ma dostęp, jak są rotowane? Czy stosujecie pseudonimizację w środowiskach nieprodukcyjnych (test, dev, staging)?

**Testy techniczne.** Audytor wybiera trzy bazy danych zawierające dane osobowe. Dla każdej weryfikuje: czy faktycznie jest szyfrowanie na poziomie storage (TDE w SQL Server, encryption at rest w PostgreSQL, ATRest w MongoDB), jakim algorytmem (AES-256 jako standard, AES-128 jako minimum, wszystko poniżej = ustalenie), jak są zabezpieczone klucze (oddzielnie od bazy, idealnie w HSM lub cloud KMS). Drugi test: skan TLS portali zewnętrznych przy użyciu narzędzia takiego jak SSL Labs lub testssl.sh — sprawdza wersje TLS, suity szyfrów, problemy z certyfikatami.

**Częste ustalenia.**
- Baza produkcyjna szyfrowana, ale środowiska dev/test z kopią produkcji bez szyfrowania i bez pseudonimizacji (klasyczny błąd, częsta przyczyna naruszeń).
- Klucze szyfrowania w tym samym serwerze co dane (równoznaczne z brakiem szyfrowania w kontekście ataku z dostępem do serwera).
- TLS 1.0/1.1 nadal aktywne na starszych portalach (poniżej standardu od 2020).
- Brak polityki rotacji kluczy lub polityka istniejąca, ale niewykonywana.

Powiązany obszar: [audyt kryptografii (NIS2 art. 21(2)(h) + RODO art. 32)](audyt-kryptografii-nis2-rodo.html) — szczegółowa metodologia.

## Kategoria 2: Poufność, integralność, dostępność, odporność (CIA-R)

**Co wchodzi w zakres.** Kontrola dostępu, segregacja środowisk, monitoring zmian (integralność), zarządzanie tożsamością, MFA, monitorowanie nieautoryzowanych zmian danych, zabezpieczenia przed DDoS.

**Dokumenty do zebrania.** Polityka kontroli dostępu, polityka MFA, polityka segregacji obowiązków, lista użytkowników uprzywilejowanych, raporty access review, dokumentacja architektury sieci (segmentacja), polityka logowania (które systemy logują, gdzie są logi, jak długo, kto ma dostęp).

**Pytania do wywiadu.** Jakie systemy zawierające dane osobowe mają wymuszone MFA? Jak często robicie access review i co z tego wynika? Jak długo trwa od momentu wypowiedzenia umowy do zablokowania wszystkich kont byłego pracownika? Czy macie segregację środowisk (produkcja oddzielona od test/dev na poziomie sieciowym i tożsamości)?

**Testy techniczne.**
- Test MFA: audytor prosi o pokazanie konfiguracji MFA w trzech systemach krytycznych z danymi osobowymi (np. CRM, system kadrowo-płacowy, baza klientów). Sprawdza realny stan, nie deklarowany.
- Test off-boardingu: lista 5 osób, które odeszły w ostatnim miesiącu — czy konta są zablokowane, kiedy, w jakich systemach.
- Test kont uprzywilejowanych: lista kont admin/root, weryfikacja czy są aktualnie potrzebne, czy są MFA, czy logi są audytowalne.
- Test segregacji: czy konsultant developerski może wejść z produkcji do bazy produkcyjnej? Czy są mosty między dev a prod?

**Kryteria oceny.** Standard 2026: MFA dla wszystkich kont uprzywilejowanych (100%), MFA dla wszystkich systemów zewnętrznie dostępnych (VPN, panele cloud, e-mail), access review minimum raz na 6 miesięcy, off-boarding do 24h od końca umowy, pełna segregacja środowisk (oddzielne tożsamości, nie tylko sieciowo).

Pełna metodologia tego obszaru: [audyt MFA i kontroli dostępu](audyt-mfa-i-kontroli-dostepu-nis2.html).

## Kategoria 3: Zdolność do przywrócenia dostępności (BCP/DR dla danych osobowych)

**Co wchodzi w zakres.** Backupy danych osobowych, plan disaster recovery, test odtwarzania, RPO/RTO udokumentowane.

**Dokumenty do zebrania.** Polityka backupów (z konkretnymi RPO/RTO per system z danymi osobowymi), raporty z testów odtwarzania (DR drill) z ostatnich 24 miesięcy, mapa systemów-zależności, plan komunikacji kryzysowej dla naruszenia dostępności.

**Pytania do wywiadu.** Jaki RPO/RTO masz dla bazy klientów? Kiedy ostatnio testowałeś przywrócenie z backupu i z jakim wynikiem? Co się stanie z danymi osobowymi, jeśli serwer w głównej lokalizacji jest niedostępny przez 7 dni? Czy backupy mają immutable retention (odporność na ransomware)?

**Testy techniczne.** Audytor prosi o przywrócenie wybranej tabeli z bazą klientów z backupu z konkretnego dnia w ostatnim miesiącu. Mierzy czas, sprawdza spójność danych. To jest test krytyczny — sam fakt, że backupy istnieją, nie znaczy nic. Druga próba: czy backup jest off-site (poza główną lokalizacją), trzecia — czy jest air-gapped lub immutable.

**Kryteria oceny.** Minimum dla art. 32: regularne testy odtwarzania (minimum raz w roku, idealnie kwartalnie), backupy w strategii 3-2-1 (3 kopie, 2 nośniki, 1 off-site), immutable lub air-gapped dla danych krytycznych.

Powiązany obszar: [audyt ciągłości działania (BCP/DR)](audyt-ciaglosci-dzialania-bcp-dr-nis2.html).

## Kategoria 4: Regularne testowanie i ocenianie skuteczności

To kategoria, w której większość polskich firm jest słabo audytowana, bo skupia się na implementacji ("mamy MFA, mamy szyfrowanie") zamiast na weryfikacji skuteczności ("czy MFA jest faktycznie używany, czy są obejścia, jaka jest pokrycie").

**Dokumenty do zebrania.** Harmonogram testów penetracyjnych (z ostatnich 24 miesięcy), raporty pentestów, harmonogram skanów podatności, raporty z testów phishing simulations, raporty z testów DR, plan przeglądu skuteczności środków technicznych i organizacyjnych.

**Pytania do wywiadu.** Kiedy ostatnio robiłeś pentest systemów zawierających dane osobowe, jaki był zakres i kto wykonywał? Jak często robisz vulnerability scanning i jakim narzędziem? Czy w ramach przygotowania do art. 32 wykonano formalną ocenę skuteczności środków przez niezależną stronę?

**Testy techniczne.** Audytor sprawdza ostatni raport pentestu — co było w scopie, jakie podatności znaleziono, jaki jest aktualny status remediacji. Drugi test: ostatni vulnerability scan — czy są CVE krytyczne starsze niż 30 dni bez remediacji i czy są mitigants kompensujące.

**Kryteria oceny.** Pentesty: minimum raz w roku dla systemów zewnętrznych, raz na 2 lata dla wewnętrznych krytycznych. Skany podatności: minimum miesięczne dla infrastruktury, ciągłe dla aplikacji webowych. Phishing simulations: kwartalne. Przegląd skuteczności środków: roczny, formalny, z udziałem IOD i CISO.

## Powiązanie art. 32 z analizą ryzyka

Kluczowa pułapka audytowa: art. 32 RODO wymaga, by środki bezpieczeństwa były "odpowiednie do ryzyka". To znaczy, że bez przeprowadzonej analizy ryzyka nie da się formalnie ocenić, czy środki są wystarczające. Audytor musi sprawdzić:

1. Czy firma przeprowadziła analizę ryzyka dla każdej kluczowej operacji przetwarzania (typowo: kadry, marketing, klienci, dostawcy, monitoring pracowników, dane zdrowotne jeśli applicable).
2. Czy analiza ryzyka identyfikuje ryzyka specyficzne dla typu danych (np. ryzyko dyskryminacji przy danych zdrowotnych, ryzyko stalkingu przy danych lokalizacyjnych).
3. Czy wybór środków bezpieczeństwa jest uzasadniony wynikiem analizy ryzyka.
4. Czy istnieje udokumentowane ryzyko rezydualne, zaakceptowane formalnie.

Bez tej dokumentacji audyt art. 32 nie może zakończyć się oceną pozytywną — nawet jeśli wdrożone środki są zaawansowane. UODO w kilku decyzjach (m.in. nakaz wobec spółki energetycznej z 2023 r.) wprost wskazał brak analizy ryzyka jako podstawową przyczynę naruszenia art. 32, mimo wdrożonych konkretnych środków technicznych.

Jeśli odpowiadasz za przygotowanie firmy do takiego audytu i potrzebujesz szablonu analizy ryzyka dla typowych operacji przetwarzania (z gotową listą zagrożeń, prawdopodobieństw i wpływów), warto zapisać się do newslettera skanujfirme.pl — przesyłamy template'y formalnej analizy ryzyka RODO w XLSX/DOCX, użyteczne jako baza do dostosowania.

## Format ustaleń w raporcie audytu art. 32

Każde ustalenie z audytu art. 32 powinno mieć w raporcie strukturę spójną z innymi obszarami audytu. Przykład typowego ustalenia:

> **Ustalenie 32-04 (klasyfikacja: wysokie):** Baza klientów w systemie CRM zawierająca dane osobowe 47 000 osób nie ma włączonego szyfrowania w spoczynku.
>
> **Dowody:** (1) Wywiad z administratorem CRM (data, imię); (2) Konfiguracja serwera bazy danych zweryfikowana przez audytora (data, opis weryfikacji); (3) Brak polityki szyfrowania CRM w dokumentacji RODO.
>
> **Ryzyko prawne:** Naruszenie art. 32 ust. 1 lit. a RODO. W przypadku naruszenia (kradzież dysku, dostęp nieautoryzowany na poziomie systemu plików) ekspozycja danych osobowych ze skutkiem prawnym (obowiązek zgłoszenia do UODO i osób), reputacyjnym i finansowym.
>
> **Rekomendacja korygująca:** Włączenie szyfrowania na poziomie storage (TDE) lub na poziomie wybranych kolumn (column-level encryption dla pól PESEL, adres, telefon). Termin docelowy: 60 dni. Odpowiedzialny: dyrektor IT. Szacunkowy koszt: 0 zł (funkcjonalność dostępna w licencji SQL Server Enterprise).
>
> **Mitigant kompensujący do czasu remediacji:** Ograniczenie dostępu na poziomie sieci do serwera bazy do 3 administratorów, włączenie audytu na poziomie systemu operacyjnego, codzienna weryfikacja logów.

Taki format pozwala zarządowi podejmować decyzje świadomie — widzi ryzyko, koszt, czas, odpowiedzialnego. To jest różnica między raportem audytowym a luźną listą obserwacji.

## Trzy pytania kontrolne dla IOD przed audytem art. 32

**Pierwsze.** Czy mamy aktualny rejestr czynności przetwarzania (RCP)? Jeśli nie — audyt art. 32 nie może się zacząć, bo nie wiadomo, jakie operacje są w zakresie. Najpierw uzupełnij RCP, potem audyt.

**Drugie.** Czy zrobiliśmy analizę ryzyka dla operacji wysokiego ryzyka? Jeśli przetwarzasz dane zdrowotne, dane dzieci, dane biometryczne, dane lokalizacyjne na dużą skalę, dane finansowe wrażliwe — formalna analiza ryzyka jest punktem wyjścia, nie outputem.

**Trzecie.** Czy mamy zewnętrzne dowody skuteczności (pentesty, certyfikaty, audyty)? UODO traktuje brak takich dowodów jako sygnał, że firma "deklaruje, ale nie weryfikuje". W audycie art. 32 zewnętrzne dowody zwiększają wiarygodność oceny o jeden poziom dojrzałości.

## Esencja

Audyt RODO art. 32 nie jest audytem checklisty. Jest oceną adekwatności środków technicznych i organizacyjnych do ryzyka przetwarzania. Cztery elementy muszą wystąpić: środki kryptograficzne (pseudonimizacja, szyfrowanie), CIA-R systemów (poufność, integralność, dostępność, odporność), zdolność do przywrócenia, regularne testowanie skuteczności. Brak któregokolwiek elementu = niezgodność.

Punkt krytyczny: art. 32 wymaga, by środki były odpowiednie do ryzyka. Bez przeprowadzonej analizy ryzyka żaden audyt nie zakończy się pozytywnie, nawet jeśli wdrożone środki techniczne są zaawansowane. UODO konsekwentnie wskazuje brak analizy ryzyka jako przyczynę pierwotną naruszeń.

Cztery kategorie metodologii — kryptografia, CIA-R, BCP/DR, testowanie skuteczności — wymagają różnych dowodów i różnych testów technicznych. Audytor nie może opierać się tylko na dokumentach. Musi weryfikować konfiguracje techniczne, robić skany TLS, prosić o przywrócenie z backupu, sprawdzać raporty pentestów, weryfikować realny stan MFA. Audyt deklaratywny (tylko dokumenty) jest niewystarczający dla art. 32.

Format ustaleń w raporcie audytowym musi wiązać ustalenie z dowodami, ryzykiem prawnym, rekomendacją i mitigantem kompensującym. Bez tej struktury raport nie jest narzędziem decyzyjnym dla zarządu. UODO oceniając poszczególne firmy patrzy na ten format — udokumentowana świadomość ryzyka i plan korygujący istotnie wpływają na łagodzenie sankcji.

W 2026 roku art. 32 RODO i art. 21 NIS2 są reżimami zharmonizowanymi w zakresie technicznym (kryptografia, MFA, ciągłość, monitoring), ale różnymi w celu (RODO chroni osoby fizyczne, NIS2 chroni infrastrukturę). Firma robi jedno wdrożenie techniczne i dwa odrębne audyty z dwoma raportami. Lub jeden audyt zharmonizowany, który omawia oba reżimy — to oszczędność znacząca, ale wymagająca audytora znającego oba systemy.

---

<ul>
<li>Rozporządzenie Parlamentu Europejskiego i Rady (UE) 2016/679 z dnia 27 kwietnia 2016 r. (RODO/GDPR), art. 32 — Bezpieczeństwo przetwarzania. https://eur-lex.europa.eu/eli/reg/2016/679/oj</li>
<li>UODO (2023). <em>Decyzje Prezesa UODO 2018–2023 — bezpieczeństwo przetwarzania (art. 32)</em>. https://uodo.gov.pl/pl/138</li>
<li>EROD/EDPB (2022). <em>Guidelines 9/2022 on personal data breach notification under GDPR</em>. European Data Protection Board. https://www.edpb.europa.eu/our-work-tools/our-documents/guidelines/</li>
<li>ENISA (2021). <em>Handbook on Security of Personal Data Processing</em>. European Union Agency for Cybersecurity. https://www.enisa.europa.eu/publications/handbook-on-security-of-personal-data-processing</li>
<li>ISO/IEC 27701:2019. <em>Privacy Information Management — Extension to ISO/IEC 27001 and ISO/IEC 27002</em>. International Organization for Standardization.</li>
<li>NIST SP 800-53 Rev. 5 (2020). <em>Security and Privacy Controls for Information Systems and Organizations</em>. https://doi.org/10.6028/NIST.SP.800-53r5</li>
<li>NIST SP 800-57 Part 1 Rev. 5 (2020). <em>Recommendation for Key Management — Part 1: General</em>. https://doi.org/10.6028/NIST.SP.800-57pt1r5</li>
<li>Mozilla TLS Configuration Recommendations. https://wiki.mozilla.org/Security/Server_Side_TLS</li>
<li>Polska Ustawa z dnia 10 maja 2018 r. o ochronie danych osobowych (Dz.U. 2018 poz. 1000 ze zm.)</li>
<li>UODO. <em>Wytyczne w sprawie zgłaszania naruszeń ochrony danych osobowych</em> (2019, aktualizacja 2022). https://uodo.gov.pl/</li>
</ul>
