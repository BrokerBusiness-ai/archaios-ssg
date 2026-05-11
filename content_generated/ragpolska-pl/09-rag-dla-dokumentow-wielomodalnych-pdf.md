---
title: "RAG dla dokumentów wielomodalnych — PDF, tabele, obrazy, kod"
slug: "rag-dla-dokumentow-wielomodalnych-pdf"
excerpt: "Real-world dokumenty firmowe nie są czystym tekstem. PDFs z tabelami, obrazami, kodem wymagają specjalistycznych technik. Pełen przewodnik."
category_slug: "techniki-rag"
tags: "PDF, tabele, multimodal RAG, OCR, struktura, średni"
reading_time: 11
is_published: true
is_featured: false
meta_title: "Multimodal RAG — PDF, tabele, obrazy, kod (przewodnik 2026)"
meta_description: "Pełen przewodnik RAG dla wielomodalnych dokumentów: PDF z tabelami, obrazy, kod. Tools, techniki, common pitfalls."
funnel: "MOFU"
author_slug: "marek-porycki"
related_slugs: "rag-enterprise-architektura, chunking-strategy-fixed-do-semantic, agentic-rag-multi-step-tools-planning"
product_slugs: ""
---

W demos i tutorials RAG zawsze działa na czystym tekście. Real-world dokumenty firmowe — nie. Standardy księgowe są w PDF z tabelami zagnieżdżonymi w tekście. Dokumenty techniczne mają diagrams kluczowe dla zrozumienia. Polityki HR mają flowcharts. Reports mają wykresy. Specyfikacje mają kod. Ignorowanie tych elementów oznacza, że RAG ma dostęp do 30-50% information w dokumentach.

Multimodal RAG — RAG handling tabele, obrazy, kod, complex layouts — jest jednym z trudniejszych obszarów w 2026 roku. Tools dojrzewają, ale wciąż wymaga thoughtful architecture i często custom code dla domain-specific edge cases.

Ten tekst opisuje praktyczne approaches dla multimodal RAG. Adresat: ML engineers implementing RAG na real-world enterprise documents.

## Wyzwania per typ contentu

**Tabele:**
- Standard text extraction loses structure;
- Pojedyncza tabela może mieć kluczowe info;
- Headers, rows, cells — wymaga strukturalnego understanding.

**Obrazy:**
- Diagrams, charts, infographics zawierają information;
- Standard OCR daje tylko text z obrazu (niewystarczające dla diagramów);
- Vision models (GPT-4V, Claude with vision) potrzebne dla deep understanding.

**Kod:**
- Code blocks mają syntactic structure;
- Standard text chunking destroys code semantics;
- Specialized parsers (tree-sitter) potrzebne.

**Complex layouts:**
- Multi-column PDFs (academic papers, magazines);
- Sidebar texts;
- Footnotes;
- Headers/footers.

**Cross-page references:**
- "Patrz tabela 3 na stronie 12";
- Standard chunking rozłącza powiązania;
- Wymaga sophisticated metadata.

## Stack tools dla document processing

**Tier 1: comprehensive document processing.**

**Unstructured.io** (open-source + komercyjny):
- Wszechstronny parser dla wielu formatów;
- Detects elements (text, tables, images, lists);
- Strukturalny output;
- Comprehensive language support including Polish;
- API + open-source library.

**LlamaParse (LlamaIndex):** komercyjny, advanced PDF parsing z tabel.

**Reducto:** komercyjny, najwyższej jakości dla complex documents (tabele, diagramy).

**Adobe PDF Services API:** zamknięty, dobry dla complex Adobe-format PDFs.

**Microsoft Document Intelligence:** zamknięty, integracja z Azure.

**Tier 2: specialized.**

**Camelot, Tabula:** Python libraries dla extraction tabel z PDF.

**PaddleOCR, Tesseract:** OCR engines dla images.

**LayoutParser:** detects layouts (multi-column, headers, etc.).

**Tier 3: vision models.**

**GPT-4V, Claude 3.5 Sonnet z vision, Gemini 1.5 Pro:** dla deep image understanding.

**Local: LLaVA, CogVLM:** open-source vision models.

## Praktyczna pipeline dla complex documents

Przykład: typowa polska firma ma 10 000 PDFs (raporty, polityki, kontrakty, specyfikacje techniczne).

**Step 1: document classification.**

Different documents wymagają different strategies:
- Plain text PDFs: standard text extraction;
- Tabular reports: table-aware extraction;
- Technical docs z diagrams: vision-enabled extraction;
- Code documentation: code-aware chunking.

LLM może klasyfikować dokumenty automatically.

**Step 2: structured extraction.**

Dla każdego document type, użyj appropriate tool.

```python
from unstructured.partition.pdf import partition_pdf

elements = partition_pdf(
    filename="document.pdf",
    strategy="hi_res",  # for complex layouts
    extract_images_in_pdf=True,
    infer_table_structure=True,
)

for element in elements:
    if element.type == "Title":
        # Process headings
    elif element.type == "Table":
        # Process tables specially
        table_html = element.metadata.text_as_html
        # Or convert to markdown
    elif element.type == "Image":
        # Send to vision model dla description
    elif element.type == "NarrativeText":
        # Standard text processing
```

**Step 3: element-specific processing.**

**Tables:**

```python
def process_table(table_element):
    # Convert to markdown for LLM-friendly format
    markdown_table = table_to_markdown(table_element)
    
    # Optional: generate description
    description = llm.complete(f"""
    Describe this table briefly:
    {markdown_table}
    """)
    
    # Store: markdown + description + metadata
    return {
        "content": markdown_table,
        "description": description,
        "metadata": {
            "type": "table",
            "source": "document.pdf",
            "page": table_element.metadata.page_number,
        }
    }
```

**Images:**

```python
def process_image(image_path):
    # Use vision model to describe
    description = vision_llm.describe(image_path, prompt="""
    Describe this image in detail. If it's a diagram, explain
    relationships and structure. If it's a chart, explain trends and key data points.
    """)
    
    return {
        "content": description,
        "image_path": image_path,
        "metadata": {"type": "image", "source": "..."}
    }
```

**Code blocks:**

```python
def process_code(code_block):
    # Use code-aware chunking
    if len(code_block) < 1000:
        return [code_block]  # keep small code intact
    
    # For large code, split per function/class
    return code_aware_split(code_block, language="python")
```

**Step 4: embedding strategy.**

Każdy element type może mieć different embedding strategy:
- Text: standard embedding;
- Tables: embed both raw table i description (multi-vector);
- Images: embed description (i potentially keep image dla retrieval);
- Code: embed both code i description.

**Step 5: retrieval z multi-modal results.**

```python
def retrieve_multimodal(query):
    # Standard retrieval
    text_results = vector_db.search(embed(query), filter={"type": "text"})
    table_results = vector_db.search(embed(query), filter={"type": "table"})
    image_results = vector_db.search(embed(query), filter={"type": "image"})
    
    # Combine z reasonable weighting
    combined = combine_results([text_results, table_results, image_results])
    
    return combined
```

**Step 6: prompt engineering dla LLM z multimodal context.**

```python
prompt = f"""
You have access to information from multiple sources:

TEXT EXCERPTS:
{format_text_excerpts(text_results)}

TABLES:
{format_tables(table_results)}

IMAGE DESCRIPTIONS:
{format_image_descriptions(image_results)}

User question: {query}

Provide a comprehensive answer using all available information.
Cite sources (document, page).
"""
```

## Vision models — kiedy potrzebne

**Use cases gdzie vision crucial:**
- Diagrams architektoniczne (data flows, system architectures);
- Engineering drawings;
- Charts z numerical data nie w tekście;
- Photos z visual information (np. damage assessments);
- Diagrams flow procesów;
- Hand-written notes (rzadkie ale możliwe).

**Use cases gdzie text extraction wystarcza:**
- Standardowe raporty z tabelami w tekście;
- Polityki, kontrakty, dokumenty prawne;
- Reports z chart titles i captions;
- Educational documents z explanations.

**Cost considerations:**

Vision API calls są drogie (GPT-4V ~10x cena standard text). Dla 10 000 dokumentów z 5 obrazów avg = 50 000 vision calls. Cost: $5000-15000.

Alternative: use vision tylko on-demand (kiedy retrieved content includes image, na request user clicks "explain image").

## Specific challenges per format

**PDFs:**
- Format najtrudniejszy — many variants, layouts, encodings;
- Scanned PDFs wymagają OCR;
- PDF/A vs PDF/X differences;
- Polish character encoding sometimes problematic.

**Word Documents (.docx):**
- Easier than PDF (XML structure);
- python-docx library helpful;
- Comments, tracked changes — special handling.

**Excel (.xlsx):**
- Tables natural format;
- openpyxl, pandas dla extraction;
- Wielo-sheet workbooks — each sheet osobno?

**PowerPoint (.pptx):**
- Slide text + speaker notes;
- python-pptx dla extraction;
- Images often kluczowe (diagrams, screenshots).

**HTML/web pages:**
- BeautifulSoup, scrapy;
- Boilerplate detection (common elements like nav, footer);
- Article extraction (newspaper3k, trafilatura).

**Markdown:**
- Easiest — preserves structure naturally;
- Code blocks, headers, links wszystkie clear.

## Polskie dokumenty — specyficzne challenges

**Polskie PDF z poprzednich dekad:** często słabej jakości scan'y, OCR errors.

**Polskie znaki diakrytyczne:** ą, ę, ć, ł, ń, ó, ś, ź, ż. Niektóre OCR engines mają issues. Tesseract z polish trained data dobry. Adobe wciąż lepsze dla complex layouts.

**Polskie tabele w dokumentach urzędowych:** często non-standard formats. Manual review chunkow może być potrzebny.

**Mixed język documents:** common w polskich firmach (specifications po angielsku, descriptions po polsku). Multilingual processing wymagane.

**Standardowe polskie formaty (PIT, faktury, deklaracje):** specialized tools (e.g., dla faktur — InvoiceXpert, Stampli) mogą być lepsze niż generic.

## Implementation example — pełen workflow

```python
import os
from unstructured.partition.pdf import partition_pdf
from openai import OpenAI

client = OpenAI()

def process_document(pdf_path):
    """Process PDF z multi-modal awareness."""
    
    # Extract elements
    elements = partition_pdf(
        filename=pdf_path,
        strategy="hi_res",
        extract_images_in_pdf=True,
        infer_table_structure=True,
    )
    
    chunks = []
    
    for elem in elements:
        if elem.category == "Table":
            # Table: store as markdown + description
            table_md = elem.metadata.text_as_html
            description = client.chat.completions.create(
                model="gpt-4o",
                messages=[{
                    "role": "user",
                    "content": f"Describe this table briefly:\n{table_md}"
                }]
            ).choices[0].message.content
            
            chunks.append({
                "type": "table",
                "content": table_md,
                "description": description,
                "page": elem.metadata.page_number,
            })
            
        elif elem.category == "Image":
            # Image: vision model description
            image_path = elem.metadata.image_path
            with open(image_path, "rb") as img_file:
                description = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[{
                        "role": "user",
                        "content": [
                            {"type": "text", "text": "Describe this image."},
                            {"type": "image_url", "image_url": {
                                "url": f"data:image/jpeg;base64,{base64.b64encode(img_file.read()).decode()}"
                            }}
                        ]
                    }]
                ).choices[0].message.content
            
            chunks.append({
                "type": "image",
                "content": description,
                "image_path": image_path,
                "page": elem.metadata.page_number,
            })
            
        else:
            # Standard text
            chunks.append({
                "type": "text",
                "content": elem.text,
                "page": elem.metadata.page_number,
            })
    
    return chunks

# Process
chunks = process_document("polityka_HR.pdf")

# Generate embeddings
for chunk in chunks:
    text_to_embed = chunk["content"]
    if chunk["type"] in ["table", "image"]:
        # For non-text, embed description (better semantic)
        text_to_embed = chunk.get("description", chunk["content"])
    
    chunk["embedding"] = embed(text_to_embed)

# Store in vector DB
store_in_vector_db(chunks)
```

## Najczęstsze błędy

**Błąd 1: standard text extraction dla complex PDFs.** Outputs incoherent jumble. Tables jako stream of cells. Use specialized tools.

**Błąd 2: ignorowanie obrazów.** "Tylko text matters". Naprawdę important info często w diagrams.

**Błąd 3: vision API calls dla każdego image bez consideration.** Drogi, wolny. Be selective.

**Błąd 4: brak metadata.** Po extraction — tracimy info "to było z page 12 of polityka HR". Crucial dla user trust i citations.

**Błąd 5: jeden chunking strategy dla wszystkich.** Tables, code, prose — wymagają różnych approaches.

**Błąd 6: brak preview po extraction.** Nie sprawdzasz, co tools faktycznie wyciągnęły. Sometimes total mess.

## Best practices

1. **Start z document classification.** Wiedz, jakie typy masz przed building pipeline.
2. **Test extraction quality.** Manual review 10-20 sample documents.
3. **Multi-vector strategy dla tabel/obrazów.** Embed both raw content i description.
4. **Preserve metadata religiously.** Source, page, type, position.
5. **User feedback loop.** Zbieraj feedback, gdy retrieved content nie matches user expectation.
6. **Iterate.** First version always imperfect. Plan for 2-3 iteracje.

## Bibliografia

<ul>
<li>Unstructured. (2024). <em>Unstructured Documentation</em>. <a href="https://docs.unstructured.io/">https://docs.unstructured.io/</a></li>
<li>LlamaIndex. (2024). <em>LlamaParse Documentation</em>. <a href="https://github.com/run-llama/llama_parse">https://github.com/run-llama/llama_parse</a></li>
<li>OpenAI. (2024). <em>GPT-4 Vision Documentation</em>. <a href="https://platform.openai.com/docs/guides/vision">https://platform.openai.com/docs/guides/vision</a></li>
<li>Anthropic. (2024). <em>Claude Vision Documentation</em>. <a href="https://docs.anthropic.com/claude/docs/vision">https://docs.anthropic.com/claude/docs/vision</a></li>
<li>Liu, H., et al. (2023). <em>LLaVA: Large Language and Vision Assistant</em>. <a href="https://arxiv.org/abs/2304.08485">https://arxiv.org/abs/2304.08485</a></li>
<li>Lewis, M., et al. (2024). <em>LayoutParser: Layout Detection for Documents</em>. <a href="https://layout-parser.github.io/">https://layout-parser.github.io/</a></li>
<li>PaddleOCR. (2024). <em>PaddleOCR Documentation</em>. <a href="https://github.com/PaddlePaddle/PaddleOCR">https://github.com/PaddlePaddle/PaddleOCR</a></li>
</ul>

---

**Multimodal documents są standard, nie wyjątek.** W cotygodniowym newsletterze RAGPolska.pl publikujemy konkretne implementations, tools comparison, case studies. [Zapisz się — bezpłatnie](#newsletter-signup).
