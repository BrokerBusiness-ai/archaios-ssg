---
title: "Audyt NIS2 art. 21 krok po kroku — pełna metodologia audytora dla 10 obszarów"
slug: "audyt-nis2-art-21-krok-po-kroku-metodologia-audytora"
excerpt: "Pełna procedura audytora: jak zweryfikować zgodność firmy z 10 obszarami art. 21 NIS2. Dla każdego obszaru — pytania, dowody, testy techniczne, kryteria oceny."
category_slug: "audyt-nis2-skanuj"
tags: "NIS2, audyt, art. 21, metodologia, audytor, dowody, dyrektywa 2022/2555, zaawansowany"
reading_time: 22
is_published: true
is_featured: true
meta_title: "Audyt NIS2 art. 21 krok po kroku — metodologia audytora (2026)"
meta_description: "Operacyjna metodologia audytu NIS2 art. 21: 10 obszarów, dowody do zebrania, testy techniczne, kryteria oceny, format raportu. Dla audytorów wewnętrznych i zewnętrznych."
funnel: "MOFU-pillar"
author_slug: "marek-porycki"
related_slugs: "kompletny-audyt-firmy-2026,audyt-rodo-art-32-bezpieczenstwo-techniczne,audyt-mfa-i-kontroli-dostepu-nis2,audyt-kryptografii-nis2-rodo,audyt-ciaglosci-dzialania-bcp-dr-nis2,audyt-lancucha-dostaw-it-nis2,audyt-incydentow-24-72h-rodo-nis2"
product_slugs: ""
---

Dyrektywa NIS2 (UE 2022/2555) w artykule 21 wymienia dziesięć obszarów, w których podmiot kluczowy lub istotny musi wdrożyć "odpowiednie i proporcjonalne środki techniczne, operacyjne i organizacyjne zarządzania ryzykiem". Tekst dyrektywy nie podaje, jak audytor ma to zweryfikować. Polska *Ustawa o krajowym systemie cyberbezpieczeństwa* w wersji znowelizowanej (status: projekt na maj 2026) również nie definiuje metodologii. ENISA opublikowała wytyczne implementacyjne (*Technical Implementation Guidance*, 2024), ale są one ukierunkowane na podmiot — nie na audytora.

Ten tekst jest tym, czego brakuje pomiędzy literą dyrektywy a praktyką: pełną metodologią audytora dla każdego z dziesięciu obszarów art. 21. Dla każdego obszaru: jakie pytania zadać, jakie dokumenty zebrać, jakie testy techniczne wykonać, jak ocenić dojrzałość i jak sformułować ustalenie. Adresat: audytorzy wewnętrzni (zespoły compliance, dyrektorzy bezpieczeństwa), audytorzy zewnętrzni (firmy konsultingowe, biegli), oraz członkowie zarządu chcący zrozumieć, na co zwracać uwagę przy zamawianiu audytu zewnętrznego.

Założenie ogólne: audyt NIS2 art. 21 nie ocenia "czy firma jest zgodna" w sensie binarnym. Ocenia dojrzałość każdego obszaru w skali wielopunktowej, lokalizuje luki względem stanu pożądanego i formułuje rekomendacje korygujące. Wynikiem audytu jest raport z mierzalną oceną oraz plan działań naprawczych. Czas wykonania pełnego audytu dla średniej firmy (50–250 pracowników): 6–10 tygodni pracy audytora plus zaangażowanie zespołu wewnętrznego (estymacja 80–160 godzin po stronie firmy).

## Struktura audytu — pięć faz przekrojowych

Niezależnie od obszaru, każdy element audytu NIS2 przechodzi przez pięć faz, których audytor nie powinien skracać.

**Faza A: planowanie i scope.** Definicja zakresu (czy audyt obejmuje wszystkie systemy IT, czy wybrane krytyczne; czy obejmuje wszystkie lokalizacje, czy główną siedzibę), ustalenie zespołu po stronie firmy, harmonogram, lista wymaganych dokumentów do przygotowania przed startem (typowo 30–60 pozycji).

**Faza B: zebranie dowodów.** Trzy źródła równolegle: dokumenty (polityki, procedury, rejestry, raporty), wywiady (z osobami pełniącymi role kluczowe — CISO, IOD, IT manager, członkowie zarządu, wybrani pracownicy operacyjni), obserwacja i testy techniczne (przegląd konfiguracji, walk-through procesów, próby symulacyjne).

**Faza C: ocena dojrzałości.** Dla każdego obszaru: skala 0–5 (0 = nie istnieje, 1 = ad hoc, 2 = repetytywne, 3 = zdefiniowane i udokumentowane, 4 = zarządzane z metrykami, 5 = zoptymalizowane z ciągłym doskonaleniem). Każdy poziom ma jasne kryteria — co audytor musi zobaczyć, by uznać że jest na tym poziomie.

**Faza D: analiza luki.** Porównanie aktualnej dojrzałości z poziomem docelowym (dla NIS2 typowo poziom 3 jako minimum dla podmiotów kluczowych, poziom 2 jako minimum dla istotnych). Identyfikacja luk, oszacowanie ryzyka rezydualnego, hierarchia priorytetów.

**Faza E: raport i plan działań.** Raport zawiera: ocenę w 10 obszarach (skala 0–5), listę ustaleń (findings) z klasyfikacją (krytyczne, wysokie, średnie, niskie), plan działań naprawczych (CAPA — Corrective and Preventive Actions) z odpowiedzialnymi i terminami. Format zgodny z [raportem audytowym dla zarządu](raport-audytowy-dla-zarzadu-jak-go-napisac.html).

Te pięć faz powtarza się równolegle dla każdego z dziesięciu obszarów. Czas faz A i E jest stały (po około tydzień), fazy B i C zajmują 4–7 tygodni, faza D — tydzień.

## Obszar 1: Polityka analizy ryzyka i bezpieczeństwa systemów IT (art. 21(2)(a))

**Co dyrektywa wymaga.** Firma musi mieć udokumentowaną politykę zarządzania ryzykiem cybernetycznym, opartą na metodyce (ISO/IEC 27005, NIST RMF lub równoważne), z regularnym przeglądem (minimum raz w roku) oraz integracją z ogólnym systemem zarządzania ryzykiem firmy.

**Dokumenty do zebrania.** Polityka zarządzania ryzykiem cybernetycznym (dokument formalny, podpisany przez zarząd), rejestr ryzyk (risk register) z aktualną datą aktualizacji, metodyka wyceny ryzyka (jak liczone są prawdopodobieństwo i wpływ), protokoły z ostatnich przeglądów ryzyka (minimum z ostatnich 24 miesięcy), raporty dla zarządu z zarządzania ryzykiem.

**Pytania do wywiadu z CISO/dyrektorem IT.** Kto jest odpowiedzialny za politykę? Kiedy ostatnio była aktualizowana? Jakie są pięć top ryzyk cybernetycznych firmy w tym kwartale i jakie mitigants są wdrożone? Jak ryzyko cybernetyczne jest integrowane z ogólnym risk managementem firmy (ERM)? Czy zarząd kwartalnie omawia top ryzyka cybernetyczne?

**Testy do wykonania.** Audytor wybiera trzy aktywa krytyczne (np. system ERP, baza klientów, system płacowy) i prosi o przedstawienie kompletnej analizy ryzyka dla każdego — od identyfikacji zagrożeń, przez wycenę prawdopodobieństwa i wpływu, po wybrane środki kontrolne i ryzyko rezydualne. Sprawdza spójność z polityką ogólną.

**Kryteria oceny dojrzałości.**
- Poziom 0: brak polityki lub polityka istniejąca tylko formalnie, bez stosowania.
- Poziom 1: polityka jest, ale stosowana ad hoc, jeden risk register, ale nieaktualizowany.
- Poziom 2: polityka stosowana w niektórych obszarach (zwykle IT), nie wszędzie, aktualizowana okazjonalnie.
- Poziom 3: polityka kompletnie udokumentowana, stosowana w całej firmie, aktualizowana raz w roku z udziałem zarządu, risk register aktualny.
- Poziom 4: poziom 3 + metryki skuteczności (KRI — Key Risk Indicators), kwartalne przeglądy zarządu, integracja z ERM.
- Poziom 5: poziom 4 + ciągłe doskonalenie metodyki, benchmarking z branżą, threat intelligence aktywnie wykorzystywane w aktualizacji rejestru.

**Częste ustalenia.** Większość polskich średnich firm jest na poziomie 1–2: polityka istnieje, ale w wersji ogólnikowej, risk register prowadzony jest przez jedną osobę (zwykle dyrektor IT) bez udziału biznesu, zarząd nie ma kwartalnych raportów. Aby przekroczyć poziom 3, firma potrzebuje formalnej metodyki, dedykowanego CISO lub osoby odpowiedzialnej za risk management, oraz włączenia ryzyka cybernetycznego do agendy zarządu.

## Obszar 2: Obsługa incydentów cyberbezpieczeństwa (art. 21(2)(b))

**Co dyrektywa wymaga.** Procedury wykrywania, analizy, zawiadamiania, reagowania i analizy poincydentalnej. Powiązanie z obowiązkiem raportowania do CSIRT-u w terminach 24h / 72h / 1 miesiąc.

**Dokumenty do zebrania.** Incident Response Plan (IRP) — formalny dokument, lista członków zespołu reagowania (CSIRT wewnętrzny lub osoby pełniące tę rolę), procedury eskalacji, runbooki dla typowych scenariuszy (ransomware, phishing, DDoS, naruszenie danych, kompromitacja konta uprzywilejowanego), rejestr incydentów z ostatnich 24 miesięcy z klasyfikacją, raporty post-incident review (PIR), umowy z zewnętrznym SOC lub forensykami (jeśli outsourcowane).

**Pytania do wywiadu.** Ile incydentów było w ostatnich 12 miesiącach (w podziale na poziomy)? Pokaż ostatni raport PIR — co się stało, jak długo trwało wykrycie, kontener, mitygacja? Jakie scenariusze macie w runbookach i kiedy je ostatnio ćwiczyliście? Kto budzi członka zarządu o 3:00 w nocy przy krytycznym incydencie?

**Testy do wykonania.** Symulacja stołowa (tabletop exercise) typowego scenariusza — np. ransomware. Audytor prowadzi scenariusz: "10 maja 2026 o 02:14 monitoring SOC zgłasza, że 80 stacji w dziale księgowości jest zaszyfrowanych, w notatce ransomware żądanie 800 000 EUR w bitcoin w ciągu 72h". Audytor obserwuje: kto jest powiadamiany, w jakim czasie, jakie decyzje są podejmowane, jakie zewnętrzne strony są kontaktowane (CSIRT NASK, ubezpieczyciel, prawnicy, klienci, UODO jeśli RODO), kiedy zarząd otrzymuje pierwszą informację.

**Kryteria oceny dojrzałości.**
- Poziom 0: brak formalnego IRP, "ogarniamy jak przyjdzie".
- Poziom 1: IRP istnieje, ale w wersji generycznej, nieaktualizowanej, nikt nigdy nie ćwiczył.
- Poziom 2: IRP + runbooki dla 1–2 scenariuszy, jedno ćwiczenie w przeszłości, niezbyt świeże.
- Poziom 3: IRP + 5+ runbooków + roczne ćwiczenia + pełen rejestr incydentów + PIR po każdym poważnym incydencie.
- Poziom 4: poziom 3 + metryki MTTD (Mean Time To Detect) i MTTR (Mean Time To Respond), kwartalne ćwiczenia, integracja z SOAR.
- Poziom 5: poziom 4 + threat hunting proaktywny, purple teaming, ciągłe doskonalenie runbooków.

**Częste ustalenia.** W połowie polskich średnich firm IRP jest "u jednego kolesia w głowie" — IT manager wie co robić, ale nikt poza nim. Brak ćwiczeń to standard. Polskie CSIRT-y (NASK, CERT.GOV.PL, sektorowe) raportują, że pierwsze 60 minut po incydencie firmy zwykle marnują na ustalanie kto kogo powiadomi.

## Obszar 3: Ciągłość działania, kopie zapasowe i zarządzanie kryzysowe (art. 21(2)(c))

**Co dyrektywa wymaga.** Plan ciągłości działania (BCP), plan disaster recovery (DR), strategia kopii zapasowych, plan komunikacji kryzysowej, zarządzanie kryzysem. Wszystko z udokumentowanymi RTO (Recovery Time Objective) i RPO (Recovery Point Objective) dla kluczowych usług.

**Dokumenty do zebrania.** Business Continuity Plan z analizą BIA (Business Impact Analysis), Disaster Recovery Plan z mapą zależności systemów, polityka kopii zapasowych, raporty z testów DR z ostatnich 24 miesięcy, plan komunikacji kryzysowej, lista alternatywnych lokalizacji pracy.

**Pytania do wywiadu.** Jaki masz RTO dla systemu finansowego? Kiedy ostatnio testowaliście DR i z jakim wynikiem? Co się stanie z firmą jeśli serwerownia w głównej lokalizacji jest niedostępna przez 7 dni? Kto decyduje o ogłoszeniu sytuacji kryzysowej?

**Testy do wykonania.** Test backupu: audytor wybiera trzy systemy krytyczne, prosi o przywrócenie z backupu wybranego dnia z ostatnich 30 dni. Sprawdza czy proces działa, ile trwa, czy dane są spójne. To jest kluczowy test — sam fakt istnienia backupów nie znaczy nic bez weryfikacji odzyskiwania.

**Kryteria oceny dojrzałości.**
- Poziom 0: backupy może są, plan BCP nie istnieje.
- Poziom 1: backupy są (3-2-1 nieprzestrzegane), BCP w wersji generycznej.
- Poziom 2: 3-2-1 wdrożone, BCP istnieje, jedno testowanie odzyskiwania w przeszłości.
- Poziom 3: BCP + DR + BIA + RTO/RPO udokumentowane dla wszystkich systemów krytycznych, roczne testy DR, kopie immutable.
- Poziom 4: poziom 3 + kwartalne testy DR, automatyczna weryfikacja integralności backupów, off-site air-gapped copies.
- Poziom 5: poziom 4 + active-active multi-site, chaos engineering, ciągła weryfikacja.

Szczegóły metodologii dla tego obszaru: [audyt ciągłości działania (BCP/DR)](audyt-ciaglosci-dzialania-bcp-dr-nis2.html).

## Obszar 4: Bezpieczeństwo łańcucha dostaw (art. 21(2)(d))

**Co dyrektywa wymaga.** Identyfikacja dostawców krytycznych, ocena ryzyka per dostawca, klauzule bezpieczeństwa w umowach, monitorowanie zgodności dostawców, plan reakcji na incydent po stronie dostawcy.

**Dokumenty do zebrania.** Mapa dostawców z klasyfikacją (krytyczny / istotny / standardowy), oceny ryzyka per dostawca krytyczny, wzory klauzul bezpieczeństwa stosowane w umowach, raporty z due diligence (SOC 2, ISO 27001, audyty wewnętrzne), procedura on-boardingu nowego dostawcy.

**Pytania do wywiadu.** Ilu macie dostawców krytycznych i według jakich kryteriów ich klasyfikujecie? Pokaż umowę z dostawcą krytycznym — gdzie są klauzule cyberbezpieczeństwa? Co się stanie jeśli dostawca cloud (np. AWS, Azure) ma 48-godzinny incydent? Czy monitorujecie zgodność dostawców regularnie czy tylko przy podpisaniu?

**Testy do wykonania.** Audytor wybiera trzech dostawców krytycznych. Dla każdego prosi o: aktualną ocenę ryzyka (nie starszą niż 12 miesięcy), kompletną umowę z klauzulami, dokumenty potwierdzające zgodność (certyfikaty), historię incydentów. Sprawdza, czy klauzule umowne pokrywają minimum: prawo do audytu, obowiązek raportowania incydentów, klauzule o sub-procesorach, zwrot/zniszczenie danych po zakończeniu umowy.

**Kryteria oceny dojrzałości.** Większość firm średnich jest na poziomie 1–2: mają jakąś listę dostawców, ale nieformalną klasyfikację, klauzule bezpieczeństwa są w niektórych umowach (zwykle tych nowszych), regularne oceny dostawców nie istnieją.

Pełna metodologia tego obszaru: [audyt łańcucha dostaw IT](audyt-lancucha-dostaw-it-nis2.html).

## Obszar 5: Bezpieczeństwo w pozyskiwaniu, rozwoju i utrzymaniu systemów (art. 21(2)(e))

**Co dyrektywa wymaga.** SDLC z wbudowanym bezpieczeństwem (secure development lifecycle), zarządzanie podatnościami (vulnerability management), patch management, security testing.

**Dokumenty do zebrania.** Polityka SDLC (jeśli firma rozwija oprogramowanie wewnętrznie), polityka zarządzania podatnościami, polityka patch managementu, raporty ze skanów podatności z ostatnich 12 miesięcy, raporty z testów penetracyjnych, harmonogram pentestów.

**Pytania do wywiadu.** Jak często skanujecie infrastrukturę pod kątem podatności? Jaki jest średni czas od opublikowania CVE krytycznego do zapatchowania w produkcji? Kiedy ostatnio robiliście pentest, kto i z jakim zakresem?

**Testy do wykonania.** Audytor prosi o ostatni raport z vulnerability scan i wybiera trzy podatności krytyczne starsze niż 30 dni. Pyta: czemu nie zapatchowane, jaki jest plan, czy są mitigants kompensujące. To pokazuje, czy firma faktycznie zarządza ryzykiem czy tylko skanuje. Drugi test: czy są SBOM-y (Software Bill of Materials) dla aplikacji krytycznych.

**Kryteria oceny dojrzałości.** Poziom 3 wymaga: polityka, regularne skany (minimum miesięczne dla infrastruktury, ciągłe dla aplikacji webowych), SLA na patche (typowo 7 dni krytyczne, 30 dni wysokie, 90 dni średnie), roczne pentesty, security awareness w procesach rozwoju.

## Obszar 6: Polityki oceny skuteczności środków zarządzania ryzykiem (art. 21(2)(f))

**Co dyrektywa wymaga.** Sposób mierzenia, czy wdrożone środki bezpieczeństwa faktycznie działają. Metryki, KPI/KRI, regularny przegląd.

**Dokumenty do zebrania.** Lista metryk bezpieczeństwa (KPI/KRI), dashboards/raporty z metrykami, polityki przeglądów skuteczności, protokoły z przeglądów.

**Pytania do wywiadu.** Jakie macie top pięć metryk bezpieczeństwa, które monitorujecie regularnie? Pokaż mi dashboard za ostatni miesiąc. Co zrobiliście, gdy metryka odchyliła się od baseline?

**Testy do wykonania.** Audytor wybiera trzy metryki (np. liczba incydentów high severity, średni MTTR, % stacji z aktualnym patch level) i sprawdza: czy jest baseline, czy są regularne raporty, czy odchylenia powodują action items. Brak action items przy istniejących odchyleniach = poziom 2 niezależnie od jakości dashboardu.

**Kryteria oceny dojrzałości.** To jest obszar, w którym polskie firmy są zwykle najsłabsze — mają wdrożone kontrole, ale nie mierzą ich skuteczności. Większość jest na poziomie 1.

## Obszar 7: Cyberhigiena i szkolenia (art. 21(2)(g))

**Co dyrektywa wymaga.** Program szkoleń z cyberhigieny dla pracowników, regularnych ćwiczeń phishing, polityki podstawowe (hasła, MFA, urządzenia BYOD, czyste biurko), monitoring postaw.

**Dokumenty do zebrania.** Program szkoleń (zakres, częstotliwość, formaty), zapisy z ostatnich 24 miesięcy szkoleń (kto, kiedy, czy zaliczył test), raporty z phishing simulations, polityka cyberhigieny.

**Pytania do wywiadu.** Jaki procent pracowników przeszedł szkolenie w ostatnich 12 miesiącach? Jaki jest click-rate w ostatnich symulacjach phishing i czy spada w czasie? Jakie tematy są w szkoleniach poza phishing?

**Testy do wykonania.** Audytor przeprowadza krótki wywiad z 5–8 losowymi pracownikami operacyjnymi (nie z IT) z różnych działów. Pyta o trzy rzeczy: czy wiedzą do kogo zgłosić podejrzaną wiadomość, czy potrafią wymienić trzy zasady bezpiecznego hasła, czy wiedzą czym jest MFA. Odpowiedzi pokazują realny stan kultury, nie deklarowany.

**Kryteria oceny dojrzałości.** Poziom 3 wymaga: roczne szkolenie obowiązkowe dla wszystkich, kwartalne phishing simulations, dedykowane onboarding security training. Poziom 4 i wyżej: ciągły program, gamifikacja, mierzenie efektywności w czasie.

## Obszar 8: Polityki kryptografii (art. 21(2)(h))

**Co dyrektywa wymaga.** Polityka szyfrowania danych w spoczynku i w tranzycie, zarządzanie kluczami, polityka transport layer security, ograniczenia algorytmów słabych.

Pełna metodologia: [audyt kryptografii](audyt-kryptografii-nis2-rodo.html).

## Obszar 9: Bezpieczeństwo zasobów ludzkich, kontrola dostępu, zarządzanie aktywami (art. 21(2)(i))

**Co dyrektywa wymaga.** Procesy on-boardingu i off-boardingu z perspektywy bezpieczeństwa, zarządzanie tożsamością (IAM), kontrola dostępu, klasyfikacja aktywów, inwentarz zasobów (asset inventory).

**Dokumenty do zebrania.** Polityka IAM, procedura on/off-boardingu, inwentarz aktywów (sprzęt + oprogramowanie + dane), polityka klasyfikacji aktywów, raporty z przeglądów uprawnień (access reviews) z ostatnich 12 miesięcy.

**Pytania do wywiadu.** Jak długo trwa od momentu wypowiedzenia umowy do zablokowania kont byłego pracownika? Kto przeprowadza access review i jak często? Czy macie kompletny asset inventory — także laptopy domowe pracowników, urządzenia BYOD, instancje cloud?

**Testy do wykonania.** Audytor prosi o listę pracowników, którzy odeszli w ostatnich 30 dniach. Dla 3 wybranych sprawdza: czy konta zostały zablokowane (data, godzina), czy odebrany sprzęt, czy hasła do współdzielonych systemów zostały zmienione. Drugi test: prośba o listę kont uprzywilejowanych (administratorzy) i sprawdzenie, czy nie ma kont "zombie" (utworzone do projektów dawno zamkniętych).

## Obszar 10: Uwierzytelnianie wieloskładnikowe i kanały komunikacji (art. 21(2)(j))

**Co dyrektywa wymaga.** MFA dla dostępu do systemów krytycznych, bezpieczne kanały komunikacji wewnętrznej (szyfrowana poczta, komunikatory, video), zabezpieczone połączenia zdalne.

**Dokumenty do zebrania.** Polityka MFA, lista systemów z włączonym MFA, lista wyjątków (kto, dlaczego, do kiedy), polityka pracy zdalnej, polityka komunikatorów wewnętrznych.

**Pytania do wywiadu.** Jaki procent kont (ogółem i uprzywilejowanych) ma MFA? Jakie wyjątki istnieją i z jakimi uzasadnieniami? Czy MFA chroni także systemy starsze (legacy)?

**Testy do wykonania.** Audytor prosi o pokazanie konfiguracji MFA w trzech systemach: VPN, system finansowy, panel administracyjny chmury. Sprawdza realny stan: czy faktycznie wymagane, czy jest możliwość pominięcia, jakie metody (push, TOTP, SMS — SMS jest dziś poniżej standardu). Drugi test: czy MFA chroni także RDP/SSH dla administratorów.

Pełna metodologia: [audyt MFA i kontroli dostępu](audyt-mfa-i-kontroli-dostepu-nis2.html).

## Składanie wyników — macierz audytu i raport końcowy

Po przejściu wszystkich dziesięciu obszarów audytor składa macierz oceny: każdy obszar otrzymuje punkt 0–5, plus liczba ustaleń per klasyfikacja (krytyczne / wysokie / średnie / niskie). Macierz pokazuje obszar po obszarze, gdzie firma jest, gdzie powinna być (zwykle minimum 3 dla podmiotów kluczowych), jaka jest luka.

Format macierzy w raporcie:

| Obszar art. 21 | Aktualna dojrzałość | Cel | Luka | Ustalenia krytyczne/wysokie |
|---|---|---|---|---|
| (a) Polityka ryzyka | 2 | 3 | 1 | 0 / 2 |
| (b) Obsługa incydentów | 1 | 3 | 2 | 1 / 3 |
| (c) Ciągłość | 2 | 4 | 2 | 0 / 4 |
| (d) Łańcuch dostaw | 1 | 3 | 2 | 1 / 2 |
| (e) SDLC i podatności | 3 | 3 | 0 | 0 / 1 |
| (f) Ocena skuteczności | 1 | 3 | 2 | 0 / 2 |
| (g) Cyberhigiena | 2 | 3 | 1 | 0 / 1 |
| (h) Kryptografia | 3 | 4 | 1 | 0 / 1 |
| (i) IAM i aktywa | 2 | 3 | 1 | 1 / 2 |
| (j) MFA | 2 | 4 | 2 | 1 / 2 |

Macierz jest wizualizowana w raporcie jako heatmapa (czerwony / żółty / zielony) i prezentowana zarządowi. Każde ustalenie krytyczne i wysokie powinno mieć w raporcie: opis, dowody, ryzyko biznesowe, rekomendację korygującą, szacunkowy koszt i czas wdrożenia, odpowiedzialnego.

Jeśli przygotowujesz lub odbierasz pierwszy taki audyt i potrzebujesz template'u macierzy oraz formatu ustaleń — możesz dołączyć do newslettera skanujfirme.pl, w którym przesyłamy szablon raportu w XLSX/DOCX wraz z listą 30+ pytań kontrolnych do każdego obszaru. To nie jest substytut audytu, ale punkt startowy, który skraca pierwszą iterację o tygodnie.

## Trzy pytania kontrolne do zarządu przed zleceniem audytu

**Pierwsze.** Czy znamy obecną dojrzałość firmy w dziesięciu obszarach art. 21, choćby z grubsza? Jeśli nie — pierwszym krokiem powinien być self-audit (krótki, oparty na [checkliście 50 pytań](self-audit-firmy-checklist-50-pytan.html)), nie zewnętrzny audyt za 150 000 zł.

**Drugie.** Jaki jest nasz cel docelowy? Dla podmiotu kluczowego minimum to poziom 3 w każdym obszarze. Dla istotnego — poziom 2. Bez celu nie da się ocenić sukcesu audytu.

**Trzecie.** Kto jest beneficjentem raportu? Zarząd? Zarząd plus ubezpieczyciel cyber? Zarząd plus regulator (jeśli już są pytania z UODO lub CSIRT)? Cel adresata wpływa na format raportu, zakres dowodów, język.

## Esencja

Audyt NIS2 art. 21 nie jest checklistą. Jest procesem oceny dojrzałości w dziesięciu wymiarach, w którym audytor zbiera dowody (dokumenty, wywiady, testy techniczne), ocenia poziom dojrzałości w skali 0–5, identyfikuje luki względem stanu pożądanego i formułuje plan działań korygujących.

Pięć faz przekrojowych — planowanie, zebranie dowodów, ocena dojrzałości, analiza luki, raport — powtarza się dla każdego z dziesięciu obszarów. Czas pełnego audytu dla średniej firmy: 6–10 tygodni. Koszt: zwykle 80 000–250 000 zł zależnie od skali i zakresu.

Dziesięć obszarów art. 21 — od polityki zarządzania ryzykiem przez obsługę incydentów, ciągłość działania, łańcuch dostaw, SDLC, ocenę skuteczności, cyberhigienę, kryptografię, IAM, po MFA — wymaga różnych metod audytowych, różnych dowodów, różnej głębokości testów technicznych. Audytor nie patrzy tylko na dokumenty. Pyta operacyjnych pracowników. Robi tabletop exercises. Sprawdza realny patch level. Weryfikuje, czy backup faktycznie się przywraca. Bez tej warstwy testów technicznych audyt jest tylko teatrem zgodności.

Macierz dojrzałości jest narzędziem komunikacji z zarządem. Pokazuje aktualny stan, cel, lukę. Zarząd nie potrzebuje wszystkich detali — potrzebuje wiedzieć, gdzie firma jest najbardziej narażona i jakie są priorytety wydatków na bezpieczeństwo w nadchodzących 12–24 miesiącach.

NIS2 w 2026 roku nie jest już regulacją odległą. Polska transponowała dyrektywę z opóźnieniem, ale obowiązki są wiążące. Audyt jest dziś nie tylko narzędziem zgodności — jest narzędziem zarządzania ryzykiem, którego zarządy używają, aby świadomie decydować, gdzie inwestować w bezpieczeństwo, a gdzie tolerować ryzyko rezydualne. To różnica między firmą reaktywną a firmą zarządzaną dorosłej.

---

<ul>
<li>Dyrektywa Parlamentu Europejskiego i Rady (UE) 2022/2555 z dnia 14 grudnia 2022 r. w sprawie środków na rzecz wysokiego wspólnego poziomu cyberbezpieczeństwa na terytorium Unii (NIS2). https://eur-lex.europa.eu/eli/dir/2022/2555/oj</li>
<li>ENISA (2024). <em>NIS2 Technical Implementation Guidance for Cybersecurity Risk Management Measures</em>. European Union Agency for Cybersecurity. https://www.enisa.europa.eu/publications</li>
<li>ISO/IEC 27001:2022. <em>Information security, cybersecurity and privacy protection — Information security management systems — Requirements</em>. International Organization for Standardization.</li>
<li>ISO/IEC 27005:2022. <em>Information security, cybersecurity and privacy protection — Guidance on managing information security risks</em>. International Organization for Standardization.</li>
<li>NIST (2018). <em>Framework for Improving Critical Infrastructure Cybersecurity</em>, Version 1.1. National Institute of Standards and Technology. https://doi.org/10.6028/NIST.CSWP.04162018</li>
<li>NIST SP 800-53 Rev. 5 (2020). <em>Security and Privacy Controls for Information Systems and Organizations</em>. National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-53r5</li>
<li>NIST SP 800-30 Rev. 1 (2012). <em>Guide for Conducting Risk Assessments</em>. National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-30r1</li>
<li>NIST SP 800-61 Rev. 2 (2012). <em>Computer Security Incident Handling Guide</em>. National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-61r2</li>
<li>Ustawa z dnia 5 lipca 2018 r. o krajowym systemie cyberbezpieczeństwa (Dz.U. 2018 poz. 1560 ze zm.), wraz z projektem nowelizacji transponującej NIS2 (status: maj 2026).</li>
<li>CSIRT NASK / CERT Polska. <em>Krajobraz bezpieczeństwa polskiego internetu — raporty roczne 2022–2024</em>. https://www.cert.pl/publikacje/</li>
<li>Verizon (2024). <em>Data Breach Investigations Report (DBIR) 2024</em>. https://www.verizon.com/business/resources/reports/dbir/</li>
</ul>
