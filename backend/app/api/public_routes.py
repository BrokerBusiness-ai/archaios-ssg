"""Public API v1 — read-only endpointy bez autentykacji.

Pozwala innym stronom / aplikacjom czytać Twój content (artykuły, kategorie).
Rate limiting przez nginx/Cloudflare jeśli potrzebne (na razie soft).

WAŻNE: żadnych endpointów write/delete — tylko GET. Żadnych draftów —
tylko is_published=True. Żadnych emaili / subscriberów — chronione.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.services import article_service, category_service, author_service


router = APIRouter(prefix="/v1/public", tags=["public-api"])


# ── Articles ──────────────────────────────────────────────────────

@router.get("/articles", summary="List published articles")
async def list_articles(
    page: int = 1,
    per_page: int = 20,
    category_slug: str | None = None,
    tag: str | None = None,
    db: Session = Depends(get_db),
):
    """Public list of published articles. Paginated."""
    per_page = min(per_page, 100)  # max 100 per page
    result = article_service.list_articles(
        db, page=page, per_page=per_page,
        published_only=True,
        category_slug=category_slug,
        tag=tag,
    )
    return {
        "page": page,
        "per_page": per_page,
        "total": result.total,
        "items": [_article_to_public_dict(a) for a in result.items],
    }


@router.get("/articles/{slug}", summary="Get article by slug")
async def get_article(slug: str, db: Session = Depends(get_db)):
    article = article_service.get_article_by_slug(db, slug)
    if not article or not article.is_published:
        raise HTTPException(404, "Article not found")
    return _article_to_public_dict(article, full=True)


# ── Categories ────────────────────────────────────────────────────

@router.get("/categories", summary="List categories")
async def list_categories(db: Session = Depends(get_db)):
    cats = category_service.list_categories(db)
    return [{"slug": c.slug, "name": c.name, "description": c.description,
             "icon": c.icon, "color": c.color} for c in cats]


# ── Authors ───────────────────────────────────────────────────────

@router.get("/authors", summary="List authors")
async def list_authors(db: Session = Depends(get_db)):
    authors = author_service.list_authors(db)
    return [_author_to_public_dict(a) for a in authors if a.is_active]


@router.get("/authors/{slug}", summary="Get author by slug")
async def get_author(slug: str, db: Session = Depends(get_db)):
    author = author_service.get_author_by_slug(db, slug)
    if not author or not author.is_active:
        raise HTTPException(404, "Author not found")
    return _author_to_public_dict(author, full=True)


# ── Helpers ───────────────────────────────────────────────────────

def _article_to_public_dict(a, full: bool = False) -> dict:
    """Pole zwracane publicznie. NIE pokazujemy: drafts, internal notes, views detail."""
    base = {
        "id": a.id,
        "slug": a.slug,
        "title": a.title,
        "excerpt": a.excerpt,
        "category_slug": getattr(a, "category_slug", None),
        "category_name": getattr(a, "category_name", None),
        "author": a.author,
        "author_slug": a.author_slug,
        "tags": a.tags or "",
        "image_url": a.image_url,
        "reading_time": a.reading_time,
        "published_at": a.published_at.isoformat() if a.published_at else None,
        "url": f"https://zdrowie.fit/artykuly/{a.slug}.html",
    }
    if full:
        base.update({
            "content": a.content,
            "bibliography": a.bibliography,
            "meta_title": a.meta_title,
            "meta_description": a.meta_description,
        })
    return base


def _author_to_public_dict(au, full: bool = False) -> dict:
    base = {
        "slug": au.slug,
        "name": au.name,
        "credentials": au.credentials,
        "bio_short": au.bio_short,
        "photo_url": au.photo_url,
    }
    if full:
        base.update({
            "bio_long": au.bio_long,
            "linkedin": au.linkedin,
            "twitter": au.twitter,
            "website": au.website,
            "specializations": au.specializations,
        })
    return base
