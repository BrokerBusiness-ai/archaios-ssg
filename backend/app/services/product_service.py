"""Product CRUD + matching articles."""

from datetime import datetime
from typing import Optional
from slugify import slugify
from sqlalchemy.orm import Session

from app.models.product import Product
from app.schemas.product import ProductCreate, ProductUpdate


def _unique_slug(db: Session, name: str, exclude_id: Optional[int] = None) -> str:
    base = slugify(name, max_length=200) or "produkt"
    slug, counter = base, 1
    while True:
        q = db.query(Product).filter(Product.slug == slug)
        if exclude_id:
            q = q.filter(Product.id != exclude_id)
        if not q.first():
            return slug
        slug = f"{base}-{counter}"
        counter += 1


def list_products(db: Session, active_only: bool = False, now: Optional[datetime] = None) -> list[Product]:
    q = db.query(Product)
    if active_only:
        now = now or datetime.utcnow()
        q = q.filter(Product.is_active == True)
        q = q.filter((Product.valid_from == None) | (Product.valid_from <= now))  # noqa: E711
        q = q.filter((Product.valid_to == None) | (Product.valid_to >= now))       # noqa: E711
    return q.order_by(Product.priority.desc(), Product.name).all()


def get_product_by_id(db: Session, product_id: int) -> Optional[Product]:
    return db.query(Product).get(product_id)


def get_product_by_slug(db: Session, slug: str) -> Optional[Product]:
    return db.query(Product).filter(Product.slug == slug).first()


def create_product(db: Session, data: ProductCreate) -> Product:
    slug = _unique_slug(db, data.name)
    p = Product(slug=slug, **data.model_dump())
    db.add(p)
    db.commit()
    db.refresh(p)
    return p


def update_product(db: Session, product_id: int, data: ProductUpdate) -> Optional[Product]:
    p = db.query(Product).get(product_id)
    if not p:
        return None
    updates = data.model_dump(exclude_unset=True)
    if "name" in updates:
        p.slug = _unique_slug(db, updates["name"], exclude_id=product_id)
    for k, v in updates.items():
        setattr(p, k, v)
    db.commit()
    db.refresh(p)
    return p


def delete_product(db: Session, product_id: int) -> bool:
    p = db.query(Product).get(product_id)
    if not p:
        return False
    db.delete(p)
    db.commit()
    return True


def match_products_for_article(db: Session, article, limit: int = 2) -> list[Product]:
    """Zwraca posortowaną listę produktów pasujących do artykułu (wg priorytetu)."""
    all_products = list_products(db, active_only=True)
    matching = [p for p in all_products if p.matches(article)]
    return matching[:limit]
