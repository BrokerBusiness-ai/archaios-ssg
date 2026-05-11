---
title: "Raportowanie incydentów NIS2 — protokół 24/72h krok po kroku"
slug: "raportowanie-incydentow-24-72h-protokol"
excerpt: "Trójstopniowy protokół raportowania: 24h wczesne ostrzeżenie, 72h powiadomienie, 30 dni sprawozdanie. Kto, do kogo, jakim formularzem, co dokładnie napisać."
category_slug: "wdrozenia-nis2"
tags: "NIS2, incydenty, raportowanie, CSIRT NASK, procedura, średni"
reading_time: 12
is_published: true
is_featured: false
meta_title: "Raportowanie incydentów NIS2 — protokół 24/72h (przewodnik 2026)"
meta_description: "Trójstopniowy protokół raportowania incydentów NIS2: 24h, 72h, 30 dni. Wzory zgłoszeń, kontakt z CSIRT NASK, kary za zaniedbanie."
funnel: "MOFU"
author_slug: "marek-porycki"
related_slugs: "nis2-checklista-gotowosci-10-obszarow, kogo-obowiazuje-nis2-w-polsce, nis1-vs-nis2-co-sie-zmienilo"
product_slugs: ""
---

W cyberbezpieczeństwie czas reakcji decyduje o skali strat. Atakujący w sieci średnio przebywa 277 dni przed wykryciem (IBM Cost of a Data Breach Report 2023), a od momentu wykrycia do skutecznej reakcji mija średnio kolejne 73 dni. NIS2 atakuje te liczby od strony regulacyjnej — wprowadza obowiązek bardzo szybkiego raportowania, co pośrednio wymusza istnienie procedur wykrywania i reakcji.

Trójstopniowy protokół raportowania incydentów (artykuł 23 dyrektywy 2022/2555) to jeden z najbardziej operacyjnych obszarów NIS2. Inne wymagania można odraczać — szkolenia, polityki, audyty można rozłożyć w czasie. Raportowanie incydentów musi działać natychmiast, bo pierwszy poważny incydent ujawni jakość Twojego systemu.

Ten tekst opisuje protokół krok po kroku: kiedy zaczyna płynąć czas, co dokładnie napisać w każdym z trzech raportów, kto w firmie odpowiada, jaką formą kontaktować się z CSIRT NASK, jakie są kary za zaniechanie. Zawiera również wzory komunikatów i listy kontrolne.

## Kiedy incydent jest "istotny"

Pierwsza decyzja: czy zdarzenie wymaga zgłoszenia do CSIRT NASK. Nie każda anomalia w sieci, nie każdy phishing skierowany do pracownika, nie każda chwilowa niedostępność systemu. Dyrektywa NIS2 (artykuł 23 ust. 3) definiuje incydent istotny przez dwa kryteria.

Kryterium A — wpływ na świadczenie usługi: incydent powoduje lub może spowodować poważne zakłócenia operacyjne usług lub straty finansowe dla danego podmiotu.

Kryterium B — wpływ na podmioty trzecie: incydent wpływa lub może wpłynąć na inne osoby fizyczne lub prawne, powodując znaczne szkody materialne lub niematerialne.

Wystarczy spełnienie jednego z dwóch kryteriów, żeby incydent był istotny.

W praktyce: ransomware, który zaszyfrował dwa stanowiska księgowe, wstrzymał wystawianie faktur na 6 godzin — istotny (kryterium A: zakłócenie operacyjne). Wyciek bazy 5 000 adresów email klientów — istotny (kryterium B: szkoda dla osób trzecich). DDoS, który przez 30 minut spowolnił sklep internetowy — w zależności od skali firmy, prawdopodobnie istotny dla średniego sklepu, nieistotny dla giganta. Skuteczny phishing, który przejął jedno konto pracownika operacyjnego — w zależności od dostępów tego konta, najczęściej istotny.

Próg istotności jest niższy niż pod NIS1. Większość firm w fazie wdrożenia myli się w przeciwnym kierunku — uznają incydenty za nieistotne, podczas gdy z perspektywy regulatora są istotne. Bezpieczna strategia: w wątpliwości raportować. Podmiot nie ponosi sankcji za nadmiarowe raportowanie; ponosi za zaniechanie.

CSIRT NASK ma narzędzie konsultacyjne dla podmiotów rejestrowanych — można skonsultować klasyfikację incydentu telefonicznie. W praktyce odpowiedzi są zwykle udzielane w ciągu 2–4 godzin.

## Etap 1: Wczesne ostrzeżenie (24 godziny)

Termin: 24 godziny od momentu, w którym podmiot stwierdza, że incydent jest istotny. Nie od momentu, kiedy incydent się rozpoczął — od momentu identyfikacji jego istotności.

Co należy zawrzeć (artykuł 23 ust. 4 lit. a):
- wskazanie czy incydent może być spowodowany działaniem niezgodnym z prawem lub o charakterze złośliwym;
- wskazanie czy incydent może mieć wpływ transgraniczny;
- wstępne informacje o naturze zdarzenia (ransomware? wyciek danych? DDoS? naruszenie poufności?).

Cel wczesnego ostrzeżenia jest jasny: dać CSIRT NASK i ENISA możliwość wczesnej koordynacji, jeśli atak jest kampanią obejmującą wiele podmiotów. W 2024 roku kampania ataków na polski sektor logistyczny została zidentyfikowana jako koordynowana właśnie dzięki wczesnym ostrzeżeniom z trzech niezależnych firm.

Kanał zgłoszenia: portal CSIRT NASK (https://incydent.cert.pl), telefon dyżurny (24/7), email zarejestrowany podczas rejestracji w systemie. W przypadku pilnym — telefon zawsze najszybszy.

Wzór wczesnego ostrzeżenia (treść około 200–400 słów):

> Niniejszym, jako [nazwa podmiotu], [NIP], zgłaszamy wczesne ostrzeżenie zgodnie z art. 23 ust. 4 lit. a dyrektywy NIS2 i odpowiednimi przepisami ustawy o krajowym systemie cyberbezpieczeństwa. W dniu [data] o godzinie [czas] stwierdziliśmy istotny incydent cyberbezpieczeństwa. Wstępna ocena: [typ incydentu — ransomware / wyciek danych / nieautoryzowany dostęp / DDoS / inne]. Możliwe pochodzenie złośliwe: [tak/nie/nieustalone]. Możliwy wpływ transgraniczny: [tak/nie/nieustalone — uzasadnienie]. Wstępna ocena zakresu: [systemy dotknięte, szacunkowa liczba osób dotkniętych, szacunkowy zakres danych]. Zespół reagowania: [imiona, role]. Kontakt do osoby odpowiedzialnej: [imię, nazwisko, telefon, email]. Bardziej szczegółowe powiadomienie zostanie przekazane w terminie 72 godzin.

Co NIE musi być w wczesnym ostrzeżeniu: pełna analiza techniczna, identyfikacja wektora ataku, decyzja o powiadomieniu osób trzecich, dokładne liczby. Wystarczy ramowa diagnoza.

## Etap 2: Powiadomienie (72 godziny)

Termin: 72 godziny od momentu identyfikacji istotności incydentu. To rozszerzenie wczesnego ostrzeżenia o pełniejsze informacje.

Co należy zawrzeć (artykuł 23 ust. 4 lit. b):
- aktualizacja informacji z wczesnego ostrzeżenia;
- wstępna ocena incydentu, w tym jego dotkliwości i wpływu;
- jeśli dostępne — wskaźniki kompromitacji (IOCs).

W praktyce powiadomienie po 72 godzinach powinno odpowiadać na pytania: co dokładnie się stało, jaka jest skala, jakie dane są dotknięte, jakie systemy są niedostępne, kogo to dotyczy, co już zostało zrobione, jakie są następne kroki.

Wzór powiadomienia (treść około 600–1200 słów, struktura obowiązkowa):

> 1. Identyfikacja podmiotu (powtórzenie z wczesnego ostrzeżenia).
> 2. Aktualizacja informacji z wczesnego ostrzeżenia: [co potwierdzone, co zmienione].
> 3. Opis zdarzenia: oś czasu (kiedy zaczął się incydent / kiedy wykryty / kiedy uznany za istotny / co działo się w międzyczasie), wektor wejścia (jeśli ustalony), zakres systemów dotkniętych, zakres danych dotkniętych.
> 4. Ocena dotkliwości: liczba użytkowników/klientów dotkniętych, charakter danych dotkniętych (osobowe / finansowe / strategiczne / inne), szacunkowe straty finansowe, czas niedostępności usługi.
> 5. Wpływ na osoby trzecie: czy wymaga powiadomienia osób fizycznych zgodnie z RODO, czy wymaga powiadomienia partnerów biznesowych, czy istnieje ryzyko transgraniczne.
> 6. Wskaźniki kompromitacji (IOCs) — jeśli dostępne: adresy IP atakujące, hashe plików złośliwych, domeny C2, sygnatury, użyte luki (CVE), techniki MITRE ATT&CK.
> 7. Działania podjęte: izolacja, neutralizacja, odzyskiwanie, komunikacja wewnętrzna, komunikacja zewnętrzna.
> 8. Plan dalszych działań: kolejne kroki techniczne, harmonogram odzyskiwania, plan komunikacji.
> 9. Zaangażowane podmioty zewnętrzne: firma reagowania na incydenty, zewnętrzni audytorzy, ubezpieczyciel cyber, organy ścigania (jeśli zaangażowane).
> 10. Kontakt: osoba odpowiedzialna, dyżur 24/7 (jeśli istnieje).

Powiadomienie po 72 godzinach jest dokumentem operacyjnym, który CSIRT NASK wykorzystuje do oceny, czy incydent wymaga rozszerzonego wsparcia, koordynacji międzysektorowej, eskalacji do ENISA. To również moment, w którym formalnie aktywuje się obowiązek współpracy z organem.

## Etap 3: Sprawozdanie końcowe (1 miesiąc)

Termin: maksymalnie miesiąc od momentu powiadomienia. Jeśli incydent w tym czasie nie został zakończony — sprawozdanie pośrednie z opisem postępu i terminem sprawozdania końcowego.

Co należy zawrzeć (artykuł 23 ust. 4 lit. c):
- szczegółowy opis incydentu, w tym jego dotkliwości i skutków;
- rodzaj zagrożenia lub przyczyny źródłowe, które prawdopodobnie wywołały incydent;
- zastosowane i podejmowane środki łagodzące;
- ewentualnie — wpływ transgraniczny incydentu.

Sprawozdanie końcowe to dokument analityczny. Cel: udokumentowanie nauki organizacyjnej i wspólnej wiedzy sektorowej.

Struktura sprawozdania końcowego (typowo 3 000–8 000 słów):

> 1. Streszczenie wykonawcze — 1 strona.
> 2. Pełna oś czasu incydentu — od pierwszego znaku kompromitacji do zakończenia odzyskiwania.
> 3. Analiza wektora ataku — jak dokładnie atakujący wszedł.
> 4. Analiza eskalacji — jak atakujący poruszał się w sieci.
> 5. Analiza ekstrakcji — co i jak wyniesione (jeśli wyciek).
> 6. Analiza przyczyn źródłowych (root cause analysis) — dlaczego incydent stał się możliwy. To centralna część sprawozdania.
> 7. Skutki: finansowe (koszty bezpośrednie, koszty pośrednie, utracone przychody, koszty komunikacji, koszty prawne), operacyjne (godziny niedostępności usługi, wpływ na klientów), reputacyjne (jeśli incydent stał się publiczny), regulacyjne (jeśli wszczęte postępowania).
> 8. Działania naprawcze: techniczne (co zostało zmienione w infrastrukturze), proceduralne (jakie procedury zaktualizowano), organizacyjne (jakie zmiany w strukturze).
> 9. Działania prewencyjne: jakie środki wdrożone, żeby zapobiec podobnym incydentom.
> 10. Lekcje wyciągnięte: co organizacja nauczyła się o sobie, swoich procesach, swoich dostawcach.
> 11. Zaktualizowane wskaźniki ryzyka — jak ten incydent zmienia ocenę ryzyka.

Sprawozdania końcowe są ważne nie tylko regulacyjnie. To najlepsza dokumentacja postincydentu dla wewnętrznych potrzeb (szkoleń, ubezpieczyciela, audytorów). Często firmy traktują je jako biurokratyczny obowiązek. Lepsze podejście: traktować je jako materiał ekspercki, który wzmocni zespół i przygotuje firmę na podobne sytuacje w przyszłości.

## Kto w firmie odpowiada za raportowanie

NIS2 nie wymaga jednoosobowego stanowiska odpowiedzialnego za raportowanie incydentów, ale wymaga jasno zdefiniowanej odpowiedzialności. W większości firm rola jest podzielona:

Pierwsza linia — zespół IT/security: wykrywa incydent, prowadzi pierwszą reakcję techniczną, zbiera dane techniczne. Często osoba dyżurna lub on-call.

Druga linia — Cybersecurity Officer / koordynator bezpieczeństwa: ocenia istotność incydentu, decyduje o uruchomieniu protokołu raportowania, koordynuje pracę między działami, przygotowuje treści raportów.

Trzecia linia — zarząd: zatwierdza decyzję o raportowaniu, odpowiada za komunikację z mediami i klientami (jeśli incydent jest publiczny), podpisuje sprawozdania.

Wsparcie: dział prawny (ocena ryzyka regulacyjnego), dział PR/komunikacji (plan komunikacyjny), HR (jeśli incydent dotyczy pracowników).

Procedura wewnętrzna powinna mieć jasno zdefiniowane: kogo budzi się o 3 nad ranem, kto ma uprawnienia do uruchomienia protokołu raportowania bez konsultacji z zarządem (zazwyczaj Cybersecurity Officer), kto może podejmować decyzje o izolacji systemów, kto jest pierwszą osobą kontaktową dla CSIRT NASK.

W firmie 60-osobowej te role mogą być łączone. Zazwyczaj: kierownik IT pełni jednocześnie funkcję Cybersecurity Officera i pierwszej linii. Zarząd reprezentuje członek odpowiedzialny za operacje. Łącznie 2–3 osoby na pełnej procedurze. W większych firmach — bardziej rozdzielone.

## Sankcje za zaniechanie raportowania

NIS2 nie traktuje opóźnienia w raportowaniu jako drobne uchybienie. Artykuł 34 dyrektywy stanowi, że niedopełnienie obowiązków raportowania może być przedmiotem maksymalnych kar — do 10 mln EUR lub 2% globalnego obrotu dla podmiotów kluczowych.

Praktyczne podejście organów nadzoru w UE (na podstawie pierwszych precedensów z 2024–2025): kary za opóźnienie do 7 dni, jeśli incydent ostatecznie był zgłoszony — zwykle pouczenie lub niewielka grzywna. Kary za zatajenie incydentu lub świadome opóźnienie powyżej 30 dni — zwykle wysokie kary, szczególnie jeśli okazało się, że incydent mógłby być prewencyjnie zidentyfikowany przez inne podmioty, gdyby zgłoszenie nastąpiło w terminie.

Najgorsze konsekwencje są nie regulacyjne, lecz reputacyjne. Incydent, który wychodzi do publicznej wiadomości po fakcie, jest dla firmy znacznie bardziej destrukcyjny niż incydent komunikowany proaktywnie. Ataki ransomware z 2024 roku, w których firmy zwlekały z komunikacją, miały trzy razy wyższy spadek wartości giełdowej niż firmy, które komunikowały otwarcie od pierwszych godzin (analiza Verizon DBIR 2024).

## Lista kontrolna gotowości procedury raportowania

Sprawdź, czy w Twojej firmie istnieje:

1. Pisemna procedura raportowania incydentów z trzema etapami i konkretnymi terminami.
2. Lista osób odpowiedzialnych z ich kontaktami 24/7.
3. Aktywna rejestracja w systemie CSIRT NASK z aktualnym kontaktem (telefon dyżurny, email).
4. Wzory raportów wczesnego ostrzeżenia, powiadomienia 72h i sprawozdania końcowego (gotowe szablony).
5. Procedura klasyfikacji istotności incydentu z konkretnymi przykładami.
6. Procedura komunikacji wewnętrznej (kto kogo informuje, w jakiej kolejności, jakimi kanałami).
7. Procedura komunikacji zewnętrznej (klienci, partnerzy, media).
8. Lista współpracujących podmiotów zewnętrznych (firma incident response, ubezpieczyciel, kancelaria prawna specjalizująca się w cyber).
9. Coroczny ćwiczebny test procedury (tabletop exercise lub symulacja).
10. Aktualizacja procedury po każdym istotnym incydencie z lessons learned.

Brak któregoś z tych elementów = realne ryzyko awarii procedury w momencie pierwszego incydentu.

## Bibliografia

<ul>
<li>Komisja Europejska. (2022). <em>Dyrektywa Parlamentu Europejskiego i Rady (UE) 2022/2555 z dnia 14 grudnia 2022 r. (NIS2)</em> — art. 23 (raportowanie incydentów). <a href="https://eur-lex.europa.eu/legal-content/PL/TXT/?uri=CELEX:32022L2555">https://eur-lex.europa.eu/legal-content/PL/TXT/?uri=CELEX:32022L2555</a></li>
<li>IBM Security. (2023). <em>Cost of a Data Breach Report 2023</em>. IBM Corporation. <a href="https://www.ibm.com/reports/data-breach">https://www.ibm.com/reports/data-breach</a></li>
<li>Verizon. (2024). <em>2024 Data Breach Investigations Report</em>. Verizon Business. <a href="https://www.verizon.com/business/resources/reports/dbir/">https://www.verizon.com/business/resources/reports/dbir/</a></li>
<li>CSIRT NASK. (2024). <em>Procedura zgłaszania incydentów istotnych zgodnie z NIS2</em>. NASK PIB. [DO WERYFIKACJI URL]</li>
<li>ENISA. (2023). <em>Incident Notification under NIS2: Guidelines for CSIRTs</em>. European Union Agency for Cybersecurity. [DO WERYFIKACJI URL]</li>
<li>MITRE Corporation. (2024). <em>MITRE ATT&CK Framework v15</em>. <a href="https://attack.mitre.org/">https://attack.mitre.org/</a></li>
</ul>

---

**Pierwszy poważny incydent ujawni jakość Twojej procedury.** W cotygodniowym newsletterze TestNIS2.pl publikujemy gotowe szablony zgłoszeń, scenariusze ćwiczeń tabletop i analizy realnych incydentów polskich firm. [Zapisz się — bezpłatnie](#newsletter-signup).
