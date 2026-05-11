---
title: "Vector databases — Qdrant, Weaviate, pgvector, Pinecone (2026)"
slug: "vector-databases-qdrant-weaviate-pgvector"
excerpt: "Pełen przewodnik po vector databases dla RAG. Qdrant, Weaviate, pgvector, Pinecone, Milvus. Benchmarki, wybór per skala, deployment."
category_slug: "infrastruktura"
tags: "vector database, Qdrant, Weaviate, pgvector, Pinecone, średni"
reading_time: 11
is_published: true
is_featured: false
meta_title: "Vector databases dla RAG — porównanie 2026"
meta_description: "Pełne porównanie vector databases: Qdrant, Weaviate, pgvector, Pinecone, Milvus. Benchmarki, koszty, wybór per skala i use case."
funnel: "TOFU"
author_slug: "marek-porycki"
related_slugs: "rag-enterprise-architektura, embeddings-model-wymiary-polskie-korpusy, hybrid-search-dense-sparse-reranking"
product_slugs: ""
---

W RAG architekturze vector database to silnik. To gdzie żyją wszystkie embeddings i gdzie dzieje się semantic search. Zła decyzja vector DB oznacza: latency w produkcji, skalowanie problems, koszty rosnące dramatycznie z rozmiarem, ograniczenia features (np. brak hybrid search). Wybór jest szczególnie ważny — vector DBs są stateful, migracja między platformami to wieloetapowy projekt.

W 2026 roku krajobraz vector DB jest dojrzały: open-source liders (Qdrant, Weaviate, Milvus), commercial managed (Pinecone), simple solutions dla istniejącej infrastruktury (pgvector dla PostgreSQL). Każdy ma swoje mocne i słabe strony.

Ten tekst opisuje praktyczny wybór vector DB dla polskiej średniej firmy z benchmarks, deployment considerations, cost analysis. Adresat: ML engineers, DevOps, architekci AI.

## Krótkie przypomnienie — czym jest vector DB

Vector database to specjalizowana baza danych zoptymalizowana pod search w wysoko-wymiarowej przestrzeni wektorów. Klasyczne RDBMS (MySQL, PostgreSQL bez extensions) są niewydajne dla similarity search w 1024-3072 wymiarach.

Główne features:
- **Storage** dla wektorów (typowo float32, czasem int8 z kompresją);
- **Approximate Nearest Neighbor search (ANN)** — algorytmy jak HNSW, IVF, ScaNN dla szybkiego znajdowania top-k podobnych wektorów;
- **Filtering** — combine vector search z metadata filters;
- **Hybrid search** — combine dense (vectors) z sparse (BM25);
- **Indexing** — efficient updates bez pełnego re-build.

## Qdrant — open-source leader

**Charakterystyka:**
- Open-source (Apache 2.0).
- Napisany w Rust (wysoka wydajność).
- Hosted lub self-hosted.
- Jeden z najszybszych w benchmarks dla typowych RAG workloadów.

**Features:**
- HNSW indexing (efficient ANN);
- Filtering on metadata;
- Hybrid search (dense + sparse);
- Multi-vector per record;
- Snapshots i backup;
- Distributed deployment (cluster).

**Deployment:**
- Self-hosted Docker / Kubernetes;
- Qdrant Cloud (managed);
- Qdrant Hybrid Cloud (managed control, your infrastructure).

**Cena:**
- Self-hosted: tylko koszty infrastruktury;
- Cloud: od $40/m za starter, scale per usage.

**Idealne use case:**
- Średnie i większe RAG deployments;
- Performance-critical applications;
- Open-source preferowane.

## Weaviate — features-rich

**Charakterystyka:**
- Open-source (BSD-3).
- Napisany w Go.
- Bardziej "feature-rich" niż Qdrant (built-in modules dla embeddings, OCR, classification).

**Features:**
- HNSW indexing;
- Multi-tenancy (separation per użytkownik/team);
- Built-in vectorizers (transformers, CLIP, etc.);
- Generative search (LLM integration built-in);
- Hybrid search;
- GraphQL API.

**Deployment:**
- Self-hosted;
- Weaviate Cloud Services (managed);
- Various cloud marketplaces.

**Cena:**
- Self-hosted: tylko infra;
- Cloud: od ~$25/m starter.

**Idealne use case:**
- Multi-tenant systems;
- Feature-rich requirements;
- Teams które chcą built-in vectorization.

## pgvector — extension dla PostgreSQL

**Charakterystyka:**
- Open-source extension dla PostgreSQL.
- Najprostszy deployment jeśli masz już Postgres.
- Performance gorszy niż dedicated vector DBs, ale wystarcza dla wielu use cases.

**Features:**
- Vector type w PostgreSQL;
- HNSW i IVFFlat indexing (od pgvector 0.5+);
- Native PostgreSQL features (transactions, joins, ACID);
- Hybrid search z full-text PostgreSQL.

**Deployment:**
- Każdy PostgreSQL z extension installed;
- AWS RDS, Google Cloud SQL, Azure z pgvector support.

**Cena:**
- Tylko koszt PostgreSQL hosting (jeśli masz, prawie zero incremental cost).

**Idealne use case:**
- Już używacie PostgreSQL;
- Małe-średnie skale (<10M vectors);
- Mixed transactional + vector workloads;
- Kiedy "good enough" performance jest wystarczające.

**Limitations:**
- Performance ~3-5x gorszy niż dedicated vector DBs przy dużych skalach;
- Mniej zaawansowane filtering niż Qdrant/Weaviate;
- Limited multi-tenancy features.

## Pinecone — managed enterprise

**Charakterystyka:**
- Komercyjny, managed-only.
- Najszerzej używana platforma w US enterprise.
- Pioneer w RAG-specific features.

**Features:**
- Managed (zero ops);
- Multi-region;
- Hybrid search;
- Namespaces (multi-tenancy);
- Filtering, metadata.

**Cena:**
- Free tier do 1 index, 100k vectors;
- Pay-per-use od ~$70/m;
- Enterprise contracts negocjowane.

**Idealne use case:**
- Brak zespołu DevOps do utrzymania vector DB;
- US-based companies (data residency);
- Enterprise z budżetem na managed services.

**Limitations:**
- Vendor lock-in;
- Wyższe koszty long-term niż self-hosted alternatives;
- Compliance considerations dla EU (data residency w EU dostępna ale ograniczona).

## Milvus — enterprise scale

**Charakterystyka:**
- Open-source (Apache 2.0).
- Specjalizowane dla bardzo dużych skali (>100M vectors).
- Cloud-native architecture (Kubernetes).

**Features:**
- Wsparcie dla wielu indexing algorithms (HNSW, IVF, ScaNN, DiskANN);
- GPU acceleration (dla extreme performance);
- Multi-tenancy;
- Time-travel queries;
- Distributed natively.

**Deployment:**
- Self-hosted (Kubernetes);
- Zilliz Cloud (managed Milvus).

**Idealne use case:**
- Bardzo duża skala (>50M vectors);
- Performance-critical applications wymagające GPU;
- Enterprise z dedykowanym DevOps team.

## ChromaDB — dla developmentu

**Charakterystyka:**
- Open-source, simplest setup.
- Zoptymalizowany dla developmentu i prototypów.

**Features:**
- Embedded mode (in-memory, w aplikacji);
- Client-server mode dla production.

**Idealne use case:**
- Pierwsze eksperymenty;
- Prototypes;
- Małe applications (do 1M vectors).

**Limitations:**
- Performance gorszy niż production-grade alternatives;
- Limited features dla enterprise.

## Benchmarks — performance comparison

Dla typowego workload (10M vectors 768-dim, 100 QPS):

**Latency p99 (search top-10):**
- Qdrant: 8-15 ms;
- Weaviate: 12-25 ms;
- Milvus: 10-20 ms;
- Pinecone: 30-60 ms (ze względu na network);
- pgvector (HNSW): 25-45 ms.

**Throughput max:**
- Qdrant: ~3000 QPS na nodzie z 32 cores;
- Weaviate: ~2000 QPS na nodzie z 32 cores;
- Milvus: ~5000 QPS (z GPU acceleration);
- Pinecone: scales horizontally automatically;
- pgvector: ~500 QPS na nodzie.

**Storage efficiency:**
- Qdrant: dobry (Rust, efficient memory).
- Weaviate: średni (Go z overhead).
- pgvector: niski (PostgreSQL overhead).

## Wybór per skala

**Małe (<1M vectors):**
- Najprościej: pgvector lub Chroma.
- Jeśli już Postgres: pgvector;
- Jeśli zaczynacie greenfield: Chroma dla developmentu, Qdrant dla produkcji.

**Średnie (1M-50M vectors):**
- Qdrant lub Weaviate dla self-hosted.
- pgvector wciąż możliwy, ale near limit.
- Pinecone jeśli managed preferowane.

**Duże (>50M vectors):**
- Milvus z GPU acceleration.
- Qdrant cluster.
- Pinecone enterprise tier.

**Bardzo duże (>1B vectors):**
- Milvus distributed.
- Custom solutions (FAISS + custom serving).
- Specjalistyczne komercyjne (Vespa, OpenSearch z vector search).

## Deployment considerations

**Self-hosted:**

Plusy:
- Pełna kontrola;
- Niższe long-term koszty;
- Compliance (dane lokalne);
- Customization possibilities.

Minusy:
- Wymaga DevOps competence;
- Maintenance overhead;
- Backup/DR własna odpowiedzialność.

**Managed:**

Plusy:
- Zero ops;
- Automatic scaling;
- Built-in backup/DR;
- SLA support.

Minusy:
- Higher costs;
- Vendor lock-in;
- Compliance considerations;
- Less customization.

**Hybrid (managed control plane, self-hosted data):**
- Qdrant Hybrid Cloud, Weaviate Hybrid;
- Best of both worlds — managed updates, własne dane;
- Cena średnia.

## Praktyczna konfiguracja Qdrant — przykład

Najczęstsza rekomendacja dla polskiej średniej firmy: Qdrant self-hosted.

**Setup (Docker):**

```bash
docker run -p 6333:6333 -p 6334:6334 \
  -v $(pwd)/qdrant_storage:/qdrant/storage:z \
  qdrant/qdrant
```

**Python client:**

```python
from qdrant_client import QdrantClient
from qdrant_client.http import models

client = QdrantClient(host="localhost", port=6333)

# Create collection
client.create_collection(
    collection_name="firm_knowledge",
    vectors_config=models.VectorParams(
        size=1024,  # embedding dimensions
        distance=models.Distance.COSINE
    )
)

# Add vectors
client.upsert(
    collection_name="firm_knowledge",
    points=[
        models.PointStruct(
            id=1,
            vector=[0.12, 0.45, ...],  # 1024 floats
            payload={"text": "...", "source": "polityka_HR.pdf"}
        ),
        # ... more points
    ]
)

# Search
results = client.search(
    collection_name="firm_knowledge",
    query_vector=[0.13, 0.42, ...],
    limit=5
)
```

## Najczęstsze błędy w wyborze vector DB

**Błąd 1: Pinecone "bo enterprise standard".** Standardem w US tech, niekoniecznie najlepszym dla polskiej średniej firmy. Sprawdź alternatives.

**Błąd 2: Chroma w produkcji.** Świetna do developmentu, problematyczna w produkcji przy skali.

**Błąd 3: pgvector przy dużej skali.** Działa do 5-10M vectors. Powyżej — performance issues.

**Błąd 4: ignorowanie hybrid search.** Czysty vector search jest często gorszy niż hybrid (vectors + BM25). Wybór DB wpływa na łatwość hybrid implementation.

**Błąd 5: brak monitoring i benchmarking własnego workload.** Generic benchmarks nie zawsze odzwierciedlają Twoje use case.

**Błąd 6: zbyt wczesna optymalizacja.** Zaczynanie od Milvus distributed setup dla 100k vectors. Przeskalowane.

**Błąd 7: ignorowanie compliance considerations.** Pinecone w US data centers dla danych RODO — rozważ data residency.

## Migracja między vector DB

Jeśli zmieniasz vector DB:

1. Export wszystkich vectors z metadata (jeśli DB pozwala);
2. Setup nowej DB z tymi samymi specs (dimensions, distance metric);
3. Import (batch);
4. Weryfikacja accuracy (porównaj search results);
5. Cutover (zmiana w aplikacji);
6. Wycofanie starej DB po validation period.

Migracja 10M vectors typowo: 2-5 dni pracy + downtime planning.

## Bibliografia

<ul>
<li>Qdrant. (2024). <em>Qdrant Documentation</em>. <a href="https://qdrant.tech/documentation/">https://qdrant.tech/documentation/</a></li>
<li>Weaviate. (2024). <em>Weaviate Documentation</em>. <a href="https://weaviate.io/developers/weaviate">https://weaviate.io/developers/weaviate</a></li>
<li>pgvector. (2024). <em>pgvector: Open-source vector similarity search for Postgres</em>. <a href="https://github.com/pgvector/pgvector">https://github.com/pgvector/pgvector</a></li>
<li>Pinecone. (2024). <em>Pinecone Documentation</em>. <a href="https://docs.pinecone.io/">https://docs.pinecone.io/</a></li>
<li>Milvus. (2024). <em>Milvus Documentation</em>. <a href="https://milvus.io/docs">https://milvus.io/docs</a></li>
<li>Malkov, Y. A., & Yashunin, D. A. (2018). <em>Efficient and robust approximate nearest neighbor search using Hierarchical Navigable Small World graphs</em>. <em>IEEE TPAMI</em>, 42(4), 824–836. <a href="https://doi.org/10.1109/TPAMI.2018.2889473">https://doi.org/10.1109/TPAMI.2018.2889473</a></li>
<li>ANN Benchmarks. (2024). <em>Benchmarks for Approximate Nearest Neighbors</em>. <a href="http://ann-benchmarks.com/">http://ann-benchmarks.com/</a></li>
</ul>

---

**Vector DB to silnik RAG — warto wybrać świadomie.** W cotygodniowym newsletterze RAGPolska.pl publikujemy benchmarki, deployment guides, case studies. [Zapisz się — bezpłatnie](#newsletter-signup).
