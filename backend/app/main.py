"""Zdrowie Fit API — entry point."""

from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from app.api import admin_routes, article_routes, auth_routes, category_routes, author_routes, product_routes, upload_routes, stats_routes, newsletter_routes, public_routes, integrations_routes
from app.core.config import settings
from app.core.database import Base, SessionLocal, engine
from app.services.seed_service import seed_all

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    description="""
Zdrowie.fit API — pełen dostęp do CMS, statystyk, newslettera + integracji.

## Autentykacja

**Public endpoints** (`/api/v1/public/*`) — bez auth, read-only.

**Authenticated endpoints** — header `X-API-Key: zfit_xxx...`. Wygeneruj klucz w admin panelu:
`/admin/integrations`. Scopes: `read`, `write`, `admin`, `newsletter`.

## Webhooks

Backend wysyła POST do skonfigurowanych URL gdy zachodzi event (article.published,
subscriber.created, etc). HMAC-SHA256 signing przez header `X-Signature`.
Konfiguracja: `/admin/integrations`.

## GPT Actions / MCP

OpenAPI spec dostępny: `/api/openapi.json`. Można importować bezpośrednio jako
GPT Action (Custom GPT) lub MCP server config.
    """.strip(),
)


# OpenAPI security scheme — dla GPT Actions / Swagger Try It Out
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    from fastapi.openapi.utils import get_openapi
    schema = get_openapi(
        title=app.title, version=app.version,
        description=app.description, routes=app.routes,
    )
    schema["components"]["securitySchemes"] = {
        "ApiKeyAuth": {
            "type": "apiKey",
            "in": "header",
            "name": "X-API-Key",
            "description": "Format: zfit_xxxxxxxx — wygeneruj w /admin/integrations",
        }
    }
    schema["servers"] = [
        {"url": "http://127.0.0.1:8765", "description": "Local dev"},
        {"url": "https://api.zdrowie.fit", "description": "Production"},
    ]
    app.openapi_schema = schema
    return schema


app.openapi = custom_openapi

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Templates
TEMPLATE_DIR = Path(__file__).resolve().parent.parent / "templates"
app.state.templates = Jinja2Templates(directory=str(TEMPLATE_DIR))

# Static (admin CSS/JS if needed)
STATIC_DIR = Path(__file__).resolve().parent.parent / "static"
if STATIC_DIR.exists():
    app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

# Uploads (zdjęcia wrzucone przez admina)
UPLOADS_DIR = Path(__file__).resolve().parent.parent / "uploads"
UPLOADS_DIR.mkdir(exist_ok=True)
app.mount("/uploads", StaticFiles(directory=str(UPLOADS_DIR)), name="uploads")

# API routes
app.include_router(auth_routes.router, prefix="/api")
app.include_router(article_routes.router, prefix="/api")
app.include_router(category_routes.router, prefix="/api")
app.include_router(author_routes.router, prefix="/api")
app.include_router(product_routes.router, prefix="/api")
app.include_router(upload_routes.router, prefix="/api")
app.include_router(stats_routes.router, prefix="/api")
app.include_router(newsletter_routes.router, prefix="/api")

# Public read-only API (bez auth)
app.include_router(public_routes.router, prefix="/api")

# Integrations management (admin auth)
app.include_router(integrations_routes.api_router, prefix="/api")
app.include_router(integrations_routes.admin_router)

# Admin panel (server-rendered)
app.include_router(admin_routes.router)


@app.on_event("startup")
def on_startup():
    db = SessionLocal()
    try:
        seed_all(db)
    finally:
        db.close()


@app.get("/api/health")
def health():
    return {"status": "ok", "app": settings.APP_NAME, "version": settings.VERSION}
