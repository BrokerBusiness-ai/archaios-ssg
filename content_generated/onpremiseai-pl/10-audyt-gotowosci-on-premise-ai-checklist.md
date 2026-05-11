---
title: "Audyt gotowości firmy na on-premise AI — checklist 40 pytań"
slug: "audyt-gotowosci-on-premise-ai-checklist"
excerpt: "Konkretny self-audit gotowości firmy na wdrożenie AI on-premise. 40 pytań w pięciu obszarach. Punktacja, interpretacja, plan działań."
category_slug: "strategia-onprem"
tags: "audyt gotowości, on-premise AI, checklist, BOFU, początkujący"
reading_time: 12
is_published: true
is_featured: false
meta_title: "Self-audit gotowości na on-premise AI — 40 pytań (BOFU 2026)"
meta_description: "Self-audit gotowości firmy na on-premise AI. 40 pytań w 5 obszarach: strategia, kompetencje, infrastruktura, dane, governance."
funnel: "BOFU"
author_slug: "marek-porycki"
related_slugs: "ai-on-premise-w-2026-przewodnik, kiedy-chmura-kiedy-on-premise, koszt-on-premise-vs-chmura-tco"
product_slugs: ""
---

Wdrożenie AI on-premise to inwestycja 250 000-3 000 000 zł plus znaczące zaangażowanie organizacyjne. Decyzja "robimy to" wymaga uczciwej oceny gotowości firmy. Brak gotowości nie oznacza "nigdy" — oznacza "najpierw przygotuj fundamenty". Nieprzygotowane firmy często wdrażają i ponoszą porażkę po 12-18 miesiącach, marnując kapitał i kompromitując strategię AI w organizacji.

Ten tekst zawiera 40-pytaniowy self-audit gotowości w pięciu obszarach: strategia (8 pytań), kompetencje (8), infrastruktura (8), dane (8), governance (8). Każde pytanie ma punktację. Suma wskazuje, czy firma jest gotowa, częściowo gotowa, czy musi najpierw zbudować fundamenty.

Czas wykonania: 30-60 minut. Wymagana wiedza: dyrektor IT lub osoba z bliską znajomością infrastruktury, danych i procesów firmy.

## Sekcja 1: strategia (8 pytań, 16 punktów)

**Pytanie 1.** Czy zarząd ma jasną odpowiedź na pytanie "dlaczego on-premise, a nie chmura"?

- TAK, z konkretnymi argumentami: 2 pkt
- CZĘŚCIOWO — ogólne argumenty: 1 pkt
- NIE: 0 pkt

**Pytanie 2.** Czy zidentyfikowaliśmy konkretne use cases AI o wartości biznesowej?

- TAK — minimum 3 use cases z opisem ROI: 2 pkt
- CZĘŚCIOWO — pomysły bez kalkulacji ROI: 1 pkt
- NIE: 0 pkt

**Pytanie 3.** Czy mamy budżet zatwierdzony na 3-letni cykl wdrożenia (minimum 500 000 zł)?

- TAK: 2 pkt
- CZĘŚCIOWO — częściowy budżet: 1 pkt
- NIE: 0 pkt

**Pytanie 4.** Czy zarząd jest zaangażowany w decyzję (nie tylko delegował do IT)?

- TAK — regular sponsor zarządczy z czasem: 2 pkt
- CZĘŚCIOWO: 1 pkt
- NIE — zostawione IT: 0 pkt

**Pytanie 5.** Czy mamy realistyczne oczekiwania timeline (minimum 12-18 miesięcy do produkcji)?

- TAK — plan 12-18+ miesięcy: 2 pkt
- CZĘŚCIOWO — plan 6-12 miesięcy: 1 pkt
- NIE — oczekiwania 3-6 miesięcy: 0 pkt

**Pytanie 6.** Czy decyzja jest wynikiem analizy alternatyw (chmura, hybryda), nie ideologii?

- TAK — udokumentowana ewaluacja alternatyw: 2 pkt
- CZĘŚCIOWO: 1 pkt
- NIE — decyzja bez analizy: 0 pkt

**Pytanie 7.** Czy wybór jest zgodny z compliance requirements (RODO, NIS2, AI Act, sektorowe)?

- TAK — udokumentowana analiza compliance: 2 pkt
- CZĘŚCIOWO: 1 pkt
- NIE / niewiadomo: 0 pkt

**Pytanie 8.** Czy mamy plan komunikacji wewnętrznej i change management?

- TAK: 2 pkt
- CZĘŚCIOWO: 1 pkt
- NIE: 0 pkt

## Sekcja 2: kompetencje (8 pytań, 16 punktów)

**Pytanie 9.** Czy mamy w zespole co najmniej jednego ML/AI engineer z doświadczeniem w deployments LLM?

- TAK — full-time: 2 pkt
- CZĘŚCIOWO — part-time lub konsultant: 1 pkt
- NIE — planujemy zatrudnić: 0 pkt

**Pytanie 10.** Czy mamy kompetencje GPU/MLOps (deployment, monitoring, scaling modeli)?

- TAK: 2 pkt
- CZĘŚCIOWO: 1 pkt
- NIE: 0 pkt

**Pytanie 11.** Czy nasz zespół IT zna Linux, Docker, Python na poziomie produkcyjnym?

- TAK: 2 pkt
- CZĘŚCIOWO: 1 pkt
- NIE: 0 pkt

**Pytanie 12.** Czy mamy kompetencje cyberbezpieczeństwa specyficzne dla AI (prompt injection, model security)?

- TAK: 2 pkt
- CZĘŚCIOWO — ogólny cyber, nie AI-specific: 1 pkt
- NIE: 0 pkt

**Pytanie 13.** Czy mamy plan rozwoju kompetencji (szkolenia, konferencje, certyfikacje)?

- TAK — udokumentowany budżet rozwoju: 2 pkt
- CZĘŚCIOWO: 1 pkt
- NIE: 0 pkt

**Pytanie 14.** Czy mamy plan zatrudnienia (jeśli wymagane) — jasna roadmapa, wynagrodzenia rynkowe?

- TAK: 2 pkt
- CZĘŚCIOWO: 1 pkt
- NIE: 0 pkt

**Pytanie 15.** Czy mamy partnerską relację z konsultantem zewnętrznym (na pomoc w trudnych decyzjach)?

- TAK — kontrakt podpisany: 2 pkt
- CZĘŚCIOWO — wstępne rozmowy: 1 pkt
- NIE: 0 pkt

**Pytanie 16.** Czy nasz zespół rozumie różnicę między prompt engineering, RAG, fine-tuningiem (i wie, kiedy co)?

- TAK: 2 pkt
- CZĘŚCIOWO: 1 pkt
- NIE: 0 pkt

## Sekcja 3: infrastruktura (8 pytań, 16 punktów)

**Pytanie 17.** Czy mamy fizyczne miejsce na sprzęt AI (server room, colocation)?

- TAK — z mocą i chłodzeniem dla GPU: 2 pkt
- CZĘŚCIOWO: 1 pkt
- NIE: 0 pkt

**Pytanie 18.** Czy nasza infrastruktura sieciowa jest gotowa (segmentation, security, monitoring)?

- TAK: 2 pkt
- CZĘŚCIOWO: 1 pkt
- NIE: 0 pkt

**Pytanie 19.** Czy mamy backup i disaster recovery dla istniejącej infrastruktury?

- TAK — testowane: 2 pkt
- CZĘŚCIOWO: 1 pkt
- NIE: 0 pkt

**Pytanie 20.** Czy mamy monitoring infrastruktury (Prometheus/Grafana lub równoważny)?

- TAK: 2 pkt
- CZĘŚCIOWO: 1 pkt
- NIE: 0 pkt

**Pytanie 21.** Czy mamy CI/CD pipelines dla deployments?

- TAK: 2 pkt
- CZĘŚCIOWO: 1 pkt
- NIE: 0 pkt

**Pytanie 22.** Czy mamy Identity and Access Management (IAM) dla wewnętrznych systemów?

- TAK — z MFA i SSO: 2 pkt
- CZĘŚCIOWO: 1 pkt
- NIE: 0 pkt

**Pytanie 23.** Czy nasze API gateway pozwala na rate limiting i autentykację?

- TAK: 2 pkt
- CZĘŚCIOWO: 1 pkt
- NIE: 0 pkt

**Pytanie 24.** Czy mamy plan upgrade'u sprzętu co 3-5 lat?

- TAK: 2 pkt
- CZĘŚCIOWO: 1 pkt
- NIE: 0 pkt

## Sekcja 4: dane (8 pytań, 16 punktów)

**Pytanie 25.** Czy nasze dane krytyczne dla AI są skatalogowane (data catalog)?

- TAK: 2 pkt
- CZĘŚCIOWO: 1 pkt
- NIE: 0 pkt

**Pytanie 26.** Czy mamy data governance (kto może uzyskać dostęp do jakich danych)?

- TAK — formalna polityka: 2 pkt
- CZĘŚCIOWO: 1 pkt
- NIE: 0 pkt

**Pytanie 27.** Czy nasze dane są w odpowiedniej jakości dla AI (clean, structured, complete)?

- TAK — zweryfikowane: 2 pkt
- CZĘŚCIOWO — częściowo: 1 pkt
- NIE — major data quality issues: 0 pkt

**Pytanie 28.** Jeśli planujemy fine-tuning, mamy dane treningowe (minimum 500 wysokiej jakości przykładów)?

- TAK / nie planujemy fine-tuningu: 2 pkt
- CZĘŚCIOWO — mamy mniej / niskiej jakości: 1 pkt
- NIE — planujemy ale nie mamy danych: 0 pkt

**Pytanie 29.** Jeśli planujemy RAG, mamy bazę wiedzy do indeksacji?

- TAK / nie planujemy RAG: 2 pkt
- CZĘŚCIOWO: 1 pkt
- NIE: 0 pkt

**Pytanie 30.** Czy zidentyfikowaliśmy i zaadresowaliśmy ryzyka RODO związane z użyciem danych w AI?

- TAK — DPIA wykonane: 2 pkt
- CZĘŚCIOWO: 1 pkt
- NIE: 0 pkt

**Pytanie 31.** Czy mamy procedury anonimizacji / pseudonimizacji danych przed wysłaniem do modelu?

- TAK / nie wprowadzamy danych osobowych: 2 pkt
- CZĘŚCIOWO: 1 pkt
- NIE: 0 pkt

**Pytanie 32.** Czy mamy retention policy dla logów i zapytań do AI?

- TAK: 2 pkt
- CZĘŚCIOWO: 1 pkt
- NIE: 0 pkt

## Sekcja 5: governance (8 pytań, 16 punktów)

**Pytanie 33.** Czy mamy formalnie wyznaczonego AI Lead lub odpowiednika?

- TAK — z udokumentowanym mandatem: 2 pkt
- CZĘŚCIOWO: 1 pkt
- NIE: 0 pkt

**Pytanie 34.** Czy mamy AI policy (zasady używania AI w firmie, akceptowalne use cases, ograniczenia)?

- TAK — udokumentowana, komunikowana: 2 pkt
- CZĘŚCIOWO: 1 pkt
- NIE: 0 pkt

**Pytanie 35.** Czy mamy proces approvalu nowych AI use cases (security review, compliance check, ROI assessment)?

- TAK: 2 pkt
- CZĘŚCIOWO: 1 pkt
- NIE: 0 pkt

**Pytanie 36.** Czy mamy procedury monitorowania jakości outputów AI (czy hallucinations, czy biased)?

- TAK: 2 pkt
- CZĘŚCIOWO: 1 pkt
- NIE: 0 pkt

**Pytanie 37.** Czy mamy plan reagowania na incydenty AI (model failure, security incident, compliance violation)?

- TAK: 2 pkt
- CZĘŚCIOWO: 1 pkt
- NIE: 0 pkt

**Pytanie 38.** Czy mamy procedury aktualizacji modeli (kiedy, jak, kto decyduje)?

- TAK: 2 pkt
- CZĘŚCIOWO: 1 pkt
- NIE: 0 pkt

**Pytanie 39.** Czy mamy plan compliance z AI Act (jeśli aplikuje)?

- TAK / nie podlegamy AI Act: 2 pkt
- CZĘŚCIOWO: 1 pkt
- NIE: 0 pkt

**Pytanie 40.** Czy mamy program edukacji pracowników o AI (acceptable use, risks)?

- TAK: 2 pkt
- CZĘŚCIOWO: 1 pkt
- NIE: 0 pkt

## Punktacja i interpretacja

Maksimum: 80 punktów. Sekcje: strategia (16), kompetencje (16), infrastruktura (16), dane (16), governance (16).

**70-80 punktów: gotowość znakomita.** Twoja firma ma fundamenty na produkcyjne wdrożenie. Niewielkie korekty wymagane. Możesz rozpocząć pełen pilot lub bezpośrednio przejść do produkcji ograniczonej skali.

**55-69 punktów: gotowość wysoka.** Solidne fundamenty z istotnymi obszarami do uzupełnienia. Adekwatne dla pilotu z planem rozwoju. Pełna produkcja możliwa po 6-12 miesiącach uzupełnień.

**40-54 punkty: gotowość umiarkowana.** Działający fundament, ale istotne luki w kilku obszarach. Pilot możliwy, ale wymaga znacznej zewnętrznej pomocy. Pełna produkcja: 12-18 miesięcy budowy fundamentów najpierw.

**25-39 punktów: gotowość niska.** Krytyczne luki w wielu obszarach. Pilot możliwy w bardzo wąskim zakresie. Najpierw budowa fundamentów (kompetencje, governance, infrastruktura) w okresie 12-24 miesięcy. Inwestycja w on-premise AI bez tego ryzyka katastrofy.

**Poniżej 25 punktów: gotowość minimalna.** Nie warto wdrażać on-premise AI w obecnej formie. Lepiej zacznij od chmury (API zewnętrzne) dla 12+ miesięcy. Buduj fundamenty równolegle. Powtórz audyt po 12 miesiącach.

## Mapowanie wyników na priorytety działań

**Niski wynik w sekcji 1 (strategia):** problem zarządczy. Pierwsze działania: warsztat strategiczny zarządu, zdefiniowanie use cases, kalkulacja ROI, zatwierdzenie budżetu.

**Niski wynik w sekcji 2 (kompetencje):** problem talentowy. Pierwsze działania: rekrutacja ML/AI engineer (lub kontrakt z firmą zewnętrzną), program rozwoju zespołu IT.

**Niski wynik w sekcji 3 (infrastruktura):** problem techniczny. Pierwsze działania: assessment infrastruktury, plan modernizacji, kontrakt z dostawcą sprzętu.

**Niski wynik w sekcji 4 (dane):** problem danych. Pierwsze działania: data audit, data quality program, formalna ocena RODO.

**Niski wynik w sekcji 5 (governance):** problem proceduralny. Pierwsze działania: opracowanie AI policy, procedur, programów edukacyjnych.

## Co dalej po self-audit

**Krok 1: walidacja wyniku.** Test wykonany przez jedną osobę może być stronniczy. Walidacja przez 2-3 osoby z różnych perspektyw (CTO + dyrektor compliance + dyrektor finansowy).

**Krok 2: prezentacja zarządowi.** Wyniki self-auditu jako podstawa decyzji strategicznej. Konkretne priorytety i budżet.

**Krok 3: external assessment (jeśli wynik niski).** Wynik poniżej 50 — warto zewnętrzny audyt dla obiektywizacji. Koszt: 30 000-80 000 zł. Wartość: konkretny plan budowy fundamentów.

**Krok 4: plan 12-miesięczny.** Konkretne działania uzupełniające w obszarach najsłabszych. Z budżetem, odpowiedzialnymi, terminami.

**Krok 5: powtórzenie self-auditu za 6-12 miesięcy.** Mierzenie postępu. Decyzja o przejściu do następnej fazy.

## Częste wzory wyników

**Wzór A: wysokie compliance, niskie technical.** Dobrze przygotowani regulacyjnie, ale brak kompetencji. Częste w sektorze finansowym i ochronie zdrowia. Działania: rekrutacja talentów, partnership z konsultantem.

**Wzór B: wysokie technical, niskie governance.** Kompetentni technicznie, ale chaos zarządczy. Częste w startupach i tech firmach. Działania: formalizacja procesów, AI policy, governance.

**Wzór C: wysokie strategy, niskie wszystko inne.** Zarząd ma wizję, ale firma nie ma fundamentów. Częste w organizacjach po pivot strategicznym. Działania: realistyczny harmonogram, najpierw fundamenty.

**Wzór D: średnie wszystko.** Nic ekstremalnego, wszystko w średnim stanie. Działania: równoczesny rozwój wszystkich obszarów, długi (24-36 miesięcy) cykl budowy.

## Najczęstsze błędy w self-audicie

**Błąd 1: zbyt pochlebna ocena.** "Mamy częściowo wszystko, ale damy radę". Realnie: częściowo = niedostateczne dla produkcji.

**Błąd 2: ignorowanie sekcji.** "Strategia jest najważniejsza, reszta się ułoży". Każda sekcja jest fundamentem.

**Błąd 3: jednorazowy assessment.** Self-audit raz, decyzja na lata. Lepiej: powtarzanie co 6-12 miesięcy z trendami.

**Błąd 4: brak działań po assessmecie.** Wynik 38 punktów, decyzja "zaczynamy". Bez planu uzupełnienia luk = gwarantowana porażka.

**Błąd 5: ignorowanie zewnętrznego audytu mimo niskiego wyniku.** Self-audit jest punktem wyjścia. Wynik <40 oznacza, że warto inwestować w zewnętrzny assessment.

## Bibliografia

<ul>
<li>NIST. (2023). <em>AI Risk Management Framework (AI RMF 1.0)</em>. National Institute of Standards and Technology. <a href="https://www.nist.gov/itl/ai-risk-management-framework">https://www.nist.gov/itl/ai-risk-management-framework</a></li>
<li>Komisja Europejska. (2024). <em>EU AI Act</em>. <a href="https://eur-lex.europa.eu/eli/reg/2024/1689/oj">https://eur-lex.europa.eu/eli/reg/2024/1689/oj</a></li>
<li>OECD. (2023). <em>OECD AI Principles</em>. OECD. <a href="https://oecd.ai/en/ai-principles">https://oecd.ai/en/ai-principles</a></li>
<li>Gartner. (2024). <em>AI Maturity Model</em>. Gartner Research. <a href="https://www.gartner.com/">https://www.gartner.com/</a></li>
<li>McKinsey. (2024). <em>AI Readiness Assessment</em>. McKinsey Quarterly. <a href="https://www.mckinsey.com/">https://www.mckinsey.com/</a></li>
<li>Komisja Europejska. (2022). <em>Dyrektywa NIS2</em>. <a href="https://eur-lex.europa.eu/legal-content/PL/TXT/?uri=CELEX:32022L2555">https://eur-lex.europa.eu/legal-content/PL/TXT/?uri=CELEX:32022L2555</a></li>
</ul>

---

**Self-audit to początek strategii AI on-premise, nie koniec.** W cotygodniowym newsletterze OnPremiseAI.pl publikujemy konkretne plany 90-dniowe dla różnych poziomów gotowości, narzędzia, case studies. [Zapisz się — bezpłatnie](#newsletter-signup) i wykorzystaj ten test jako punkt wyjścia rocznej strategii.
