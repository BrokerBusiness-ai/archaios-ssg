"""Zdrowie Fit API — entry point."""

from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from app.api import admin_routes, article_routes, auth_routes, category_routes, author_routes, product_routes, upload_routes
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
)

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
