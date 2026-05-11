---
title: "NIS2 dla MŚP — uproszczone wymagania i realne koszty wdrożenia"
slug: "nis2-dla-msp-uproszczone-wymagania"
excerpt: "Małe i średnie firmy też podlegają NIS2 — ale w innym reżimie. Co dokładnie wymagane, ile kosztuje, jak zrobić to bez konsultantów za 200 tys. zł."
category_slug: "audyt-nis2"
tags: "NIS2, MŚP, małe firmy, średnie firmy, koszty, wdrożenie, początkujący"
reading_time: 11
is_published: true
is_featured: false
meta_title: "NIS2 dla MŚP — wymagania, koszty, jak zrobić bez konsultantów"
meta_description: "Czy mała firma musi wdrażać NIS2? Jakie są uproszczenia? Realny budżet 30-80 tys. zł i krok po kroku procedura dla SME."
funnel: "MOFU"
author_slug: "marek-porycki"
related_slugs: "kogo-obowiazuje-nis2-w-polsce, nis2-checklista-gotowosci-10-obszarow, raportowanie-incydentow-24-72h-protokol"
product_slugs: ""
---

Pierwsze wrażenie po przeczytaniu dyrektywy NIS2: to wymagania pisane pod korporacje. Dziesięć obszarów polityk, trójstopniowy protokół raportowania, ocena ryzyka łańcucha dostaw, certyfikacje, audyty zewnętrzne. Średnia firma produkcyjna z 80 pracownikami i 15 mln euro obrotu czyta to i widzi rok pracy zespołu compliance, którego nie ma, i konsultacje za 250 000 zł.

Rzeczywistość jest bardziej zniuansowana. NIS2 wprowadza zasadę proporcjonalności — wymagania mają być adekwatne do wielkości i ryzyka podmiotu. W praktyce oznacza to, że średniej firmy nie obowiązują te same standardy techniczne co wielkiej korporacji energetycznej. Ale "proporcjonalne" nie znaczy "lekkie". Znaczy: realnie wykonalne dla podmiotu o określonej skali, ale wciąż wymagające systematycznego podejścia.

Ten tekst jest dla zarządów MŚP, które już ustaliły, że ich firma podlega NIS2 jako podmiot ważny (procedura kwalifikacyjna w artykule [Kogo dokładnie obowiązuje NIS2 w Polsce](/kogo-obowiazuje-nis2-w-polsce)). Pokazuję, co dokładnie trzeba wdrożyć, ile to realnie kosztuje, i które elementy można zrobić siłami własnymi, a które wymagają wsparcia zewnętrznego.

## Zasada proporcjonalności — co naprawdę oznacza

Artykuł 21 ust. 1 dyrektywy NIS2 stanowi: "Państwa członkowskie zapewniają, by podmioty kluczowe i ważne wprowadziły odpowiednie i proporcjonalne środki techniczne, operacyjne i organizacyjne". Słowo "proporcjonalne" jest celowe. Oznacza, że organ nadzorczy oceniając compliance bierze pod uwagę: wielkość podmiotu, narażenie na ryzyko, stan techniki dostępny w sektorze, koszty wdrożenia w stosunku do prawdopodobieństwa i skutków incydentów.

W praktyce: 60-osobowa firma kurierska nie musi mieć Security Operations Center 24/7 z dziesięcioma analitykami. Wystarczy zorganizowany proces obsługi incydentów, dostępny zespół IT (własny lub zewnętrzny), zdefiniowane procedury eskalacji. Z drugiej strony — firma musi mieć podstawowe procedury wszystkich dziesięciu obszarów. Brak procedury kryptografii nie usprawiedliwia wielkością firmy. Procedura może być prosta — "wszystkie dane wrażliwe szyfrujemy AES-256 w tranzycie i w spoczynku, klucze przechowujemy w sejfie X" — ale musi istnieć, być udokumentowana i wdrożona.

Granica między "proporcjonalne" a "niewystarczające" jest tematem obecnych dyskusji w środowisku regulatorów. Pierwsze precedensy ukształtują się prawdopodobnie w 2026–2027 roku, po pierwszych kontrolach UKE i CSIRT NASK. Do tego czasu — bezpieczna strategia to wdrożenie wszystkich dziesięciu obszarów w wersji minimalnej, ale faktycznej.

## Dziesięć obszarów w wersji MŚP

Przejdziemy każdy z dziesięciu obszarów artykułu 21 i pokażemy minimum wystarczające dla typowej średniej firmy produkcyjnej, kurierskiej lub usługowej.

**1. Polityka analizy ryzyka i bezpieczeństwa systemów informatycznych.** Minimum: dokument 6–10 stron opisujący metodologię oceny ryzyka (ISO 31000 lub uproszczone matryce 5×5), inwentaryzacja zasobów IT (sprzęt, oprogramowanie, dane, użytkownicy), lista zidentyfikowanych ryzyk z oceną prawdopodobieństwa i wpływu, plan postępowania z najwyższymi ryzykami. Aktualizacja minimum raz w roku lub po istotnej zmianie. Czas wdrożenia siłami własnymi: 40–60 godzin pracy. Koszt jeśli z konsultantem: 8 000–15 000 zł.

**2. Obsługa incydentów.** Minimum: procedura zgłaszania incydentów wewnątrz firmy (kto, do kogo, jakim kanałem), klasyfikacja incydentów (krytyczny / wysoki / średni / niski), procedura eskalacji do CSIRT NASK z trójstopniowym protokołem 24h/72h/30 dni, rejestr incydentów. Czas: 20–30 godzin. Koszt z konsultantem: 5 000–10 000 zł.

**3. Ciągłość działania i zarządzanie kryzysowe.** Minimum: plan ciągłości działania (BCP) dla kluczowych systemów IT, procedura wykonywania kopii zapasowych z testowaniem odtwarzania (minimum kwartalnie), plan odzyskiwania po awarii (DRP), zasady zarządzania kryzysowego z wyznaczonym zespołem kryzysowym i schematem kontaktów. Czas: 30–50 godzin. Koszt z konsultantem: 10 000–20 000 zł. Tu często warto wsparcie — testy odzyskiwania robione przez kogoś z doświadczeniem ujawniają luki niewidoczne dla wewnętrznego zespołu.

**4. Bezpieczeństwo łańcucha dostaw.** Minimum: lista kluczowych dostawców usług IT (hosting, SaaS, outsourcing IT, dostawcy oprogramowania krytycznego), klauzule cyberbezpieczeństwa w umowach z nimi, ocena ryzyka dla każdego kluczowego dostawcy (kwestionariusz lub audyt), plan reakcji na incydent po stronie dostawcy. Czas: 20–40 godzin. Koszt z konsultantem: 8 000–15 000 zł. Najczęstszy błąd: pominięcie zewnętrznych firm IT, które utrzymują serwery, ERP czy CRM. To są dostawcy krytyczni — ich incydent jest Twoim incydentem.

**5. Bezpieczeństwo w pozyskiwaniu, rozwoju i utrzymaniu sieci i systemów informatycznych.** Minimum: procedura zarządzania zmianami w infrastrukturze IT, procedura aktualizacji oprogramowania (patch management) z czasem reakcji na krytyczne podatności (zalecane: 14 dni dla krytycznych, 30 dni dla wysokich), procedura zakupu nowego sprzętu i oprogramowania z oceną bezpieczeństwa. Czas: 25–40 godzin. Koszt z konsultantem: 7 000–12 000 zł.

**6. Polityki i procedury oceny skuteczności środków zarządzania ryzykiem.** Minimum: roczny audyt wewnętrzny systemu cyberbezpieczeństwa, regularne testy podatności (pen-test minimum raz w roku, skanowanie automatyczne kwartalnie), wskaźniki skuteczności (np. liczba incydentów, czas reakcji, procent personelu przeszkolonego). Czas: 15–25 godzin opracowanie + roczne nakłady na audyty (5 000–15 000 zł), pen-test (8 000–25 000 zł zewnętrznie).

**7. Podstawowe praktyki cyberhigieny i szkolenia.** Minimum: roczne szkolenie cyberhigieny dla całego personelu (phishing, hasła, USB, social engineering), specjalistyczne szkolenie dla zespołu IT, dedykowane szkolenie dla zarządu, dokumentacja przeprowadzonych szkoleń. Koszt: szkolenia online 50–200 zł na osobę, dla 80-osobowej firmy łącznie 5 000–15 000 zł rocznie. Szkolenia stacjonarne dla zarządu: 3 000–8 000 zł.

**8. Polityki i procedury kryptografii.** Minimum: identyfikacja danych wymagających szyfrowania (dane osobowe, finansowe, strategiczne), polityka szyfrowania w tranzycie (TLS 1.2+, VPN dla połączeń zdalnych), polityka szyfrowania w spoczynku (dyski, kopie zapasowe), zarządzanie kluczami szyfrującymi. Czas: 15–25 godzin. Koszt z konsultantem: 5 000–10 000 zł. Najczęściej już wdrożone na poziomie technicznym — wymaga formalizacji w dokumencie.

**9. Bezpieczeństwo zasobów ludzkich, polityki kontroli dostępu i zarządzania aktywami.** Minimum: procedura nadawania i odbierania dostępów (onboarding/offboarding), polityka haseł (długość, złożoność, MFA dla krytycznych systemów), regularny przegląd uprawnień (minimum kwartalnie), inwentarz sprzętu i licencji, procedura postępowania ze sprzętem przy odejściu pracownika. Czas: 20–35 godzin. Koszt z konsultantem: 6 000–12 000 zł.

**10. Korzystanie z uwierzytelniania wieloskładnikowego (MFA).** Wdrożenie MFA dla: dostępów administracyjnych, dostępów do systemów krytycznych (ERP, CRM, finanse, dane osobowe), dostępów zdalnych (VPN), poczty służbowej. Koszt: większość systemów ma wbudowane MFA bezpłatnie (Microsoft 365, Google Workspace). Dedykowane rozwiązanie (np. Duo, Okta, Yubico) — 30–80 zł na użytkownika miesięcznie.

## Realny budżet wdrożenia dla MŚP

Sumując powyższe dla typowej firmy z 60–100 pracownikami:

Wariant A — wdrożenie siłami własnymi (możliwe, gdy w firmie jest zespół IT z czasem na dodatkowe zadanie i znajomością procesów organizacyjnych): około 250–400 godzin pracy zespołu IT i compliance plus zewnętrzne usługi (pen-test, audyt zewnętrzny rozważalny). Koszt twardy: 30 000–60 000 zł rocznie. Czas wdrożenia: 4–8 miesięcy przy normalnym obciążeniu zespołu.

Wariant B — wdrożenie z wsparciem konsultanta (zalecane, gdy firma nigdy nie miała formalnego systemu cyberbezpieczeństwa): konsultant pomaga w opracowaniu polityk, audytuje stan obecny, prowadzi szkolenia. Koszt: 80 000–160 000 zł na pełne wdrożenie + 15 000–30 000 zł rocznie na utrzymanie. Czas: 3–5 miesięcy.

Wariant C — outsourcing pełny do firmy MSSP (Managed Security Service Provider): nadaje się dla firm, które nie chcą budować własnych kompetencji. Koszt: 60 000–150 000 zł rocznie w zależności od skali, ale zwykle bez kosztu wdrożeniowego. Niska elastyczność, uzależnienie od dostawcy. Pozostaje obowiązek zarządczy — nie można "kupić compliance"; zarząd nadal odpowiada osobiście.

Realistyczna rekomendacja dla większości MŚP: wariant hybrydowy. Konsultant na 2–3 miesiące pomaga zbudować dokumentację i procesy. Wewnętrzny pracownik (najczęściej IT lub administracja) przejmuje utrzymanie. Pen-test i audyt zewnętrzny — coroczne usługi zewnętrzne. Łączny pierwszy rok: 60 000–120 000 zł. Kolejne lata: 25 000–50 000 zł.

## Najczęstsze błędy MŚP przy wdrożeniu NIS2

**Błąd 1: wykorzystanie szablonów polityk pobranych z internetu bez adaptacji.** Konsekwencja: dokumenty bez powiązania z faktycznymi procesami firmy. Pierwsza kontrola odkrywa, że "polityka kontroli dostępu" mówi o procedurach, których nikt nie stosuje. Lepiej: prostszy dokument napisany od zera w oparciu o realny proces.

**Błąd 2: traktowanie wdrożenia jako jednorazowy projekt.** Compliance NIS2 to system zarządzania, nie projekt. Po zakończeniu wdrożenia trzeba utrzymywać: aktualizacje polityk po zmianach, regularne szkolenia, monitoring incydentów, coroczne audyty. Firmy, które po wdrożeniu "zamykają temat", po 18 miesiącach mają nieaktualne dokumenty i zerową świadomość organizacyjną.

**Błąd 3: zlecenie całości jednej firmie konsultingowej bez angażowania własnego zespołu.** Konsultant wychodzi z projektem, nikt w firmie nie rozumie wdrożonych procedur. Pierwsza kontrola lub incydent ujawnia, że w firmie nie ma osoby zdolnej operacyjnie obsłużyć system. Lepiej: konsultant z mentoringiem dla wewnętrznego pracownika, który przejmuje rolę po wdrożeniu.

**Błąd 4: pomijanie szkoleń zarządu.** Najtrudniejszy element politycznie. Zarządy często deklarują brak czasu na trzygodzinne szkolenie cyberbezpieczeństwa. Konsekwencja: w razie incydentu i kontroli, brak dokumentacji szkoleń zarządu jest bezpośrednim naruszeniem artykułu 20 ust. 2 dyrektywy. Indywidualna odpowiedzialność członka zarządu staje się realnym ryzykiem prawnym.

**Błąd 5: ignorowanie łańcucha dostaw.** Średnie firmy często mają 5–15 zewnętrznych dostawców IT (hosting, SaaS-y, firma utrzymująca ERP, dostawca poczty, dostawca CRM). Każdy z nich wymaga oceny ryzyka. Pominięcie tego obszaru to częsta luka — nie pojawia się ona w dokumentach wewnętrznych, ale dyrektywa wymaga dokładnie tego.

## Rola pracownika odpowiedzialnego za cyberbezpieczeństwo

NIS2 nie wymaga formalnego stanowiska CISO (Chief Information Security Officer) w MŚP. Wymaga jednak, żeby w firmie była osoba z jasno zdefiniowaną odpowiedzialnością za cyberbezpieczeństwo. W praktyce to często: osoba z działu IT (administrator, koordynator, kierownik IT) z dodatkową rolą "Cybersecurity Officer", osoba z compliance/RODO z rozszerzonymi kompetencjami, w mniejszych firmach — bezpośrednio dyrektor operacyjny lub członek zarządu odpowiedzialny za IT.

Kluczowe: ta osoba musi mieć formalne umocowanie (uchwała zarządu lub rozszerzony zakres obowiązków), realny czas (minimum 20% etatu w firmie 60-osobowej, więcej w większej), bezpośredni dostęp do zarządu (nie przez 3 poziomy hierarchii), budżet do dyspozycji (minimum 30 000 zł rocznie na narzędzia, audyty, szkolenia).

Bez tych warunków stanowisko jest fikcyjne. Pierwsza kontrola od razu to ujawnia.

## Quick wins — co można zrobić w pierwszych 30 dniach

Zanim ruszysz z systemowym wdrożeniem, są elementy, które dają natychmiastową poprawę bezpieczeństwa i są wymagane przez NIS2:

Włącz uwierzytelnianie wieloskładnikowe (MFA) dla wszystkich kont administratorów IT, kont z dostępem do systemów finansowych i HR, kont zarządu, dostępu zdalnego. Czas: 1–2 dni dla 60-osobowej firmy.

Zorganizuj szkolenie phishing dla całego zespołu. Nawet jednorazowe godzinne szkolenie online redukuje skuteczność typowych ataków o 50–70 procent (badania Verizon DBIR 2024). Koszt: 50–100 zł na osobę.

Wykonaj audyt aktywnych kont w głównych systemach (ERP, CRM, poczta, AD). W typowej firmie znajdziesz 10–25 procent kont nieaktywnych pracowników, którzy odeszli w ostatnich 12 miesiącach. Każde takie konto to ryzyko — nieużywane konto z nieobowiązującym hasłem to potencjalna brama wejścia.

Przetestuj odtworzenie kopii zapasowej. W 30–40 procent przypadków kopie zapasowe istnieją, ale nie zostały nigdy przetestowane. Test ujawnia: czy procedura odtworzenia działa, ile trwa, czy plik kopii nie jest uszkodzony, czy zespół wie jak to zrobić.

Przeprowadź podstawowy skan podatności infrastruktury (dostępne narzędzia open-source: OpenVAS, Nessus Essentials darmowy do 16 IP). Wynik dostarcza priorytetowej listy podatności do załatania.

Te pięć działań kosztuje łącznie 5 000–15 000 zł i zajmuje 2–3 tygodnie. Daje fundament, na którym buduje się resztę.

## Podsumowanie kosztów i timeline

Realistyczny scenariusz dla firmy 60–100-osobowej, średnio dojrzałej technologicznie, bez wcześniejszego systemu compliance:

Miesiące 1–2: quick wins (5 000–15 000 zł), wybór modelu wdrożenia (hybrydowy zalecany), kontraktowanie konsultanta jeśli wybrany.

Miesiące 3–5: opracowanie dokumentacji wszystkich 10 obszarów, wdrożenie procedur w organizacji, szkolenia personelu i zarządu, ocena dostawców (40 000–80 000 zł).

Miesiąc 6: pierwszy audyt wewnętrzny, korekta luk, formalna decyzja zarządu zatwierdzająca system, rejestracja w CSIRT NASK (15 000–30 000 zł).

Miesiące 7–12: stabilizacja, pierwszy pen-test zewnętrzny, audyt zewnętrzny rozważalny przed pierwszą kontrolą (15 000–35 000 zł).

Łącznie pierwszy rok: 75 000–160 000 zł. Drugi rok i kolejne: 25 000–50 000 zł na utrzymanie.

Szczegółowy plan działań w artykule [NIS2: kompletna checklista gotowości w 10 obszarach](/nis2-checklista-gotowosci-10-obszarow).

## Bibliografia

<ul>
<li>Komisja Europejska. (2022). <em>Dyrektywa Parlamentu Europejskiego i Rady (UE) 2022/2555 z dnia 14 grudnia 2022 r. (NIS2)</em> — art. 21 ust. 1 (zasada proporcjonalności). <a href="https://eur-lex.europa.eu/legal-content/PL/TXT/?uri=CELEX:32022L2555">https://eur-lex.europa.eu/legal-content/PL/TXT/?uri=CELEX:32022L2555</a></li>
<li>ENISA. (2024). <em>Cybersecurity for SMEs: Challenges and Recommendations</em>. European Union Agency for Cybersecurity. [DO WERYFIKACJI URL]</li>
<li>Verizon. (2024). <em>2024 Data Breach Investigations Report</em>. Verizon Business. <a href="https://www.verizon.com/business/resources/reports/dbir/">https://www.verizon.com/business/resources/reports/dbir/</a></li>
<li>ISO. (2018). <em>ISO 31000:2018 — Risk management — Guidelines</em>. International Organization for Standardization. <a href="https://www.iso.org/standard/65694.html">https://www.iso.org/standard/65694.html</a></li>
<li>NIST. (2020). <em>Special Publication 800-53 Rev. 5: Security and Privacy Controls</em>. National Institute of Standards and Technology. <a href="https://doi.org/10.6028/NIST.SP.800-53r5">https://doi.org/10.6028/NIST.SP.800-53r5</a></li>
<li>Polska Izba Informatyki i Telekomunikacji. (2024). <em>Raport: Stan cyberbezpieczeństwa polskich MŚP</em>. PIIT. [DO WERYFIKACJI dokładny tytuł i URL]</li>
</ul>

---

**Zaczynasz wdrożenie NIS2 i potrzebujesz konkretnych wzorców dokumentów?** W cotygodniowym newsletterze TestNIS2.pl publikujemy szablony polityk, procedur i checklist gotowych do adaptacji. Co tydzień jeden dokument do wykorzystania w Twojej firmie. [Zapisz się — bezpłatnie](#newsletter-signup).
