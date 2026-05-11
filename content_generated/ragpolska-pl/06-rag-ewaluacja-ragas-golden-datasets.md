---
title: "RAG ewaluacja — RAGAs, golden datasets, production metrics (2026)"
slug: "rag-ewaluacja-ragas-golden-datasets"
excerpt: "Bez ewaluacji nie wiesz, czy RAG działa. Pełna metodologia: RAGAs framework, golden datasets, production metrics, A/B testing strategies."
category_slug: "techniki-rag"
tags: "RAG evaluation, RAGAs, metrics, golden dataset, średni"
reading_time: 11
is_published: true
is_featured: false
meta_title: "RAG ewaluacja — RAGAs, metrics, golden datasets (2026)"
meta_description: "Pełna metodologia ewaluacji RAG: RAGAs framework, golden datasets, retrieval i generation metrics, production monitoring."
funnel: "MOFU"
author_slug: "marek-porycki"
related_slugs: "rag-enterprise-architektura, hybrid-search-dense-sparse-reranking, rag-production-deployment-checklist"
product_slugs: ""
---

W większości RAG wdrożeń ewaluacja jest myślą po fakcie. "Wdrożymy, zobaczymy jak działa". Ten approach kończy się jednym z dwóch scenariuszy: (1) RAG działa "OK", ale nie wiemy czy mógłby działać lepiej, jakie konkretne improvements warto inwestować; lub (2) RAG działa źle, ale nie potrafimy zlokalizować problemu (retrieval? generation? embedding? chunking?). Bez systematic evaluation iteracja jest ślepa.

Dobra ewaluacja RAG odpowiada na trzy pytania: (1) czy retrieval znajduje relevant context? (2) czy LLM korzysta z context właściwie? (3) czy końcowa odpowiedź odpowiada na query użytkownika? Każde pytanie wymaga różnych metrics i methodologies.

Ten tekst opisuje pełną framework ewaluacji RAG dla production systems. Adresat: ML engineers, RAG developers, dyrektorzy techniczni odpowiedzialni za quality production AI.

## Trzy poziomy ewaluacji

**Poziom 1: component evaluation.**

Each component testowany osobno:
- Retrieval evaluation (czy znajduje right docs?);
- Embedding quality (czy similar queries dają similar embeddings?);
- Re-ranking effectiveness (czy poprawia order?).

**Poziom 2: end-to-end evaluation.**

Cały pipeline testowany razem:
- Czy końcowa odpowiedź jest correct?
- Czy odpowiedź jest grounded w context (no hallucinations)?
- Czy odpowiedź jest helpful?

**Poziom 3: production monitoring.**

W produkcji, na real traffic:
- User satisfaction (CSAT, NPS);
- Engagement metrics (czy users wracają?);
- Adoption metrics (% docelowej grupy używa);
- Failure modes (kiedy RAG zawodzi).

Pełna evaluation strategy obejmuje wszystkie trzy poziomy.

## Retrieval metrics

**Mean Reciprocal Rank (MRR):** dla każdego query, 1 / pozycja pierwszego relevant doc. Avg across queries.

**Recall@k:** % queries gdzie relevant doc jest w top-k.

**Precision@k:** % top-k results that are relevant.

**nDCG@k (Normalized Discounted Cumulative Gain):** uwzględnia degree of relevance (nie tylko binary), waguje pozycję.

**Hit rate:** czy ANY relevant doc jest w top-k (binary).

**Wymagania:** golden dataset z (query, relevant_docs) pairs.

## Generation metrics — RAGAs framework

RAGAs (RAG Assessment) to popular open-source framework dla RAG evaluation, używający LLM-as-judge.

**Faithfulness:** czy odpowiedź jest grounded w retrieved context? Czy LLM hallucines fakty spoza context?

LLM-as-judge:
1. Z odpowiedzi extract factual claims;
2. Dla każdego claim, weryfikuj czy context supports;
3. Faithfulness = % claims supported by context.

**Answer Relevance:** czy odpowiedź odpowiada na konkretne query?

LLM-as-judge:
1. LLM generuje synthetic queries z odpowiedzi;
2. Compare similarity z original query;
3. Higher similarity = more relevant answer.

**Context Relevance:** czy retrieved context jest relevant dla query?

LLM-as-judge:
1. LLM identyfikuje sentences w context potrzebne dla odpowiedzi;
2. Context relevance = % sentences potrzebnych.

**Context Recall:** dla queries z ground truth answer, czy potrzebne info jest w retrieved context?

**Context Precision:** czy relevant info jest na top of retrieved context (good ranking)?

**Implementacja RAGAs:**

```python
from ragas import evaluate
from ragas.metrics import (
    faithfulness,
    answer_relevancy,
    context_precision,
    context_recall
)
from datasets import Dataset

# Prepare evaluation dataset
data = {
    "question": ["Ile dni urlopu mam?"],
    "answer": ["Zgodnie z polityką firmy masz 26 dni urlopu wypoczynkowego rocznie."],
    "contexts": [["Polityka HR: Każdy pracownik ma 26 dni urlopu wypoczynkowego..."]],
    "ground_truth": ["26 dni urlopu wypoczynkowego rocznie."]
}
dataset = Dataset.from_dict(data)

# Run evaluation
result = evaluate(
    dataset=dataset,
    metrics=[
        faithfulness,
        answer_relevancy,
        context_precision,
        context_recall,
    ],
)
print(result)
```

## Golden dataset — fundament ewaluacji

Golden dataset to zbiór (query, expected_answer, relevant_docs) — ground truth do mierzenia performance.

**Sposoby tworzenia:**

**Approach 1: manual creation by domain experts.**
- Najwyższa jakość;
- Czasochłonne (1-3 godziny per 10 examples z reasonable quality);
- Recommended size: minimum 50 examples, optimal 200-500.

**Approach 2: synthetic generation z LLM.**
- LLM generuje queries dla pre-existing documents;
- Tania i szybka;
- Lower quality (LLM bias);
- Useful jako bootstrap, supplementowane manual examples.

**Approach 3: from production logs.**
- Real user queries z production;
- Manual labeling (które dokumenty były relevant);
- Najbardziej representative;
- Wymaga production deployment najpierw.

**Approach 4: existing benchmarks.**
- Generic benchmarks (MS MARCO, BEIR) — limited dla domain-specific use cases;
- Domain-specific benchmarks rzadko dostępne.

**Best practice:** combine approaches. Start z synthetic (50-100), supplement z domain expert manual (50-100), iterate z production logs (500+).

## Polish-specific evaluation considerations

**Translacja golden dataset:** istniejące benchmarki głównie po angielsku. Translacja na polski:
- Manual translacja by polski speaker (najlepsze);
- LLM translation (acceptable dla bootstrap, ale weryfikuj);
- Sprawdź czy semantic meaning preserved.

**Polish-specific test cases:**
- Polish odmiany słów (czy retrieval matches "urlopu", "urlopów"?);
- Polish akronimy (RODO, NIS2, ZUS — czy retrieval handles?);
- Polish names (imiona, nazwiska, miasta);
- Mixed Polish-English queries (frequent w business contexts).

**LLM-as-judge z polskim:** GPT-4o, Claude Sonnet 4.6 dobre dla polskiego. Lokalne modele (Llama 3.3 70B) acceptable, ale lower quality dla nuance.

## Production monitoring — beyond benchmarks

Benchmarks są snapshot. Production wymaga ciągłego monitoringu:

**Metryka 1: latency distribution.**

```
P50, P95, P99 dla:
- Embedding generation;
- Vector search;
- Re-ranking;
- LLM generation;
- End-to-end.
```

Anomalie: spike w P99 może wskazywać na specific edge cases failing.

**Metryka 2: user satisfaction.**

- Thumbs up/down per response (in-app);
- Detailed feedback (when offered);
- Follow-up questions (negatywny signal — initial answer nie wystarczył);
- Conversation length distribution.

**Metryka 3: source attribution.**

- Czy users klikają source citations? (engagement);
- Czy source documents są relevant w opinii users?

**Metryka 4: failure modes.**

- Empty context (retrieval found nothing);
- Hallucinated answers (post-hoc analysis);
- Off-topic responses;
- Contradictory answers across sessions.

**Metryka 5: business impact.**

- Reduction w support tickets (jeśli RAG dla customer service);
- Time saved (jeśli RAG dla pracowników);
- Conversion impact (jeśli RAG w sales).

## A/B testing dla RAG

Dla iteracji nad RAG quality, A/B testing jest gold standard.

**Co A/B testować:**
- Different embedding models;
- Chunking strategies;
- Top-k values (5 vs 10 vs 20);
- With/without re-ranking;
- Different LLMs dla generation;
- Prompt templates.

**Setup:**
- Random assignment users do variants A i B;
- Metryki tracked per variant;
- Sufficient sample size dla statistical significance.

**Sample size considerations:**
- Dla detecting 5% improvement w binary metric (satisfaction): typowo 1000+ users per variant;
- Dla continuous metrics (latency): często mniejsze samples wystarczą;
- Power analysis przed launch.

**Praktyczne challenges:**
- Many RAG aplikacji ma niski wolumen (hundreds queries/day) — A/B test trwa tygodnie;
- Quality metrics wymagają labeling, time-consuming;
- Confounding factors (questions o różnej trudności w różnych okresach).

**Alternative dla małego volume:**
- Offline evaluation z golden dataset;
- Expert review;
- Synthetic experiments z LLM judge.

## Common evaluation pitfalls

**Pitfall 1: tylko offline benchmarks.** Real user behavior może różnić się od benchmark queries. Production monitoring kluczowe.

**Pitfall 2: jeden number = całość quality.** RAG ma multiple dimensions. Pojedyncza metryka rzadko captures.

**Pitfall 3: golden dataset too small.** 20 examples nie daje statistically meaningful insights. Minimum 50, target 200+.

**Pitfall 4: LLM-as-judge z weak LLM.** Judging requires good judge. Use top models (GPT-4o, Claude Sonnet) dla evaluation.

**Pitfall 5: ignorowanie cost/latency tradeoffs.** Best quality możliwe ale za $$$ i 5 sekund per query. Production needs balance.

**Pitfall 6: brak baseline comparison.** "Recall@5 = 0.85". Czy to dobrze? Bez baseline (poprzednia wersja, alternative approach) — bezsensu.

**Pitfall 7: optimization tylko per offline metrics.** Production users mogą uczyć się obchodzić limitations RAG, real-world quality różni od benchmarks.

## Continuous evaluation strategy

Dla production RAG:

**Weekly:**
- Production metrics review (latency, user satisfaction, failure rate);
- Sample 20-50 random conversations dla quality check.

**Monthly:**
- Full evaluation na golden dataset (regression check);
- Update golden dataset z nowych production examples;
- A/B test results review (jeśli aktywne).

**Quarterly:**
- Deep dive analysis (failure modes, edge cases);
- Embedding model evaluation (czy nowsze warto upgrade);
- Re-ranking model evaluation;
- Strategic decisions (architectural changes).

**Yearly:**
- Comprehensive audit (all components);
- Comparison alternative architectures;
- Plan major upgrades.

## Tools ecosystem

**RAGAs:** open-source RAG evaluation framework. Łatwy start. Comprehensive metrics.

**LangSmith (LangChain):** komercyjny. Tracing, evaluation, monitoring zintegrowane. $39/m starter.

**LlamaIndex evaluation:** built-in evaluation tools w LlamaIndex framework.

**ARES:** academic research framework dla RAG evaluation.

**TruEra (TruLens):** open-source observability dla LLM apps, w tym RAG.

**Custom:** dla unique needs, custom evaluation pipelines z pandas + LLM judges.

## Bibliografia

<ul>
<li>Es, S., et al. (2024). <em>RAGAs: Automated Evaluation of Retrieval Augmented Generation</em>. EACL 2024. <a href="https://arxiv.org/abs/2309.15217">https://arxiv.org/abs/2309.15217</a></li>
<li>RAGAs Team. (2024). <em>RAGAs Documentation</em>. <a href="https://docs.ragas.io/">https://docs.ragas.io/</a></li>
<li>Saad-Falcon, J., et al. (2023). <em>ARES: An Automated Evaluation Framework for Retrieval-Augmented Generation Systems</em>. <a href="https://arxiv.org/abs/2311.09476">https://arxiv.org/abs/2311.09476</a></li>
<li>Liu, Y., et al. (2023). <em>G-Eval: NLG Evaluation using GPT-4 with Better Human Alignment</em>. EMNLP 2023. <a href="https://arxiv.org/abs/2303.16634">https://arxiv.org/abs/2303.16634</a></li>
<li>BEIR Team. (2021). <em>BEIR: Heterogeneous Benchmark for Zero-shot Evaluation of IR Models</em>. <a href="https://arxiv.org/abs/2104.08663">https://arxiv.org/abs/2104.08663</a></li>
<li>LangSmith. (2024). <em>LLM Application Observability and Evaluation</em>. <a href="https://www.langchain.com/langsmith">https://www.langchain.com/langsmith</a></li>
<li>TruLens. (2024). <em>Evaluation and Tracking for LLM Applications</em>. <a href="https://www.trulens.org/">https://www.trulens.org/</a></li>
</ul>

---

**Bez ewaluacji RAG iteracja jest ślepa.** W cotygodniowym newsletterze RAGPolska.pl publikujemy konkretne evaluation pipelines, golden datasets, A/B test results. [Zapisz się — bezpłatnie](#newsletter-signup).
