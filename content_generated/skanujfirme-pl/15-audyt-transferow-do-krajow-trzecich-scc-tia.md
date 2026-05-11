---
title: "Audyt transferów do krajów trzecich — SCC, TIA, USA po Schrems II"
slug: "audyt-transferow-do-krajow-trzecich-scc-tia"
excerpt: "Każde użycie AWS, Google, OpenAI to potencjalny transfer danych osobowych do USA. Pełna metodyka audytu transferów: SCC, TIA, DPF, środki uzupełniające."
category_slug: "rodo"
tags: "RODO, transfery danych, SCC, TIA, Schrems II, DPF, USA, średniozaawansowany"
reading_time: 13
is_published: true
is_featured: false
meta_title: "Audyt transferów do krajów trzecich — SCC, TIA, DPF (2026)"
meta_description: "Metodyka audytu transferów danych osobowych poza UE/EOG. SCC, TIA, EU-US DPF, środki uzupełniające. Co audytor sprawdza, jakie luki są typowe."
funnel: "MOFU"
author_slug: "marek-porycki"
related_slugs: "audyt-umow-powierzenia-art-28-rodo,audyt-rodo-art-32-bezpieczenstwo-techniczne,audyt-rodo-krok-po-kroku,dpia-w-praktyce-kiedy-obowiazuje-jak-wykonac,audyt-incydentow-24-72h-rodo-nis2"
product_slugs: ""
---

W lipcu 2020 r. Trybunał Sprawiedliwości UE w wyroku Schrems II unieważnił Privacy Shield — ramy ułatwiające transfer danych z UE do USA. W lipcu 2023 r. Komisja Europejska wydała decyzję adekwatności dla nowych ram EU-US Data Privacy Framework (DPF). Pomiędzy tymi datami polskie firmy żyły w stanie quasi-zawieszenia: transferowały dane do USA na podstawie SCC bez pełnej pewności prawnej. W 2026 r. DPF działa, ale audyt transferów pozostaje jednym z najtrudniejszych obszarów RODO — bo łączy wymogi prawne, techniczne (czy faktycznie szyfrujesz dane przed transferem) i kontekstowe (co konkretnie robi z danymi dostawca w państwie trzecim).

Każda polska średnia firma transferuje dane do krajów trzecich, najczęściej nie wiedząc o tym. Używasz AWS — transfer. Używasz Google Workspace — transfer. Mailchimp, HubSpot, Salesforce — transfer. ChatGPT enterprise, Claude API, Microsoft Copilot — transfer. Audyt transferów to mapa rzeczywistego pomiędzy-jurysdykcyjnego krwiobiegu danych firmy oraz weryfikacja, czy każdy transfer ma legalną podstawę i adekwatne środki techniczne.

Ten tekst jest pełną metodyką audytu transferów. Strukturuje się wokół trzech narzędzi prawnych (decyzja adekwatności, SCC, art. 49 ust. 1 wyjątki) plus narzędzia weryfikacji (TIA — Transfer Impact Assessment) plus środki uzupełniające (Supplementary Measures). Adresat: IOD/DPO, audytorzy RODO, działy prawne odpowiedzialne za umowy z dostawcami zagranicznymi.

## Definicja transferu — co właściwie audytujemy

Art. 44 RODO: "Przekazanie danych osobowych przetwarzanych lub mających być przetwarzane po przekazaniu do państwa trzeciego lub organizacji międzynarodowej następuje tylko wtedy, gdy administrator i podmiot przetwarzający spełniają warunki określone w niniejszym rozdziale".

Transfer obejmuje:
- przesłanie danych z UE do serwera w państwie trzecim
- udzielenie dostępu (zdalny) do danych z UE z państwa trzeciego (np. support engineer w Indiach loguje się do bazy w Polsce)
- użycie usługi cloud, której back-end znajduje się w państwie trzecim (nawet jeśli front-end usługi jest w UE)

Transfer NIE obejmuje (kontrowersyjnie, ale przyjęta interpretacja EROD):
- przejazdu danych przez kraje trzecie tranzytem (np. backbone internet)
- danych w transferze szyfrowane silnie, gdzie kraj trzeci nie ma kluczy

Audyt transferów polega na zbudowaniu pełnej mapy transferów rzeczywistych w firmie. To znacznie więcej niż lista zagranicznych dostawców — to każda integracja, każdy webhook, każdy SaaS, każda chmura wykorzystywana w organizacji.

## Trzy ścieżki legalizacji transferu

**Ścieżka 1: Decyzja adekwatności (art. 45).** Komisja Europejska wydaje decyzję uznającą państwo trzecie za zapewniające adekwatny poziom ochrony. Na maj 2026 r. decyzje istnieją dla: Andory, Argentyny, Faroe, Guernsey, Izraela, Wyspy Man, Japonii, Jersey, Nowej Zelandii, Korei Południowej, Szwajcarii, Urugwaju, Wielkiej Brytanii (post-Brexit), oraz USA (poprzez EU-US Data Privacy Framework — DPF, tylko dla podmiotów certyfikowanych).

**Ścieżka 2: Odpowiednie zabezpieczenia (art. 46).** Najczęściej w postaci Standardowych Klauzul Umownych (SCC) wydanych przez KE w czerwcu 2021 r. (Decyzja Wykonawcza (UE) 2021/914). Cztery moduły SCC odpowiadające relacjom: kontroler→kontroler, kontroler→processor, processor→processor, processor→kontroler. Plus inne narzędzia: BCR (Binding Corporate Rules dla grup kapitałowych), kodeksy postępowania, certyfikaty.

**Ścieżka 3: Odstępstwa (art. 49).** Wyjątkowe podstawy: zgoda wyraźna podmiotu, niezbędność umowy, ważne względy interesu publicznego, dochodzenie roszczeń, ochrona żywotnych interesów. Te podstawy są wyjątkami i NIE mogą być używane do transferów systematycznych — TYLKO ad hoc, ograniczone.

Audytor sprawdza, którą ścieżką dla każdego transferu legitymizowany jest transfer. Część firm transferuje dane do USA "na zgodę" — i to jest typowo nieprawidłowe, bo zgoda nie pasuje do regularnych transferów operacyjnych.

## EU-US Data Privacy Framework (DPF) — krytyczne uściślenia

DPF działa od lipca 2023 r. dla USA. Mechanizm: amerykański podmiot certyfikuje się dobrowolnie w Department of Commerce, deklaruje przestrzeganie zasad DPF, podlega kontroli FTC. Polska firma transferująca do tego podmiotu nie potrzebuje SCC.

Co audytor weryfikuje przy DPF:
- Czy konkretny podmiot, do którego transferujemy dane, jest aktualnie certyfikowany w DPF (lista publiczna na dataprivacyframework.gov).
- Czy konkretna usługa, z której korzystamy u tego podmiotu, jest objęta zakresem certyfikacji (część podmiotów certyfikuje tylko niektóre usługi).
- Czy certyfikat jest aktywny (są podmioty z wygaśniętą certyfikacją, mimo że nadal pojawiają się na "starych" listach).

Niuans: DPF jest narzędziem słabszym niż wcześniejsze Privacy Shield z perspektywy zabezpieczeń przed inwigilacją USA. Schrems III (w toku przed TSUE w 2025 r.) może DPF ponownie unieważnić. Ostrożny audytor zaleca, by transfery do USA były obsługiwane przez DPF + zaplanowane fallback SCC + zaplanowane środki uzupełniające. To strategia odporności.

## Standardowe klauzule umowne (SCC 2021)

SCC 2021 zastąpiły poprzednie wersje (2001, 2004, 2010). Cztery moduły. Każdy zestaw klauzul obowiązkowy ma trzy załączniki:
- **Załącznik I.A:** opis stron i kategorii transferu
- **Załącznik I.B:** opis transferu (kategorie danych, kategorie podmiotów, częstotliwość, charakter, cele, okresy retencji)
- **Załącznik II:** środki techniczne i organizacyjne

Audytor sprawdza:
- Czy SCC są w aktualnej wersji 2021 (firmy często mają nadal stare SCC z 2010 r., co po grudniu 2022 r. nie jest już dopuszczalne dla nowych transferów).
- Czy załączniki I.A, I.B, II są kompletnie wypełnione (najczęstszy błąd: załączniki puste lub generyczne).
- Czy klauzule są zharmonizowane z umową główną (DPA + SCC powinny być spójne, nie sprzeczne).
- Czy klauzula odnosząca się do prawa właściwego i jurysdykcji jest poprawna (musi być prawo państwa członkowskiego UE).

## Transfer Impact Assessment (TIA) — najtrudniejszy element audytu

TIA to formalna ocena, czy w państwie trzecim, do którego transferujesz dane, prawo i praktyka pozwalają zachować ochronę równoważną RODO. Wymaga jej art. 46 RODO w wykładni EROD (Recommendations 01/2020). TIA jest obowiązkową częścią transferów na SCC; dla DPF nie jest formalnie wymagana, ale rekomendowana.

**Etapy TIA:**

1. **Identyfikacja transferu w szczegółach:** kategorie danych, kategorie podmiotów, cele, częstotliwość, sposób przesyłania.

2. **Identyfikacja narzędzia transferu:** SCC moduł, DPF, BCR, art. 49 odstępstwo.

3. **Ocena prawa państwa trzeciego:** czy istnieją regulacje umożliwiające dostęp władz publicznych do danych w sposób niezgodny ze standardami UE? Dla USA: FISA Section 702, Executive Order 12333, USA Patriot Act, CLOUD Act. Dla Chin: Cybersecurity Law, Data Security Law, Personal Information Protection Law. Dla Indii: pakiet ustaw 2023.

4. **Ocena praktyki:** czy w rzeczywistości władze państwa trzeciego korzystają z tych regulacji w stosunku do podobnych transferów? Czy istnieją skargi, wyroki, raporty?

5. **Ocena środków uzupełniających:** czy istniejące zabezpieczenia (techniczne, organizacyjne, umowne) są wystarczające, aby zniwelować ryzyko prawa państwa trzeciego?

6. **Decyzja:** transfer dozwolony / dozwolony pod warunkiem dodatkowych środków / niedozwolony.

7. **Dokumentacja:** raport TIA, akceptowany przez administratora, retencja minimum przez czas trwania transferu plus 5 lat.

Częste błędy w audycie TIA:
- TIA wykonana raz przy podpisaniu umowy, nigdy nie zaktualizowana.
- TIA wykonana powierzchownie ("USA = OK na podstawie DPF"), bez analizy specyficznych regulacji.
- Brak dokumentacji decyzji administratora.

## Środki uzupełniające (Supplementary Measures)

Gdy TIA pokazuje, że samo SCC nie wystarcza, art. 46 wymaga dodatkowych środków. EROD w Recommendations 01/2020 wymienia trzy kategorie:

**Środki techniczne.** Najmocniejsza kategoria. Obejmuje: szyfrowanie end-to-end (klucze pozostają w UE, dostawca w państwie trzecim nie ma kluczy), pseudonimizację, anonimizację, podział danych. Kluczowy test: czy nawet w przypadku przymusowego ujawnienia (np. nakaz amerykańskiego sądu) dostawca może rzeczywiście przekazać czytelne dane?

**Środki kontraktowe.** Klauzule w SCC: zobowiązanie dostawcy do natychmiastowego informowania administratora o nakazach od władz, zobowiązanie do prawnego kontestowania nakazów, zobowiązanie do publikowania transparency reports. Te środki są SŁABE — dostawca może być prawnie zmuszony do ukrycia faktu nakazu (gag order w USA).

**Środki organizacyjne.** Wewnętrzne polityki dostawcy, audyty bezpieczeństwa, certyfikaty, szkolenia. Najsłabsza kategoria, ma znaczenie głównie uzupełniające.

Audytor sprawdza, czy dla każdego "ryzykownego" transferu (do USA, Chin, Indii bez DPF/decyzji adekwatności) są wdrożone środki uzupełniające. Brak środków uzupełniających przy istniejącym ryzyku = ustalenie krytyczne.

## Typowe scenariusze transferów w polskiej średniej firmie

**Scenariusz 1: AWS / Microsoft Azure z regionem UE.** Twierdzenie dostawcy: "Twoje dane są w regionie EU-Central-1". Realnie: kontrola pozostaje w USA (administracja, support, fall-back). Audyt: SCC + TIA + ocena, czy region UE faktycznie izoluje od US persons. Środki uzupełniające: BYOK (Bring Your Own Key) lub HYOK (Hold Your Own Key) gdzie możliwe.

**Scenariusz 2: SaaS marketingowy (HubSpot, Mailchimp, Salesforce Marketing Cloud).** Dane w USA. Sprawdź: DPF cert + jaki konkretnie serwis jest objęty + środki techniczne (część dostawców oferuje opcję "EU region" — sprawdź realnie). Często brak środków uzupełniających przy danych behawioralnych klientów.

**Scenariusz 3: AI (ChatGPT, Claude, Gemini, Copilot).** Transfer treści promptów do USA. Sprawdź: czy wersja enterprise z opt-out z trenowania + DPF + ustawienia prywatności. Dla danych wrażliwych (medycznych, prawnych, klientów) — częsta luka. Coraz częstszy temat audytu w 2026 r.

**Scenariusz 4: Support outsourcing (Indie, Filipiny).** Pracownicy zewnętrzni z dostępem do bazy klientów. Sprawdź: SCC, kontrolę dostępu, logowanie, szyfrowanie połączeń, ograniczenie zakresu danych. Często brak TIA dla Indii (zwłaszcza po ustawach 2023 r.).

**Scenariusz 5: Slack, Microsoft Teams.** Komunikacja wewnętrzna, w której są dane osobowe pracowników i klientów. Transfer do USA przez backend dostawcy. Sprawdź: DPF + ustawienia retencji + szyfrowanie + ewentualnie opcję "Enterprise Key Management".

## Mapa transferów — output audytu

Wynikiem audytu jest mapa transferów z minimum następującymi kolumnami:

| Dostawca | Kategorie danych | Kraj transferu | Narzędzie prawne | TIA wykonana | Środki uzupełniające | Ryzyko rezydualne |
|---|---|---|---|---|---|---|
| AWS S3 (region us-east-1) | klienci, transakcje | USA | DPF + SCC | TAK (2025-08) | szyfrowanie BYOK, audit logs | niskie |
| HubSpot Marketing | leady, behawior | USA | DPF | TAK (2024-12) | brak (luka) | średnie |
| ChatGPT Enterprise | prompty z bazy klientów | USA | DPF | NIE | opt-out z trenowania | wysokie — luka audytowa |
| Support outsourcing (Indie) | tickety klientów | Indie | SCC moduł 2 | NIE (luka) | brak | wysokie — luka audytowa |
| Slack Enterprise | komunikacja wewnętrzna | USA | DPF | TAK (2025-01) | Enterprise Key Mgmt | niskie |

Taka mapa, regularnie aktualizowana (minimum kwartalnie), jest jednym z najmocniejszych dowodów świadomości zarządczej w audycie RODO. UODO przy kontrolach pyta wprost: "Pokaż mapę transferów". Jej brak = ustalenie systemowe.

Jeśli przygotowujesz lub odbierasz pierwszy audyt transferów i potrzebujesz szablonu mapy w XLSX z metodyką wypełniania oraz checklistą TIA per kraj — przesyłamy ten pakiet w newsletterze skanujfirme.pl. Mapa transferów to dokument operacyjny, nie jednorazowy artefakt — z szablonem łatwiej utrzymać aktualność.

## Trzy pytania kontrolne dla IOD przed audytem transferów

**Pierwsze.** Czy mam pełną listę dostawców z transferem do krajów trzecich? Bez listy audyt jest niemożliwy. Lista wymaga zaangażowania IT (kto jakich SaaS używa), zakupów (jakie umowy podpisaliśmy), security (jakie integracje techniczne istnieją).

**Drugie.** Dla każdego transferu — które z trzech narzędzi prawnych go legitymizuje? Brak odpowiedzi = niezgodność.

**Trzecie.** Dla transferów na SCC — czy mam aktualną TIA? Bez TIA SCC są niewystarczające w wykładni EROD.

## Esencja

Audyt transferów do krajów trzecich łączy trzy wymiary: prawny (decyzja adekwatności / SCC / wyjątki art. 49), kontekstowy (TIA — czy prawo państwa trzeciego pozwala zachować ochronę RODO) i techniczny (środki uzupełniające — czy szyfrowanie, pseudonimizacja eliminują ryzyko realne).

EU-US Data Privacy Framework działa od lipca 2023 r. Pokrywa transfery do certyfikowanych podmiotów w USA, ale jest narzędziem słabszym niż wcześniejsze Privacy Shield. Schrems III w toku może DPF zakwestionować. Ostrożna strategia: DPF + zaplanowane fallback SCC + środki uzupełniające jako redundancja.

SCC 2021 wymagają kompletnego wypełnienia trzech załączników (I.A, I.B, II). Najczęstszy błąd: załączniki puste lub generyczne. To natychmiast widoczne w audycie.

TIA jest najtrudniejszym elementem audytu. Wymaga analizy prawa, praktyki i kontekstu konkretnego transferu. TIA wykonana powierzchownie ("USA = OK") jest gorsza niż brak TIA — bo daje fałszywe poczucie zgodności.

Środki uzupełniające: trzy kategorie (techniczne, kontraktowe, organizacyjne). Najmocniejsze są techniczne — szyfrowanie z kluczami w UE, pseudonimizacja, podział danych. Środki kontraktowe są słabe (dostawca może być prawnie zmuszony do ukrycia faktów). Audytor szuka konkretnych środków, nie deklaracji.

Mapa transferów jako output audytu jest jednocześnie narzędziem decyzyjnym dla zarządu i dowodem zgodności dla UODO. Bez mapy nie da się ani świadomie zarządzać ryzykiem, ani efektywnie odpowiadać na kontrole.

W 2026 r. transfer do USA przez ChatGPT, Claude, Copilot jest coraz częstszym tematem audytów. Dane wrażliwe w promptach AI to obszar, gdzie wiele firm jest w stanie nieświadomej niezgodności — i gdzie pierwsze decyzje UODO są kwestią czasu.

---

<ul>
<li>Rozporządzenie Parlamentu Europejskiego i Rady (UE) 2016/679 z dnia 27 kwietnia 2016 r. (RODO), Rozdział V (art. 44–50) — Przekazywanie danych osobowych do państw trzecich. https://eur-lex.europa.eu/eli/reg/2016/679/oj</li>
<li>Wyrok TSUE z dnia 16 lipca 2020 r. w sprawie C-311/18 (Schrems II). https://curia.europa.eu/juris/document/document.jsf?docid=228677</li>
<li>Decyzja Wykonawcza Komisji (UE) 2021/914 z dnia 4 czerwca 2021 r. w sprawie standardowych klauzul umownych dotyczących przekazywania danych osobowych do państw trzecich. https://eur-lex.europa.eu/eli/dec_impl/2021/914/oj</li>
<li>Decyzja Wykonawcza Komisji (UE) 2023/1795 z dnia 10 lipca 2023 r. w sprawie odpowiedniego stopnia ochrony danych osobowych w ramach EU-US Data Privacy Framework. https://eur-lex.europa.eu/eli/dec_impl/2023/1795/oj</li>
<li>EROD (2021). <em>Recommendations 01/2020 on measures that supplement transfer tools to ensure compliance with the EU level of protection of personal data</em>, version 2.0. https://www.edpb.europa.eu/our-work-tools/our-documents/recommendations/</li>
<li>EROD (2022). <em>Guidelines 05/2021 on the Interplay between the application of Article 3 and the provisions on international transfers as per Chapter V of the GDPR</em>. https://www.edpb.europa.eu/</li>
<li>U.S. Department of Commerce. <em>EU-US Data Privacy Framework Program</em>. https://www.dataprivacyframework.gov/</li>
<li>UODO. <em>Wytyczne w sprawie międzynarodowego przekazywania danych osobowych</em>. https://uodo.gov.pl/pl/138</li>
<li>European Commission. <em>Adequacy decisions — list of countries</em>. https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/adequacy-decisions_en</li>
<li>noyb (European Center for Digital Rights). <em>Resources on Schrems II implementation</em>. https://noyb.eu/en</li>
</ul>
