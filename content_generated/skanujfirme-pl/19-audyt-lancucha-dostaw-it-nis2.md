---
title: "Audyt łańcucha dostaw IT — NIS2 art. 21(2)(d), klauzule i due diligence"
slug: "audyt-lancucha-dostaw-it-nis2"
excerpt: "62% naruszeń przychodzi przez dostawców (Verizon DBIR 2024). Pełna metodyka audytu łańcucha dostaw IT — mapowanie, klasyfikacja, klauzule kontraktowe, monitoring."
category_slug: "audyt-nis2-skanuj"
tags: "łańcuch dostaw, supply chain, NIS2 art. 21, dostawcy IT, due diligence, średniozaawansowany"
reading_time: 12
is_published: true
is_featured: false
meta_title: "Audyt łańcucha dostaw IT — NIS2 art. 21(2)(d) (2026)"
meta_description: "Metodyka audytu supply chain. Mapowanie dostawców krytycznych, klauzule kontraktowe, due diligence, monitoring incydentów u dostawców. Standard 2026."
funnel: "MOFU"
author_slug: "marek-porycki"
related_slugs: "audyt-nis2-art-21-krok-po-kroku-metodologia-audytora,audyt-umow-powierzenia-art-28-rodo,audyt-transferow-do-krajow-trzecich-scc-tia,audyt-incydentow-24-72h-rodo-nis2,audyt-rodo-art-32-bezpieczenstwo-techniczne"
product_slugs: ""
---

Verizon Data Breach Investigations Report 2024 podaje liczbę, która powinna zmienić budżety bezpieczeństwa każdej średniej polskiej firmy: 62% naruszeń bezpieczeństwa rozpoczyna się od dostawcy. Atak na SolarWinds (2020) skompromitował 18 000 organizacji. Atak na Kaseya VSA (2021) zainfekował 1500 firm przez jednego dostawcę MSP. Atak na MOVEit (2023) — 2700 organizacji, w tym instytucje rządowe. To nie są incydenty marginalne — to dominująca kategoria zagrożeń 2024–2026.

NIS2 art. 21 ust. 2 lit. d wprost wymaga "bezpieczeństwa łańcucha dostaw, w tym aspektów bezpieczeństwa dotyczących stosunków między podmiotem a jego bezpośrednimi dostawcami lub usługodawcami". To nie jest opcjonalne. Dla każdego podmiotu kluczowego lub istotnego — audyt supply chain jest wymogiem regulacyjnym.

Ten tekst jest pełną metodyką audytu łańcucha dostaw IT. Obejmuje cztery obszary: mapowanie i klasyfikację dostawców, due diligence przy on-boardingu, klauzule kontraktowe, monitoring i reakcję na incydenty u dostawców. Adresat: audytorzy NIS2, CISO, dyrektorzy procurement, prawnicy odpowiedzialni za umowy z dostawcami IT.

## Obszar 1: Mapowanie i klasyfikacja dostawców

Najczęstsza luka audytowa: firma nie wie, ilu ma dostawców IT.

**Co audytor sprawdza.**
- Pełna lista dostawców IT (cloud, SaaS, hardware, software vendor, outsourcing, konsultanci, partnerzy integracyjni)
- Klasyfikacja per dostawca: krytyczny / istotny / standardowy
- Mapa "dostawca → systemy, do których ma dostęp / dane, które przetwarza"
- Aktualność listy (data ostatniej aktualizacji)

**Kryteria klasyfikacji.**

*Krytyczny:* dostawca, którego niedostępność lub kompromitacja zatrzyma działanie kluczowego procesu biznesowego (np. dostawca cloud hostujący ERP, dostawca CRM, dostawca systemu kadrowego, dostawca usług płatniczych).

*Istotny:* dostawca z dostępem do danych wrażliwych lub krytycznych systemów wtórnych (np. firma marketing automation z bazą leadów, biuro księgowe z danymi pracowników, agencja PR z planami strategicznymi).

*Standardowy:* dostawca pomocniczy bez dostępu do danych krytycznych (np. dostawca papieru, sprzętu biurowego, kawy).

**Częste obserwacje.**
- "Lista dostawców" pochodzi z działu zakupów i jest tylko dostawcami z formalnymi umowami. Wszystkie "shadow IT" SaaS kupione przez działy bez wiedzy IT nie są na liście.
- Klasyfikacja istnieje w polityce, ale nie jest stosowana. Wszyscy są "ważni".
- Brak aktualizacji od 2 lat. Połowa dostawców już nie współpracuje, ale wciąż widnieje na liście. Część nowych nie została dodana.

**Test:** audytor prosi o listę 5 losowo wybranych zakupów IT z ostatnich 12 miesięcy (z systemu księgowego). Sprawdza, czy dostawcy z tych zakupów są na "oficjalnej liście dostawców IT" w zarządzaniu compliance. Dziurawa lista = ustalenie.

## Obszar 2: Due diligence przy on-boardingu

Każdy nowy dostawca IT z dostępem do danych lub systemów krytycznych powinien przejść due diligence. Bez tego firma kupuje "kota w worku".

**Standardowy zakres due diligence:**

*Compliance.* Czy dostawca jest zgodny z RODO (UE/EOG), NIS2 (jeśli applicable), regulacjami sektorowymi? Pyta o IOD, polityki, raporty audytowe.

*Certyfikaty.* ISO 27001, SOC 2 Type II, ISO 22301 (BCM), ISO 27701 (privacy). Dostawca podaje certyfikaty + datę ważności. Audytor sprawdza realność (czy certyfikat jest aktualny, czy zakres obejmuje konkretną usługę).

*Bezpieczeństwo techniczne.* Jakie środki techniczne wdrożone (szyfrowanie, MFA, monitoring)? Czy są wyniki ostatnich pentestów?

*Lokalizacja danych.* Gdzie geograficznie są przechowywane dane? Czy są transfery do krajów trzecich? (Patrz: [audyt transferów do krajów trzecich](audyt-transferow-do-krajow-trzecich-scc-tia.html)).

*Sub-procesorzy.* Kto jeszcze ma dostęp do danych? Czy są umowy wiążące sub-procesorów odpowiednikami art. 28 RODO?

*Historia incydentów.* Czy dostawca miał incydenty bezpieczeństwa w ostatnich 3 latach? Jak je obsłużył?

*Stabilność finansowa.* Dla dostawców krytycznych — czy firma jest stabilna finansowo? Risk of going out of business mid-contract.

**Co audytor sprawdza.**
- Procedura due diligence (formalny dokument)
- Wypełnione kwestionariusze due diligence dla dostawców krytycznych z ostatnich 24 miesięcy
- Lista dostawców, którzy NIE przeszli due diligence — z uzasadnieniem (i planem)

**Typowe luki.**
- Due diligence istnieje "w teorii" — żaden dostawca nie przeszedł go w pełni.
- Kwestionariusze są wypełniane, ale nikt nie weryfikuje odpowiedzi (dostawca może deklarować cokolwiek).
- Brak procesu "gate" — dostawca zostaje podpisany bez ukończenia due diligence.

## Obszar 3: Klauzule kontraktowe

Umowa z dostawcą IT z dostępem do danych musi zawierać minimum następujące klauzule. Audytor weryfikuje każdą:

**Klauzula 1: Zgodność z RODO art. 28.** Pełna DPA (Data Processing Agreement). Patrz: [audyt umów powierzenia art. 28 RODO](audyt-umow-powierzenia-art-28-rodo.html).

**Klauzula 2: Obowiązek raportowania incydentów.** Dostawca zobowiązuje się raportować incydenty bezpieczeństwa w ciągu określonego czasu (typowo 24 godziny od wykrycia). Format raportu. Lista kontaktów.

**Klauzula 3: Prawo do audytu.** Administrator/zleceniodawca ma prawo audytować praktyki bezpieczeństwa dostawcy (lub zamówić audyt u trzeciej strony). Warunki (częstotliwość, koszty, zakres).

**Klauzula 4: Sub-procesorzy.** Lista aktualnych sub-procesorów, mechanizm zgody na nowych, prawo sprzeciwu.

**Klauzula 5: Bezpieczeństwo techniczne — minimum.** Wymóg konkretnych środków (szyfrowanie w spoczynku i tranzycie, MFA, regularne pentesty, polityka patch managementu).

**Klauzula 6: Continuity i SLA.** Service Level Agreement z konkretnymi RTO i RPO. Klauzula penalty za nieprzestrzeganie. Plan continuity dostawcy.

**Klauzula 7: Zwrot/destrukcja danych przy zakończeniu.** Procedura, terminy (typowo 30–60 dni), certyfikat zniszczenia.

**Klauzula 8: Lokalizacja geograficzna.** Wymóg konkretnych regionów (np. "dane przechowywane wyłącznie w EU-Central-1 lub EU-West-1"). Procedura zgody na zmianę lokalizacji.

**Klauzula 9: Ubezpieczenie cyber.** Dostawca posiada polisę cyber-insurance na minimum X mln zł. Procedura w przypadku roszczeń.

**Klauzula 10: Terminacja awaryjna.** Prawo do natychmiastowej terminacji bez kosztów w przypadku poważnego naruszenia bezpieczeństwa przez dostawcę.

**Co audytor sprawdza.**
- 3 umowy z dostawcami krytycznymi (losowo wybrane). Każda klauzula słowo po słowie.
- Aktualność umów (data ostatniego aneksu). Umowy starsze niż 3 lata zwykle nie mają nowoczesnych klauzul cyber.
- Spójność między DPA a umową główną.

**Częste luki.**
- Umowa standardowa dostawcy, niedostosowana do specyfiki klienta.
- Brak klauzuli raportowania incydentów (lub "dostawca zgłasza incydenty zgodnie ze swoimi standardami" — bez konkretu).
- Klauzula audytowa ograniczona do "udostępnienia certyfikatu ISO 27001" — to nie jest klauzula audytowa.
- SLA bez sankcji finansowych — pozbawia ją wartości operacyjnej.

## Obszar 4: Monitoring i reakcja na incydenty u dostawców

Audyt nie kończy się na on-boardingu. Dostawca, który był OK 2 lata temu, może mieć dziś poważne luki.

**Co audytor sprawdza.**
- Procedura ciągłego monitoringu dostawców krytycznych
- Lista źródeł monitoringu (raporty SOC 2 Type II coroczne, BitSight/SecurityScorecard ratings, monitoring threat intelligence pod kątem incydentów u dostawców)
- Procedura reakcji na incydent u dostawcy
- Historia takich incydentów w ostatnich 24 miesiącach

**Standardy 2026.**
- Dostawcy krytyczni — przegląd minimum raz na pół roku (renewal due diligence).
- Monitoring ratings (BitSight, SecurityScorecard) ciągły lub kwartalny.
- Subskrypcja threat intelligence z alertami o incydentach u dostawców.
- Procedura "isolation in case of compromise" — gdy dostawca jest ofiarą ataku, jak szybko firma odłącza dostawcę od systemów.

**Test:** "Załóżmy, że w przyszłym tygodniu Kaseya VSA (lub equivalent waszego MSP) ma incident podobny do 2021 r. Pokażcie mi procedurę reakcji. Kto powiadamia, kto decyduje o izolacji, ile to potrwa?"

## Obszar 5: Mapa supply chain — output audytu

Wynikiem audytu jest mapa łańcucha dostaw IT z minimum następującymi kolumnami:

| Dostawca | Klasyfikacja | Kategoria danych | Lokalizacja | DPA | Cert. | Pentest | Ostatni review | Ryzyko |
|---|---|---|---|---|---|---|---|---|
| AWS (EU-Central-1) | krytyczny | klienci, transakcje | UE + USA | TAK | ISO 27001, SOC 2 | brak (cloud provider) | 2025-08 | niskie |
| HubSpot | istotny | leady, behawior | USA (DPF) | TAK | SOC 2 Type II | TAK (publikuje) | 2025-11 | średnie |
| Local MSP (helpdesk) | krytyczny | dostęp do laptopów | PL | TAK | brak | brak | 2024-03 (stara) | wysokie — luka |
| Biuro księgowe | istotny | dane HR + finansowe | PL | TAK (stara, 2022) | brak | brak | nigdy | wysokie — luka |
| ChatGPT Enterprise | krytyczny (nowy) | dane operacyjne | USA (DPF) | TAK | SOC 2 | TAK | 2025-09 | średnie |
| Print provider | standardowy | drukowanie | PL | brak (nie potrzeba) | brak | brak | n/a | niskie |

Mapa pokazuje natychmiast luki: dostawcy bez aktualnego review, dostawcy bez certyfikatów istotnych dla klasyfikacji, dostawcy z DPA przestarzałymi.

Jeśli przygotowujesz lub odbierasz audyt łańcucha dostaw i potrzebujesz szablonu mapy supply chain w XLSX wraz z metodyką klasyfikacji i kwestionariuszem due diligence — przesyłamy ten pakiet w newsletterze skanujfirme.pl. Bez szablonu pierwsza iteracja zwykle zajmuje 4–6 tygodni; z szablonem — 1–2 tygodnie.

## Format ustalenia

> **Ustalenie SC-02 (klasyfikacja: wysokie):** Biuro księgowe "X" obsługuje pełen system kadrowo-płacowy z dostępem do danych osobowych 145 pracowników (w tym danych szczególnie wrażliwych — orzeczenia, zaświadczenia medyczne). Umowa z dostawcą jest z 2022 r., DPA z poprzedniej wersji RODO, brak klauzul cyber-bezpieczeństwa, brak certyfikatów ISO 27001/SOC 2, brak pentestów. Brak procesu renewal due diligence.
>
> **Dowody:** (1) Umowa z dostawcą z 2022 r.; (2) Brak dokumentów due diligence; (3) Wywiad z dyrektorem HR.
>
> **Ryzyko prawne i operacyjne:** Naruszenie NIS2 art. 21(2)(d) i RODO art. 28(1). Konsekwencje: w przypadku naruszenia u dostawcy, firma odpowiada za niewłaściwy wybór procesora. Kara administracyjna UODO do 4% obrotu. Ekspozycja danych 145 pracowników.
>
> **Rekomendacja korygująca:** (1) Renewal due diligence biura księgowego w 30 dni; (2) Renegocjacja umowy z aktualnym DPA i klauzulami cyber; (3) Decyzja: czy dostawca pozostaje, czy zmiana. Termin: 90 dni. Odpowiedzialny: dyrektor HR + IOD + dyrektor prawny.

## Trzy pytania kontrolne dla zarządu

**Pierwsze.** Ilu mamy dostawców IT krytycznych i kiedy ostatnio każdy przeszedł renewal due diligence? Konkretne liczby, nie "kilkudziesięciu, dawno".

**Drugie.** Co się stanie, gdy nasz dostawca cloud ma 48-godzinny outage globalny? Czy mamy plan continuity bez tego dostawcy?

**Trzecie.** Czy wiemy, którzy z naszych dostawców mają obowiązek raportowania pod NIS2 i czy zaczęli się do tego przygotowywać? (NIS2 dotyczy także średnich dostawców usług cyfrowych.)

## Esencja

Audyt łańcucha dostaw IT jest dziś najszybciej rosnącą kategorią ustaleń. 62% naruszeń bezpieczeństwa zaczyna się od dostawcy. NIS2 art. 21(2)(d) wymaga formalnej polityki supply chain dla każdego podmiotu kluczowego lub istotnego.

Mapowanie i klasyfikacja dostawców to fundament. Pełna lista wymaga współpracy zakupów, IT, HR, marketingu, finansów — bo "shadow IT" jest powszechne. Klasyfikacja (krytyczny / istotny / standardowy) musi być stosowana, nie tylko zapisana.

Due diligence przy on-boardingu jest gate'em — bez ukończonego DD nowy dostawca z dostępem do danych nie powinien zostać podpisany. Compliance, certyfikaty, bezpieczeństwo techniczne, lokalizacja danych, sub-procesorzy, historia incydentów, stabilność finansowa — sześć podstawowych obszarów weryfikacji.

Klauzule kontraktowe to 10 elementów: DPA, raportowanie incydentów, prawo do audytu, sub-procesorzy, środki techniczne minimum, SLA z penalty, zwrot danych, lokalizacja, ubezpieczenie cyber, terminacja awaryjna. Pominięcie któregokolwiek = ekspozycja.

Monitoring ciągły to standard 2026. Dostawca, który był OK 2 lata temu, może dziś mieć poważne luki. Renewal due diligence co 6 miesięcy dla krytycznych, ratings ciągłe (BitSight, SecurityScorecard), threat intelligence z alertami.

Mapa łańcucha dostaw — z klasyfikacją, lokalizacją, statusem DPA, datami review, oceną ryzyka — jest jedynym narzędziem zarządczym pozwalającym świadomie podejmować decyzje. Bez mapy zarząd nie wie, na ile firma jest narażona.

W 2026 r. atak na dostawcę (third-party breach) jest bardziej prawdopodobny niż atak bezpośredni. Inwestycja w audyt i zarządzanie supply chain ma wyższy ROI niż większość innych inwestycji w cybersecurity dla średniej polskiej firmy.

---

<ul>
<li>Dyrektywa Parlamentu Europejskiego i Rady (UE) 2022/2555 (NIS2), art. 21 ust. 2 lit. (d). https://eur-lex.europa.eu/eli/dir/2022/2555/oj</li>
<li>Rozporządzenie Parlamentu Europejskiego i Rady (UE) 2016/679 (RODO), art. 28. https://eur-lex.europa.eu/eli/reg/2016/679/oj</li>
<li>NIST SP 800-161 Rev. 1 (2022). <em>Cybersecurity Supply Chain Risk Management Practices for Systems and Organizations</em>. https://doi.org/10.6028/NIST.SP.800-161r1</li>
<li>NIST SP 800-53 Rev. 5 (2020). <em>Security and Privacy Controls — SR family (Supply Chain Risk Management)</em>. https://doi.org/10.6028/NIST.SP.800-53r5</li>
<li>ENISA (2023). <em>Good Practices for Supply Chain Cybersecurity</em>. https://www.enisa.europa.eu/publications/good-practices-for-supply-chain-cybersecurity</li>
<li>ENISA (2022). <em>Threat Landscape for Supply Chain Attacks</em>. https://www.enisa.europa.eu/publications/threat-landscape-for-supply-chain-attacks</li>
<li>Verizon (2024). <em>Data Breach Investigations Report 2024 — Third-Party chapter</em>. https://www.verizon.com/business/resources/reports/dbir/</li>
<li>ISO/IEC 27036 series. <em>Information security for supplier relationships</em>.</li>
<li>SANS (2024). <em>Supply Chain Compromise Guidance</em>. https://www.sans.org/</li>
<li>CISA (2024). <em>Software Bill of Materials (SBOM) Guidelines</em>. https://www.cisa.gov/sbom</li>
</ul>
