"""Category CRUD."""

from typing import Optional
from slugify import slugify
from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.article import Article
from app.models.category import Category
from app.schemas.category import CategoryCreate, CategoryUpdate, CategoryRead


def _to_read(c: Category, article_count: int = 0) -> CategoryRead:
    return CategoryRead(
        id=c.id, name=c.name, slug=c.slug, description=c.description,
        icon=c.icon, color=c.color, sort_order=c.sort_order,
        article_count=article_count, created_at=c.created_at,
    )


def list_categories(db: Session) -> list[CategoryRead]:
    counts = dict(
        db.query(Article.category_id, func.count(Article.id))
        .group_by(Article.category_id).all()
    )
    cats = db.query(Category).order_by(Category.sort_order, Category.name).all()
    return [_to_read(c, counts.get(c.id, 0)) for c in cats]


def get_category(db: Session, category_id: int) -> Optional[CategoryRead]:
    c = db.query(Category).get(category_id)
    if not c:
        return None
    count = db.query(func.count(Article.id)).filter(Article.category_id == c.id).scalar()
    return _to_read(c, count)


def create_category(db: Session, data: CategoryCreate) -> CategoryRead:
    slug = slugify(data.name, max_length=120)
    cat = Category(slug=slug, **data.model_dump())
    db.add(cat)
    db.commit()
    db.refresh(cat)
    return _to_read(cat)


def update_category(db: Session, category_id: int, data: CategoryUpdate) -> Optional[CategoryRead]:
    cat = db.query(Category).get(category_id)
    if not cat:
        return None
    updates = data.model_dump(exclude_unset=True)
    if "name" in updates:
        cat.slug = slugify(updates["name"], max_length=120)
    for key, val in updates.items():
        setattr(cat, key, val)
    db.commit()
    db.refresh(cat)
    count = db.query(func.count(Article.id)).filter(Article.category_id == cat.id).scalar()
    return _to_read(cat, count)


def delete_category(db: Session, category_id: int) -> bool:
    cat = db.query(Category).get(category_id)
    if not cat:
        return False
    db.delete(cat)
    db.commit()
    return True
