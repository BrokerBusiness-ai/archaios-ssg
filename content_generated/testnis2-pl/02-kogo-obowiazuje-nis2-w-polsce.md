---
title: "Kogo dokładnie obowiązuje NIS2 w Polsce — kompletny przewodnik kwalifikacji"
slug: "kogo-obowiazuje-nis2-w-polsce"
excerpt: "ENISA szacuje 8 000 polskich podmiotów objętych NIS2 — wzrost z około 200 podmiotów objętych NIS1. Dwa kryteria łączne: sektor (Załącznik I lub II) + rozmiar (≥50 pracowników lub ≥10 mln EUR obrotu/sumy bilansowej). Plus wyjątki — niektóre podmioty objęte niezależnie od rozmiaru. Krok po kroku — czy ciebie to dotyczy."
category_slug: "regulacje"
tags: "NIS2, podmioty-kluczowe, podmioty-istotne, Polska, zakres, kwalifikacja, średniozaawansowany"
reading_time: 11
is_published: true
is_featured: false
meta_title: "Kogo obowiązuje NIS2 w Polsce — kompletna kwalifikacja | TestNIS2"
meta_description: "Dwa kryteria łączne NIS2: sektor + rozmiar. Lista sektorów Załączników I i II, wyjątki, klasyfikacja kluczowe vs istotne, polskie specyfika."
funnel: "TOFU"
author_slug: "marek-porycki"
related_slugs: "nis2-checklista-gotowosci-10-obszarow,nis1-vs-nis2-co-sie-zmienilo,nis2-dla-msp-uproszczone-wymagania,test-gotowosci-nis2-online"
product_slugs: "archaios-cyber"
---

# Kogo dokładnie obowiązuje NIS2 w Polsce — kompletny przewodnik kwalifikacji

W październiku 2024 roku ENISA — Agencja Unii Europejskiej ds. Cyberbezpieczeństwa — opublikowała szacunki: dyrektywa NIS2 obejmie w Polsce co najmniej **8 000 podmiotów**, w porównaniu z około 200 podmiotami objętymi pierwotną dyrektywą NIS1. Wzrost ponad czterdziestokrotny. Większość polskich firm, które do 2024 roku *nie miały* obowiązków cyberbezpieczeństwa wynikających z UE — od 2025-2026 roku *ma*.

Najczęstsze pytanie polskich CIO i prezesów w pierwszych tygodniach 2025 roku: *"czy nas to dotyczy?"*. Odpowiedź zależy od dwóch kryteriów spełnionych *jednocześnie*: sektor + rozmiar. Plus dziesiątki wyjątków, niejasności interpretacyjnych i polskich specyfik. Ten artykuł jest przewodnikiem przez te zasady.

## Dwa kryteria łączne — fundament kwalifikacji

NIS2 stosuje się do podmiotu, jeśli spełnia *oba* poniższe warunki:

### Kryterium 1: sektor

Dyrektywa wymienia sektory w *dwóch załącznikach*:

**Załącznik I — sektory wysokiego znaczenia:**
- Energetyka (elektroenergetyka, ciepło, gaz, ropa naftowa, wodór)
- Transport (lotniczy, kolejowy, wodny, drogowy)
- Bankowość i infrastruktura rynków finansowych
- Sektor zdrowia (włącznie z producentami leków, wyrobów medycznych)
- Woda pitna i ścieki
- Infrastruktura cyfrowa (operatorzy DNS, rejestry domen TLD, dostawcy chmury, IXP, CDN, content delivery, dostawcy zaufania, dostawcy łączności elektronicznej)
- Zarządzanie usługami ICT (B2B managed services)
- Administracja publiczna (rządowa, niektóre samorządowa)
- Przestrzeń kosmiczna (operatorzy infrastruktury kosmicznej)

**Załącznik II — sektory pozostałe krytyczne:**
- Poczta i kurierzy
- Gospodarka odpadami
- Produkcja, dystrybucja chemikaliów
- Produkcja, dystrybucja żywności
- Produkcja (urządzenia medyczne, komputery, optyka, sprzęt elektryczny, maszyny, pojazdy mechaniczne)
- Dostawcy usług cyfrowych (online marketplace, online search engines, social networks)
- Badania (organizacje prowadzące działalność badawczą)

Mówiąc po polsku: jeśli twoja firma działa w *którymkolwiek* z tych obszarów (nawet jako średniej wielkości dostawca usług ICT, średniej wielkości firma produkcyjna, lokalny dostawca żywności w skali wojewódzkiej) — kryterium 1 jest spełnione.

### Kryterium 2: rozmiar

Domyślnie podmiot jest objęty NIS2 jeśli spełnia *co najmniej jeden* z warunków:

- **≥ 50 pracowników** (etat zgodny z definicją UE)
- **Roczny obrót ≥ 10 mln EUR**
- **Roczna suma bilansowa ≥ 10 mln EUR**

To są progi *średniego przedsiębiorstwa* w klasyfikacji UE. Mikro i małe (poniżej tych progów) są zwykle wyłączone — z istotnymi wyjątkami poniżej.

### Wyjątki — kiedy rozmiar nie ma znaczenia

Niektóre podmioty są objęte *niezależnie* od rozmiaru:

- **Operatorzy DNS** (Domain Name System)
- **Rejestry domen najwyższego poziomu (TLD)** — np. NASK dla .pl
- **Dostawcy zaufania** (qualified trust service providers wg eIDAS)
- **Niektóre podmioty publiczne** wskazane przez państwo członkowskie
- **Operatorzy infrastruktury krytycznej w sensie krytycznym** dla bezpieczeństwa narodowego

Polska może też *rozszerzyć* zakres — wskazać dodatkowe sektory lub obniżyć progi w specyficznych obszarach. Polska ustawa nowelizacyjna w 2026 wprowadza pewne *zaostrzenia* w stosunku do minimum dyrektywy.

## Klasyfikacja: essential vs important entities

Dwa typy klasyfikacji w NIS2 — z istotnymi konsekwencjami:

### Essential entities (podmioty kluczowe)

**Sektory:** wszystkie z Załącznika I, plus niektóre wskazane podmioty publiczne.

**Wymagania:** wyższy rygor — w tym *proaktywny* nadzór organu (audyty z urzędu, regularne kontrole, nakaz audytu).

**Kary:** do **10 mln EUR lub 2% globalnego obrotu** (która jest *wyższa*).

**Przykłady polskich essential entities:**
- Banki komercyjne, infrastruktura giełdowa
- Operatorzy energetyczni (PGE, Tauron, Enea, Energa)
- Szpitale wieloprofilowe powyżej 50 łóżek
- Operatorzy autostrad, linii kolejowych
- Wodociągi miast wojewódzkich
- ASP, NASK, podmioty publiczne kluczowe dla cyberbezpieczeństwa

### Important entities (podmioty istotne)

**Sektory:** wszystkie z Załącznika II + część z Załącznika I (dla średnich, nie kluczowych).

**Wymagania:** podstawowy rygor — *reaktywny* nadzór (interwencja po incydencie, sygnale, skardze).

**Kary:** do **7 mln EUR lub 1,4% globalnego obrotu** (która jest *wyższa*).

**Przykłady polskich important entities:**
- Średniej wielkości firmy produkcyjne (medical devices, części samochodowe, elektronika)
- Średniej wielkości operatorzy logistyczni
- Dostawcy usług IT B2B (managed services, hosting)
- Sieci handlowe (jeśli powyżej progu rozmiaru)
- Średniej wielkości platformy e-commerce
- Pośrednicy ubezpieczeniowi (jeśli powyżej progu)

## Konsekwencje klasyfikacji

Różnica essential vs important *nie* jest tylko nominalna. Praktycznie:

| Aspekt | Essential | Important |
|---|---|---|
| **Nadzór** | Proaktywny, audyty z urzędu | Reaktywny, po incydencie/sygnale |
| **Maksymalna kara** | 10 mln EUR / 2% obrotu | 7 mln EUR / 1,4% obrotu |
| **Częstość audytów** | Regularne, planowane | Sporadycznie, po wystąpieniu zdarzeń |
| **Pierwszeństwo wsparcia z CSIRT** | Wyższe | Standardowe |
| **Obowiązki raportowania** | Pełne | Pełne (te same wymogi 24/72h) |

Co istotne: *minimalne wymagania techniczne* są *takie same* dla obu kategorii. To jest sygnał regulatora: każdy podmiot objęty musi spełnić 10 obszarów wymagań z [pillar artykułu](/nis2-checklista-gotowosci-10-obszarow/), niezależnie od klasyfikacji.

## Polskie specyfiki

Polska ustawa nowelizacyjna 2025-2026 wprowadza kilka *polskich* specyfik:

### 1. Krajowy organ nadzoru

W Polsce nadzór NIS2 sprawuje:
- **CSIRT NASK** (Computer Security Incident Response Team) — dla większości sektorów
- **CSIRT MON** — dla sektora obronnego
- **CSIRT GOV** — dla administracji publicznej
- **Organy sektorowe** — np. KNF dla bankowości, URE dla energetyki

Każdy podmiot powinien zidentyfikować *swój* CSIRT, do którego raportuje incydenty.

### 2. Obowiązek rejestracji

Polska wymaga *rejestracji* podmiotów objętych w Krajowym Rejestrze Cyberbezpieczeństwa. Termin: 2 miesiące od wejścia w życie nowelizacji ustawy (dokładny termin zależny od finalizacji).

### 3. Polskie zaostrzenia

Niektóre wymagania NIS2 są *zaostrzane* przez polską ustawę:
- Krótszy okres na powiadomienie *zewnętrzne* (np. klientów) o niektórych typach incydentów
- Dodatkowe wymagania dla sektora finansowego (synchronizacja z polskim KNF i unijnym DORA)
- Specyficzne wymagania dla sektora zdrowia (synchronizacja z polskim NFZ)

### 4. Język raportowania

Raportowanie do CSIRT: w języku polskim. To pozornie oczywiste, ale praktycznie problematyczne dla międzynarodowych firm z polskimi oddziałami — wymaga to lokalnego procesu.

## Jak praktycznie zweryfikować, czy was dotyczy

Krok po kroku:

### Krok 1: zidentyfikuj sektor

Sprawdź, czy podstawowa działalność firmy mieści się w Załączniku I lub II. Pomocą: główny PKD firmy.

Najczęściej pomijane:
- **Producenci urządzeń medycznych** (Załącznik II) — wielu nie wie, że są objęci
- **Dostawcy hostingu / chmury B2B** (Załącznik I — infrastruktura cyfrowa)
- **Średnie firmy software'owe oferujące SaaS** (Załącznik II — dostawcy usług cyfrowych)
- **Firmy logistyczne** (Załącznik II — poczta i kurierzy, jeśli świadczą usługi kurierskie)
- **Operatorzy oczyszczalni ścieków** (Załącznik I — woda i ścieki)

### Krok 2: sprawdź rozmiar

Najnowsze raporty roczne: liczba pracowników, obrót, suma bilansowa. Jeśli przekraczasz *którykolwiek* z trzech progów (50 pracowników / 10 mln EUR obrotu / 10 mln EUR sumy bilansowej) — kryterium spełnione.

### Krok 3: sprawdź wyjątki

Czy jesteście:
- Operatorem DNS lub rejestrem TLD?
- Dostawcą zaufania (kwalifikowanym wg eIDAS)?
- Podmiotem publicznym wskazanym imiennie?

Jeśli tak — kwalifikacja niezależnie od rozmiaru.

### Krok 4: określ klasyfikację

Czy jesteście w Załączniku I (essential) czy II (important)? Plus polskie modyfikacje — czy ustawa zaostrza wasze wymagania?

### Krok 5: zarejestrujcie się

Po wejściu w życie polskiej ustawy: rejestracja w KRC (Krajowy Rejestr Cyberbezpieczeństwa).

## Częste nieporozumienia

### "Jesteśmy małą firmą, więc nas to nie dotyczy"

*Nieprawda*, jeśli jesteście w sektorach z wyjątkami od progu rozmiaru. Mała firma będąca operatorem DNS lub dostawcą zaufania — *jest* objęta.

### "Mamy ISO 27001, więc jesteśmy zgodni"

*Częściowo*. ISO 27001 pokrywa większość wymagań NIS2, ale *nie wszystkie*. NIS2 wymaga konkretnych elementów (raportowanie 24/72h do CSIRT, szkolenia zarządu, mapowanie łańcucha dostaw), które ISO nie precyzuje. Plus: NIS2 wymaga *zarejestrowania*, ISO nie.

### "Nasza spółka-córka w Polsce jest mała"

*Sprawdźcie zasady grupowe*. NIS2 generalnie traktuje podmioty *odrębnie*, ale niektóre wytyczne sugerują patrzenie na *grupę* w określonych przypadkach. Wymaga interpretacji prawnej.

### "Nasi klienci są w UE, my w Polsce, więc nie podlegamy"

*Polska jest częścią UE*. Polskie podmioty są objęte polską implementacją NIS2. Plus dyrektywa ma efekt eksterytorialny — niektóre obowiązki dotyczą nawet podmiotów spoza UE oferujących usługi w UE.

### "To dotyczy IT, nie biznesu"

*Nieprawda*. NIS2 *eksplicit* wymaga zaangażowania zarządu — szkolenia, odpowiedzialność osobista, plany ciągłości działania. To jest sprawa dla CEO, nie tylko CIO. Szczegółowo: [Odpowiedzialność osobista zarządu w NIS2](/odpowiedzialnosc-zarzadu-nis2/).

## Co robić, jeśli jesteście objęci

Jeśli kwalifikacja wskazuje, że NIS2 was dotyczy:

**1. Audyt gotowości** — diagnoza w 10 obszarach z [pillar checklist](/nis2-checklista-gotowosci-10-obszarow/).

**2. Plan wdrożenia 12-miesięczny** — fazy: diagnoza → krytyczne obszary → procesy → audyt.

**3. Powołanie odpowiedzialnej osoby** — CISO lub equivalent z mandatem zarządu.

**4. Konsultacje prawne** — szczególnie dla: branży regulowanej, międzynarodowej struktury grupowej, niejednoznacznych przypadków klasyfikacji.

**5. Ścieżka komunikacji z CSIRT** — kto, kiedy, jak raportuje. Numer telefonu, email, formularz online.

**6. Budżet** — realistycznie 100k-500k PLN / rok dla średniej firmy, 500k-3M PLN / rok dla dużej (zależy od stopnia obecnej dojrzałości).

## Co robić, jeśli *nie jesteście* objęci

Nie znaczy "nic". Trzy przyczyny dlaczego nadal warto wdrażać dobre praktyki cyber:

1. **Klienci wymagają.** Coraz więcej kontraktów B2B zawiera klauzule cyber. Niespełnienie = utrata kontraktów.
2. **Łańcuch dostaw.** Jeśli wasi klienci są podmiotami NIS2 — *oni* są zobowiązani audytować *was*. Bez podstawowej higieny cyber wypadacie z list dostawców.
3. **Ataki nie sprawdzają regulacji.** Ransomware uderza w każdą firmę — niezależnie od tego, czy was kwalifikuje się jako "kluczowych" prawnie. Bez gotowości skutki są katastrofalne.

Małe firmy mogą skorzystać z [uproszczonej checkisty NIS2 dla MŚP](/nis2-dla-msp-uproszczone-wymagania/) — większość najważniejszych elementów stosuje się też do nich, choć formalnego obowiązku nie ma.

## Trzy pytania kontrolne

Po pierwsze: czy potraficie *natychmiast* wskazać, czy wasza firma jest w Załączniku I, Załączniku II, czy nieobjęta? Jeśli wymaga to konsultacji — zróbcie ją. Bez jasnej kwalifikacji każda dalsza praca compliance jest na piasku.

Po drugie: jeśli jesteście objęci — kto w organizacji ma *imienną* odpowiedzialność za NIS2? Jeśli odpowiedź to "wszyscy" lub "departament IT" — to *nikt*. NIS2 wymaga konkretnej osoby z mandatem.

Po trzecie: czy wasi *kluczowi dostawcy* są objęci NIS2? Jeśli tak — czy wasze umowy z nimi zawierają klauzule audytowe i raportowania incydentów? Jeśli nie — to luka w waszym łańcuchu dostaw, za którą *wy* odpowiadacie regulacyjnie.

W każdy poniedziałek wysyłamy w newsletterze TestNIS2 *konkretne* analizy interpretacyjne nowych wytycznych ENISA, polskich nowelizacji ustawy, case studies wdrożeń. Dla zarządów i CISO: 5 minut tygodniowo, decyzje oparte na faktach. **Zapisz się na newsletter** (formularz w stopce) — bez spamu, wypisujesz się jednym klikiem.

## Esencja

NIS2 obejmie ~8 000 polskich podmiotów (vs ~200 NIS1). Dwa kryteria łączne: sektor (Załącznik I lub II) + rozmiar (≥50 pracowników LUB ≥10 mln EUR obrotu/sumy bilansowej). Plus wyjątki — niektóre podmioty objęte niezależnie od rozmiaru (operatorzy DNS, rejestry TLD, dostawcy zaufania).

Klasyfikacja: **essential entities** (Załącznik I, kary do 10 mln EUR / 2% obrotu, nadzór proaktywny) vs **important entities** (Załącznik II, kary do 7 mln EUR / 1,4% obrotu, nadzór reaktywny). Wymagania techniczne *takie same*.

Polskie specyfiki: nadzór CSIRT NASK + CSIRT MON + CSIRT GOV + organy sektorowe (KNF, URE), obowiązek rejestracji w KRC, polskie zaostrzenia w niektórych sektorach, raportowanie po polsku.

Najczęściej pomijane sektory: producenci urządzeń medycznych, dostawcy SaaS, firmy hostingowe B2B, operatorzy oczyszczalni ścieków, firmy logistyczne (kurierzy).

Częste nieporozumienia: "jesteśmy mali" (wyjątki!), "mamy ISO 27001" (częściowo!), "to dotyczy IT" (zarząd też!).

Najtrudniejsza prawda: większość polskich firm objętych NIS2 *nie wie*, że jest objęta. Brak rejestracji nie zwalnia z obowiązków — tylko zwiększa ryzyko sankcji za nie-zgłoszenie się + brak gotowości w razie kontroli.

Pierwszy krok strategiczny — *jasna* kwalifikacja. Jeśli dotyczy was — czas zacząć. Jeśli nie — czas budować dobre praktyki, bo łańcuch dostaw was dosięgnie inaczej.

---

## Bibliografia

<ul>
<li>Dyrektywa Parlamentu Europejskiego i Rady (UE) 2022/2555 z dnia 14 grudnia 2022 r. <em>Dziennik Urzędowy Unii Europejskiej</em>, L 333.</li>

<li>European Union Agency for Cybersecurity (ENISA). (2024). <em>NIS2 Implementation Toolbox</em>. https://www.enisa.europa.eu/topics/network-and-information-systems/nis-directive</li>

<li>European Commission. (2023). <em>Implementing Regulation (EU) on essential and important entities under NIS2</em>.</li>

<li>European Commission. (2024). <em>Communication on the implementation of NIS2 — sectoral scope guidance</em>.</li>

<li>Krajowy System Cyberbezpieczeństwa. (2018, z nowelizacjami). Ustawa o krajowym systemie cyberbezpieczeństwa. <em>Dziennik Ustaw</em>, poz. 1560.</li>

<li>European Banking Authority (EBA). (2024). <em>Guidelines on ICT risk management — sector-specific NIS2 implementation</em>.</li>
</ul>
