---
title: "Audyt incydentów 24/72h — procedura reagowania, RODO + NIS2 zharmonizowane (cornerstone)"
slug: "audyt-incydentow-24-72h-rodo-nis2"
excerpt: "RODO art. 33 i NIS2 art. 23 wymagają zgłoszenia incydentu w różnych reżimach. Jeden incydent może wymagać obu zgłoszeń. Pełna metodyka audytu zdolności reagowania w obu reżimach."
category_slug: "audyt-nis2-skanuj"
tags: "incydenty, RODO art. 33, NIS2 art. 23, 24h, 72h, CSIRT, UODO, cornerstone, zaawansowany"
reading_time: 18
is_published: true
is_featured: true
meta_title: "Audyt incydentów 24/72h — RODO + NIS2 zharmonizowane (cornerstone 2026)"
meta_description: "Jeden incydent, dwa reżimy zgłaszania. Pełna metodyka audytu procedury reagowania RODO art. 33 + NIS2 art. 23. Procesy, dowody, klasyfikacje, testy."
funnel: "MOFU-cornerstone"
author_slug: "marek-porycki"
related_slugs: "audyt-nis2-art-21-krok-po-kroku-metodologia-audytora,audyt-rodo-art-32-bezpieczenstwo-techniczne,audyt-ciaglosci-dzialania-bcp-dr-nis2,dpia-w-praktyce-kiedy-obowiazuje-jak-wykonac,raport-audytowy-dla-zarzadu-jak-go-napisac"
product_slugs: ""
---

W 2026 roku polska średnia firma stała w punkcie, w którym jeden poważny incydent cyberbezpieczeństwa może aktywować trzy odrębne ścieżki obowiązkowego zgłaszania: do UODO w terminie 72 godzin (RODO art. 33), do polskiego CSIRT-u w terminach 24h/72h/1 miesiąc (NIS2 art. 23, jeśli firma jest podmiotem kluczowym lub istotnym) oraz potencjalnie do regulatorów sektorowych (KNF, URE, UKE, MZ). Trzy reżimy, trzy zakresy informacji, trzy timing'i, trzy formaty. Wszystko w sytuacji, gdy zarząd firmy próbuje jeszcze zrozumieć, co się stało.

Audyt zdolności reagowania na incydenty jest cornerstone'm w audycie holistycznym, bo łączy ze sobą obszary, które na papierze są odrębne: bezpieczeństwo (NIS2 art. 21(2)(b)), ciągłość działania (NIS2 art. 21(2)(c)), zarządzanie ryzykiem (RODO art. 32), procedury zgłaszania (RODO art. 33 + NIS2 art. 23). W rzeczywistości operacyjnej są jednym pipeline'em, którego nie da się ocenić w częściach.

Ten tekst jest pełną metodyką audytu zharmonizowanego pipeline'u incydentowego. Pokazuje, jak audytor weryfikuje gotowość firmy do obsłużenia incydentu kompleksowo — od wykrycia, przez klasyfikację (czy jest naruszeniem RODO, czy podlega NIS2, czy oba), procedury eskalacji, zgłoszenia regulatorom, komunikację z poszkodowanymi, dokumentację post-incident. Adresat: audytorzy wewnętrzni i zewnętrzni, CISO, IOD, członkowie zarządu odpowiedzialni za ryzyko operacyjne.

## Dwa reżimy zgłaszania — co i kiedy

**RODO art. 33 — zgłoszenie do UODO.** Termin: 72 godziny od stwierdzenia naruszenia. Próg: każde naruszenie ochrony danych, chyba że jest mało prawdopodobne, aby skutkowało ryzykiem naruszenia praw lub wolności osób fizycznych. Format: formularz UODO + opis incydentu, kategorii danych, liczby poszkodowanych, prawdopodobnych konsekwencji, środków zaradczych.

**RODO art. 34 — komunikacja z poszkodowanymi.** Termin: bez zbędnej zwłoki, jeśli naruszenie powoduje wysokie ryzyko. Format: jasna, prosta informacja w języku zrozumiałym, z opisem konsekwencji i działań.

**NIS2 art. 23 — zgłoszenie do CSIRT-u.** Trzy terminy kaskadowe:
- 24 godziny: wczesne ostrzeżenie (early warning) z podstawowymi informacjami o tym, że nastąpił poważny incydent
- 72 godziny: zgłoszenie incydentu z bardziej szczegółową oceną i zaktualizowaną informacją
- 1 miesiąc: raport końcowy z opisem przyczyn źródłowych, środków łagodzących i lessons learned

W Polsce zgłoszenia trafiają do właściwego CSIRT-u sektorowego (zwykle CSIRT NASK dla większości sektorów, CSIRT GOV.PL dla podmiotów publicznych, CSIRT MON dla sektora obronnego, sektorowe CSIRT-y dla finansów, energii, transportu).

**Kluczowa pułapka.** Jeden incydent może aktywować oba reżimy. Ransomware na bazę klientów to: (a) naruszenie ochrony danych osobowych — RODO art. 33, (b) poważny incydent cyberbezpieczeństwa — NIS2 art. 23. Firma musi w 24 godziny zgłosić CSIRT (NIS2 early warning), w 72 godziny zgłosić UODO i zaktualizować CSIRT, w miesiąc dosłać raport końcowy do CSIRT. Trzy odrębne dokumenty, trzy odrębne narracje, ale wszystko z tego samego zespołu pracującego pod presją.

Audyt sprawdza, czy firma to wszystko rozumie i ma procedury obsłużenia kaskady terminów.

## Klasyfikacja incydentu — pierwszy test audytu

Pierwszy test, jaki wykonuje audytor: czy firma ma jasne kryteria klasyfikacji incydentu. Bez tego — każda decyzja eskalacyjna jest improwizacją.

**Kryteria RODO** (czy jest "naruszenie ochrony danych osobowych" w rozumieniu art. 4 pkt 12):

- Naruszenie poufności: nieuprawniony dostęp lub ujawnienie
- Naruszenie integralności: nieuprawniona modyfikacja
- Naruszenie dostępności: utrata, zniszczenie, niedostępność

Każdy z trzech wymaga oceny: czy generuje ryzyko dla praw i wolności osób fizycznych. Skala oceny zwykle 3-poziomowa: brak ryzyka (nie zgłaszamy), ryzyko (zgłaszamy UODO), wysokie ryzyko (zgłaszamy UODO + informujemy poszkodowanych).

**Kryteria NIS2** (czy jest "poważny incydent" w rozumieniu dyrektywy):

Według art. 23 ust. 3 — incydent jest poważny, jeśli:
- spowodował poważne zakłócenie operacyjne usług lub straty finansowe dla podmiotu, lub
- wpłynął lub może wpłynąć na inne osoby fizyczne lub prawne przez powodowanie znaczących szkód materialnych lub niematerialnych

Rozporządzenie wykonawcze KE (2024/2690) doprecyzowuje progi dla różnych sektorów. Dla średniej firmy z sektora cyfrowego "poważny" zaczyna się typowo przy: utracie dostępności usługi krytycznej na ponad 1 godzinę, ekspozycji danych wrażliwych powyżej 1000 rekordów, ataku ransomware z paraliżem operacyjnym, naruszeniu integralności systemu krytycznego.

**Co audytor sprawdza.** Czy firma ma udokumentowaną matrycę klasyfikacji łączącą oba reżimy. Idealny format:

| Scenariusz | RODO art. 33? | NIS2 art. 23? | Działania |
|---|---|---|---|
| Ransomware bez ujawnienia danych | NIE (brak naruszenia danych) | TAK (zakłócenie operacyjne) | NIS2 CSIRT 24h + dokumentacja |
| Phishing z eksfiltracją 5000 rekordów | TAK | TAK (jeśli podmiot kluczowy/istotny) | RODO UODO 72h + NIS2 CSIRT 24h + informacja osób |
| DDoS bez ujawnienia danych | NIE | TAK (jeśli utrata dostępności) | NIS2 CSIRT 24h |
| Błąd konfiguracji ujawnia 50 rekordów | TAK (potencjalne ryzyko) | NIE (zwykle nie spełnia progu poważnego) | RODO UODO 72h |
| Insider eksfiltrował 1 plik z 3 rekordami | TAK | NIE | RODO UODO 72h (zwykle bez powiadamiania osób) |
| Wyciek MFA tokenów administratora | TAK (potencjalne) | TAK (jeśli krytyczny dostęp) | Oba reżimy |

Bez takiej matrycy zespoły improwizują pod presją czasu — i albo zgłaszają nadmiarowo (generując niepotrzebne procedury kontrolne), albo nie zgłaszają obowiązkowych incydentów.

## Procedura reagowania — siedem faz

Audytor weryfikuje pełen cykl reagowania w siedmiu fazach. Dla każdej fazy: dowody (dokumenty, raporty PIR), wywiady (z osobami z zespołu reagowania), testy techniczne (tabletop exercise).

**Faza 1: Wykrycie.** Skąd firma wie, że jest incydent? Źródła: monitoring (SIEM, EDR, IDS/IPS), alerty użytkowników, alerty zewnętrzne (CSIRT, dostawcy, klienci), audyty post-fakto. Audyt sprawdza średni MTTD (Mean Time To Detect) — dla incydentów wykrytych w 12 miesiącach. Cel: minuty, nie godziny. Branża pokazuje, że MTTD w średnich firmach polskich jest zwykle 8–96 godzin, co jest poniżej standardu 2026.

**Faza 2: Triage i klasyfikacja.** Co to za incydent? Jaka kategoria, jaki poziom, jakie reżimy? Audyt sprawdza: dokumentacja matrycy klasyfikacji, lista osób uprawnionych do klasyfikacji, czas od wykrycia do klasyfikacji. Cel: 1–4 godziny.

**Faza 3: Powiadomienie wewnętrzne.** Kto musi wiedzieć? Zarząd, IOD, prawni, IT, komunikacja, ubezpieczyciel, zewnętrzny SOC/forensik. Audyt sprawdza: lista kontaktów z aktualną kompletnością, kanały komunikacji (poza tym, który może być skompromitowany — np. e-mail firmowy w przypadku ransomware), procedury eskalacyjne dla nocy/weekendów.

**Faza 4: Kontener i mitigacja.** Powstrzymanie rozprzestrzeniania. Audyt sprawdza: runbooki dla typowych scenariuszy, lista decyzji odwracalnych vs. nieodwracalnych (czy zespół wie, że odpięcie serwerów może zniszczyć dowody forensykowe), procedury komunikacji z forensykami zewnętrznymi.

**Faza 5: Zgłoszenia regulatorom.** RODO art. 33 (UODO 72h), NIS2 art. 23 (CSIRT 24h/72h/1m), regulatorzy sektorowi. Audyt sprawdza: szablony zgłoszeń, lista kontaktów regulatorów, procedury akceptacji treści zgłoszenia (kto podpisuje), retencja dokumentacji zgłoszeń.

**Faza 6: Komunikacja zewnętrzna.** Poszkodowani (art. 34 RODO), klienci, partnerzy, media, akcjonariusze. Audyt sprawdza: szablony komunikatów, plan PR/IR, decyzje kto kogo informuje i w jakiej kolejności.

**Faza 7: Post-incident review (PIR).** Co się stało, co działało, co nie, co zmienić. Audyt sprawdza: PIR-y z ostatnich 12 miesięcy, lista action items z PIR-ów, status ich realizacji.

## Symulacja stołowa — kluczowy test audytu

Audytor nie ocenia gotowości firmy tylko z dokumentów. Najlepszy test to symulacja stołowa (tabletop exercise) — prowadzi scenariusz, obserwuje, jak zespół reaguje.

Typowy scenariusz dla średniej firmy:

> **10 maja 2026, godzina 02:14.** Monitoring SOC zgłasza alert: 80 stacji w dziale księgowości oraz serwer plików F:\KSIEGOWOSC są zaszyfrowane. W każdej zaszyfrowanej lokalizacji notatka: "Twoje pliki zostały zaszyfrowane. Aby je odzyskać, skontaktuj się z [email_address] w ciągu 72 godzin. Cena: 800 000 EUR w bitcoin. Niezapłacenie skutkuje publikacją danych. Mamy 47 GB danych z systemu kadrowego, finansowego oraz bazy klientów (12 400 osób)".
>
> Pytania symulacyjne:
>
> 1. Kto jest powiadamiany w ciągu pierwszej godziny? W jakiej kolejności? Jakimi kanałami?
> 2. Kto decyduje, czy zapłacić okup?
> 3. Czy zgłaszamy do UODO? Kiedy? Kto przygotowuje treść?
> 4. Czy zgłaszamy do CSIRT? Kiedy?
> 5. Czy odpinamy zaszyfrowane stacje od sieci, czy zostawiamy dla forensyki?
> 6. Czy istnieje aktualny backup tych danych? Kiedy ostatnio testowany?
> 7. Czy zatrudniamy zewnętrznego forensyka? Mamy go zakontraktowanego prewencyjnie?
> 8. Co mówimy klientom? Kiedy? Kto pisze?
> 9. Czy informujemy media proaktywnie czy reaktywnie?
> 10. Co mówimy pracownikom? Kiedy?

Audytor obserwuje przez 2–3 godziny dyskusję zespołu (członkowie zarządu, CISO, IOD, dyrektor IT, dyrektor komunikacji, prawnik). Z dyskusji wynika ocena dojrzałości w obszarze reagowania.

**Częste obserwacje z takich symulacji w polskich firmach.**
- Pierwsze 60 minut traci się na ustalanie, kto kogo powiadomi. Lista kontaktów jest, ale w intranecie do którego nie ma dostępu z domu.
- Decyzja "czy zapłacić" wisi w powietrzu, bo nie ma jasnej linii w zarządzie.
- IOD jest informowany "po sprawie", a powinien być w godzinie 1.
- Nie ma pewności, czy backup pomoże, bo nie był testowany od 18 miesięcy.
- Komunikacja z klientami jest improwizowana, bo nie ma szablonu.
- Forensik jest "tym, którego kiedyś znaliśmy", nie aktualnym partnerem.

Każda z tych obserwacji jest ustaleniem audytowym z jasną rekomendacją korygującą.

## Format zgłoszenia do UODO (art. 33)

UODO udostępnia formularz online. Audytor sprawdza, czy firma ma wewnętrzny szablon przygotowany, gotowy do wypełnienia w trybie awaryjnym. Szablon zawiera:

- Dane administratora (nazwa, adres, NIP, kontakt do IOD)
- Data i godzina stwierdzenia naruszenia
- Charakter naruszenia (poufność / integralność / dostępność / kombinacja)
- Kategorie i przybliżona liczba podmiotów danych
- Kategorie i przybliżona liczba rekordów danych
- Prawdopodobne konsekwencje naruszenia
- Środki zastosowane lub proponowane w celu zminimalizowania ewentualnych negatywnych skutków
- Wskazanie, czy planowane jest poinformowanie osób (art. 34)

Tip dla audytu: w prawdziwym incydencie liczba poszkodowanych może być nieznana w 72h. RODO dopuszcza zgłoszenia uzupełnione — pierwsze zgłoszenie w 72h z dostępnymi informacjami, aktualizacja w kolejnych dniach. Zespół audytowy musi to wiedzieć, żeby nie odkładać zgłoszenia czekając na "pełną informację".

## Format zgłoszenia do CSIRT (NIS2 art. 23)

CSIRT (NASK lub sektorowy) ma własny portal zgłoszeniowy. Trzy formaty kaskadowe:

**Early warning (24h):** typowo 1–2 strony tekstu — co się stało, kiedy, jaki potencjalny wpływ, czy podejrzewa się działanie złośliwe, czy może mieć skutki transgraniczne.

**Zgłoszenie incydentu (72h):** rozszerzona ocena ze wstępną analizą przyczyn, wykazem dotkniętych systemów i usług, działań podjętych, działań planowanych.

**Raport końcowy (1 miesiąc):** pełna analiza root cause, lista wszystkich środków podjętych, lista lessons learned, plan korygujący długoterminowy.

Audytor sprawdza, czy firma ma szablony wszystkich trzech formatów oraz czy w zespole jest osoba odpowiedzialna za zewnętrzne komunikaty (kto pisze, kto akceptuje, kto wysyła).

Jeśli przygotowujesz lub odbierasz audyt gotowości incydentowej i potrzebujesz szablonu wszystkich tych dokumentów (zgłoszenia UODO + early warning CSIRT + zgłoszenie incydentu CSIRT + raport końcowy CSIRT + szablon komunikatu do poszkodowanych z art. 34), warto dołączyć do newslettera skanujfirme.pl — przesyłamy pakiet w DOCX z polami do uzupełnienia. To narzędzie minimalizuje ryzyko, że zespół pod presją zapomni o jakimś elemencie.

## Macierz dojrzałości pipeline'u incydentowego

Po przejściu wszystkich siedmiu faz audytor składa macierz oceny zharmonizowanego pipeline'u:

| Element pipeline'u | Aktualna dojrzałość | Cel | Luka |
|---|---|---|---|
| Matryca klasyfikacji RODO+NIS2 | 1 | 3 | 2 |
| Wykrycie (MTTD) | 2 | 3 | 1 |
| Triage i klasyfikacja | 1 | 3 | 2 |
| Powiadomienie wewnętrzne | 2 | 3 | 1 |
| Runbooki dla typowych scenariuszy | 1 | 3 | 2 |
| Szablony zgłoszeń UODO + CSIRT | 1 | 3 | 2 |
| Szablony komunikacji zewnętrznej | 1 | 3 | 2 |
| Symulacje (regularność, jakość) | 0 | 3 | 3 |
| PIR i implementacja lessons learned | 1 | 3 | 2 |

Macierz jest natychmiast czytelna dla zarządu — pokazuje priorytety inwestycyjne. Większość polskich firm średnich jest na poziomie 1 w większości elementów, z zerem w symulacjach.

## Format ustaleń w raporcie audytu pipeline'u incydentowego

Przykład typowego ustalenia:

> **Ustalenie INC-02 (klasyfikacja: krytyczne):** Firma nie ma szablonu zgłoszenia incydentu do CSIRT zgodnego z NIS2 art. 23 oraz nie ma listy kontaktów do właściwego CSIRT-u sektorowego. Termin 24h na early warning nie jest osiągalny przy istniejącym przygotowaniu.
>
> **Dowody:** (1) Wywiad z CISO i IOD — brak świadomości formatu i ścieżki CSIRT; (2) Brak szablonu w archiwum dokumentów; (3) Brak osoby wskazanej jako odpowiedzialnej za zgłoszenia NIS2.
>
> **Ryzyko prawne:** Naruszenie NIS2 art. 23 ust. 4. W przypadku poważnego incydentu — kara administracyjna do 10 mln EUR lub 2% obrotu (podmiot kluczowy) lub do 7 mln EUR lub 1,4% obrotu (podmiot istotny). Plus reputacyjna ekspozycja związana z niedotrzymaniem terminu komunikacji.
>
> **Rekomendacja korygująca:** (1) Identyfikacja właściwego CSIRT-u sektorowego (w 7 dni); (2) Przygotowanie szablonów early warning + zgłoszenie 72h + raport końcowy 1m (w 14 dni); (3) Wyznaczenie osoby odpowiedzialnej w organizacji (w 7 dni); (4) Tabletop exercise testujący ścieżkę w pełnym łańcuchu (w 30 dni). Odpowiedzialny: CISO + IOD wspólnie.

## Trzy pytania kontrolne dla zarządu przed audytem pipeline'u incydentowego

**Pierwsze.** Czy wiemy, na które reżimy (RODO, NIS2, sektorowe) podlegamy zgłaszaniu incydentów? Jeśli nie ma pewności, jakiekolwiek planowanie procedur jest spekulacją.

**Drugie.** Kiedy ostatnio przeprowadziliśmy tabletop exercise z pełnym łańcuchem reagowania? Jeśli odpowiedź to "nigdy" lub "tak dawno, że nie pamiętamy" — pipeline jest teoretyczny, niezweryfikowany.

**Trzecie.** Kto budzi członka zarządu o 3:00 w nocy? Konkretne imię i nazwisko, telefon prywatny. Bez tego ścieżka eskalacyjna ma dziurę w najgorszym momencie.

## Esencja

Pipeline reagowania na incydenty 2026 jest zharmonizowany między RODO art. 33 (zgłoszenie do UODO 72h + komunikacja z poszkodowanymi art. 34) a NIS2 art. 23 (zgłoszenie do CSIRT 24h/72h/1m). Jeden incydent może aktywować oba reżimy. Audyt sprawdza zdolność firmy do obsłużenia kaskady terminów pod presją.

Klasyfikacja incydentu jest punktem krytycznym. Bez matrycy łączącej oba reżimy zespoły improwizują, co skutkuje albo nadmiernymi zgłoszeniami (generującymi własne ryzyko), albo pominięciem obowiązkowego. Matryca musi być prosta, jasna, kompletna i znana zespołowi reagowania.

Siedem faz pipeline'u — wykrycie, triage, powiadomienie, kontener, zgłoszenia regulatorom, komunikacja zewnętrzna, PIR — wymaga różnych narzędzi i kompetencji. Audyt sprawdza każdą fazę osobno: dowody (dokumenty), wywiady (z zespołem), testy techniczne (tabletop exercise jako kluczowy test gotowości realnej).

Symulacja stołowa jest najlepszym testem audytu. W 2–3 godziny ujawnia luki, których dokumenty nie pokazują: kto budzi kogo o 3:00, czy lista kontaktów jest aktualna, czy IOD jest w pierwszej godzinie czy w trzeciej, czy decyzja o płatności okupu jest własnością konkretnego organu, czy backup jest faktycznie sprawny.

Szablony zgłoszeń (UODO + CSIRT trzy formaty + komunikat art. 34 RODO) muszą być gotowe przed incydentem, nie pisane pod presją. Pakiet szablonów + lista kontaktów regulatorów + matryca decyzyjna to minimum operacyjne, jakie audytor oczekuje.

Macierz dojrzałości pipeline'u — 9 elementów ocenianych w skali 0–5 — pokazuje zarządowi priorytety inwestycyjne. Większość polskich firm średnich jest dziś na poziomie 1 w większości elementów, z zerem w symulacjach. To jest największa systemowa luka 2026 — i prawdopodobnie najbardziej kosztowna, gdy zmieni się statystyka incydentów (statystyka, która od 2022 r. konsekwentnie idzie w górę zarówno globalnie, jak i w Polsce).

---

<ul>
<li>Rozporządzenie Parlamentu Europejskiego i Rady (UE) 2016/679 z dnia 27 kwietnia 2016 r. (RODO), art. 33 — Zgłaszanie naruszenia organowi nadzorczemu, art. 34 — Zawiadamianie osoby, której dane dotyczą. https://eur-lex.europa.eu/eli/reg/2016/679/oj</li>
<li>Dyrektywa Parlamentu Europejskiego i Rady (UE) 2022/2555 (NIS2), art. 23 — Obowiązki zgłaszania incydentów. https://eur-lex.europa.eu/eli/dir/2022/2555/oj</li>
<li>Rozporządzenie Wykonawcze Komisji (UE) 2024/2690 z dnia 17 października 2024 r. ustanawiające zasady stosowania dyrektywy (UE) 2022/2555 w odniesieniu do progów istotności dla incydentów. https://eur-lex.europa.eu/eli/reg_impl/2024/2690/oj</li>
<li>EROD/EDPB (2022). <em>Guidelines 9/2022 on personal data breach notification under GDPR</em>. https://www.edpb.europa.eu/our-work-tools/our-documents/guidelines/</li>
<li>EROD/EDPB (2021). <em>Guidelines 01/2021 on Examples regarding Personal Data Breach Notification</em>. https://www.edpb.europa.eu/</li>
<li>UODO. <em>Wytyczne w sprawie zgłaszania naruszeń ochrony danych osobowych — formularz i procedura</em>. https://uodo.gov.pl/pl/138/</li>
<li>NIST SP 800-61 Rev. 2 (2012). <em>Computer Security Incident Handling Guide</em>. National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-61r2</li>
<li>ENISA (2024). <em>Good Practices for Incident Reporting under NIS2</em>. European Union Agency for Cybersecurity. https://www.enisa.europa.eu/publications</li>
<li>CSIRT NASK / CERT Polska. <em>Procedury zgłaszania incydentów</em>. https://csirt.gov.pl/ oraz https://www.cert.pl/</li>
<li>Verizon (2024). <em>Data Breach Investigations Report (DBIR) 2024</em>. https://www.verizon.com/business/resources/reports/dbir/</li>
<li>Polska Ustawa z dnia 5 lipca 2018 r. o krajowym systemie cyberbezpieczeństwa (Dz.U. 2018 poz. 1560 ze zm.), wraz z projektem nowelizacji transponującej NIS2.</li>
</ul>
