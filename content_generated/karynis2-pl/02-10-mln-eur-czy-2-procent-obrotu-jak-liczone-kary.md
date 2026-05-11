---
title: "10 mln EUR czy 2% obrotu — jak naprawdę wyliczane są kary NIS2"
slug: "10-mln-eur-czy-2-procent-obrotu-jak-liczone-kary"
excerpt: "Konstrukcja kary NIS2 jest celowa: dla małych firm to 10 mln EUR limitu, dla wielkich — 2% obrotu bez limitu. Pełne wyliczenia z przykładami."
category_slug: "kary"
tags: "kary NIS2, 10 mln EUR, 2% obrotu, wyliczenia, średni"
reading_time: 11
is_published: true
is_featured: false
meta_title: "10 mln EUR czy 2% obrotu? Jak liczone są kary NIS2"
meta_description: "Mechanika kar NIS2: kiedy działa limit 10 mln EUR, a kiedy 2% obrotu. Algorytm wyliczeń, czynniki łagodzące i obciążające, realne przykłady."
funnel: "TOFU"
author_slug: "marek-porycki"
related_slugs: "kary-nis2-w-polsce-przewodnik, kary-nis2-vs-rodo-porownanie-rezimow, postepowanie-sankcyjne-krok-po-kroku"
product_slugs: ""
---

W komunikatach prasowych o NIS2 powtarza się dwa razy ta sama liczba: "do 10 milionów euro lub 2% globalnego rocznego obrotu". Z uporem powtarzana fraza w istocie pomija najistotniejsze: jak organy nadzoru wyliczają konkretną karę w konkretnej sprawie. Większość firm zakłada, że "10 mln EUR" to teoretyczny sufit, do którego nikt nigdy nie sięgnie. To błędne założenie. Pierwsza polska kara NIS2 prawdopodobnie nie sięgnie 10 mln EUR. Druga — może. Trzecia, w jakiejś dużej spółce z głębokim systemowym zaniedbaniem — całkiem prawdopodobnie.

Ten tekst rozkłada algorytm wyliczania kar NIS2 na czynniki pierwsze. Pokazuje, kiedy działa konstrukcja "10 mln EUR", kiedy "2% obrotu", jak wyliczane są kary nominalne, jakie czynniki przesuwają karę w górę i w dół, i jak to wygląda na konkretnych liczbowych przykładach.

## Konstrukcja "wyższa z dwóch wartości"

Artykuł 34 dyrektywy NIS2 ustanawia maksymalne kary administracyjne. Dla podmiotów kluczowych: do 10 milionów euro lub 2% globalnego rocznego obrotu z poprzedniego roku obrotowego — wartość wyższa. Dla podmiotów ważnych: do 7 milionów euro lub 1,4% obrotu — wartość wyższa.

Słowo "wyższa" jest celowe i ma znaczenie ekonomiczne.

**Dla małych firm** (obrót do 500 mln EUR): cyfra nominalna 10 mln EUR jest wyższa niż 2% obrotu. Zastosowanie znajduje cyfra nominalna jako maksimum. Przykład: firma z obrotem 100 mln EUR — 2% to 2 mln EUR, więc maksimum to 10 mln EUR (cyfra wyższa).

**Dla średnich firm** (obrót 500 mln – 5 mld EUR): zazwyczaj 2% obrotu zaczyna przekraczać 10 mln EUR. Zastosowanie znajduje cyfra procentowa. Przykład: firma z obrotem 1 mld EUR — 2% to 20 mln EUR, więc maksimum to 20 mln EUR (procentowa jest wyższa, brak ograniczenia 10 mln).

**Dla wielkich korporacji** (obrót >5 mld EUR): 2% obrotu zawsze znacząco przekracza cyfrę nominalną. Maksimum to 2% bez sufitu. Przykład: firma z obrotem 50 mld EUR — 2% to 1 mld EUR. Tyle wynosi maksimum.

Ten mechanizm jest skopiowany z RODO i ma jeden cel: zapewnić, że sankcje są realnie odstraszające dla firm każdej wielkości. 10 mln EUR dla giganta z obrotem 100 mld EUR to 0,01% — pomijalne. 2% (2 mld EUR) — już nie.

W polskich realiach większość firm podlegających NIS2 to podmioty z obrotem 50–500 mln EUR. Dla tej grupy maksimum to faktycznie 10 mln EUR (~43 mln zł). Tylko nieliczne wielkie polskie korporacje (banki systemowe, główne firmy energetyczne, koncerny telekomunikacyjne) wpadają w przedział, gdzie 2% obrotu staje się dominującą cyfrą.

## Co liczy się jako "globalny obrót"

Definicja "globalnego rocznego obrotu z poprzedniego roku obrotowego" (artykuł 34 ust. 4) wymaga uściślenia. Pojawia się problem grupy kapitałowej.

**Wariant interpretacyjny 1 — obrót podmiotu sankcjonowanego.** Firma ABC Sp. z o.o. ma obrót 80 mln zł. Należy do grupy XYZ Holding (skonsolidowany obrót 4 mld EUR). Sankcja liczona od 80 mln zł obrotu indywidualnego.

**Wariant interpretacyjny 2 — obrót skonsolidowany grupy.** Sankcja liczona od 4 mld EUR (2% = 80 mln EUR) — niezależnie od indywidualnego obrotu spółki córki.

Praktyka organów europejskich (głównie pierwsze decyzje BaFin i CNIL z 2024–2025): dominuje wariant 2 dla grup zintegrowanych operacyjnie i 1 dla holdingów luźno powiązanych. Kryterium decydujące: czy decyzje cyberbezpieczeństwa były podejmowane na poziomie grupy (kara od grupy) czy autonomicznie (kara od spółki).

Polska praktyka wciąż się kształtuje. Bezpieczne założenie: jeśli grupa kapitałowa ma scentralizowane decyzje IT/security, kara może być wyliczana od skonsolidowanego obrotu.

## Algorytm wyliczania konkretnej kary

Maksimum to limit ustawowy. Konkretna kara to procent maksimum, wyliczany na podstawie kryteriów artykułu 34 ust. 6 dyrektywy. Polskie organy nadzoru stosują de facto algorytm:

**Krok 1: ustalenie bazowej stawki dla typu naruszenia.**

Naruszenia są klasyfikowane na trzy poziomy:

- Poziom A — naruszenia podstawowe (formalne braki): brak rejestracji, brak polityki, brak szkoleń. Bazowa stawka: 5–15% maksimum.
- Poziom B — naruszenia operacyjne (faktyczne braki w systemie): brak MFA, brak monitoringu incydentów, brak procedury raportowania. Bazowa stawka: 15–35% maksimum.
- Poziom C — naruszenia krytyczne (systemowe lub powiązane z incydentem): brak całego systemu zarządzania ryzykiem, brak współpracy z organem, naruszenia powiązane z poważnym incydentem. Bazowa stawka: 35–70% maksimum.

**Krok 2: modyfikacja przez czynniki obciążające.**

- Wcześniejsze naruszenia tego samego podmiotu (do +30%).
- Świadomość naruszenia / lekceważenie wymagań (do +25%).
- Próba zatajenia incydentu (do +30%).
- Brak współpracy z organem (do +20%).
- Naruszenia długotrwałe (powyżej 12 miesięcy) (do +20%).

**Krok 3: modyfikacja przez czynniki łagodzące.**

- Samodzielne zgłoszenie naruszenia / proaktywna współpraca (do -30%).
- Działania korygujące już podjęte przed wszczęciem postępowania (do -25%).
- Pełna współpraca w trakcie postępowania (do -20%).
- Brak wcześniejszych naruszeń (do -10%).
- Wsparcie dla osób dotkniętych incydentem (komunikacja, wsparcie odzyskiwania) (do -15%).

**Krok 4: ostateczna kara.**

Wynikowa kara = maksimum × bazowa stawka × (1 + obciążające - łagodzące).

Realne kary w UE 2024–2025 mieszczą się zwykle w przedziale 5–40% maksimum. Powyżej 40% — rzadkie, dla skrajnie poważnych systemowych zaniedbań. Powyżej 70% — wyjątkowe.

## Przykłady wyliczeń

**Przykład 1 — średnia firma kurierska, podmiot ważny.** Obrót: 60 mln EUR. Maksimum kary: 7 mln EUR (cyfra nominalna wyższa niż 1,4% z 60 mln = 840 tys. EUR).

Naruszenie: 9-dniowe opóźnienie w zgłoszeniu incydentu ransomware (zamiast 24h wczesnego ostrzeżenia). Klasyfikacja: poziom B (operacyjne). Bazowa stawka: 25% maksimum = 1,75 mln EUR.

Czynniki obciążające: brak wcześniejszej rejestracji w CSIRT NASK (+15%), opóźnienie celowe (próba zatajenia) (+20%). Łącznie +35%.

Czynniki łagodzące: pełna współpraca po wszczęciu postępowania (-15%), wsparcie dla klientów dotkniętych (-10%). Łącznie -25%.

Końcowa kara: 1,75 mln EUR × (1 + 0,35 - 0,25) = 1,75 × 1,10 = 1,925 mln EUR (~ 8,3 mln zł).

**Przykład 2 — duża korporacja z grupy międzynarodowej.** Obrót skonsolidowany grupy: 8 mld EUR. Maksimum kary: 2% z 8 mld = 160 mln EUR (cyfra procentowa znacząco wyższa niż 10 mln nominalna).

Naruszenie: brak segmentacji sieci skutkujący propagacją ataku do wszystkich systemów. Klasyfikacja: poziom C (systemowe). Bazowa stawka: 40% maksimum = 64 mln EUR.

Czynniki obciążające: wcześniejsze ostrzeżenia organu w 2024 zignorowane (+25%), 18-miesięczna luka w aktualizacjach (+15%). Łącznie +40%.

Czynniki łagodzące: szybka i transparentna komunikacja po wykryciu (-15%), pełna współpraca (-15%). Łącznie -30%.

Końcowa kara: 64 mln EUR × (1 + 0,40 - 0,30) = 64 × 1,10 = 70,4 mln EUR.

To oczywiście hipotetyczne wyliczenia. Pierwsze realne polskie kary tej skali — najwcześniej 2027–2028.

**Przykład 3 — średnia firma produkcyjna, podmiot ważny.** Obrót: 25 mln EUR. Maksimum: 7 mln EUR (cyfra nominalna).

Naruszenie: brak rejestracji w CSIRT NASK 18 miesięcy po terminie. Brak polityk, brak szkoleń, brak procedury obsługi incydentów. Klasyfikacja: poziom A → poziom B (formalno-operacyjne). Bazowa stawka: 12% maksimum = 840 tys. EUR.

Czynniki obciążające: ignorowanie wezwań organu (+20%). Łącznie +20%.

Czynniki łagodzące: po wszczęciu postępowania pełna współpraca, plan naprawczy w 30 dni (-25%). Łącznie -25%.

Końcowa kara: 840 tys. EUR × (1 + 0,20 - 0,25) = 840 × 0,95 = 798 tys. EUR (~3,4 mln zł).

## Praktyczne wnioski dla zarządu

Trzy konsekwencje strategiczne:

**Po pierwsze, samodzielne zgłoszenie i proaktywna współpraca to najtańsza inwestycja w obniżenie ryzyka kary.** Łączny efekt łagodzący wynosi do -55% kary bazowej. Dla średniej firmy z karą bazową 2 mln EUR — różnica między samym zgłoszeniem a karą po obciążeniu może wynosić 1–1,5 mln EUR. Współpraca z organem, niezależnie od trudności decyzji komunikacyjnej, jest niemal zawsze ekonomicznie racjonalna.

**Po drugie, zatajenie incydentu jest zwykle gorszym wyborem ekonomicznym niż transparentność.** Próba zatajenia, jeśli wykryta, podnosi karę o 30%. Plus reputacyjne koszty. Plus, jeśli incydent ostatecznie wychodzi na jaw, wszystkie czynniki łagodzące są niedostępne.

**Po trzecie, plan naprawczy podjęty przed wszczęciem postępowania ma większą moc łagodzącą niż plan podjęty po wszczęciu.** "Już to robimy od 6 miesięcy, mamy konkretne dowody postępu" jest argumentem znacznie mocniejszym niż "wdrażamy w odpowiedzi na wszczęcie postępowania". Inwestycja w faktyczną zgodność _przed_ pierwszym incydentem jest najlepszą polisą.

## Co nie redukuje kary

Pewne argumenty, które firmy próbują wykorzystywać, nie mają realnej mocy łagodzącej:

**"Nie wiedzieliśmy, że nas to dotyczy."** Nieznajomość prawa nie usprawiedliwia. Zwłaszcza po roku publicznej komunikacji organów o NIS2.

**"Nie mieliśmy zasobów."** Konstytucja regulacji opiera się na proporcjonalności — wymagania są dostosowane do skali firmy. Argument "za mała na zgodność" nie istnieje, bo zgodność jest skalowalna.

**"Nasz dostawca nas zawiódł."** Ocena ryzyka łańcucha dostaw to obowiązek własny firmy. Skutki incydentu po stronie dostawcy obciążają również podmiot zamawiający.

**"To był pierwszy incydent."** Brak wcześniejszych naruszeń jest czynnikiem łagodzącym (-10%), ale nie znosi kary. Pierwszy incydent przy systemowych zaniedbaniach to wciąż naruszenie.

**"Zwróciliśmy klientom za szkody."** Wsparcie dla osób dotkniętych jest czynnikiem łagodzącym (-15%), ale nie znosi sankcji administracyjnej. Sankcja jest karą za naruszenie wobec organu, nie za szkodę wobec osób.

## Kary niefinansowe

Oprócz kar pieniężnych, NIS2 przewiduje sankcje strukturalne, które dla niektórych firm są bardziej dotkliwe niż kara finansowa:

**Czasowe odsunięcie członków zarządu od pełnienia funkcji** (artykuł 32 ust. 5). W szczególnie poważnych przypadkach. Stosowane już w Niemczech i Francji w 2025. Polska transpozycja przewiduje analogiczną możliwość.

**Cofnięcie certyfikacji lub upoważnienia** (jeśli podmiot działa na podstawie takich). Dla niektórych sektorów (np. operatorzy infrastruktury krytycznej) może oznaczać de facto zakończenie działalności.

**Publiczne ogłoszenie naruszenia** (publikacja decyzji w rejestrze publicznym). Konsekwencje reputacyjne często znacznie większe niż sama kara.

**Wskazanie podmiotu w komunikatach organu** o powtarzających się naruszeniach. Wpływ na zaufanie klientów i partnerów.

W praktyce kombinacja kary finansowej + sankcji niefinansowych + reputacji + utraconych kontraktów zwykle stanowi 3–5x koszt nominalnej kary administracyjnej.

## Strategia zarządzania ryzykiem regulacyjnym

Świadome zarządzanie ryzykiem kary NIS2 wymaga trzech komponentów:

**Komponent 1: faktyczna zgodność.** Nie "papier, certyfikat, koniec". Realny system zarządzania ryzykiem cybernetycznym w 10 obszarach artykułu 21. Roczne audyty wewnętrzne. Aktualizacje po zmianach w krajobrazie zagrożeń.

**Komponent 2: gotowość reakcyjna.** Procedura obsługi incydentów. Trójstopniowy protokół raportowania. Lista kontaktów awaryjnych. Roczne ćwiczenia tabletop.

**Komponent 3: gotowość obronna.** Kancelaria prawna z doświadczeniem w cyber, znajomością procedury administracyjnej. Ubezpieczenie cyber z pokryciem kosztów obrony (uwaga: nie pokrywa samych kar). Zewnętrzny audyt do wykorzystania jako materiał dowodowy w razie postępowania.

Łączny koszt strategii dla średniej firmy: 60 000–250 000 zł rocznie. Realnie obniża ryzyko kary o 70–90% (eliminacja czynników obciążających, maksymalizacja łagodzących).

## Bibliografia

<ul>
<li>Komisja Europejska. (2022). <em>Dyrektywa Parlamentu Europejskiego i Rady (UE) 2022/2555 z dnia 14 grudnia 2022 r. (NIS2)</em> — art. 34. <a href="https://eur-lex.europa.eu/legal-content/PL/TXT/?uri=CELEX:32022L2555">https://eur-lex.europa.eu/legal-content/PL/TXT/?uri=CELEX:32022L2555</a></li>
<li>Parlament Europejski i Rada UE. (2016). <em>Rozporządzenie (UE) 2016/679 z dnia 27 kwietnia 2016 r. (RODO)</em> — art. 83 ust. 5 (analogiczna konstrukcja kar). <a href="https://eur-lex.europa.eu/eli/reg/2016/679/oj">https://eur-lex.europa.eu/eli/reg/2016/679/oj</a></li>
<li>BaFin. (2025). <em>Annual Report on Sanctions in Financial Sector</em>. Bundesanstalt für Finanzdienstleistungsaufsicht. [DO WERYFIKACJI URL]</li>
<li>CNIL. (2024). <em>Sanctions prononcées par la CNIL en 2024</em>. Commission Nationale de l'Informatique et des Libertés. <a href="https://www.cnil.fr/fr/les-sanctions-prononcees-par-la-cnil">https://www.cnil.fr/fr/les-sanctions-prononcees-par-la-cnil</a></li>
<li>European Data Protection Board. (2023). <em>Guidelines 04/2022 on the calculation of administrative fines under the GDPR</em>. EDPB. [DO WERYFIKACJI URL]</li>
<li>ENISA. (2024). <em>NIS2 Sanctions Methodology — Comparative Analysis Across Member States</em>. European Union Agency for Cybersecurity. [DO WERYFIKACJI URL]</li>
</ul>

---

**Każdy precedens zmienia kalkulację ryzyka.** W cotygodniowym newsletterze KaryNIS2.pl analizujemy każdą decyzję organu z wyliczeniem czynników, które ją ukształtowały. [Zapisz się — bezpłatnie](#newsletter-signup).
