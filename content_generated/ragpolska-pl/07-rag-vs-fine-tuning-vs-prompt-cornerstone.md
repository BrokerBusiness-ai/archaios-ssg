---
title: "RAG vs fine-tuning vs prompt engineering — pełna decyzja (cornerstone)"
slug: "rag-vs-fine-tuning-vs-prompt-cornerstone"
excerpt: "Cornerstone trzech głównych technik customizacji LLM. Decision matrix, kombinacje, koszty, kiedy która technika wins. Konkretne przykłady."
category_slug: "techniki-rag"
tags: "RAG, fine-tuning, prompt engineering, decision, cornerstone, zaawansowany"
reading_time: 14
is_published: true
is_featured: true
meta_title: "RAG vs fine-tuning vs prompt — pełna decyzja (cornerstone 2026)"
meta_description: "Cornerstone wyboru techniki customizacji LLM. RAG, fine-tuning, prompt engineering. Decision matrix, kombinacje, koszty, kiedy co."
funnel: "MOFU-cornerstone"
author_slug: "marek-porycki"
related_slugs: "rag-enterprise-architektura, chunking-strategy-fixed-do-semantic, agentic-rag-multi-step-tools-planning"
product_slugs: ""
---

W każdej rozmowie o LLM application development pojawia się to samo pytanie: "Czy fine-tuning, czy RAG?". Pytanie jest często źle sformułowane. To nie jest binarna decyzja, to spectrum technik z różnymi tradeoffs. Prompt engineering, RAG, fine-tuning — wszystkie trzy mają swoje miejsce, często w kombinacji. Dobrze zaprojektowana LLM aplikacja używa wszystkich trzech.

Najczęstsze rozumowanie ogólne: prompt engineering rozwiązuje 70% problemów, RAG dodaje aktualną wiedzę firmową dla kolejnych 25%, fine-tuning dopina ostatnie 5% specific behaviors. Ten model jest uproszczeniem, ale daje useful intuition. Reality: różne use cases wymagają różnych proporcji.

Ten cornerstone-text definiuje pełną decision framework: kiedy która technika ma sens, jak je kombinować, jakie są koszty i tradeoffs, jak iterować od prostszego do bardziej złożonego. Adresat: ML engineers, architekci AI, dyrektorzy techniczni planujący stack dla LLM applications.

## Trzy techniki — krótki overview

**Prompt engineering:**
- Modyfikacja samego promptu;
- System messages, instrukcje, few-shot examples;
- Brak modyfikacji modelu;
- Najtańszy i najszybszy.

**RAG (Retrieval-Augmented Generation):**
- Dynamic injection of relevant context;
- Vector database z embeddings;
- Model używa swoich oryginalnych params + provided context;
- Średni koszt, średnia complexity.

**Fine-tuning:**
- Modyfikacja parametrów modelu;
- Trening na specific data;
- Permanent change w modelu;
- Najwyższy koszt, najwyższa complexity.

## Kiedy prompt engineering wystarcza

**Use cases:**
- Generic tasks (writing, summarization, translation);
- Tasks z pre-existing knowledge w modelu (general knowledge);
- Tasks gdzie format outputu jest standard;
- Pierwsze wszystkie projekty (zaczynaj od prompt engineering).

**Indicators "prompt is enough":**
- Default model output jest "OK", potrzebujesz "good";
- Need specific format (JSON, markdown structure);
- Need specific tone lub style;
- Multi-step reasoning achievable z chain-of-thought prompting.

**Techniques:**
- Clear, specific instructions;
- Few-shot examples;
- Chain-of-thought ("let's think step by step");
- Role assignment ("you are an expert legal advisor");
- Output structure templates;
- Constraint specification.

**Limits prompt engineering:**
- Cannot teach model new facts (knowledge cutoff);
- Limited by context window;
- Effects volatile (small prompt changes → big result changes);
- Doesn't change model's underlying behavior.

## Kiedy RAG ma sens

**Use cases:**
- Application z access do firmowej wiedzy;
- Knowledge that changes over time (policies, prices, products);
- Need source attribution (citations);
- Reduce hallucinations;
- Large knowledge corpus (won't fit w context window).

**Indicators "you need RAG":**
- LLM gives wrong answers o Twoich danych (knowledge cutoff);
- LLM hallucinates facts;
- Need to cite sources;
- Knowledge updates frequently (not feasible to retrain often);
- Large dataset (millions of pages, can't fit in prompt).

**RAG zalety:**
- Data updates real-time (vs retraining);
- Citations (transparency);
- Lower hallucinations;
- Scales to massive knowledge bases;
- Same model serves multiple knowledge bases.

**RAG wady:**
- More complex architecture (vector DB, embeddings, retrieval);
- Latency overhead (retrieval before generation);
- Quality limited by retrieval quality (garbage in, garbage out);
- Cost of running retrieval infrastructure.

## Kiedy fine-tuning ma sens

**Use cases:**
- Specific output format that's hard to specify in prompt;
- Specific voice/style/tone consistently;
- Specialized terminology (legal, medical);
- Cost optimization (smaller fine-tuned model = cheaper than larger generic);
- Specific behavior that's hard to teach with prompts.

**Indicators "you need fine-tuning":**
- Prompt is long and complex (>500 tokens of system instructions);
- Few-shot examples consume too much context;
- You repeat similar instructions consistently;
- Specific output format crucial (hard to validate w prompt);
- Want smaller model (e.g., 7B fine-tuned może match 70B generic dla narrow task).

**Fine-tuning zalety:**
- Permanent behavior change;
- Reduces prompt verbosity (cheaper inference);
- Can use smaller models;
- Consistent specialized output.

**Fine-tuning wady:**
- Static (data updates wymagają retraining);
- Cost (training infrastructure, time);
- Risk: catastrophic forgetting (model loses general capabilities);
- Requires labeled data (typowo 500-10000+ examples high quality);
- Specialized expertise needed.

Pełniejsze omówienie LoRA fine-tuning na onpremiseai.pl ([Fine-tuning lokalnego modelu LoRA](https://onpremiseai.pl/fine-tuning-lokalnego-modelu-lora-praktyka)).

## Decision matrix

| Wymaganie | Prompt | RAG | Fine-tuning |
|---|---|---|---|
| Quick experimentation | ⭐⭐⭐ | ⭐⭐ | ⭐ |
| Access do firmowej wiedzy | ❌ | ⭐⭐⭐ | ⭐⭐ |
| Aktualne dane | ❌ | ⭐⭐⭐ | ⭐ |
| Citations / source attribution | ❌ | ⭐⭐⭐ | ⭐ |
| Specific output format | ⭐⭐ | ⭐⭐ | ⭐⭐⭐ |
| Specific voice/tone | ⭐⭐ | ⭐⭐ | ⭐⭐⭐ |
| Reduce hallucinations | ⭐ | ⭐⭐⭐ | ⭐⭐ |
| Lower inference costs | ⭐⭐ | ⭐⭐ | ⭐⭐⭐ (smaller models) |
| Domain expertise | ⭐ | ⭐⭐ | ⭐⭐⭐ |
| Quick to iterate | ⭐⭐⭐ | ⭐⭐ | ⭐ |
| Update data ease | ⭐⭐⭐ | ⭐⭐⭐ | ⭐ |

## Kombinacje — najczęstsze patterns

**Pattern 1: prompt + RAG (najczęstszy).**
- 80% LLM aplikacji enterprise;
- Prompt engineering dla format, instructions, behavior;
- RAG dla access do firmowej wiedzy.

Example: customer service chatbot. Prompt: "You are a polite customer service agent...". RAG: dynamicznie dołącza relevant policy documents.

**Pattern 2: prompt + fine-tuning.**
- Specialized tasks z stałymi danymi;
- Fine-tuning dla output format, voice;
- Prompt for input formatting.

Example: legal contract analyzer. Fine-tuned na contract analysis. Prompt: "Analyze this contract: {contract_text}".

**Pattern 3: prompt + RAG + fine-tuning (najpotężniejszy).**
- Wymaga investment w wszystkie trzy;
- Fine-tuning dla domain expertise + style;
- RAG dla aktualnych specific danych;
- Prompt dla coordination.

Example: medical diagnosis assistant (advanced). Fine-tuned na medical literature. RAG dla patient records. Prompt dla diagnostic workflow.

**Pattern 4: agentic z wszystkimi.**
- Najnowszy trend 2025-2026;
- Agent decides which technique użyć per step;
- RAG dla retrieval, fine-tuned model dla domain reasoning, prompts dla coordination.

Pełniejsze omówienie w artykule [Agentic RAG — multi-step, tools, planning](/agentic-rag-multi-step-tools-planning).

## Koszty comparison

Realny koszt dla średniej firmy implementing typowy use case (chatbot dla pracowników):

**Pure prompt engineering:**
- Setup: 5 000-20 000 zł;
- Development: 20 000-60 000 zł;
- Per-query cost: ~$0.01-0.05;
- Total annual (50 000 queries): 50 000-100 000 zł.

**Prompt + RAG:**
- Setup: 30 000-80 000 zł;
- Development: 80 000-250 000 zł (RAG infrastructure);
- Per-query cost: ~$0.02-0.08;
- Total annual: 150 000-400 000 zł.

**Prompt + fine-tuning:**
- Setup: 50 000-150 000 zł;
- Development: 100 000-400 000 zł (data prep + training);
- Per-query cost: ~$0.005-0.02 (smaller model);
- Total annual: 200 000-500 000 zł (z amortization fine-tuningu).

**Prompt + RAG + fine-tuning:**
- Setup: 100 000-300 000 zł;
- Development: 200 000-800 000 zł;
- Per-query cost: $0.02-0.08;
- Total annual: 400 000-1 200 000 zł.

## Iteracyjna ścieżka — co kiedy implementować

**Phase 1 (miesiące 1-3): prompt engineering.**
- Najtańszy i najszybszy way to validate use case;
- Try with various models (GPT-4o, Claude, Gemini);
- Baseline performance metrics;
- Identify gaps.

**Phase 2 (miesiące 4-9): add RAG (jeśli wymagany).**
- Wdrożenie RAG infrastructure;
- Indexing firmowej wiedzy;
- Pomiar improvement vs phase 1;
- Production deployment.

**Phase 3 (miesiące 10-18): consider fine-tuning (jeśli ROI uzasadniony).**
- Tylko gdy phase 2 ujawnia consistent format/style needs;
- Cost-benefit analysis (fine-tuning vs improvement value);
- Implementation jeśli decision positive.

**Phase 4 (years 2+): advanced techniques.**
- Agentic systems;
- Multi-agent architectures;
- Specialized fine-tunes per use case.

Większość firm spędza years w Phase 1+2. Phase 3 dla naprawdę specific needs. Phase 4 dla cutting-edge.

## Najczęstsze błędy w decyzjach

**Błąd 1: skok do fine-tuning bez próby prompt + RAG.** "Fine-tuning brzmi advanced, użyjemy". Często prompt + RAG wystarcza za 10x mniejszy koszt.

**Błąd 2: czysty prompt dla aplikacji wymagających firmowej wiedzy.** "Wystarczy good prompt". Bez RAG model nie zna aktualnych polityk firmy.

**Błąd 3: RAG bez prompt engineering optimization.** Implementacja RAG, ale prompt = "Answer the question based on context". Optimization promptu daje znaczne improvements za zero cost.

**Błąd 4: fine-tuning na shifting data.** Fine-tune na danych aktualnych z momentu treningu. Po 6 miesiącach data się zmienia, fine-tune outdated. Better RAG.

**Błąd 5: brak iteracji.** Wybór single technique na początku, brak revisitingu. Optimal mix może się zmieniać z time.

**Błąd 6: ignorowanie complexity costs.** Każda dodana technique = więcej moving parts, więcej maintenance, więcej things to break.

## Decision tree — practical

```
Czy zadanie wymaga firmowej wiedzy?
├── NIE → Prompt engineering wystarczy
└── TAK → Następne pytanie

Czy ta wiedza zmienia się w czasie?
├── TAK → Należy RAG
└── NIE → Następne pytanie

Czy potrzebujesz citations / source attribution?
├── TAK → Należy RAG
└── NIE → Następne pytanie

Czy potrzebujesz specific behavior format który trudno specify w prompt?
├── TAK → Rozważ fine-tuning (po prompt + RAG)
└── NIE → Prompt + RAG wystarczy

Czy chcesz lower inference costs przez smaller model?
├── TAK → Fine-tuning może być warto
└── NIE → Prompt + RAG wystarczy
```

## Specific use case examples

**Use case 1: customer service FAQ chatbot.**
- Optimal: prompt + RAG.
- Prompt: clear instructions o tone, escalation rules.
- RAG: FAQ knowledge base, current policies.
- Fine-tuning: niepotrzebne (overhead niewspółmierny do benefit).

**Use case 2: code review assistant z firmową code style guide.**
- Optimal: prompt + fine-tuning.
- Prompt: code review instructions.
- Fine-tuning: na firmowym kodzie z reviews — model uczy się stylu.
- RAG: niekoniecznie (style guide stable).

**Use case 3: medical diagnostic assistant.**
- Optimal: prompt + RAG + fine-tuning.
- Prompt: diagnostic workflow.
- RAG: aktualne medical literature, patient records.
- Fine-tuning: medical reasoning, terminology.

**Use case 4: marketing content generator dla firmowego brand voice.**
- Optimal: prompt + fine-tuning.
- Prompt: campaign brief, target audience.
- Fine-tuning: na examples brand voice.
- RAG: opcjonalnie dla competitive intelligence.

**Use case 5: legal document analyzer.**
- Optimal: prompt + RAG (+ fine-tuning dla advanced).
- Prompt: analysis structure, risk identification framework.
- RAG: case law database, contract templates.
- Fine-tuning: dla advanced — legal reasoning patterns.

## Bibliografia

<ul>
<li>Lewis, P., et al. (2020). <em>Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks</em>. NeurIPS 2020. <a href="https://arxiv.org/abs/2005.11401">https://arxiv.org/abs/2005.11401</a></li>
<li>Hu, E., et al. (2021). <em>LoRA: Low-Rank Adaptation of Large Language Models</em>. ICLR 2022. <a href="https://arxiv.org/abs/2106.09685">https://arxiv.org/abs/2106.09685</a></li>
<li>Wei, J., et al. (2022). <em>Chain-of-Thought Prompting Elicits Reasoning in Large Language Models</em>. NeurIPS 2022. <a href="https://arxiv.org/abs/2201.11903">https://arxiv.org/abs/2201.11903</a></li>
<li>Brown, T. B., et al. (2020). <em>Language Models are Few-Shot Learners</em>. NeurIPS 2020. <a href="https://arxiv.org/abs/2005.14165">https://arxiv.org/abs/2005.14165</a></li>
<li>Liu, H., et al. (2024). <em>When Should You Fine-Tune Your LLM? A Comprehensive Comparison with RAG</em>. <a href="https://arxiv.org/abs/2403.06634">https://arxiv.org/abs/2403.06634</a></li>
<li>Ouyang, L., et al. (2022). <em>Training language models to follow instructions with human feedback</em>. NeurIPS 2022. <a href="https://arxiv.org/abs/2203.02155">https://arxiv.org/abs/2203.02155</a></li>
<li>Khattab, O., et al. (2023). <em>DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines</em>. <a href="https://arxiv.org/abs/2310.03714">https://arxiv.org/abs/2310.03714</a></li>
</ul>

---

**Wybór techniki to decyzja architektoniczna na lata.** W cotygodniowym newsletterze RAGPolska.pl publikujemy konkretne case studies, decyzje, lessons learned z polskich wdrożeń. [Zapisz się — bezpłatnie](#newsletter-signup).
