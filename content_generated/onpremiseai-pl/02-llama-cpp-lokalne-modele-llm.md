---
title: "llama.cpp — lokalne modele LLM krok po kroku (2026)"
slug: "llama-cpp-lokalne-modele-llm"
excerpt: "Pełen przewodnik po llama.cpp — flagowym silniku inference dla lokalnych modeli. Instalacja, kwantyzacja, optymalizacja, integracja produkcyjna."
category_slug: "technika-onprem"
tags: "llama.cpp, GGUF, kwantyzacja, lokalny LLM, początkujący"
reading_time: 11
is_published: true
is_featured: false
meta_title: "llama.cpp — kompletny przewodnik instalacji i optymalizacji"
meta_description: "Pełen przewodnik po llama.cpp: instalacja per platform, kwantyzacja modeli GGUF, parametry inference, integracja API, troubleshooting."
funnel: "TOFU"
author_slug: "marek-porycki"
related_slugs: "ai-on-premise-w-2026-przewodnik, gpu-vs-cpu-vs-mac-dla-lokalnego-llm, ollama-lm-studio-vllm-narzedzia-produkcyjne"
product_slugs: ""
---

W maju 2023 roku Georgi Gerganov, niezależny developer z Sofii, opublikował projekt open-source o nazwie llama.cpp. Cel: uruchomienie modelu Llama Meta lokalnie na zwykłym laptopie. Zaledwie kilka miesięcy później llama.cpp stał się de facto standardem dla lokalnych deployments LLM. Praktycznie każde popularne narzędzie do uruchamiania lokalnych modeli (Ollama, LM Studio, GPT4All, Open WebUI) bazuje na llama.cpp pod spodem.

Filozofia llama.cpp: minimalizm i wydajność. Napisany w czystym C/C++, kompiluje się na każdej platformie, nie wymaga żadnych zależności poza standardowymi bibliotekami. Działa równie dobrze na laptopie z Apple Silicon, na serwerze z NVIDIA H100, na Raspberry Pi (wolno, ale działa).

Ten tekst opisuje pełen workflow llama.cpp dla średniej polskiej firmy: instalacja, pobieranie modeli, kwantyzacja, parametry inference, integracja produkcyjna, troubleshooting. Adresat: inżynierowie IT odpowiedzialni za lokalne deployments LLM, dyrektorzy IT chcący zrozumieć technologie pod produktem.

## Instalacja — trzy ścieżki

**Ścieżka 1: kompilacja ze źródeł (zalecane).**

Najszybsza i najbardziej elastyczna metoda. Wymagane: kompilator C++ (clang, gcc), make, git.

```bash
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp
make
```

Po kilku minutach kompilacji otrzymujesz binarki gotowe do użycia.

Dla GPU NVIDIA — kompilacja z CUDA:
```bash
make GGML_CUDA=1
```

Dla Apple Silicon — automatycznie używa Metal:
```bash
make
```

Dla AMD GPU (ROCm):
```bash
make GGML_HIPBLAS=1
```

**Ścieżka 2: gotowe binarki.**

Github releases ma pre-compiled binaries dla najpopularniejszych platform (Windows, macOS, Linux). Szybsze, ale mniej elastyczne.

**Ścieżka 3: Docker.**

Oficjalne Docker images:
```bash
docker pull ghcr.io/ggerganov/llama.cpp:server-cuda
```

Wygodne dla deployments na serwerach, gorsze dla developmentu.

## Pobieranie modeli — format GGUF

llama.cpp używa własnego formatu GGUF (poprzednio GGML). Konwersja modeli z formatów Hugging Face do GGUF wymaga narzędzia konwersyjnego dostępnego w llama.cpp.

Najszybsza ścieżka: pobierz pre-konwertowany model GGUF z Hugging Face. Repozytorium TheBloke (https://huggingface.co/TheBloke) udostępnia tysiące modeli w GGUF różnymi kwantyzacjami. Aktywna społeczność.

Przykład pobrania Llama 3.3 70B w kwantyzacji Q4_K_M:
```bash
wget https://huggingface.co/bartowski/Llama-3.3-70B-Instruct-GGUF/resolve/main/Llama-3.3-70B-Instruct-Q4_K_M.gguf
```

Plik: ~40 GB. Pobranie zajmuje czas zależny od łącza.

## Kwantyzacja — wybór trade-off

Kwantyzacja to redukcja precyzji wagi modelu w celu zmniejszenia rozmiaru i zwiększenia prędkości. Im niższa precyzja, tym szybsza inference, ale gorsze wyniki.

**Standardowe poziomy kwantyzacji w GGUF:**

- **Q8_0:** 8-bit, blisko oryginału. Rozmiar: ~50% oryginału. Jakość: praktycznie identyczna.
- **Q6_K:** 6-bit. Rozmiar: ~38% oryginału. Jakość: bardzo dobra.
- **Q5_K_M:** 5-bit medium. Rozmiar: ~32% oryginału. Jakość: dobra.
- **Q4_K_M:** 4-bit medium. Rozmiar: ~25% oryginału. Jakość: akceptowalna dla większości zastosowań — najczęściej używana.
- **Q3_K_M:** 3-bit. Rozmiar: ~20% oryginału. Jakość: zauważalna degradacja, ale wciąż użyteczna.
- **Q2_K:** 2-bit. Rozmiar: ~15% oryginału. Jakość: mocna degradacja, dla bardzo ograniczonego sprzętu.

Dla Llama 3.3 70B konkretne rozmiary:
- pełna precyzja FP16: 140 GB.
- Q8_0: 75 GB.
- Q5_K_M: 50 GB.
- Q4_K_M: 40 GB.
- Q3_K_M: 33 GB.

Rekomendacja standardowa: Q4_K_M jako sweet spot. Q5_K_M jeśli sprzęt pozwala.

## Pierwsze uruchomienie

Najprostsza komenda — uruchomienie inference:

```bash
./llama-cli -m Llama-3.3-70B-Instruct-Q4_K_M.gguf \
  -p "Wyjaśnij krótko, czym jest cyberbezpieczeństwo w kontekście NIS2." \
  -n 512
```

Parametry:
- `-m`: ścieżka do modelu;
- `-p`: prompt;
- `-n`: maksymalna liczba tokenów do wygenerowania.

Pierwsze uruchomienie ładuje model do pamięci (kilkadziesiąt sekund dla dużego modelu na GPU). Kolejne wywołania w tej samej sesji są szybkie.

## Tryb serwera — produkcyjny deployment

Dla produkcyjnego deployment llama.cpp ma wbudowany HTTP server kompatybilny z OpenAI API:

```bash
./llama-server -m Llama-3.3-70B-Instruct-Q4_K_M.gguf \
  --host 0.0.0.0 \
  --port 8080 \
  --ctx-size 8192 \
  --n-gpu-layers 80
```

Parametry produkcyjne:
- `--host 0.0.0.0`: nasłuchuje na wszystkich interfejsach;
- `--port 8080`: port API;
- `--ctx-size 8192`: maksymalny kontekst (RAM/VRAM-zależny);
- `--n-gpu-layers 80`: ile warstw modelu na GPU (zostawia resztę na CPU).

Po uruchomieniu serwer eksponuje endpointy:
- `POST /v1/chat/completions` — kompatybilne z OpenAI;
- `POST /v1/completions` — legacy completion API;
- `GET /health` — health check.

Każda aplikacja napisana pod OpenAI API może działać z lokalnym modelem przez prostą zmianę `base_url`.

## Optymalizacja wydajności

**Optymalizacja 1: dobór warstw GPU.** `--n-gpu-layers` decyduje, ile warstw modelu jest w VRAM. Dla największych modeli na ograniczonej VRAM:
- 40 GB VRAM: ~50 warstw modelu 70B (reszta na CPU);
- 80 GB VRAM: pełen model 70B na GPU;
- 24 GB VRAM: ~25 warstw modelu 70B (znacznie wolniejsze, model częściowo na CPU).

**Optymalizacja 2: batch size.** `--batch-size` (domyślnie 512) decyduje o przetwarzaniu równoległym. Dla pojedynczego użytkownika — niska wartość. Dla multi-user — wyższe wartości (do 2048).

**Optymalizacja 3: continuous batching.** `--cont-batching` (włączone domyślnie w nowszych wersjach) — kluczowe dla multi-user serving. Pozwala na efektywne obsługiwanie wielu requestów równolegle.

**Optymalizacja 4: KV cache quantization.** `--cache-type-k q4_0 --cache-type-v q4_0` — kwantyzuje KV cache, zwalniając VRAM dla większego kontekstu lub większego modelu.

**Optymalizacja 5: speculative decoding.** Użycie małego "draft model" do wstępnego generowania, weryfikowanego przez duży model. Może 2-3x przyspieszyć inference. Wymagane: drugi mały model.

## Realne benchmarki — Llama 3.3 70B Q4_K_M

Prędkość generowania (tokens/sekundę) na różnym sprzęcie:

- **Mac Studio M4 Ultra 192 GB:** 14-20 t/s.
- **2x RTX A6000 (48 GB każda):** 25-35 t/s.
- **1x A100 80 GB:** 35-50 t/s.
- **1x H100 80 GB:** 60-90 t/s.
- **CPU only (server-grade Xeon):** 1-3 t/s.
- **MacBook M3 Max 64 GB:** 6-10 t/s.

Dla porównania: GPT-4o przez API zwykle 30-80 t/s, ale z latencją początkową 200-500 ms.

Lokalna prędkość 15+ t/s jest wystarczająca dla większości zastosowań interaktywnych (czat, content generation). Dla aplikacji wymagających ekstremalnie szybkiej odpowiedzi (autocomplete) — zwykle za wolne.

## Integracja z aplikacjami

**Python — openai library:**

```python
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:8080/v1",
    api_key="not-needed"  # llama.cpp nie wymaga
)

response = client.chat.completions.create(
    model="local",
    messages=[{"role": "user", "content": "Witaj"}]
)
print(response.choices[0].message.content)
```

**Node.js — openai library:**

```javascript
import OpenAI from 'openai';

const client = new OpenAI({
    baseURL: 'http://localhost:8080/v1',
    apiKey: 'not-needed'
});

const response = await client.chat.completions.create({
    model: 'local',
    messages: [{ role: 'user', content: 'Witaj' }]
});
console.log(response.choices[0].message.content);
```

**curl:**

```bash
curl http://localhost:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [{"role": "user", "content": "Witaj"}]
  }'
```

Praktycznie każda aplikacja napisana pod OpenAI API może działać bez modyfikacji.

## Production deployment — best practices

**Practice 1: systemd service na Linux.**

Plik `/etc/systemd/system/llama-server.service`:
```ini
[Unit]
Description=llama.cpp server
After=network.target

[Service]
Type=simple
User=llama
WorkingDirectory=/opt/llama.cpp
ExecStart=/opt/llama.cpp/llama-server \
  -m /opt/models/llama-3.3-70b.gguf \
  --host 0.0.0.0 \
  --port 8080 \
  --n-gpu-layers 80
Restart=always

[Install]
WantedBy=multi-user.target
```

Uruchomienie:
```bash
systemctl enable llama-server
systemctl start llama-server
```

**Practice 2: reverse proxy z auth.** llama.cpp nie ma wbudowanej autoryzacji. Dla produkcji wymagany reverse proxy (nginx, Caddy, Traefik) z autentykacją.

**Practice 3: rate limiting.** Lokalny model ma ograniczoną przepustowość (jednoczesna obsługa kilku-kilkudziesięciu requestów). Rate limiting na poziomie reverse proxy chroni przed przeciążeniem.

**Practice 4: monitoring.** Metryki do monitorowania: VRAM usage, GPU utilization, requests per second, average latency, queue length. Prometheus + Grafana standard.

**Practice 5: backup/failover.** Dla critical workloads — drugi node z modelem dla failover. Load balancer rozdzielający requests.

## Najczęstsze problemy i rozwiązania

**Problem 1: "out of memory" przy uruchamianiu modelu.** Solucja: zmniejsz `--n-gpu-layers`, użyj mniejszej kwantyzacji, użyj mniejszego modelu, lub dodaj VRAM/RAM.

**Problem 2: bardzo wolne inference (1-2 t/s).** Solucja: model częściowo na CPU. Zwiększ `--n-gpu-layers` (jeśli VRAM pozwala) lub użyj mniejszego modelu.

**Problem 3: wyniki niskiej jakości.** Solucja: użyj wyższej kwantyzacji (Q5_K_M zamiast Q4_K_M), użyj większego modelu (70B zamiast 13B), tune prompts.

**Problem 4: hallucinations.** Solucja: używaj RAG (retrieval-augmented generation), niższa temperatura (0.1-0.3 zamiast 0.7), explicit instructions w promcie.

**Problem 5: timeout na długich kontekstach.** Solucja: zwiększ `--ctx-size` (wymaga więcej VRAM/RAM), użyj streaming response.

**Problem 6: różne wyniki przy każdym uruchomieniu.** Solucja: ustaw `--seed` (powtarzalność), użyj `--temp 0` (deterministyczność).

## Aktualizacje i wersjonowanie

llama.cpp aktualizuje się bardzo aktywnie — kilka commitów dziennie. Praktyczne podejście:

- update co 4-8 tygodni (nie codziennie);
- testowanie nowej wersji w środowisku staging przed produkcją;
- zachowanie poprzedniej wersji jako rollback option;
- śledzenie release notes (https://github.com/ggerganov/llama.cpp/releases).

Aktualizacje czasem łamią kompatybilność starych modeli GGUF. W razie problemu — pobierz świeżą wersję modelu przekonwertowaną pod nową wersję llama.cpp.

## Bibliografia

<ul>
<li>Gerganov, G. (2024). <em>llama.cpp: LLM inference in C/C++</em>. <a href="https://github.com/ggerganov/llama.cpp">https://github.com/ggerganov/llama.cpp</a></li>
<li>Touvron, H., et al. (2024). <em>Llama 3.3: Improving Open Foundation Models</em>. Meta AI Research. <a href="https://ai.meta.com/blog/meta-llama-3/">https://ai.meta.com/blog/meta-llama-3/</a></li>
<li>Frantar, E., et al. (2023). <em>GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers</em>. ICLR 2023. <a href="https://arxiv.org/abs/2210.17323">https://arxiv.org/abs/2210.17323</a></li>
<li>Dettmers, T., et al. (2023). <em>QLoRA: Efficient Finetuning of Quantized LLMs</em>. NeurIPS 2023. <a href="https://arxiv.org/abs/2305.14314">https://arxiv.org/abs/2305.14314</a></li>
<li>Hugging Face. (2024). <em>GGUF Format Documentation</em>. <a href="https://huggingface.co/docs/hub/en/gguf">https://huggingface.co/docs/hub/en/gguf</a></li>
<li>Leviathan, Y., et al. (2023). <em>Fast Inference from Transformers via Speculative Decoding</em>. ICML 2023. <a href="https://arxiv.org/abs/2211.17192">https://arxiv.org/abs/2211.17192</a></li>
</ul>

---

**llama.cpp to fundament lokalnego AI — warto go opanować.** W cotygodniowym newsletterze OnPremiseAI.pl publikujemy konkretne konfiguracje, benchmarki, optymalizacje. [Zapisz się — bezpłatnie](#newsletter-signup).
