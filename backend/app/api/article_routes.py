"""Article CRUD + public endpoints."""

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.core.auth import get_current_admin
from app.core.config import settings
from app.core.database import get_db
from app.schemas.article import ArticleCreate, ArticleRead, ArticleUpdate, PaginatedArticles
from app.services import article_service as svc

router = APIRouter(prefix="/articles", tags=["articles"])


# ── Public ───────────────────────────────────────────────────────

@router.get("/", response_model=PaginatedArticles)
def list_articles(
    page: int = Query(1, ge=1),
    per_page: int = Query(settings.ARTICLES_PER_PAGE, ge=1, le=100),
    category: str | None = None,
    tag: str | None = None,
    search: str | None = None,
    sort: str = Query("newest", pattern="^(newest|oldest|popular|title)$"),
    published_only: bool = True,
    featured: bool = False,
    db: Session = Depends(get_db),
):
    return svc.list_articles(
        db, page=page, per_page=per_page,
        category_slug=category, tag=tag, search=search, sort=sort,
        published_only=published_only, featured_only=featured,
    )


@router.get("/slug/{slug}", response_model=ArticleRead)
def get_by_slug(slug: str, db: Session = Depends(get_db)):
    article = svc.get_article_by_slug(db, slug, count_view=True)
    if not article:
        raise HTTPException(404, "Artykuł nie znaleziony")
    return article


@router.get("/{article_id}", response_model=ArticleRead)
def get_by_id(article_id: int, db: Session = Depends(get_db)):
    article = svc.get_article_by_id(db, article_id)
    if not article:
        raise HTTPException(404, "Artykuł nie znaleziony")
    return article


# ── Admin ────────────────────────────────────────────────────────

@router.post("/", response_model=ArticleRead, status_code=201)
def create_article(data: ArticleCreate, db: Session = Depends(get_db), _: str = Depends(get_current_admin)):
    return svc.create_article(db, data)


@router.put("/{article_id}", response_model=ArticleRead)
def update_article(article_id: int, data: ArticleUpdate, db: Session = Depends(get_db), _: str = Depends(get_current_admin)):
    result = svc.update_article(db, article_id, data)
    if not result:
        raise HTTPException(404, "Artykuł nie znaleziony")
    return result


@router.delete("/{article_id}", status_code=204)
def delete_article(article_id: int, db: Session = Depends(get_db), _: str = Depends(get_current_admin)):
    if not svc.delete_article(db, article_id):
        raise HTTPException(404, "Artykuł nie znaleziony")


@router.post("/{article_id}/toggle-publish", response_model=ArticleRead)
def toggle_publish(article_id: int, db: Session = Depends(get_db), _: str = Depends(get_current_admin)):
    result = svc.toggle_publish(db, article_id)
    if not result:
        raise HTTPException(404, "Artykuł nie znaleziony")
    return result


@router.post("/{article_id}/toggle-featured", response_model=ArticleRead)
def toggle_featured(article_id: int, db: Session = Depends(get_db), _: str = Depends(get_current_admin)):
    result = svc.toggle_featured(db, article_id)
    if not result:
        raise HTTPException(404, "Artykuł nie znaleziony")
    return result
