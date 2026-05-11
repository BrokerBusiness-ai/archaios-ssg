---
title: "Audyt kultury bezpieczeństwa — diagnoza zespołu"
slug: "audyt-kultury-bezpieczenstwa-diagnoza-zespolu"
excerpt: "Najtrudniejszy do oceny, najtrwalej wpływający na bezpieczeństwo wymiar audytu. Metodologia: ankiety, wywiady, testy, model Westruma. Konkretne narzędzia."
category_slug: "procesy"
tags: "kultura bezpieczeństwa, audyt zespołu, Westrum, NEAT, średni"
reading_time: 11
is_published: true
is_featured: false
meta_title: "Audyt kultury bezpieczeństwa — pełna metodologia (2026)"
meta_description: "Jak audytować kulturę bezpieczeństwa w zespole. Model Westruma, ankiety NEAT, testy phishingowe, wywiady. Konkretna metodologia dla średniej firmy."
funnel: "MOFU"
author_slug: "marek-porycki"
related_slugs: "kompletny-audyt-firmy-2026, diagnoza-dojrzalosci-procesow-it, audyt-rodo-krok-po-kroku"
product_slugs: ""
---

W badaniach Verizon DBIR 2024 wzór się powtarza: 68% naruszeń bezpieczeństwa zaczyna się od czynnika ludzkiego — phishingu, nieostrożnego użytkownika, naruszenia procedury, social engineeringu. Najlepsze technologie na świecie nie zatrzymają człowieka, który kliknie na link złośliwy. Z drugiej strony, zespół z silną kulturą bezpieczeństwa wykrywa próby ataków, ostrzega innych, raportuje anomalie — kompensuje braki technologiczne.

Kultura bezpieczeństwa jest najtrudniejszym wymiarem audytu firmy. Nie da się jej oszacować przez analizę dokumentów. Wymaga ankietowania, wywiadów, testów, obserwacji. Jest też wymiarem najtrwalej wpływającym na bezpieczeństwo — kultura zmienia się w latach, nie miesiącach. Ten tekst opisuje pełną metodologię audytu kultury bezpieczeństwa dla średniej polskiej firmy.

## Cztery wymiary kultury bezpieczeństwa

**Wymiar 1: świadomość.** Czy pracownicy rozumieją, dlaczego procedury bezpieczeństwa istnieją? Znają główne ryzyka? Widzą sens w wymaganiach, czy traktują jako biurokrację?

**Wymiar 2: postawy.** Czy zespół traktuje bezpieczeństwo jako wspólną odpowiedzialność, czy jako problem działu IT? Czy zgłaszają wątpliwości? Czy tworzą obejścia procedur (workarounds)?

**Wymiar 3: zachowania.** Konkretne praktyki: hasła (managery vs karteczki), pendrive (szyfrowane?), praca zdalna (firmowe vs prywatne urządzenia), reakcja na phishing (zgłaszają vs klikają), reakcja na nietypowe sytuacje (raportują vs ignorują).

**Wymiar 4: liderzy.** Czy zarząd modeluje pożądane zachowania? Czy CISO ma realny wpływ czy tylko formalne stanowisko? Czy szkolenia są priorytetem czy obowiązkiem do odhaczenia?

## Model Westruma — typologia kultur organizacyjnych

Ron Westrum (2004) wyróżnił trzy typy kultur organizacyjnych w kontekście przekazywania informacji o problemach:

**Patologiczna (power-oriented):** informacja blokowana, problemy ukrywane, posłańcy karani. "Nie pisz tego w mailu", "to nie wyszło z naszego działu", "nie będziemy się tym zajmować, dopóki nas nie złapią". Cyberbezpieczeństwo w takiej kulturze jest reaktywne, kosmetyczne.

**Biurokratyczna (rule-oriented):** informacja przepływa przez formalne kanały, problemy traktowane proceduralnie, posłańcy ignorowani. "Zgodnie z procedurą...", "nie jest to nasza odpowiedzialność", "musisz wypełnić formularz". Cyberbezpieczeństwo formalne, papierowe.

**Generatywna (performance-oriented):** informacja aktywnie poszukiwana, problemy traktowane jako okazje do uczenia, posłańcy szkoleni. "Co tu się stało?", "co możemy z tego nauczyć?", "jak temu zapobiec?". Cyberbezpieczeństwo proaktywne, integralne.

W typowej polskiej średniej firmie kultura jest mieszana — różne działy mają różne kultury. Dział IT często bardziej generatywny, dział sprzedaży bardziej biurokratyczny, dział produkcji bardziej patologiczny.

Audyt kultury bezpieczeństwa identyfikuje ten typ na poziomie organizacyjnym i działowym.

## Metoda 1: ankiety anonimowe

Najszerszy zasięg, najmniej głęboka analiza, ale niezbędne dla obrazu organizacyjnego.

**Konstrukcja ankiety:** 25–40 pytań pokrywających cztery wymiary. Każde pytanie ma skalę Likerta (1–5), niektóre pytania otwarte na komentarze.

**Przykładowe pytania:**

*Świadomość:*
- "Wiem, jakie są główne zagrożenia cyberbezpieczeństwa dla naszej firmy."
- "Rozumiem, dlaczego musimy używać MFA / haseł / szyfrowania."

*Postawy:*
- "Cyberbezpieczeństwo to wspólna odpowiedzialność wszystkich pracowników."
- "Czuję się komfortowo zgłaszając podejrzane maile lub aktywności."

*Zachowania:*
- "Używam managera haseł zamiast zapisywać je w plikach."
- "Wiem, jak zgłosić podejrzany email."

*Liderzy:*
- "Mój przełożony aktywnie wspiera praktyki cyberbezpieczeństwa."
- "Zarząd komunikuje znaczenie cyberbezpieczeństwa."

**Anonimowość:** absolutnie kluczowa. Pracownicy nie odpowiedzą szczerze, jeśli mają obawę, że wynik trafi do ich kierownika. Narzędzia: SurveyMonkey, Microsoft Forms (z anonymous), Google Forms (anonymous).

**Próg uczestnictwa:** minimum 50% pracowników, optymalnie 75%+. Niski udział wskazuje już na problem kulturowy (apatia, nieufność, brak czasu).

**Analiza:** średnie i mediany dla każdego pytania. Identyfikacja obszarów słabszych. Porównanie między działami. Kategoria pytań otwartych — analiza tekstowa, identyfikacja powtarzających się tematów.

Output: raport ankietowy z wynikami numerycznymi i analizą jakościową komentarzy.

## Metoda 2: testy phishingowe

Najskuteczniejszy test rzeczywistych zachowań w wymiarze 3 (zachowania).

**Procedura:** kontrolowana symulacja kampanii phishingowej. Wysłanie do wszystkich pracowników wiadomości udających legalny komunikat (np. fałszywa rachunki, fałszywa prośba HR, fałszywa wiadomość od dostawcy).

**Co mierzyć:**
- procent pracowników, którzy kliknęli na link;
- procent, którzy podali dane (login, hasło) na fałszywej stronie;
- procent, którzy zgłosili wiadomość do IT/security;
- czas między otrzymaniem a zgłoszeniem.

**Benchmark branżowy (Proofpoint, KnowBe4 raporty 2024):**
- typowy procent klikających: 15–25%;
- po podstawowym szkoleniu: 8–15%;
- po zaawansowanym programie: 3–8%;
- procent zgłaszających: typowo 8–20%;
- po programie świadomości: 30–50%.

**Narzędzia:** GoPhish (open-source), KnowBe4 (komercyjny), PhishMe.

**Etyczność:** test musi być wcześniej zapowiedziany ogólnie ("w najbliższych miesiącach przeprowadzimy test phishingowy"). Pracownicy, którzy klikną, powinni otrzymać szkolenie, nie karę. Cel — uczenie, nie publiczne kompromitowanie.

Output: raport z wynikami testu plus plan działań szkoleniowych.

## Metoda 3: wywiady z pracownikami

Najgłębsza analiza, ale ograniczony zasięg.

**Próbka:** 15–30 osób z różnych szczebli i działów. Wybór losowy z elementem stratyfikacji (zarząd, kierownicy, specjaliści, juniorzy, różne działy).

**Forma:** wywiad indywidualny, 45–60 minut. Anonimowość zapewniona przez audytora — wyniki agregowane, nie przypisane do osób.

**Pytania pogłębione:**
- "Opowiedz o sytuacji, gdy ktoś w firmie miał wątpliwość bezpieczeństwa. Co się stało?"
- "Jak zareagowałeś, gdy ostatnio dostałeś podejrzaną wiadomość?"
- "Co byłoby najtrudniejsze, gdybyś musiał zmienić swoją rutynę pracy ze względu na bezpieczeństwo?"
- "Jakie procedury bezpieczeństwa wydają Ci się sensowne, jakie nie?"
- "Czy masz wrażenie, że ktoś byłby ukarany za błąd cyberbezpieczeństwa, czy traktowano by to jako naukę?"
- "Czy zgłosiłbyś incydent, który sam spowodowałeś?" (kluczowe pytanie kulturowe)

**Analiza:** transkrypcje (lub szczegółowe notatki) → kodowanie tematyczne → identyfikacja powtarzających się wzorców.

Output: raport jakościowy ze wzorcami i cytatami (anonimowymi).

## Metoda 4: obserwacje w miejscu pracy

Audytor spędza czas w firmie obserwując rzeczywiste zachowania.

**Co obserwować:**
- jak pracownicy obsługują hasła (sticky notes, managery, łatwe hasła);
- czy ekrany są blokowane przy odejściu od stanowiska;
- jak obsługiwane są pliki na pendrivach i wymiennych nośnikach;
- jak komunikuje się o incydentach (otwarcie czy szeptem);
- jak reagują kierownicy w razie problemów (pomocnie czy karnie);
- czy używane są tymczasowe obejścia procedur.

Obserwacje wymagają delikatności — pracownicy świadomi obecności audytora zachowują się inaczej. Najlepsze: obecność audytora przez kilka dni, w kilku miejscach, w różnym czasie.

Output: raport obserwacji z konkretnymi przykładami zachowań.

## Metoda 5: analiza incydentów wewnętrznych

Każdy zarejestrowany incydent jest oknem na kulturę.

**Pytania analityczne:**
- Czy incydent był zgłoszony, gdy się pojawił, czy odkryty później?
- Kto zgłosił — sam zaangażowany pracownik czy ktoś inny?
- Jak długo trwało zgłoszenie od momentu zauważenia?
- Jak zarząd zareagował — wsparciem do uczenia czy presją kary?
- Co się zmieniło po incydencie — czy lessons learned wdrożone czy zignorowane?

Zdrowa kultura: szybkie zgłoszenia, otwarta komunikacja, konkretne wnioski wdrożone. Patologiczna kultura: incydenty ukrywane, odkrywane przypadkiem, posłańcy karani.

Output: analiza ostatnich 12–24 miesięcy incydentów jako wskaźnik kultury.

## Realny budżet audytu kultury

**Audyt kultury wewnętrzny (siłami własnymi):** 40 000–100 000 zł kosztów twardych (narzędzia ankietowe, testy phishingowe), plus 200–400 godzin czasu zespołu. Wymagania: kompetencja w prowadzeniu wywiadów, narzędzia analityczne.

**Audyt kultury zewnętrzny:** 60 000–180 000 zł zewnętrznych usług. Korzyści: niezależność, doświadczenie, brak konfliktu interesów.

**Audyt kultury hybrydowy:** 30 000–80 000 zł zewnętrznych usług + zespół wewnętrzny. Najczęściej optymalny.

Czas pełnego audytu kultury: 8–14 tygodni.

## Co najczęściej ujawniają audyty kultury

W 30+ audytach kultury polskich firm:

**Ustalenie 1:** rozdźwięk między oficjalną deklaracją a rzeczywistością. Zarząd deklaruje "cyber to nasza priorytet", pracownicy odbierają "cyber to przeszkoda do pracy". Klasyczne dla kultury biurokratycznej.

**Ustalenie 2:** jeden dział wybitnie różni się od reszty. Zwykle dział IT lub specjaliści cyber mają kulturę generatywną, reszta firmy biurokratyczną. Bezpieczeństwo zatrzymuje się na granicy IT.

**Ustalenie 3:** strach przed zgłoszeniem własnego błędu. 40–60% pracowników w wywiadach przyznaje, że nie zgłosiłoby incydentu, który sami spowodowali. Klasyczna patologia kultury.

**Ustalenie 4:** szkolenia jako biurokracja. Pracownicy odbywają e-learning, ale 80% nie pamięta treści po miesiącu. Forma: passive learning bez kontekstu.

**Ustalenie 5:** liderzy nie modelują zachowań. CEO używa prostego hasła, prosi sekretariat o "zalogowanie się za niego do bankowości", e-mail służbowy na prywatnym laptopie. Sygnał dla całej firmy.

## Strategie poprawy kultury

Kultura zmienia się w latach, nie tygodniach. Ale są dźwignie krótkoterminowe:

**Dźwignia 1: leadership behaviors.** Zarząd jako pierwszy przykład. Demonstrowanie używania managera haseł, MFA, regularnych szkoleń.

**Dźwignia 2: transformacja szkoleń.** Z e-learningu pasywnego na warsztatowy interaktywny. Z generycznych treści na konkretnie firmowe scenariusze.

**Dźwignia 3: nagradzanie zgłoszeń.** Każde zgłoszenie phishingu/anomalii — publiczne uznanie, czasem konkretna nagroda. Buduje normę "zgłaszanie jest dobre".

**Dźwignia 4: psychological safety.** Komunikacja "błędy są okazjami do uczenia". Brak punitive culture za uczciwe błędy. Zachowanie konsekwencji za zaniedbania świadome.

**Dźwignia 5: regularność.** Cyberbezpieczeństwo jako stały element komunikacji wewnętrznej (cotygodniowy biuletyn, miesięczne briefy zarządu, kwartalne aktualizacje).

**Dźwignia 6: champions cyber.** Wybór 5–15 osób w firmie (nie z IT) jako "champions cyber" — naturalni liderzy w swoich działach, którzy popularyzują dobre praktyki.

## Najczęstsze błędy w audytach kultury

**Błąd 1: pomijanie wymiaru kultury w audycie firmy.** Audyt techniczny + compliance, kultura ignorowana. Wynik: pełna mapa techniczna, brak rozumienia, dlaczego ludzie nie przestrzegają procedur.

**Błąd 2: ankieta jako jedyna metoda.** Ankieta daje skalowalność, ale nie głębi. Bez wywiadów — fragmentaryczny obraz.

**Błąd 3: brak anonimowości.** Pracownicy nie odpowiadają szczerze. Wynik bezwartościowy.

**Błąd 4: testy phishingowe jako narzędzie kary.** "Kto kliknął, ten ukarany" niszczy zaufanie. Lepiej: kto kliknął, ten szkolony.

**Błąd 5: jednokrotny audyt bez follow-upu.** Kultura zmienia się latami. Coroczne audyty z porównaniem trendów dają realny obraz rozwoju.

## Bibliografia

<ul>
<li>Westrum, R. (2004). <em>A typology of organisational cultures</em>. <em>Quality and Safety in Health Care</em>, 13(suppl 2), ii22–ii27. <a href="https://doi.org/10.1136/qshc.2003.009522">https://doi.org/10.1136/qshc.2003.009522</a></li>
<li>Schein, E. H. (2017). <em>Organizational Culture and Leadership</em> (5th ed.). Wiley. ISBN: 978-1119212041.</li>
<li>Edmondson, A. (2019). <em>The Fearless Organization: Creating Psychological Safety in the Workplace for Learning, Innovation, and Growth</em>. Wiley. ISBN: 978-1119477242.</li>
<li>Verizon. (2024). <em>2024 Data Breach Investigations Report</em>. Verizon Business. <a href="https://www.verizon.com/business/resources/reports/dbir/">https://www.verizon.com/business/resources/reports/dbir/</a></li>
<li>Proofpoint. (2024). <em>State of the Phish Report 2024</em>. Proofpoint. <a href="https://www.proofpoint.com/us/resources/threat-reports/state-of-phish">https://www.proofpoint.com/us/resources/threat-reports/state-of-phish</a></li>
<li>SANS Institute. (2024). <em>Security Awareness Report</em>. SANS. <a href="https://www.sans.org/security-awareness-training/resources/security-awareness-report">https://www.sans.org/security-awareness-training/resources/security-awareness-report</a></li>
<li>NIST. (2020). <em>SP 800-50 Rev. 1: Building an Information Technology Security Awareness Program</em>. National Institute of Standards and Technology. <a href="https://csrc.nist.gov/publications/detail/sp/800-50/rev-1/draft">https://csrc.nist.gov/publications/detail/sp/800-50/rev-1/draft</a></li>
</ul>

---

**Kultura bezpieczeństwa to wymiar najtrudniejszy do zmierzenia, ale najtrwalej wpływający.** W cotygodniowym newsletterze SkanujFirme.pl publikujemy szablony ankiet kulturowych, scenariusze wywiadów, programy zmiany kultury. [Zapisz się — bezpłatnie](#newsletter-signup).
