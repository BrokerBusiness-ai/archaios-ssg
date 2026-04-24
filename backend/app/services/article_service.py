"""Article CRUD + search + publish logic."""

import math
from datetime import datetime
from typing import Optional

from slugify import slugify
from sqlalchemy import func, or_
from sqlalchemy.orm import Session, joinedload

from app.models.article import Article
from app.models.category import Category
from app.models.author import Author  # noqa: F401  (dla relationship lazy load)
from app.schemas.article import ArticleCreate, ArticleUpdate, PaginatedArticles, ArticleListItem, ArticleRead


def _unique_slug(db: Session, title: str, exclude_id: Optional[int] = None) -> str:
    base = slugify(title, max_length=300)
    slug = base
    counter = 1
    while True:
        q = db.query(Article).filter(Article.slug == slug)
        if exclude_id:
            q = q.filter(Article.id != exclude_id)
        if not q.first():
            return slug
        slug = f"{base}-{counter}"
        counter += 1


def _author_name(a: Article) -> str:
    return a.author_obj.name if a.author_obj else (a.author or "Zdrowie Fit Team")


def _author_slug(a: Article) -> str:
    return a.author_obj.slug if a.author_obj else ""


def _to_list_item(a: Article) -> ArticleListItem:
    return ArticleListItem(
        id=a.id, title=a.title, slug=a.slug, excerpt=a.excerpt,
        category_id=a.category_id,
        category_name=a.category.name if a.category else "",
        category_slug=a.category.slug if a.category else "",
        author_id=a.author_id,
        author=_author_name(a),
        author_slug=_author_slug(a),
        image_url=a.image_url, icon=a.icon,
        tags=a.tags, reading_time=a.reading_time,
        is_published=a.is_published, is_featured=a.is_featured,
        views=a.views, published_at=a.published_at, created_at=a.created_at,
    )


def _to_read(a: Article) -> ArticleRead:
    return ArticleRead(
        id=a.id, title=a.title, slug=a.slug, excerpt=a.excerpt, content=a.content,
        category_id=a.category_id,
        category_name=a.category.name if a.category else "",
        category_slug=a.category.slug if a.category else "",
        author_id=a.author_id,
        author=_author_name(a),
        author_slug=_author_slug(a),
        image_url=a.image_url,
        og_image_custom=a.og_image_custom or "",
        icon=a.icon,
        tags=a.tags, reading_time=a.reading_time,
        bibliography=a.bibliography or "",
        related_slugs=a.related_slugs or "",
        product_slugs=a.product_slugs or "",
        is_published=a.is_published, is_featured=a.is_featured,
        meta_title=a.meta_title, meta_description=a.meta_description,
        views=a.views, published_at=a.published_at,
        created_at=a.created_at, updated_at=a.updated_at,
    )


def list_articles(
    db: Session,
    page: int = 1,
    per_page: int = 12,
    category_slug: Optional[str] = None,
    tag: Optional[str] = None,
    published_only: bool = False,
    featured_only: bool = False,
    search: Optional[str] = None,
    sort: str = "newest",
) -> PaginatedArticles:
    q = db.query(Article).options(joinedload(Article.category), joinedload(Article.author_obj))

    if published_only:
        q = q.filter(Article.is_published == True)
    if featured_only:
        q = q.filter(Article.is_featured == True)
    if category_slug:
        q = q.join(Category).filter(Category.slug == category_slug)
    if tag:
        q = q.filter(Article.tags.ilike(f"%{tag}%"))
    if search:
        pattern = f"%{search}%"
        q = q.filter(or_(
            Article.title.ilike(pattern),
            Article.excerpt.ilike(pattern),
            Article.content.ilike(pattern),
            Article.tags.ilike(pattern),
        ))

    if sort == "oldest":
        q = q.order_by(Article.created_at.asc())
    elif sort == "popular":
        q = q.order_by(Article.views.desc())
    elif sort == "title":
        q = q.order_by(Article.title.asc())
    else:
        q = q.order_by(Article.created_at.desc())

    total = q.count()
    pages = max(1, math.ceil(total / per_page))
    items = q.offset((page - 1) * per_page).limit(per_page).all()

    return PaginatedArticles(
        items=[_to_list_item(a) for a in items],
        total=total, page=page, per_page=per_page, pages=pages,
    )


def get_article_by_id(db: Session, article_id: int) -> Optional[ArticleRead]:
    a = db.query(Article).options(joinedload(Article.category), joinedload(Article.author_obj)).get(article_id)
    return _to_read(a) if a else None


def get_article_by_slug(db: Session, slug: str, count_view: bool = False) -> Optional[ArticleRead]:
    a = db.query(Article).options(joinedload(Article.category), joinedload(Article.author_obj)).filter(Article.slug == slug).first()
    if not a:
        return None
    if count_view:
        a.views += 1
        db.commit()
        db.refresh(a)
    return _to_read(a)


def create_article(db: Session, data: ArticleCreate) -> ArticleRead:
    slug = _unique_slug(db, data.title)
    article = Article(slug=slug, **data.model_dump())
    if data.is_published:
        article.published_at = datetime.utcnow()
    db.add(article)
    db.commit()
    db.refresh(article)
    return get_article_by_id(db, article.id)  # type: ignore


def update_article(db: Session, article_id: int, data: ArticleUpdate) -> Optional[ArticleRead]:
    article = db.query(Article).get(article_id)
    if not article:
        return None
    updates = data.model_dump(exclude_unset=True)

    if "title" in updates:
        article.slug = _unique_slug(db, updates["title"], exclude_id=article_id)

    was_published = article.is_published
    for key, val in updates.items():
        setattr(article, key, val)

    if not was_published and article.is_published:
        article.published_at = datetime.utcnow()

    db.commit()
    db.refresh(article)
    return get_article_by_id(db, article.id)


def delete_article(db: Session, article_id: int) -> bool:
    article = db.query(Article).get(article_id)
    if not article:
        return False
    db.delete(article)
    db.commit()
    return True


def toggle_publish(db: Session, article_id: int) -> Optional[ArticleRead]:
    article = db.query(Article).get(article_id)
    if not article:
        return None
    article.is_published = not article.is_published
    if article.is_published and not article.published_at:
        article.published_at = datetime.utcnow()
    db.commit()
    return get_article_by_id(db, article_id)


def toggle_featured(db: Session, article_id: int) -> Optional[ArticleRead]:
    article = db.query(Article).get(article_id)
    if not article:
        return None
    article.is_featured = not article.is_featured
    db.commit()
    return get_article_by_id(db, article_id)
