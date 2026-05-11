# Zdrowie.fit API Integrations

Pełen pakiet integracji: API keys, webhooks, public read-only API, GPT Actions / MCP.

## 🚀 Quick start

### 1. Wygeneruj API key

Admin panel → http://127.0.0.1:8765/admin/integrations → **+ Nowy API Key** → zapisz `zfit_xxxxxxxxxx` (pokazany RAZ).

### 2. Test

```bash
curl -H "X-API-Key: zfit_xxx..." http://127.0.0.1:8765/api/articles/
```

---

## 🔐 Authentication

Header: `X-API-Key: zfit_xxxxxxxxxxxxxxxxx`

### Scopes

| Scope | Co pozwala |
|---|---|
| `read` | GET — artykuły, kategorie, autorzy, statystyki |
| `write` | POST/PUT/DELETE artykułów, kategorii, autorów, produktów |
| `admin` | Wszystko + zarządzanie API keys, webhooks, subscribers |
| `newsletter` | POST `/api/newsletter` (do form submitów z zewnątrz) |

CSV w polu scopes: `"read,write,newsletter"` daje 3 scopes.

---

## 📖 Public Read-Only API (`/api/v1/public/*`)

**Bez auth.** Bezpiecznie udostępniaj swój content innym aplikacjom.

```bash
curl https://api.zdrowie.fit/api/v1/public/articles?page=1&per_page=10
curl https://api.zdrowie.fit/api/v1/public/articles/cold-exposure-zimne-prysznice-nauka
curl https://api.zdrowie.fit/api/v1/public/categories
curl https://api.zdrowie.fit/api/v1/public/authors
```

Filtry:
- `?category_slug=fizyczne` — tylko z tej kategorii
- `?tag=stres` — tylko z tym tagiem
- `?per_page=50` — max 100

---

## 🔔 Webhooks

Backend wysyła POST do Twojego URL gdy się dzieje event.

### Eventy

- `article.created` — nowy artykuł (draft lub published)
- `article.published` — artykuł opublikowany (is_published: false → true)
- `article.updated` — artykuł edytowany
- `article.deleted` — artykuł usunięty
- `subscriber.created` — nowy subscriber (po confirmation, status=active)
- `subscriber.unsubscribed` — subscriber się wypisał

### Payload

```json
{
  "schema_version": "1.0",
  "event": "article.published",
  "timestamp": "2026-05-01T10:00:00Z",
  "data": {
    "id": 42,
    "slug": "cold-exposure-zimne-prysznice-nauka",
    "title": "Cold exposure — co naprawdę mówi nauka",
    "category_slug": "fizyczne",
    "is_published": true,
    "url": "https://zdrowie.fit/artykuly/cold-exposure-zimne-prysznice-nauka.html",
    "published_at": "2026-05-01T10:00:00Z"
  }
}
```

### HMAC verification (Python)

```python
import hmac, hashlib

SECRET = "your-webhook-secret"  # pokazany RAZ przy tworzeniu

def verify(body: bytes, signature_header: str) -> bool:
    expected = "sha256=" + hmac.new(SECRET.encode(), body, hashlib.sha256).hexdigest()
    return hmac.compare_digest(expected, signature_header)

# FastAPI endpoint:
@app.post("/incoming-webhook")
async def handle(request: Request):
    body = await request.body()
    sig = request.headers.get("X-Signature", "")
    if not verify(body, sig):
        raise HTTPException(401, "Invalid signature")
    payload = await request.json()
    # ... handle event
```

### Auto-disable

Po 10 kolejnych failach (5xx errors lub network issues) webhook automatycznie się wyłącza.
W admin panelu kliknij „Resume" żeby reset. Liczba failures resetuje się po pierwszym sukcesie.

---

## 🤖 Integracje

### n8n

1. **Schedule Trigger** → co dzień
2. **HTTP Request** node:
   - Method: GET
   - URL: `https://api.zdrowie.fit/api/articles/`
   - Headers: `X-API-Key: zfit_xxx...`
3. **Loop** + **Filter** po `is_published=false` → wysyła Slack message dla każdego draftu

### Make.com (Integromat)

1. **HTTP** module → "Make a request"
2. URL: `https://api.zdrowie.fit/api/v1/public/articles`
3. Process JSON response → forward to Google Sheets / Airtable / etc.

### Webhook receiver na Slack

1. Slack → Apps → Incoming Webhooks → utwórz workflow z URL
2. W Zdrowie.fit admin → Integrations → New Webhook:
   - URL: Slack webhook URL
   - Events: `article.published,subscriber.created`
3. Test webhook → sprawdź czy Slack dostaje JSON

### GPT Actions (Custom GPT)

1. ChatGPT → Configure → Actions → **Import OpenAPI**
2. URL: `https://api.zdrowie.fit/api/openapi.json`
3. Authentication: **API Key** → Header → `X-API-Key`
4. Klucz: wygeneruj w admin panelu, scope `read` lub `write`

Po imporcie GPT może rozumieć pytania typu *„pokaż mi top 5 artykułów z tego miesiąca"* — wykonuje GET na odpowiedni endpoint.

### MCP (Model Context Protocol)

OpenAPI spec można też użyć jako MCP tool definition. Claude Desktop / dowolny MCP client:

```json
{
  "mcpServers": {
    "zdrowie-fit": {
      "command": "npx",
      "args": ["-y", "openapi-mcp-server", "https://api.zdrowie.fit/api/openapi.json"],
      "env": {
        "API_KEY": "zfit_xxx..."
      }
    }
  }
}
```

---

## 🛡️ Best practices

- **Rotacja kluczy**: co 90 dni regeneruj API key, revokuj stary
- **Najmniejsze uprawnienia**: jeśli n8n tylko czyta, daj scope `read` (nie `admin`)
- **Webhook secret**: NIGDY nie commituj do repo, tylko ENV variable
- **HMAC verification**: ZAWSZE waliduj X-Signature przed przetwarzaniem payload
- **Monitoring**: sprawdzaj `last_used_at` API keys — jeśli klucz nieużywany 30+ dni, revoke
- **Rate limiting**: domyślnie 60 req/min per klucz (konfigurowalne)

---

## 🚨 Troubleshooting

### `401 Unauthorized` mimo że klucz wpisany

- Sprawdź czy klucz nie jest revoked (`/admin/integrations` → status)
- Sprawdź expires_at
- Header musi być DOKŁADNIE `X-API-Key`, nie `X-Api-Key` ani `Authorization: Bearer`

### `403 Forbidden — missing scope`

Klucz ma scope `read`, endpoint wymaga `write`. Wygeneruj nowy klucz z proper scopes.

### Webhook nie wysyła

- Sprawdź `is_active` w admin panelu — auto-disable po 10 failach
- Test webhook z UI (klik „Test") — wysyła test event z payloadem
- Sprawdź logi backendu — `tail -f` na uvicorn output

### GPT Actions nie widzi endpointów

- OpenAPI musi być publicznie dostępne (jeśli backend lokalny — użyj ngrok)
- Security scheme musi być `apiKey` w header, nie `bearer` (już skonfigurowane)
- Po imporcie sprawdź w GPT „Available Actions" — wszystkie endpointy powinny być widoczne

---

## 📊 Endpointy — szybka referencja

### Articles
- `GET /api/articles/` — lista (paginacja)
- `GET /api/articles/{id}` lub `/slug/{slug}` — pojedynczy
- `POST /api/articles/` — utwórz (write)
- `PUT /api/articles/{id}` — edytuj (write)
- `DELETE /api/articles/{id}` — usuń (write)
- `POST /api/articles/{id}/toggle-publish` — publish/unpublish

### Categories / Authors / Products
Analogicznie do articles. Patrz `/api/docs` (Swagger UI).

### Stats (admin scope)
- `GET /api/stats/admin/overview` — live readers, today/week/month/year
- `GET /api/stats/admin/top?period=month&limit=10`
- `GET /api/stats/admin/daily?days=30` — wykres
- `GET /api/stats/admin/article/{slug}` — szczegóły artykułu

### Newsletter (admin scope)
- `GET /api/newsletter/admin/stats` — total/active/pending/unsubscribed
- `GET /api/newsletter/admin/list?status=active&limit=100`
- `POST /api/newsletter/` — public, signup z formularza

### Public (no auth)
- `GET /api/v1/public/articles`
- `GET /api/v1/public/articles/{slug}`
- `GET /api/v1/public/categories`
- `GET /api/v1/public/authors`
- `GET /api/v1/public/authors/{slug}`

---

## 🌐 Production — deployment backend

Aktualnie backend działa lokalnie (`http://127.0.0.1:8765`). Żeby działał z produkcji:

1. Hosting Python na **Cyber_Folks** (Python plan ma uvicorn support) lub **Hetzner VPS**
2. Subdomena `api.zdrowie.fit` → CNAME do hostingu Python
3. HTTPS (Let's Encrypt automatic)
4. `BACKEND_URL=https://api.zdrowie.fit` w `.env` projektu (już dodane jako placeholder)
5. Reverse proxy (nginx) → uvicorn na 8000
6. systemd service dla uvicorn

To ~2h roboty. Marek decyduje kiedy. Lokalnie dla developmentu wystarczy.
