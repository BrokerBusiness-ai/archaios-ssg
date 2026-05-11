---
title: "Audyt umów powierzenia (art. 28 RODO) — częste błędy, jak weryfikować"
slug: "audyt-umow-powierzenia-art-28-rodo"
excerpt: "Umowy powierzenia (DPA) art. 28 RODO są najczęstszym źródłem niezgodności w audycie. Pełna metodyka weryfikacji: co audytor szuka, jakie pułapki, jak prawidłowo skonstruować."
category_slug: "rodo"
tags: "RODO, art. 28, umowa powierzenia, DPA, procesor, audyt, średniozaawansowany"
reading_time: 12
is_published: true
is_featured: false
meta_title: "Audyt umów powierzenia art. 28 RODO — częste błędy (2026)"
meta_description: "Metodyka audytu umów powierzenia danych. Co audytor sprawdza, jakie luki spotyka, jak konstruować DPA odporne na kontrolę UODO."
funnel: "MOFU"
author_slug: "marek-porycki"
related_slugs: "audyt-rodo-art-32-bezpieczenstwo-techniczne,audyt-rodo-krok-po-kroku,dpia-w-praktyce-kiedy-obowiazuje-jak-wykonac,audyt-transferow-do-krajow-trzecich-scc-tia,audyt-lancucha-dostaw-it-nis2"
product_slugs: ""
---

W każdym audycie RODO, który prowadziłem lub w którym uczestniczyłem, umowy powierzenia okazały się najsłabszym ogniwem. Statystyka jest brutalna: w średniej polskiej firmie 30–60% umów z procesorami danych albo nie istnieje (mimo realnego powierzenia), albo istnieje w wersji oderwanej od stanu faktycznego, albo zawiera klauzule sprzeczne z art. 28 RODO. To największy obszar systemowego ryzyka prawnego, jaki spotyka się w audytach.

Powodów jest kilka. Po pierwsze, art. 28 ma długą listę elementów obligatoryjnych (osiem podstawowych wymogów) i każde z nich jest pułapką. Po drugie, firmy podpisują DPA przygotowane przez procesorów (typowo dostawców cloud, SaaS, narzędzi marketingowych), nie negocjując i nie weryfikując zgodności. Po trzecie, lista procesorów dynamicznie rośnie (każda nowa subskrypcja SaaS to potencjalny nowy procesor), a procesy on-boardingu rzadko obejmują weryfikację DPA.

Ten tekst jest pełną metodyką audytu umów powierzenia. Strukturuje się wokół ośmiu obligatoryjnych elementów z art. 28 ust. 3, dla każdego podaje, co audytor szuka, jakie typowe błędy spotyka i jak konstruować klauzulę odporną na ustalenia kontroli. Adresat: IOD/DPO, działy prawne odpowiadające za umowy z dostawcami, dyrektorzy compliance, audytorzy RODO.

## Kiedy umowa powierzenia jest wymagana

Art. 28 ust. 1 RODO: "Jeżeli przetwarzanie ma być dokonywane w imieniu administratora, korzysta on wyłącznie z usług takich podmiotów przetwarzających, które zapewniają wystarczające gwarancje wdrożenia odpowiednich środków technicznych i organizacyjnych".

Art. 28 ust. 3: "Przetwarzanie przez podmiot przetwarzający odbywa się na podstawie umowy lub innego instrumentu prawnego".

Granica między procesorem (wymaga DPA) a samodzielnym administratorem (DPA nie wymagane) bywa cienka. Procesor:
- przetwarza dane w celach administratora, na jego polecenie
- nie decyduje samodzielnie o celach przetwarzania
- nie używa danych do własnych celów

Współadministrator (art. 26) lub samodzielny administrator:
- decyduje (lub współdecyduje) o celach
- używa danych również do własnych celów
- ma własną odpowiedzialność wobec podmiotów danych

Typowe przykłady procesorów: dostawcy hosting/cloud (AWS, Azure, OVH), narzędzia CRM (HubSpot, Pipedrive), narzędzia marketingowe (Mailchimp, Brevo, GetResponse), narzędzia HR (Asseco, Comarch ERP w SaaS), płatności (PayU, Tpay), biura księgowe, biura rachunkowe, firmy windykacyjne, firmy outsourcingu IT.

Typowe przykłady NIE-procesorów (czyli samodzielni administratorzy, bez DPA): banki (mają własną podstawę prawną przetwarzania), urzędy państwowe (działają na podstawie ustawy), agencje pracy tymczasowej w pewnych konfiguracjach, dostawcy poczty tradycyjnej w zakresie samego dostarczania (ale nie analizy).

Pierwszą ofiarą audytu jest mapa procesorów. Jeśli firma nie ma kompletnej listy aktualnych procesorów (z datą weryfikacji), audyt zaczyna się od jej tworzenia — co potrafi zająć 2–3 tygodnie pracy.

## Osiem obligatoryjnych elementów art. 28 ust. 3

Każda umowa powierzenia musi zawierać osiem konkretnych elementów. Audytor weryfikuje każdy.

### Element 1: Przedmiot i czas trwania przetwarzania

**Co art. 28 wymaga.** Określenie, co dokładnie procesor przetwarza i przez jaki okres.

**Co audytor szuka.** Konkretne wskazanie celu (nie ogólne "obsługa klienta"), zakresu, długości umowy, sposób przedłużenia, sposób zakończenia.

**Częste błędy.**
- Generyczna fraza "świadczenie usług" bez konkretu — nieaudytowalne.
- Brak terminu — umowa "na czas nieokreślony" jest dopuszczalna, ale powinna mieć mechanizm zakończenia i przegląd.
- Brak ścisłego powiązania z umową głównej usługi (zwykle DPA jest aneksem do umowy SaaS lub umowy konsultingowej).

**Klauzula odporna.** "Procesor przetwarza dane osobowe w imieniu Administratora wyłącznie w celu realizacji Umowy [referencja do umowy głównej] przez okres jej obowiązywania. Po zakończeniu Umowy Procesor jest zobowiązany do zwrotu lub zniszczenia danych zgodnie z punktem [referencja do punktu o zwrocie]."

### Element 2: Charakter i cel przetwarzania

**Co art. 28 wymaga.** Wskazanie, jakie operacje (zbieranie, przechowywanie, modyfikacja, ujawnianie, usuwanie) procesor wykonuje i w jakim celu.

**Co audytor szuka.** Lista konkretnych operacji, lista konkretnych celów. Idealnie tabela: cel → operacje → kategorie danych → kategorie podmiotów.

**Częste błędy.**
- "Wszelkie operacje niezbędne do świadczenia usługi" — za szerokie, audytor odrzuca.
- Brak rozróżnienia celów (np. obsługa zamówienia, marketing, profilowanie).

### Element 3: Rodzaj danych osobowych i kategorie podmiotów

**Co art. 28 wymaga.** Wymienienie kategorii danych i kategorii podmiotów.

**Co audytor szuka.** Konkretna lista kategorii: dane identyfikacyjne (imię, nazwisko, e-mail), dane kontaktowe (telefon, adres), dane finansowe (numer konta, historia transakcji), dane zdrowotne (jeśli applicable), dane biometryczne (jeśli applicable). Plus kategorie podmiotów: pracownicy, klienci, kandydaci, dostawcy.

**Częste błędy.**
- "Dane osobowe niezbędne do realizacji usługi" — niewystarczające.
- Pominięcie szczególnych kategorii (art. 9), gdy są przetwarzane.

### Element 4: Obowiązki i prawa administratora

**Co art. 28 wymaga.** Określenie, że administrator decyduje o celach i sposobach, procesor wykonuje jego polecenia.

**Co audytor szuka.** Klauzula określająca, że procesor nie używa danych do własnych celów (np. trenowanie modeli AI procesora na danych administratora — częsta pułapka).

**Częste błędy.**
- Brak klauzuli o zakazie używania danych do własnych celów procesora.
- Pozwolenie procesorowi na "anonimizację i wykorzystanie do analiz" — to jest własny cel procesora, nie powierzenie. Klauzula obejmująca taką operację narusza art. 28.

### Element 5: Zobowiązania procesora (art. 28 ust. 3 lit. a–h)

**Osiem konkretnych zobowiązań procesora, które MUSZĄ być w DPA:**

(a) Przetwarzanie na udokumentowane polecenie administratora.
(b) Tajemnica pracowników procesora (obowiązek poufności).
(c) Stosowanie wszelkich wymaganych środków bezpieczeństwa art. 32.
(d) Sub-procesory tylko za zgodą administratora.
(e) Pomoc administratorowi w realizacji praw podmiotów (art. 12–22).
(f) Pomoc administratorowi w wypełnianiu obowiązków art. 32–36 (bezpieczeństwo, zgłaszanie naruszeń, DPIA).
(g) Po zakończeniu zwrot lub zniszczenie danych według wyboru administratora.
(h) Udostępnianie wszelkich informacji niezbędnych do wykazania zgodności + audyty.

**Co audytor szuka.** Każda z tych ośmiu klauzul, słowo po słowie. Pominięcie którejkolwiek = ustalenie krytyczne.

**Częste błędy.**
- Klauzule formalnie obecne, ale skróty/wycieżki: np. "procesor będzie pomagać administratorowi w zakresie ekonomicznie uzasadnionym" — to jest osłabienie obowiązku z art. 28 lit. e/f i niesie ryzyko.
- "Procesor może korzystać z sub-procesorów wedle uznania, informując administratora" — narusza art. 28 lit. d, który wymaga zgody (uprzedniej lub ogólnej z prawem sprzeciwu).

### Element 6: Sub-procesorzy

**Co art. 28 wymaga.** Procesor może powierzyć dane sub-procesorowi tylko za zgodą administratora (uprzednią konkretną LUB ogólną z prawem sprzeciwu). Sub-procesor musi być związany analogicznymi obowiązkami.

**Co audytor szuka.** Aktualna lista sub-procesorów (typowo dla dostawców cloud: liczne — np. AWS używa setek sub-procesorów dla różnych usług), mechanizm zgody, mechanizm aktualizacji listy z prawem sprzeciwu.

**Częste błędy.**
- Brak listy sub-procesorów (dostawca powołuje się na ogólną dostępność listy na stronie, bez konkretnej referencji).
- Brak mechanizmu sprzeciwu (administrator nie wie, że dostawca dodał nowego sub-procesora w USA).
- Sub-procesorzy poza UE/EOG bez SCC lub innych zabezpieczeń.

### Element 7: Zwrot lub zniszczenie danych

**Co art. 28 wymaga.** Po zakończeniu — zwrot lub zniszczenie, według wyboru administratora.

**Co audytor szuka.** Konkretna procedura, termin (typowo 30–60 dni), dowód zniszczenia (certyfikat lub raport), wyjątki tylko w zakresie zabezpieczenia przez prawo (np. archiwa księgowe).

**Częste błędy.**
- "Procesor usunie dane wedle własnych standardów" — niewystarczające.
- Brak terminu — proces "kiedyś" jest nieaudytowalny.

### Element 8: Audyty (art. 28 lit. h)

**Co art. 28 wymaga.** Procesor udostępnia administratorowi wszelkie informacje niezbędne do wykazania zgodności + umożliwia audyty (w tym kontrole) przeprowadzane przez administratora lub audytora przez niego upoważnionego.

**Co audytor szuka.** Klauzula audytowa z konkretnymi warunkami: częstotliwość, koszty, zakres, ograniczenia.

**Częste błędy.**
- Brak klauzuli audytowej.
- Audyt "tylko przy uzasadnionym podejrzeniu naruszenia" — to jest osłabienie obowiązku art. 28 lit. h.
- Audyt "na koszt administratora niezależnie od wyniku" — wątpliwe etycznie, choć dopuszczalne; UODO patrzy nieprzychylnie.
- Ograniczenie do certyfikatów SOC 2 / ISO 27001 jako substytutu audytu — może być uzupełnieniem, ale nie zastępstwem prawa do audytu.

## Test trzech umów — szybka diagnoza stanu

Jeśli musisz w ciągu jednego dnia ocenić, w jakim stanie są umowy powierzenia w firmie, przeprowadź test trzech umów:

1. **Wybierz dostawcę krytycznego** (np. dostawca cloud lub system kadrowo-płacowy).
2. **Wybierz dostawcę średniego znaczenia** (np. narzędzie marketingowe lub CRM).
3. **Wybierz dostawcę małego znaczenia** (np. drobne narzędzie SaaS).

Dla każdego sprawdź:
- Czy DPA istnieje (formalnie podpisana z aktualną datą).
- Czy zawiera wszystkie osiem elementów art. 28 ust. 3.
- Czy lista sub-procesorów jest dostępna i aktualna.
- Czy klauzula audytowa istnieje i jest sensowna.
- Czy transfery do krajów trzecich są obsługiwane (SCC lub równoważne).

Test trzech umów zajmuje 2–3 godziny i daje miarodajny obraz całości. Jeśli wszystkie trzy są w porządku, system jest prawdopodobnie zdrowy. Jeśli choćby jedna kuleje (zwykle ten średniego znaczenia), reszta najpewniej również.

Dla zespołów IOD i compliance, które regularnie wykonują takie testy, przygotowujemy w newsletterze skanujfirme.pl checklist trzech umów w formie szablonu XLSX z pytaniami kontrolnymi i punktacją oraz wzorzec DPA zgodny z art. 28 (do dostosowania pod konkretną umowę usługową). Jeśli to się przydaje — można zapisać się bez zobowiązań.

## Klauzule dostawców cloud — specyficzne pułapki

DPA dostawców globalnych (AWS, Google, Microsoft, Salesforce, HubSpot) to osobna kategoria. Charakterystyka:

- Standardowy DPA dostarczony przez dostawcę, możliwość negocjacji minimalna lub żadna (poza klientami Enterprise).
- Sub-procesorzy w listach setek pozycji, regularnie zmieniani.
- Transfery do USA — od czasu Schrems II i Data Privacy Framework (DPF) z 2023 r. obsługiwane przez certyfikat DPF lub SCC plus TIA.
- Klauzule audytowe ograniczone do raportów SOC 2 i ISO 27001.

Co audytor sprawdza specyficznie dla globalnych dostawców:
- Czy konkretna usługa, z której firma korzysta, jest objęta DPF (nie wszystkie usługi są).
- Czy administrator wyraził zgodę ogólną na sub-procesorów z mechanizmem sprzeciwu.
- Czy TIA (Transfer Impact Assessment) został wykonany dla transferów do USA.
- Czy dostawca informuje o zmianach sub-procesorów z odpowiednim wyprzedzeniem.

Pełna metodyka transferów: [audyt transferów do krajów trzecich (SCC, TIA, USA po Schrems II)](audyt-transferow-do-krajow-trzecich-scc-tia.html).

## Format ustaleń w raporcie audytu art. 28

Przykład ustalenia, którego struktura jest reprezentatywna:

> **Ustalenie 28-03 (klasyfikacja: krytyczne):** Brak umowy powierzenia z procesorem realizującym wysyłkę newslettera (Mailchimp, USA) — od listopada 2023 r. trwa przetwarzanie danych 18 400 subskrybentów bez ważnej DPA i bez weryfikacji transferu do USA.
>
> **Dowody:** (1) Lista procesorów przedstawiona przez IOD (data); (2) Brak DPA w archiwum umów (zweryfikowane przez audytora); (3) Wyciąg z systemu Mailchimp pokazujący dane przetwarzane.
>
> **Ryzyko prawne:** Naruszenie art. 28 ust. 3 RODO (brak DPA) oraz art. 44–49 (transfery bez podstawy). Ekspozycja: kara administracyjna UODO do 20 mln EUR lub 4% rocznego obrotu (art. 83 ust. 5). Dodatkowo: ryzyko reputacyjne i utrata zaufania subskrybentów.
>
> **Rekomendacja korygująca:** (1) Natychmiast (w 24h) zawrzeć aktualne DPA Mailchimp dostępne w panelu administracyjnym; (2) Wykonać TIA dla transferu do USA z udokumentowaniem DPF lub SCC; (3) Zaktualizować klauzulę informacyjną o transferze; (4) Powiadomić IOD o nowym procesorze formalnie. Termin: 30 dni. Odpowiedzialny: dyrektor marketingu + IOD.

Taka struktura — z kwantyfikacją (18 400 subskrybentów), powołaniem na konkretną podstawę prawną i kara, propozycją z terminem — pozwala zarządowi szybko zrozumieć ryzyko i priorytetyzować.

## Trzy pytania kontrolne dla IOD przed audytem art. 28

**Pierwsze.** Czy mamy aktualną listę procesorów? Bez kompletnej listy audyt jest niemożliwy. Lista powinna zawierać: nazwa procesora, kategoria danych, kategoria operacji, data zawarcia DPA, data ostatniej weryfikacji, status (aktywna / wygasła / wymaga aktualizacji).

**Drugie.** Czy każda DPA pokrywa osiem obligatoryjnych elementów art. 28 ust. 3? Audyt klauzula po klauzuli dla każdego procesora to praca, ale jednorazowa — potem aktualizacja przy każdej zmianie umowy.

**Trzecie.** Czy proces on-boardingu nowego dostawcy obejmuje weryfikację DPA przez IOD przed podpisaniem umowy głównej? Jeśli nie — nowe luki będą powstawać szybciej, niż stare zostaną zamknięte.

## Esencja

Umowy powierzenia (art. 28 RODO) są w polskich firmach najsłabszym ogniwem zgodności. 30–60% audytów wykrywa luki w tej kategorii: brak umowy, niekompletna umowa, klauzule sprzeczne z art. 28, brak listy sub-procesorów, brak mechanizmów audytowych.

Osiem obligatoryjnych elementów art. 28 ust. 3 — przedmiot i czas, charakter i cel, dane i podmioty, prawa administratora, osiem szczegółowych zobowiązań procesora (a–h), sub-procesorzy, zwrot/zniszczenie, audyty — musi być w każdej DPA. Brak jakiegokolwiek = niezgodność.

Test trzech umów (krytyczny, średni, mały dostawca) daje miarodajny obraz całości w 2–3 godziny. Jeśli wszystkie trzy są w porządku, system jest zdrowy. Jeśli choćby jedna kuleje, prawdopodobnie cały portfel jest problematyczny.

DPA dostawców globalnych (AWS, Google, Microsoft) to osobna kategoria — standardowe szablony, transfery do USA, długie listy sub-procesorów. Tutaj audyt skupia się na: DPF/SCC dla transferów, TIA, mechanizmie zgody ogólnej z prawem sprzeciwu.

Proces on-boardingu nowych procesorów jest kluczowy. Bez weryfikacji DPA przed podpisaniem umowy głównej luki będą się tworzyć szybciej, niż stare zostaną zamknięte. Najlepsze firmy mają w on-boardingu dostawcy gate'a "approval IOD" — bez tego umowa nie zostaje podpisana.

Art. 28 jest jednym z najczęściej cytowanych przepisów RODO w decyzjach UODO i sądów. Sankcje za brak DPA są wysokie — wyższy próg z art. 83 (do 20 mln EUR lub 4% obrotu), bo art. 28 zalicza się do "bardziej istotnych" obowiązków. Dla średniej firmy to znaczy, że jedno przeoczenie procesora może kosztować więcej niż dwuletni budżet IOD.

---

<ul>
<li>Rozporządzenie Parlamentu Europejskiego i Rady (UE) 2016/679 z dnia 27 kwietnia 2016 r. (RODO), art. 28 — Podmiot przetwarzający. https://eur-lex.europa.eu/eli/reg/2016/679/oj</li>
<li>EROD/EDPB (2021). <em>Guidelines 07/2020 on the concepts of controller and processor in the GDPR</em>, version 2.0. https://www.edpb.europa.eu/our-work-tools/our-documents/guidelines/</li>
<li>Komisja Europejska (2021). <em>Standardowe klauzule umowne między administratorami i podmiotami przetwarzającymi</em>, Decyzja Wykonawcza (UE) 2021/915. https://eur-lex.europa.eu/eli/dec_impl/2021/915/oj</li>
<li>UODO (2019, z aktualizacjami). <em>Wytyczne w sprawie umów powierzenia danych osobowych</em>. https://uodo.gov.pl/pl/138</li>
<li>UODO. <em>Decyzje Prezesa UODO w sprawach art. 28 RODO (2019–2024)</em>. https://uodo.gov.pl/pl/138/</li>
<li>EDPB-EDPS Joint Opinion 2/2021 on Standard Contractual Clauses between controllers and processors. https://www.edpb.europa.eu/</li>
<li>Komisja Europejska. <em>EU-US Data Privacy Framework</em>, Decyzja Wykonawcza Komisji (UE) 2023/1795. https://eur-lex.europa.eu/eli/dec_impl/2023/1795/oj</li>
<li>EROD (2021). <em>Recommendations 01/2020 on measures that supplement transfer tools</em>, version 2.0. https://www.edpb.europa.eu/</li>
<li>Polska Ustawa z dnia 10 maja 2018 r. o ochronie danych osobowych (Dz.U. 2018 poz. 1000 ze zm.)</li>
<li>ICO (UK). <em>Contracts and liabilities between controllers and processors</em>. https://ico.org.uk/for-organisations/guide-to-data-protection/guide-to-the-general-data-protection-regulation-gdpr/contracts-and-liabilities-between-controllers-and-processors/</li>
</ul>
