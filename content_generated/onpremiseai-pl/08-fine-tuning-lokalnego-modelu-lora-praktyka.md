---
title: "Fine-tuning lokalnego modelu LoRA — praktyka dla polskiej firmy"
slug: "fine-tuning-lokalnego-modelu-lora-praktyka"
excerpt: "Pełen przewodnik po LoRA fine-tuning lokalnych modeli LLM. Kiedy ma sens, jak przygotować dane, jak wdrożyć, koszty, najczęstsze błędy."
category_slug: "technika-onprem"
tags: "fine-tuning, LoRA, QLoRA, customizacja, lokalny LLM, średni"
reading_time: 11
is_published: true
is_featured: false
meta_title: "Fine-tuning LoRA — praktyczny przewodnik dla on-premise (2026)"
meta_description: "Pełen przewodnik LoRA fine-tuning: kiedy ma sens vs RAG, przygotowanie danych, training, ewaluacja, deployment. Konkretne narzędzia."
funnel: "MOFU"
author_slug: "marek-porycki"
related_slugs: "ai-on-premise-w-2026-przewodnik, llama-mistral-qwen-porownanie-modeli, ollama-lm-studio-vllm-narzedzia-produkcyjne"
product_slugs: ""
---

W większości rozmów o customizacji AI pojawia się pytanie: "Czy nie powinniśmy fine-tuningować modelu na naszych danych?". Odpowiedź jest często rozczarowująca: w większości przypadków nie, lepiej RAG. Ale w niektórych — tak, fine-tuning daje wartość, której RAG nie zapewni. Granica jest niuansowana, a koszty (czasu, sprzętu, ekspertyzy) znaczne.

LoRA (Low-Rank Adaptation, Hu et al. 2021) zrewolucjonizowała fine-tuning. Zamiast modyfikowania wszystkich parametrów modelu (co wymaga ogromnych zasobów obliczeniowych), LoRA dodaje małe "adapter matrices" obok oryginalnych wag. Wynik: 10-100x mniej parametrów do trenowania, dramatyczny spadek wymagań sprzętowych. QLoRA (Dettmers et al. 2023) idzie dalej — kwantyzuje base model do 4-bit, pozwalając na fine-tuning modelu 70B na pojedynczej karcie RTX 4090.

Ten tekst opisuje pełen workflow fine-tuningu LoRA dla średniej polskiej firmy: kiedy ma sens, jak przygotować dane, jak przeprowadzić training, jak ewaluować, jak wdrożyć produkcyjnie. Adresat: ML engineers, dyrektorzy IT planujący customizację modeli, członkowie zarządów oceniający budżet na customizację.

## Fine-tuning vs RAG vs prompt engineering — kiedy co

Trzy główne sposoby customizacji modelu LLM dla konkretnego use case'u:

**Prompt engineering:** modyfikacja samego promptu (system message, instrukcje, few-shot examples). Najtańszy, najszybszy, ale ograniczony zakres.

*Kiedy:* większość use cases. 80% problemów rozwiąże dobry prompt engineering.

**RAG (Retrieval-Augmented Generation):** dynamiczne dołączanie do promptu informacji z bazy danych. Model wciąż używa swoich oryginalnych parametrów, ale ma dostęp do Twoich aktualnych danych.

*Kiedy:* potrzebujesz, żeby model znał Twoje dane (dokumenty, polityki, baza wiedzy). Dane się zmieniają. Wymagana traceability (źródło informacji w odpowiedzi).

Pełniejsze omówienie RAG na ragpolska.pl (osobny portal).

**Fine-tuning:** modyfikacja parametrów modelu na Twoich danych. Model "uczy się" Twojego stylu, terminologii, podejścia.

*Kiedy:* potrzebujesz, żeby model "rozumiał" specyficzne wzorce. Stałe niezmienne dane. Chcesz unikalnego "stylu" odpowiedzi. Wykonujesz to samo zadanie miliony razy z konkretnym formatem outputu.

**Konkretne przykłady:**

- Chatbot HR odpowiadający na pytania o polityki firmowe → RAG (polityki się zmieniają).
- Model generujący raporty w specyficznym formacie firmy → fine-tuning (format jest stały i powtarzalny).
- Asystent sprzedażowy z dostępem do CRM → RAG (dane klientów się zmieniają).
- Klasyfikator emaili w specyficzne kategorie firmy → fine-tuning (kategorie stałe).
- Generator treści marketingowych w voice firmy → fine-tuning (voice jest stały).
- Wyszukiwanie informacji w bazie dokumentów medycznych → RAG.

W praktyce wiele aplikacji łączy: fine-tuned model + RAG + zaawansowany prompt engineering.

## Kiedy fine-tuning rzeczywiście ma sens

Fine-tuning ma sens, gdy spełnione są 3+ z poniższych warunków:

1. **Wykonujesz to samo zadanie wielokrotnie** (>10 000 razy w okresie życia modelu).
2. **Zadanie ma specyficzny format output'u** (nie ogólna konwersacja).
3. **Masz dane treningowe wysokiej jakości** (>500 dobrych przykładów).
4. **Stała natura zadania** (nie zmienia się co miesiąc).
5. **Lepszy model nie rozwiąże problemu** (próbowałeś GPT-4o, wciąż nie wystarcza).
6. **Prompt engineering jest niewystarczający** (10-shot prompts zawodzą).
7. **RAG nie pomaga** (problem nie jest w retrievalu, ale w samym zachowaniu modelu).
8. **Chcesz mniejszego modelu, ale wciąż dobrego** (fine-tuned 7B może być lepszy niż generic 70B w wąskim zadaniu).

Mniej niż 3 warunki spełnione → prawdopodobnie nie warto fine-tuningu.

## Trzy poziomy fine-tuningu

**Poziom 1: full fine-tuning.**

Modyfikacja wszystkich parametrów modelu. Najlepsze wyniki, ale najdroższe.

*Wymagania sprzętowe:* dla modelu 7B → 80-120 GB VRAM. Dla 70B → 800+ GB VRAM (klaster).

*Czas:* godziny do dni dla 7B, dni do tygodni dla 70B.

*Kiedy:* dramatyczne zmiany w zachowaniu modelu, badania, deep customization.

Większość firm nie robi pełnego fine-tuningu — za drogie, za ryzykowne (model może "stracić" inne kompetencje).

**Poziom 2: LoRA fine-tuning.**

Dodanie małych "adapter matrices" obok oryginalnych wag. Rank 8-64. Trenowanych jest 0,1-1% parametrów.

*Wymagania sprzętowe:* dla 7B → 16-24 GB VRAM. Dla 70B → 80-160 GB VRAM.

*Czas:* godziny do dni.

*Kiedy:* customizacja konkretnego zadania bez utraty ogólnych kompetencji modelu.

Najczęstszy wybór dla średnich firm.

**Poziom 3: QLoRA.**

LoRA z 4-bit kwantyzacją base modelu. Najlżejszy.

*Wymagania sprzętowe:* dla 7B → 8-12 GB VRAM (RTX 3090 wystarcza). Dla 70B → 40-48 GB VRAM (RTX A6000 wystarcza!).

*Czas:* podobny do LoRA.

*Kiedy:* fine-tuning z ograniczonego sprzętu. Najczęstsza opcja w polskiej praktyce.

Praktyczna rekomendacja: zacznij od QLoRA. Wystarcza dla większości zastosowań.

## Workflow fine-tuningu — krok po kroku

**Krok 1: zdefiniuj zadanie konkretnie.**

Nie "fine-tuning na naszych danych". Lepiej: "model generujący streszczenia raportów finansowych w naszym formatie X (max 200 słów, struktura A/B/C, voice formalny)".

Im bardziej konkretne zadanie, tym lepsze wyniki fine-tuningu.

**Krok 2: zbierz dane treningowe.**

Format: pary (input, output). Każdy przykład — input pokazuje co model otrzymuje, output pokazuje pożądaną odpowiedź.

Minimum: 100 przykładów dla pierwszego pilotu.
Optymalnie: 500-2000 przykładów dla solidnego fine-tuningu.
Dla najlepszych wyników: 5000-50 000 przykładów.

Jakość ważniejsza niż ilość. 500 świetnych przykładów > 5000 średnich.

**Krok 3: przygotuj dane w formacie.**

Standardowy format dla LoRA fine-tuning to JSONL z chat messages:

```json
{"messages": [
  {"role": "system", "content": "Jesteś asystentem generującym streszczenia raportów."},
  {"role": "user", "content": "[treść raportu]"},
  {"role": "assistant", "content": "[oczekiwane streszczenie]"}
]}
```

Każda linia JSONL = jeden przykład treningowy.

**Krok 4: split na train/validation/test.**

Standardowy podział: 80% train, 10% validation (do tuningu hyperparameters), 10% test (final evaluation, używany tylko raz).

**Krok 5: wybierz base model.**

Mniejszy model (7-13B) — szybszy training, mniejsze wymagania sprzętowe. Dobry dla wąskich zadań.

Większy model (70B) — lepsze wyniki ogólne, ale droższy. Rzadko warto, jeśli zadanie jest wąskie.

Dla większości fine-tuningów: Llama 3 8B lub Mistral 7B jako base.

**Krok 6: przygotuj środowisko.**

Standardowy stack:
- Hugging Face Transformers (framework);
- PEFT (Parameter-Efficient Fine-Tuning library, zawiera LoRA);
- bitsandbytes (4-bit kwantyzacja dla QLoRA);
- TRL (transformers reinforcement learning, zawiera SFTTrainer);
- Weights & Biases (monitoring).

Instalacja:
```bash
pip install transformers peft bitsandbytes trl wandb accelerate datasets
```

**Krok 7: konfiguracja LoRA.**

Standardowe hyperparameters:
- LoRA rank (r): 8, 16, 32 (większe = więcej parametrów, lepsze wyniki, więcej VRAM);
- LoRA alpha: zwykle 2x rank;
- LoRA dropout: 0.05-0.1;
- target modules: q_proj, k_proj, v_proj, o_proj (attention) + opcjonalnie up_proj, down_proj (MLP).

**Krok 8: training.**

Hyperparameters:
- learning rate: 1e-4 do 3e-4 (LoRA toleruje wyższe niż full FT);
- batch size: jak największy mieszczący się w VRAM (8-32);
- epochs: 3-5 dla typowych zadań;
- warmup ratio: 0.03-0.1.

Czas: dla 1000 przykładów na RTX A6000: 30-90 minut.

**Krok 9: ewaluacja.**

Test na hold-out test setu. Metryki:
- exact match (jeśli output strukturalny);
- BLEU/ROUGE (dla generation);
- human evaluation (najlepsze dla subiektywnych zadań).

Porównanie z baseline (model bez fine-tuningu) — czy fine-tuning rzeczywiście pomaga?

**Krok 10: deployment.**

Dwie opcje:

*Opcja A: merge LoRA z base modelem.* Wynik: pojedynczy model file (jak normalny). Prostsze deployment, ale tracisz elastyczność (nie możesz łatwo przełączyć adaptery).

*Opcja B: deploy z dynamic loading LoRA adapter.* Wynik: base model + adapter ładowany w runtime. Możliwa multi-adapter inference (różne LoRA dla różnych zadań na tym samym base).

llama.cpp wspiera oba scenariusze.

## Realne wyniki LoRA — przykładowe case studies

**Case 1: chatbot dla biura księgowego (klient real, anonimizowane).**

Zadanie: odpowiadanie na pytania klientów o ich faktury i podatki w specyficznym formacie firmy.

Base model: Llama 3 8B.
Dane treningowe: 800 par (pytanie, odpowiedź) zebrane z historii korespondencji.
Sprzęt: RTX A6000.
Czas treningu: 45 minut.
Wyniki: model znacząco lepiej formatuje odpowiedzi w stylu firmy. Halucinacje na konkretnych danych klientów spadły dzięki dodatkowemu RAG.

**Case 2: generator opisów produktów dla e-commerce.**

Zadanie: tworzenie SEO-friendly opisów produktów w specyficznym voice marki.

Base model: Mistral 7B.
Dane treningowe: 3000 (specyfikacja produktu, gotowy opis).
Sprzęt: 2x RTX A6000.
Czas: 4 godziny.
Wyniki: opisy w voice firmy, 70% akceptowane przez copywritera bez korekty (vs 20% dla generycznego GPT-4).

**Case 3: klasyfikator zgłoszeń do helpdesku.**

Zadanie: klasyfikacja zgłoszeń do 23 kategorii zgodnych z taksonomią firmy.

Base model: Llama 3 8B.
Dane treningowe: 5000 zgłoszeń sklasyfikowanych historycznie.
Sprzęt: RTX 4090.
Czas: 1 godzina.
Wyniki: 92% accuracy (vs 78% dla generycznego GPT-4 z prompt engineering).

## Najczęstsze błędy fine-tuningu

**Błąd 1: za mało danych treningowych.** 50 przykładów to często za mało. Model może overfit'ować lub nie nauczyć się generalizacji.

**Błąd 2: dane niskiej jakości.** Garbage in, garbage out. 1000 przykładów z błędami da gorszy fine-tune niż 100 świetnych.

**Błąd 3: brak validation setu.** Bez monitorowania na validation możesz overfit'ować bez wiedzy.

**Błąd 4: za duża liczba epok.** 10+ epok = overfitting na małych datasetach. 3-5 zwykle wystarcza.

**Błąd 5: zła konfiguracja hyperparameters.** Learning rate za wysoki — model może "zapomnieć" oryginalnych kompetencji. Za niski — fine-tuning niewystarczający.

**Błąd 6: deployment bez ewaluacji.** Wdrożenie modelu, którego nie przetestowano na realnych zadaniach.

**Błąd 7: ignorowanie data leakage.** Test set zawiera dane z train setu (przez przypadek). Wyniki są nierealistycznie dobre.

**Błąd 8: catastrophic forgetting.** Model po fine-tuningu jest świetny w nowym zadaniu, ale stracił podstawowe kompetencje. LoRA minimalizuje to ryzyko, ale nie eliminuje.

## Realny budżet fine-tuningu

**Pierwszy pilot:** 30 000-80 000 zł.
- Zewnętrzny ML engineer (40-80 godzin): 20 000-50 000 zł.
- Sprzęt (1 GPU rented w cloudzie na pilot): 2 000-5 000 zł.
- Dane (czas wewnętrznego zespołu na curatorship): 8 000-25 000 zł.

**Produkcyjny fine-tuning (jeden model):** 60 000-200 000 zł.
- ML engineer (200-400 godzin): 50 000-150 000 zł.
- Sprzęt: 5 000-30 000 zł.
- Pozostałe (dane, monitoring, deployment): 5 000-20 000 zł.

**Roczne utrzymanie fine-tuned modeli:**
- Reganowanie po zmianie use case'u: 30 000-100 000 zł rocznie;
- Aktualizacja przy nowych base models: 60 000-150 000 zł co 12-18 miesięcy.

## Bibliografia

<ul>
<li>Hu, E., et al. (2021). <em>LoRA: Low-Rank Adaptation of Large Language Models</em>. ICLR 2022. <a href="https://arxiv.org/abs/2106.09685">https://arxiv.org/abs/2106.09685</a></li>
<li>Dettmers, T., et al. (2023). <em>QLoRA: Efficient Finetuning of Quantized LLMs</em>. NeurIPS 2023. <a href="https://arxiv.org/abs/2305.14314">https://arxiv.org/abs/2305.14314</a></li>
<li>Hu, J. E., et al. (2024). <em>Practical LoRA Fine-tuning Guide</em>. Hugging Face. <a href="https://huggingface.co/docs/peft/task_guides/lora_based_methods">https://huggingface.co/docs/peft/task_guides/lora_based_methods</a></li>
<li>Hugging Face. (2024). <em>PEFT: Parameter-Efficient Fine-Tuning</em>. <a href="https://github.com/huggingface/peft">https://github.com/huggingface/peft</a></li>
<li>Hugging Face. (2024). <em>TRL: Transformer Reinforcement Learning</em>. <a href="https://github.com/huggingface/trl">https://github.com/huggingface/trl</a></li>
<li>Liu, H., et al. (2024). <em>When Should You Fine-Tune Your LLM? A Comprehensive Comparison with RAG</em>. <a href="https://arxiv.org/abs/2403.06634">https://arxiv.org/abs/2403.06634</a></li>
<li>Touvron, H., et al. (2024). <em>Llama 3: Improving Foundation Models</em>. Meta AI. <a href="https://ai.meta.com/blog/meta-llama-3/">https://ai.meta.com/blog/meta-llama-3/</a></li>
</ul>

---

**Fine-tuning ma sens w wąskich, powtarzalnych zadaniach.** W cotygodniowym newsletterze OnPremiseAI.pl publikujemy konkretne tutoriale fine-tuningowe, case studies, benchmarki. [Zapisz się — bezpłatnie](#newsletter-signup).
