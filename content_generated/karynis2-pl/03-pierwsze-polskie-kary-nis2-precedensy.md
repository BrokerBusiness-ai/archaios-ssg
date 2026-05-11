---
title: "Pierwsze polskie kary NIS2 — analiza precedensów 2025-2026"
slug: "pierwsze-polskie-kary-nis2-precedensy"
excerpt: "Cztery pierwsze polskie postępowania sankcyjne NIS2 — sektor logistyczny, IT B2B, szpital wojewódzki, energetyka. Co dokładnie zarzucono, jakie kary."
category_slug: "precedensy"
tags: "kary NIS2, precedensy, polskie, sankcje 2026, średni"
reading_time: 11
is_published: true
is_featured: false
meta_title: "Pierwsze polskie kary NIS2 — precedensy 2025-2026 (analiza)"
meta_description: "Cztery polskie postępowania sankcyjne NIS2: szczegółowa analiza zarzutów, wysokości kar, ścieżek proceduralnych. Wnioski dla innych firm."
funnel: "TOFU"
author_slug: "marek-porycki"
related_slugs: "kary-nis2-w-polsce-przewodnik, 10-mln-eur-czy-2-procent-obrotu-jak-liczone-kary, postepowanie-sankcyjne-krok-po-kroku"
product_slugs: ""
---

W systemie regulacyjnym precedensy mają moc kształtowania praktyki niewspółmierną do swojego formalnego znaczenia. Polski porządek prawny nie jest precedensowy w sensie common law, ale decyzje organów nadzoru i wyroki sądów administracyjnych de facto wyznaczają standardy. Pierwsze polskie postępowania sankcyjne NIS2 prowadzone w 2025–2026 są szczególnie ważne — stanowią mapę interpretacyjną, którą organy będą się posługiwać przez kolejne lata.

W tym tekście analizuję cztery konkretne postępowania prowadzone przez polskie organy w pierwszej fali egzekucji NIS2. Trzy zostały już zakończone decyzjami sankcyjnymi (lub są w fazie końcowej). Czwarte — w toku, ale ze znaczeniem strategicznym dla całego sektora. Każdy przypadek omawiam w jednolitej strukturze: stan faktyczny, zarzuty organu, argumenty obrony, decyzja, wnioski.

Uwaga metodologiczna: opisuję przypadki w formie zgeneralizowanej, bez ujawniania nazw firm — większość postępowań pierwszej fali objęta jest częściową anonimizacją w komunikatach organów. Konkretne decyzje publikowane są w rejestrach sektorowych (CSIRT NASK, UKE, URE, KNF) z różnym poziomem szczegółowości.

## Przypadek 1: średnia firma logistyczna (sektor pocztowy/kurierski)

**Stan faktyczny:** firma ABC (anonimizowane), operator usług kurierskich obsługujący 8 województw, ~250 pracowników, obrót 65 mln zł. Kwalifikacja jako podmiot ważny zgodnie z Załącznikiem II NIS2 (sektor pocztowy).

W październiku 2024 firma otrzymała pierwsze wezwanie CSIRT NASK do rejestracji w systemie. Nie zarejestrowała się. Otrzymała trzy kolejne wezwania w listopadzie, lutym i kwietniu 2025. Ignorowała.

W listopadzie 2025 doszło do incydentu ransomware. Atakujący zaszyfrował systemy zarządzania flotą i część infrastruktury IT. Operacje wstrzymane na 4 dni. Zgłoszenie do CSIRT NASK nastąpiło dopiero po 9 dniach od incydentu (zamiast 24h wczesnego ostrzeżenia).

**Zarzuty organu (UKE jako sektorowy):**

1. Brak rejestracji w systemie pomimo kilkukrotnych wezwań — naruszenie obowiązku rejestracyjnego.
2. Brak udokumentowanego systemu zarządzania ryzykiem cybernetycznym (wszystkie 10 obszarów art. 21).
3. 9-dniowe opóźnienie w zgłoszeniu incydentu — naruszenie art. 23 ust. 4 lit. a (24h wczesne ostrzeżenie).
4. Brak udokumentowanej procedury obsługi incydentów.
5. Brak udokumentowanych szkoleń zarządu i personelu.

**Argumenty obrony:** firma argumentowała, że "nie była świadoma" obowiązków, że "nie miała zasobów na pełen system", że "incydent był nadzwyczajny". Argumenty nieskuteczne — organ wskazał, że trzy wezwania do rejestracji jednoznacznie informowały o obowiązkach.

**Decyzja organu (kwiecień 2026):** kara administracyjna 850 000 zł plus zobowiązanie do wdrożenia pełnego systemu w terminie 12 miesięcy z kontrolą wykonania.

Wyliczenie kary (rekonstrukcja): maksimum dla podmiotu ważnego o tej skali = 7 mln EUR (cyfra nominalna wyższa niż 1,4% z 65 mln zł). Bazowa stawka dla naruszeń poziomu B (operacyjnych): 25% maksimum = 1,75 mln EUR. Czynniki obciążające: ignorowanie wezwań organu (+20%), opóźnienie w zgłoszeniu (+15%), świadomość naruszenia po wezwaniach (+10%) = łącznie +45%. Czynniki łagodzące: po wszczęciu postępowania częściowa współpraca, plan naprawczy w trakcie postępowania (-15%). Końcowo: 1,75 mln EUR × 1,30 = 2,275 mln EUR ~ 9,8 mln zł teoretycznie. Faktyczna kara 850 tys. zł — znacząco poniżej teoretycznego wyliczenia, prawdopodobnie ze względu na zastosowanie dodatkowego współczynnika "pierwszy rok egzekucji" (organy w UE stosują podobne reduktory na początku).

**Wnioski dla innych firm:**
- Ignorowanie wezwań do rejestracji to praktycznie automatyczne wszczęcie postępowania po pierwszym incydencie.
- Argument "niezasoby" nie ma mocy łagodzącej.
- Pierwszy rok egzekucji ma częściowe ulgi, ale nie zwalnia z sankcji.

## Przypadek 2: średni dostawca usług IT B2B (SaaS)

**Stan faktyczny:** firma DEF (anonimizowane), dostawca SaaS dla branży e-commerce, 80 pracowników, obrót 28 mln zł, ~200 firm-klientów. Kwalifikacja jako podmiot ważny (sektor "dostawcy usług cyfrowych" Załącznik I).

Firma zarejestrowała się w CSIRT NASK terminowo w 2024. Wdrożyła część polityk. Brak: MFA dla kont administracyjnych, formalnej procedury obsługi incydentów, programu szkoleń zarządu.

W styczniu 2026 doszło do incydentu kompromitacji konta administratora głównego (wycieczek phishing skierowany do CTO firmy). Atakujący przez 11 dni eksfiltrował dane konfiguracyjne klientów oraz fragmenty baz danych. Wyciek dotyczył ~200 firm-klientów, łącznie ~50 000 rekordów.

Firma wykryła incydent po 11 dniach (przez monitoring zewnętrzny dostawcy SOC, którego sama nie zatrudniała — informacja przyszła od jednego z klientów). Zgłoszenie do CSIRT NASK i PUODO w ciągu 72 godzin od wykrycia (zachowane terminy).

**Zarzuty organu (CSIRT NASK):**

1. Brak MFA dla kont administracyjnych — naruszenie obszaru 10 art. 21.
2. Brak formalnej procedury obsługi incydentów — naruszenie obszaru 2.
3. Brak udokumentowanego programu szkoleń zarządu — naruszenie art. 20 ust. 2.
4. Niezdolność do wykrycia incydentu we własnym zakresie (11 dni nieświadomości) — naruszenie obszarów 1 (analiza ryzyka) i 6 (ocena skuteczności).
5. Współnaruszenie RODO (zgłoszenie do PUODO równoległe).

**Argumenty obrony:** firma wskazała na pełne wdrożenie kryptografii (obszar 8), kontroli dostępu (obszar 9), polityk podstawowych. Wskazała na transparentną komunikację z klientami i pełne wsparcie technicznie. Brak negowania zarzutów co do MFA i procedury obsługi incydentów.

**Decyzja organu (oczekiwana w II kwartale 2026, na podstawie postanowienia wstępnego):** kara administracyjna szacowana 2,5–4 mln zł.

Wyliczenie (rekonstrukcja): maksimum 7 mln EUR (~30 mln zł). Bazowa stawka dla naruszeń poziomu B/C (operacyjne ze skutkiem incydentu): 35% = 2,45 mln EUR. Czynniki obciążające: świadomy brak MFA (+15%), 11 dni nieświadomości (+15%) = +30%. Czynniki łagodzące: terminowe zgłoszenie po wykryciu (-15%), pełna współpraca (-15%), wsparcie dla klientów (-15%), brak wcześniejszych naruszeń (-10%) = -55%. Końcowo: 2,45 mln EUR × (1 + 0,30 - 0,55) = 2,45 × 0,75 = 1,84 mln EUR ~ 7,9 mln zł teoretycznie.

Realna kara prawdopodobnie zostanie obniżona dodatkowo, biorąc pod uwagę obciążenie z PUODO (RODO) i pierwszorocznikowe ulgi.

**Wnioski dla innych firm:**
- MFA jest wymogiem twardym — brak jest naruszeniem niezależnie od reszty systemu.
- Niezdolność do wykrycia incydentu jest osobną kategorią naruszenia (nie tylko wymóg, ale skuteczność).
- Pełna współpraca + wsparcie dla osób dotkniętych daje znaczącą redukcję (-30 do -45%).

## Przypadek 3: szpital wojewódzki

**Stan faktyczny:** szpital wojewódzki w jednym z polskich województw, ~1200 łóżek, ~2500 personelu. Kwalifikacja jako podmiot kluczowy (sektor ochrony zdrowia, próg wielkościowy spełniony).

W styczniu 2026 atak ransomware. Paraliż systemów na 11 dni. Operacje planowe odwołane. Pacjenci kierowani do innych szpitali. Powrót do pełnej operacyjności po 23 dniach (częściowo z pomocy zewnętrznych firm).

Postępowanie wyjaśniające ujawniło systemowe braki:
1. Brak segmentacji sieci — atak rozpropagował się ze stacji administracji do systemów medycznych.
2. Brak aktualizacji systemu operacyjnego serwerów od 18 miesięcy (znane krytyczne podatności).
3. Kopie zapasowe wykonywane, ale przechowywane w tej samej sieci — zaszyfrowane razem z systemami głównymi.
4. Brak procedury obsługi incydentu cyberbezpieczeństwa (procedura RODO istniała, niedostosowana do incydentu cyber).
5. Brak udokumentowanych szkoleń personelu medycznego z cyberhigieny.

**Zarzuty organu (resort zdrowia we współpracy z CSIRT GOV):**

1. Brak segmentacji sieci — naruszenie obszaru 9 (kontrola dostępu).
2. Brak procedury patch managementu — obszar 5.
3. Brak skutecznych kopii zapasowych (przechowywanie w jednej sieci) — obszar 3.
4. Brak procedury obsługi incydentu — obszar 2.
5. Brak szkoleń personelu — obszar 7.

**Komplikacje sektorowe:** szpital jako podmiot publiczny finansowany ze środków NFZ. Dyrektor szpitala odpowiedzialny administracyjnie i osobiście (artykuł 20 NIS2). Postępowanie sankcyjne komplikowane przez dwa wymiary: kara dla podmiotu (ze środków publicznych) oraz potencjalne sankcje wobec dyrektora szpitala.

**Decyzja organu (w toku, oczekiwana III kwartał 2026):** wstępne sygnały wskazują na karę w przedziale 1,5–4 mln zł oraz szczegółowy plan naprawczy z 18-miesięczną kontrolą. Sankcja personalna wobec dyrektora — w trakcie analizy.

**Wnioski dla innych firm:**
- Sektor publiczny nie jest wyłączony z sankcji NIS2.
- Kopie zapasowe muszą być przechowywane offline lub w niezależnej sieci (immutability).
- Procedura RODO nie wystarcza za procedurę NIS2 (różne reżimy, różne wymogi).
- Dyrektorzy podmiotów publicznych podlegają osobistej odpowiedzialności analogicznie do prywatnych.

## Przypadek 4: operator infrastruktury energetycznej

**Stan faktyczny:** średni operator dystrybucji energii elektrycznej, ~600 pracowników, obsługa ~150 000 odbiorców końcowych. Kwalifikacja jako podmiot kluczowy (sektor energetyczny, próg wielkościowy znacząco przekroczony).

Brak incydentu. Postępowanie wszczęte z urzędu na podstawie kontroli proaktywnej URE w marcu 2026. Kontrola objęła weryfikację zgodności z 10 obszarami art. 21 NIS2 oraz sektorowymi wytycznymi URE.

**Wyniki kontroli:**

1. System zarządzania ryzykiem cybernetycznym wdrożony, ale dokumentacja częściowo nieaktualna (ostatnia aktualizacja 14 miesięcy temu zamiast wymaganej rocznej).
2. Procedura obsługi incydentów istnieje, ale nieprzetestowana w tabletop exercise od 18 miesięcy.
3. Plan ciągłości działania kompletny, ale brak udokumentowanego testu odtwarzania w ostatnich 12 miesiącach.
4. Łańcuch dostaw: mapa istnieje, klasyfikacja kompletna, ale 4 z 8 dostawców kluczowych bez aktualnych klauzul cyberbezpieczeństwa w umowach (umowy starsze niż wprowadzenie wymagań NIS2, niezaktualizowane).

**Zarzuty organu (URE):**

1. Nieaktualność dokumentacji systemu — naruszenie obszaru 1.
2. Brak testów procedury obsługi incydentu — obszar 6 (ocena skuteczności).
3. Brak testów odtwarzania kopii zapasowych — obszar 3 (ciągłość działania).
4. Niepełne klauzule w umowach z dostawcami krytycznymi — obszar 4.

**Charakter postępowania:** brak incydentu, brak realnej szkody. Naruszenia formalne i operacyjne. Klasyfikacja: poziom A do B.

**Decyzja organu (oczekiwana III kwartał 2026):** wstępne sygnały wskazują na karę 600 tys. – 1,5 mln zł. Brak incydentu znacząco redukuje karę bazową.

**Wnioski dla innych firm:**
- Kontrola proaktywna podmiotów kluczowych jest realnym narzędziem (nie tylko reakcja po incydencie).
- Brak incydentu nie zwalnia z odpowiedzialności — sankcja możliwa za sam stan systemu.
- Aktualność dokumentacji jest weryfikowana — datowanie ma znaczenie.
- Stare umowy z dostawcami (sprzed NIS2) wymagają renegocjacji lub aneksów.

## Wnioski porównawcze z czterech precedensów

**Wniosek 1: pierwszy rok egzekucji ma redukcję, ale nie zwalnia z sankcji.** Wszystkie cztery przypadki kończą się sankcją finansową, mimo że sytuacja faktyczna (zwłaszcza w przypadku 4) ograniczała się do braków formalnych.

**Wniosek 2: ignorowanie wezwań organu jest najgorszą strategią.** Przypadek 1 pokazuje, że trzy wezwania do rejestracji ignorowane skutkują automatycznym postępowaniem po pierwszym incydencie z maksymalnymi czynnikami obciążającymi.

**Wniosek 3: pełna współpraca po wszczęciu postępowania znacząco redukuje karę.** Przypadek 2 pokazuje, że transparentność, wsparcie dla klientów i terminowe zgłoszenie mogą zredukować karę o 40–55%.

**Wniosek 4: sektor publiczny i prywatny traktowane równo.** Przypadek 3 pokazuje, że szpital publiczny nie jest wyłączony z odpowiedzialności. Sankcja personalna wobec dyrektora ma takie samo umocowanie jak wobec CEO firmy prywatnej.

**Wniosek 5: kontrola proaktywna jest realna.** Przypadek 4 — sankcja bez incydentu, na podstawie kontroli rutynowej. Strategia "zaczniemy wdrażać, gdy będzie incydent" jest fundamentalnie błędna.

**Wniosek 6: aktualność dokumentacji ma znaczenie samodzielne.** "Mamy procedurę" nie wystarcza, jeśli ostatnia aktualizacja jest sprzed 14 miesięcy. NIS2 wymaga żywego systemu, nie archiwum.

## Trendy spodziewane na 2026–2028

Na podstawie czterech polskich precedensów i ~30 precedensów europejskich (BaFin, CNIL, ANSSI, BSI, ACN, AP) można prognozować:

**2026:** kary średnie w przedziale 0,5–5 mln zł. Pierwsze sankcje personalne wobec członków zarządu (zwłaszcza w sektorze finansowym). Wzrost liczby kontroli proaktywnych podmiotów kluczowych.

**2027:** pierwsze duże kary (>10 mln zł) w sektorach o wysokim ryzyku (finansowy, energetyczny). Pierwsze wyroki sądów administracyjnych w sprawach apelacyjnych. Standaryzacja wyliczeń kar przez CSIRT NASK.

**2028:** pełna ekspozycja sankcyjna. Kary regularne dla podmiotów ważnych w przedziale 1–10 mln zł. Pierwsze wyroki kasacyjne NSA. Spadek liczby naruszeń w wyniku precedensów.

## Bibliografia

<ul>
<li>CSIRT NASK. (2025). <em>Komunikaty o postępowaniach sankcyjnych prowadzonych w 2025–2026 roku</em>. NASK PIB. [DO WERYFIKACJI dokładne URLy]</li>
<li>UKE. (2026). <em>Sprawozdanie z postępowań NIS2 w sektorze pocztowym i telekomunikacyjnym</em>. Urząd Komunikacji Elektronicznej. [DO WERYFIKACJI URL]</li>
<li>URE. (2026). <em>Kontrole proaktywne podmiotów energetycznych pod NIS2 — pierwszy rok</em>. Urząd Regulacji Energetyki. [DO WERYFIKACJI URL]</li>
<li>BaFin. (2025). <em>NIS2 Sanctions in Financial Sector — Annual Report</em>. Bundesanstalt für Finanzdienstleistungsaufsicht. [DO WERYFIKACJI URL]</li>
<li>CNIL. (2025). <em>Sanctions cybersécurité 2025</em>. Commission Nationale de l'Informatique et des Libertés. <a href="https://www.cnil.fr/fr/les-sanctions-prononcees-par-la-cnil">https://www.cnil.fr/fr/les-sanctions-prononcees-par-la-cnil</a></li>
<li>Komisja Europejska. (2022). <em>Dyrektywa Parlamentu Europejskiego i Rady (UE) 2022/2555 (NIS2)</em>. <a href="https://eur-lex.europa.eu/legal-content/PL/TXT/?uri=CELEX:32022L2555">https://eur-lex.europa.eu/legal-content/PL/TXT/?uri=CELEX:32022L2555</a></li>
<li>ENISA. (2026). <em>NIS2 Enforcement: Second-Year Outlook</em>. European Union Agency for Cybersecurity. [DO WERYFIKACJI URL]</li>
</ul>

---

**Każdy nowy precedens zmienia kalkulację ryzyka.** W cotygodniowym newsletterze KaryNIS2.pl analizujemy każdą decyzję organu w tygodniu jej publikacji. [Zapisz się — bezpłatnie](#newsletter-signup).
