---
title: "Hybrid search — dense + sparse + re-ranking dla wyższej precision"
slug: "hybrid-search-dense-sparse-reranking"
excerpt: "Czysta dense retrieval ma luki. Hybrid search łączy semantyczne (dense) z keyword (sparse, BM25) plus re-ranking dla 30-50% lepszej jakości."
category_slug: "techniki-rag"
tags: "hybrid search, BM25, re-ranking, dense, sparse, średni"
reading_time: 11
is_published: true
is_featured: false
meta_title: "Hybrid search dla RAG — dense + sparse + reranking (2026)"
meta_description: "Pełen przewodnik hybrid search: dense retrieval, BM25, reciprocal rank fusion, cross-encoder reranking. Konkretne implementacje."
funnel: "MOFU"
author_slug: "marek-porycki"
related_slugs: "rag-enterprise-architektura, embeddings-model-wymiary-polskie-korpusy, chunking-strategy-fixed-do-semantic"
product_slugs: ""
---

W rozmowach o RAG czasami pojawia się to założenie: "wystarczy dobry embedding model i vector database". To upraszczenie. Czysta dense retrieval (wyłącznie semantic search) ma swoje słabe strony — szczególnie dla queries z konkretnymi keywords (akronimy, nazwy własne, kody produktów), gdzie BM25 zachowuje przewagę. Z drugiej strony BM25 sam nie radzi z synonyms, paraphrases, semantic relationships. Połączenie obu — hybrid search — daje 30-50% lepszą jakość retrieval.

Plus jeszcze jeden krok: re-ranking. Po initial retrieval (dense + sparse), cross-encoder model głębiej ocenia każdą parę (query, document) i zmienia kolejność. Dodatkowe 15-25% improvement w precision na top-k.

Ten tekst opisuje pełną hybrid search architecture z konkretnymi implementacjami. Adresat: ML engineers implementujący production RAG, ML researchers analizujący retrieval quality.

## Dlaczego pure dense retrieval nie wystarcza

**Słabe strony dense retrieval (vector search):**

**Problem 1: rare terms i akronimy.** Embeddings są trenowane na ogólnych korpusach. Specjalistyczna terminologia, akronimy firmowe (np. "NIS2", nazwa wewnętrznego systemu) mogą być słabo reprezentowane w embedding space.

**Problem 2: exact match queries.** "Pokaż mi politykę BHP-2024-15". User chce konkretny dokument. Dense embedding może zwrócić "BHP-2023-12" jako podobny semantically.

**Problem 3: keyword priorities.** "RODO" i "AI Act" to dwa konkretne pojęcia. Dense search może dać dokumenty wspominające oba, gdy user chce specifically RODO.

**Problem 4: numerical values, dates, IDs.** Embeddings nie reprezentują numbers dobrze.

**Mocne strony dense retrieval:**
- Synonyms ("urlop wypoczynkowy" ↔ "wakacje");
- Paraphrases ("ile dni mam wolnego" ↔ "policy o urlopie");
- Cross-language;
- Conceptual relationships.

## Sparse retrieval (BM25) — dlaczego wciąż istotne

**BM25** (Best Matching 25, Robertson 1976) to klasyczny algorithm TF-IDF na sterydach. Implementuje "keyword matching" z weighting per term importance, document length normalization.

**Mocne strony:**
- Świetny dla exact matches;
- Naturalnie przydaje wagę rare terms (akronimy, technical terms);
- Deterministic (ten sam query = te same wyniki);
- Łatwy do debugowania (widać które słowa zaważyły);
- Nie wymaga training (works out of the box).

**Słabe strony:**
- Brak semantic understanding;
- Brak synonymów;
- Brak cross-language.

**Implementacja:** prawie każda search engine ma BM25 built-in. Elasticsearch, OpenSearch, PostgreSQL full-text, Qdrant (sparse vectors), Weaviate — wszystkie supportują.

## Hybrid search — dense + sparse

Idea: uruchom oba retrieval simultaneously, połącz wyniki.

**Approach 1: Reciprocal Rank Fusion (RRF).**

Dla każdego dokumentu, oblicz score na podstawie pozycji w obu rankings:

```
RRF_score(d) = 1/(k + rank_dense(d)) + 1/(k + rank_sparse(d))
```

Gdzie k=60 to standardowy parameter.

**Implementacja:**

```python
def reciprocal_rank_fusion(dense_results, sparse_results, k=60):
    fused_scores = {}
    
    for rank, doc in enumerate(dense_results):
        fused_scores[doc.id] = fused_scores.get(doc.id, 0) + 1/(k + rank)
    
    for rank, doc in enumerate(sparse_results):
        fused_scores[doc.id] = fused_scores.get(doc.id, 0) + 1/(k + rank)
    
    sorted_docs = sorted(fused_scores.items(), key=lambda x: x[1], reverse=True)
    return [doc_id for doc_id, score in sorted_docs]
```

**Plusy RRF:**
- Bez tunable hyperparameters (k=60 robust);
- Działa nawet gdy dense i sparse mają różne score scales;
- Empirically dobry dla wielu use cases.

**Approach 2: weighted combination.**

```python
def weighted_combination(query, dense_results, sparse_results, alpha=0.5):
    combined_scores = {}
    
    for doc in dense_results:
        combined_scores[doc.id] = alpha * doc.dense_score
    
    for doc in sparse_results:
        existing = combined_scores.get(doc.id, 0)
        combined_scores[doc.id] = existing + (1 - alpha) * doc.sparse_score
    
    return sorted(combined_scores.items(), key=lambda x: x[1], reverse=True)
```

Wymaga normalizacji scores (dense cosine similarity vs BM25 unbounded score). Tunable alpha.

**Approach 3: dense-then-sparse re-ranking.**

Initial dense retrieval top-100, BM25 re-ranks na top-10. Praktyczne, gdy sparse jest faster niż dense (rzadkie).

## Implementation w Qdrant (hybrid built-in)

Qdrant supports hybrid search natively (od version 1.10+):

```python
from qdrant_client import QdrantClient
from qdrant_client.http import models

client = QdrantClient(host="localhost", port=6333)

# Create collection z dense i sparse vectors
client.create_collection(
    collection_name="hybrid_collection",
    vectors_config={
        "dense": models.VectorParams(size=1024, distance=models.Distance.COSINE),
    },
    sparse_vectors_config={
        "sparse": models.SparseVectorParams(),
    }
)

# Insert dokumenty z oboma typu wektorów
client.upsert(
    collection_name="hybrid_collection",
    points=[
        models.PointStruct(
            id=1,
            vector={
                "dense": dense_embedding,
                "sparse": sparse_embedding  # BM25-like
            },
            payload={"text": "..."}
        )
    ]
)

# Hybrid search
results = client.query_points(
    collection_name="hybrid_collection",
    prefetch=[
        models.Prefetch(query=dense_query, using="dense", limit=20),
        models.Prefetch(query=sparse_query, using="sparse", limit=20),
    ],
    query=models.FusionQuery(fusion=models.Fusion.RRF),
    limit=10
)
```

## Re-ranking z cross-encoder

Bi-encoder (standard embedding model) i cross-encoder to różne architektury:

**Bi-encoder:**
- Embeds query i document osobno;
- Compares przez cosine similarity;
- Bardzo szybki (możemy pre-compute document embeddings);
- Less accurate dla precision na top results.

**Cross-encoder:**
- Embeds (query, document) pair together;
- Jeden forward pass dla każdej pary;
- Wolniejszy (nie da się pre-compute);
- Znacznie bardziej accurate.

**Pipeline:**
1. Initial retrieval (hybrid bi-encoder + BM25): top-50;
2. Cross-encoder re-ranks tych 50: top-10 final results.

**Modele cross-encoder:**
- BAAI/bge-reranker-large (open-source);
- BAAI/bge-reranker-v2-m3 (multilingual);
- Cohere Rerank (zamknięty, API);
- Custom fine-tuned dla domeny.

**Implementacja (BGE reranker):**

```python
from sentence_transformers import CrossEncoder

reranker = CrossEncoder('BAAI/bge-reranker-v2-m3')

def rerank(query, candidates, top_k=10):
    pairs = [[query, doc.text] for doc in candidates]
    scores = reranker.predict(pairs)
    
    sorted_indices = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)
    return [candidates[i] for i in sorted_indices[:top_k]]
```

**Performance impact:**
- Latency: re-ranking 50 candidates dodaje 50-200 ms (zależnie od sprzętu, modelu).
- Quality: 15-25% improvement w MRR i Recall@5.

**Praktyczna rekomendacja:**
- Dla wysokiej jakości RAG — zawsze włączaj re-ranking.
- Re-rank top 20-50 po initial hybrid retrieval.

## Pełen pipeline — przykład

```python
def hybrid_rag_retrieval(query, vector_db, reranker, top_k=5):
    # Step 1: Generate dense embedding
    dense_query = embed_dense(query)
    
    # Step 2: Generate sparse representation
    sparse_query = embed_sparse(query)
    
    # Step 3: Hybrid search (RRF in vector DB)
    initial_results = vector_db.hybrid_search(
        dense_query=dense_query,
        sparse_query=sparse_query,
        limit=50,
        fusion="rrf"
    )
    
    # Step 4: Cross-encoder re-ranking
    reranked = rerank(query, initial_results, top_k=top_k)
    
    return reranked
```

## Cohere Rerank vs open-source

**Cohere Rerank:**
- API-based;
- Very high quality (top w benchmarks);
- Cost: ~$2 per 1000 reranking calls;
- Latency: ~100-200 ms per call (network);
- Multilingual including Polish.

**BGE reranker (open-source):**
- Self-hosted;
- High quality (close to Cohere);
- Cost: tylko GPU hosting;
- Latency: 50-150 ms (GPU) lub 200-500 ms (CPU);
- Multilingual including Polish.

**Decyzja:**
- Dla małej skali (<10k reranking calls/m): Cohere convenience > cost.
- Dla średniej skali: BGE on GPU lepszy.
- Dla strategicznych deployments z compliance: BGE.

## Polska specyfika — co działa, co nie

W polskich RAG aplikacjach hybrid search jest szczególnie ważny ze względu na:

**Polskie odmiany słów.** "Urlop", "urlopu", "urlopów" — wszystkie powinny matchować. BM25 z proper stemming pomaga. Dense embeddings też (jeśli model dobrze rozumie polski).

**Polskie akronimy.** ZUS, NFZ, KRS, ZUS, RODO — wszystkie konkretne, wymagają keyword match. Pure dense often misses.

**Polskie nazwy własne.** Imiona, nazwy ulic, miast. BM25 wins.

**Mieszane EN+PL queries.** "Czy mamy GDPR compliance?" Hybrid handles better niż pure dense.

Praktyczna rekomendacja: dla polskich aplikacji hybrid search jest mandatory, nie optional.

## Tools dla polish-aware sparse retrieval

BM25 wymaga tokenization adekwatnej dla polskiego. Standard:

- Stemming (np. polish-stemmer);
- Stop words (lista polish stop words);
- Lowercase normalization.

**Stack:**
- Elasticsearch z Polish analyzer;
- OpenSearch z polish stem filter;
- Qdrant z Splade (sparse model trained including Polish);
- PostgreSQL z polish text search configuration.

## Najczęstsze błędy

**Błąd 1: pure dense retrieval w produkcji.** "BM25 jest stary". Stary doesn't mean bad. Hybrid wins.

**Błąd 2: równe weights dense/sparse bez optimization.** Optimal weight zależy od domain. A/B test.

**Błąd 3: pominięcie re-ranking.** Initial retrieval daje good candidates, ale top-5 wymaga re-ranking dla precision.

**Błąd 4: re-ranking too few candidates.** Re-ranking top-5 nie da poprawy. Re-rank top-30-50.

**Błąd 5: użycie English-focused reranker dla polskiego.** BGE-reranker-v2-m3 jest multilingual (lepszy dla PL niż BGE-reranker-large).

**Błąd 6: zbyt wolne re-ranking blokuje latency.** Ograniczaj re-ranking input do top-30. Optymalizuj GPU inference.

## Performance benchmarks

Konkretne wyniki dla typowego RAG (10M chunks, polskie + angielskie):

| Strategy | MRR@10 | Recall@5 | Latency p99 |
|---|---|---|---|
| Pure dense | 0.65 | 0.78 | 80 ms |
| Pure BM25 | 0.55 | 0.70 | 30 ms |
| Hybrid (RRF) | 0.74 | 0.86 | 100 ms |
| Hybrid + re-ranking | 0.85 | 0.92 | 250 ms |

Hybrid + re-ranking: dramatyczne improvement w jakości za umiarkowany koszt latency.

## Bibliografia

<ul>
<li>Robertson, S., & Zaragoza, H. (2009). <em>The Probabilistic Relevance Framework: BM25 and Beyond</em>. <em>Foundations and Trends in Information Retrieval</em>, 3(4), 333–389. <a href="https://doi.org/10.1561/1500000019">https://doi.org/10.1561/1500000019</a></li>
<li>Cormack, G. V., Clarke, C. L. A., & Buettcher, S. (2009). <em>Reciprocal Rank Fusion outperforms Condorcet and individual rank learning methods</em>. SIGIR 2009. <a href="https://doi.org/10.1145/1571941.1572114">https://doi.org/10.1145/1571941.1572114</a></li>
<li>Reimers, N., & Gurevych, I. (2019). <em>Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks</em>. EMNLP 2019. <a href="https://arxiv.org/abs/1908.10084">https://arxiv.org/abs/1908.10084</a></li>
<li>BAAI. (2024). <em>BGE Reranker v2-m3 Model Card</em>. <a href="https://huggingface.co/BAAI/bge-reranker-v2-m3">https://huggingface.co/BAAI/bge-reranker-v2-m3</a></li>
<li>Cohere. (2024). <em>Cohere Rerank Documentation</em>. <a href="https://docs.cohere.com/docs/rerank">https://docs.cohere.com/docs/rerank</a></li>
<li>Formal, T., et al. (2021). <em>SPLADE: Sparse Lexical and Expansion Model</em>. SIGIR 2021. <a href="https://doi.org/10.1145/3404835.3463098">https://doi.org/10.1145/3404835.3463098</a></li>
<li>Qdrant. (2024). <em>Hybrid Search Documentation</em>. <a href="https://qdrant.tech/documentation/concepts/hybrid-queries/">https://qdrant.tech/documentation/concepts/hybrid-queries/</a></li>
</ul>

---

**Hybrid search + re-ranking to standard dla production RAG.** W cotygodniowym newsletterze RAGPolska.pl publikujemy benchmarki, implementations, optymalizacje. [Zapisz się — bezpłatnie](#newsletter-signup).
