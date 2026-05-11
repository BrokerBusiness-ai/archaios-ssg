---
title: "Chunking strategy — od fixed do semantic do agentic (2026)"
slug: "chunking-strategy-fixed-do-semantic"
excerpt: "Największa dźwignia poprawy RAG quality. Pełen przewodnik strategii chunkingu: fixed, recursive, semantic, agentic, contextual. Konkretne tradeoffs."
category_slug: "techniki-rag"
tags: "chunking, RAG, semantic, agentic, contextual retrieval, średni"
reading_time: 11
is_published: true
is_featured: false
meta_title: "Chunking strategy dla RAG — pełen przewodnik (2026)"
meta_description: "Pełna strategia chunkingu dokumentów dla RAG: fixed-size, recursive, semantic, agentic, contextual. Tradeoffs, narzędzia, benchmarki."
funnel: "MOFU"
author_slug: "marek-porycki"
related_slugs: "rag-enterprise-architektura, embeddings-model-wymiary-polskie-korpusy, hybrid-search-dense-sparse-reranking"
product_slugs: ""
---

W RAG architektury chunking to często niedoceniana dźwignia. Inżynierowie mogą wybrać najlepszy embedding model, najszybszy vector DB, najlepszy LLM — i wciąż mieć słabe wyniki, bo chunking jest niewłaściwy. W praktyce optymalizacja chunkingu może dać 20-40% improvement w retrieval quality, więcej niż zmiana embedding model na lepszy.

Filozofia chunkingu: dzielimy dokumenty na fragmenty, które są wystarczająco małe by efficient embed (limit context vector), ale wystarczająco duże by zawierać kompletną informację. Sweet spot zależy od typu dokumentu, queries, downstream LLM. Nie ma "best chunking strategy" — jest "best dla Twojego use case'u".

Ten tekst opisuje pięć strategii chunkingu od najprostszej (fixed) do najbardziej zaawansowanej (contextual retrieval Anthropic 2024). Adresat: ML engineers, architekci RAG implementacji.

## Strategia 1: fixed-size chunking

**Opis:** dziel dokument na fragmenty stałej długości (np. 500 tokens). Najprostszy approach.

**Implementacja:**

```python
def fixed_chunking(text, chunk_size=500, overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start = end - overlap
    return chunks
```

**Plusy:**
- Najprostsza implementacja;
- Predictable chunk size;
- Szybki processing.

**Minusy:**
- Cuts mid-sentence, mid-paragraph;
- Boundary między ważnymi konceptami;
- Często fragmentary chunks bez kontekstu.

**Kiedy używać:** prototypy, proof-of-concepts, teksty bez wyraźnej struktury (chat logs).

## Strategia 2: recursive chunking

**Opis:** rozdzielaj na hierarchii separators. Najpierw paragraphs (\n\n), potem sentences (. ), potem words ( ).

**Implementacja (LangChain):**

```python
from langchain.text_splitter import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50,
    separators=["\n\n", "\n", ". ", " ", ""]
)
chunks = splitter.split_text(text)
```

**Plusy:**
- Respektuje paragraph i sentence boundaries;
- Lepsze niż fixed dla typowych dokumentów;
- Wciąż prosta implementacja.

**Minusy:**
- Nie rozumie semantyki (czysto syntactic);
- Optimal chunk size wciąż zgadywanka.

**Kiedy używać:** default dla większości implementations. 80% RAG aplikacji wystarcza recursive chunking.

## Strategia 3: semantic chunking

**Opis:** używaj embeddings do identyfikacji semantic boundaries. Sentences z similar embedding stay together, dramatic similarity drop = chunk boundary.

**Implementacja koncepcyjna:**

```python
def semantic_chunking(text, threshold=0.7):
    sentences = split_sentences(text)
    embeddings = embed(sentences)
    
    chunks = []
    current_chunk = [sentences[0]]
    
    for i in range(1, len(sentences)):
        similarity = cosine_similarity(embeddings[i-1], embeddings[i])
        if similarity < threshold:
            chunks.append(' '.join(current_chunk))
            current_chunk = [sentences[i]]
        else:
            current_chunk.append(sentences[i])
    
    chunks.append(' '.join(current_chunk))
    return chunks
```

**Plusy:**
- Respektuje semantic structure;
- Chunks są naturalnie cohezyjne;
- Lepsze retrieval (chunks reprezentują complete ideas).

**Minusy:**
- Wolniejsze processing (wymaga embeddings podczas chunking);
- Threshold to hyperparameter wymagający tuningu;
- Variable chunk sizes.

**Kiedy używać:** dla wysokiej jakości RAG, gdzie performance gains uzasadniają complexity. Szczególnie dla dokumentów argumentacyjnych, edukacyjnych.

## Strategia 4: structure-aware chunking (markdown, HTML, code)

**Opis:** wykorzystaj structure dokumentu. Markdown headers, HTML sections, code functions stanowią naturalne boundaries.

**Implementacja dla Markdown:**

```python
from langchain.text_splitter import MarkdownHeaderTextSplitter

headers_to_split_on = [
    ("#", "Header 1"),
    ("##", "Header 2"),
    ("###", "Header 3"),
]
splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
chunks = splitter.split_text(markdown_text)
```

Chunks zachowują metadata o ich position w hierarchii (które headers).

**Implementacja dla code:**

```python
from langchain.text_splitter import RecursiveCharacterTextSplitter, Language

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=500,
    chunk_overlap=50
)
```

Splitter rozumie Python syntax (functions, classes).

**Plusy:**
- Najlepsza dla strukturyzowanych dokumentów;
- Metadata jako bonus (gdzie chunk pochodzi);
- Naturalne boundaries.

**Minusy:**
- Tylko dla strukturyzowanych formatów;
- Niektóre długie sekcje wymagają dalszego splittingu.

**Kiedy używać:** Markdown documentation, HTML, code repositories, structured PDFs.

## Strategia 5: agentic chunking

**Opis:** LLM decyduje boundaries. Model analizuje dokument, identyfikuje natural breaks, generuje chunks.

**Implementacja koncepcyjna:**

```python
def agentic_chunking(text, llm):
    prompt = f"""
    Dziel następujący tekst na cohezyjne fragmenty.
    Każdy fragment powinien zawierać complete idea lub topic.
    Nie cuts in middle sentences. Respect logical boundaries.
    
    Text:
    {text}
    
    Zwróć fragmenty jako JSON list of strings.
    """
    response = llm.complete(prompt)
    chunks = json.loads(response)
    return chunks
```

**Plusy:**
- Najwyższa jakość chunkingu (LLM intelligence);
- Adaptuje się do konkretnego dokumentu.

**Minusy:**
- Bardzo wolne (LLM call per dokument);
- Drogie (LLM API costs);
- Limited by LLM context window;
- Niedeterministyczne.

**Kiedy używać:** dla critical, high-value dokumentów. Nie dla volume processing.

## Strategia 6: contextual retrieval (Anthropic 2024)

**Opis:** Anthropic w 2024 roku opublikował dramatic improvement. Każdy chunk wzbogacony o kontekst (gdzie pochodzi z dokumentu, sąsiedztwo, summary parent section). Embeddings tych "contextualized chunks" dają 40-60% improvement retrieval.

**Implementacja:**

```python
def contextual_chunking(document, llm):
    chunks = recursive_chunking(document)
    contextualized_chunks = []
    
    for chunk in chunks:
        prompt = f"""
        <document>
        {document}
        </document>
        
        <chunk>
        {chunk}
        </chunk>
        
        Generate short context (50-100 words) explaining where this chunk fits in document.
        """
        context = llm.complete(prompt)
        contextualized_chunk = f"{context}\n\n{chunk}"
        contextualized_chunks.append(contextualized_chunk)
    
    return contextualized_chunks
```

Embed contextualized chunks. Search returns original chunks (without context overhead in LLM prompt).

**Plusy:**
- Dramatically better retrieval (Anthropic benchmark);
- Each chunk has its position context;
- Particularly good dla long, dense documents.

**Minusy:**
- LLM call per chunk (koszt setup);
- Requires re-processing if document changes.

**Kiedy używać:** dla wysokiej jakości RAG na large, complex documents (legal, technical, scientific).

## Optimal chunk size — research findings

Większość benchmarks wskazuje sweet spot 200-500 tokens dla typowych RAG aplikacji. Ale zależy od use case'u:

**Krótkie pytania faktyczne:** chunks 100-300 tokens (precision over context).

**Złożone analyse questions:** chunks 500-1000 tokens (więcej context per chunk).

**Long-form Q&A:** combine z parent document retrieval (search w small chunks, return large parents).

**Bardzo techniczne/specjalistyczne:** chunks 300-500 tokens z heavy overlap (zachowanie nuance).

**Conversational/casual content:** chunks 200-400 tokens (preserve context).

Przeprowadź A/B test z Twoim corpusem przed final decision.

## Chunk overlap — to take or not

Overlap (np. 50 tokens between consecutive chunks):

**Plusy:**
- Information at chunk boundaries nie traci się;
- Każda informacja appears w przynajmniej jednym complete chunk.

**Minusy:**
- Większa storage;
- Duplicate information w retrieval results.

**Recommendation:** 10-20% overlap dla większości use cases.

## Specific patterns dla różnych dokumentów

**PDFs z tabelami:** osobne chunks dla tabel (zachowanie struktury). Tools: Unstructured, Adobe PDF Services. Pełniejsze omówienie w artykule [RAG dla dokumentów wielomodalnych](/rag-dla-dokumentow-wielomodalnych-pdf).

**Long PDFs (>50 pages):** hierarchical chunking. Najpierw chapters, potem sections, potem paragraphs. Multi-vector retrieval.

**Conversational data (chat logs, support tickets):** chunk per conversation lub per ticket. Zachowanie kontekstu rozmowy.

**Code:** function-aware chunking. Tools: tree-sitter dla syntax-aware parsing.

**Multilingual content:** chunking nie powinien cross language boundaries. Zachowaj language consistency per chunk.

## Practical evaluation

Jak wiedzieć, czy Twój chunking jest dobry?

**Metryka 1: chunk completeness.** Czy każdy chunk zawiera complete thought? Manual review 50 random chunks.

**Metryka 2: retrieval recall.** Dla golden set queries, ile relevant chunks jest w top-k?

**Metryka 3: answer quality.** End-to-end, jaka jest quality finalnej odpowiedzi LLM?

**Metryka 4: chunk size distribution.** Czy są extreme outliers (chunks <50 tokens lub >2000 tokens)?

**Tools:** RAGAs evaluation framework, custom evaluation pipelines.

## Najczęstsze błędy w chunkingu

**Błąd 1: użycie default chunk_size bez optymalizacji.** 500 tokens domyślnie nie zawsze optymalne. Test z Twoim corpusem.

**Błąd 2: brak overlap.** Information cut at boundary jest stracona.

**Błąd 3: ignorowanie struktury dokumentu.** Markdown z headerami chunkowane jako plain text.

**Błąd 4: zbyt małe chunks.** Fragmentary, brak context.

**Błąd 5: zbyt duże chunks.** LLM context window blocked, dilution of relevant info.

**Błąd 6: brak metadata per chunk.** Source, section, type — wszystko stracone, gdy nie zachowane.

**Błąd 7: same strategy dla wszystkich typów dokumentów.** PDF z tabelami, code, prose — różne strategies.

## Rekomendacja decyzyjna

**Default rekomendacja:**
- Recursive chunking (LangChain RecursiveCharacterTextSplitter);
- Chunk size 500 tokens;
- Overlap 50 tokens;
- Metadata per chunk (source, position).

**Po pierwszym deployment:**
- Pomiar retrieval quality;
- A/B test alternative strategies;
- Iteruj na podstawie data.

**Dla wysokiej jakości:**
- Semantic chunking jeśli budżet i performance pozwalają;
- Contextual retrieval (Anthropic) dla critical applications;
- Structure-aware dla strukturyzowanych dokumentów.

## Bibliografia

<ul>
<li>Anthropic. (2024). <em>Introducing Contextual Retrieval</em>. <a href="https://www.anthropic.com/news/contextual-retrieval">https://www.anthropic.com/news/contextual-retrieval</a></li>
<li>LangChain. (2024). <em>Text Splitters Documentation</em>. <a href="https://python.langchain.com/docs/modules/data_connection/document_transformers/">https://python.langchain.com/docs/modules/data_connection/document_transformers/</a></li>
<li>LlamaIndex. (2024). <em>Node Parsers Documentation</em>. <a href="https://docs.llamaindex.ai/en/stable/module_guides/loading/node_parsers/">https://docs.llamaindex.ai/en/stable/module_guides/loading/node_parsers/</a></li>
<li>Theja, R., et al. (2024). <em>Evaluating the Ideal Chunk Size for a RAG System using LlamaIndex</em>. <a href="https://www.llamaindex.ai/blog/evaluating-the-ideal-chunk-size-for-a-rag-system-using-llamaindex-6207e5d3fec5">https://www.llamaindex.ai/blog/</a></li>
<li>Greg Kamradt. (2024). <em>5 Levels of Text Splitting for Retrieval</em>. <a href="https://github.com/FullStackRetrieval-com/RetrievalTutorials">https://github.com/FullStackRetrieval-com/RetrievalTutorials</a></li>
<li>Unstructured. (2024). <em>Unstructured Documentation — chunking strategies</em>. <a href="https://docs.unstructured.io/">https://docs.unstructured.io/</a></li>
</ul>

---

**Chunking to często ignorowana, ale kluczowa dźwignia jakości RAG.** W cotygodniowym newsletterze RAGPolska.pl publikujemy benchmarki strategii chunkingu, A/B test results, narzędzia. [Zapisz się — bezpłatnie](#newsletter-signup).
