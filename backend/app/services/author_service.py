"""Author CRUD."""

from typing import Optional
from slugify import slugify
from sqlalchemy.orm import Session

from app.models.author import Author
from app.schemas.author import AuthorCreate, AuthorUpdate


def _unique_slug(db: Session, name: str, exclude_id: Optional[int] = None) -> str:
    base = slugify(name, max_length=200) or "autor"
    slug, counter = base, 1
    while True:
        q = db.query(Author).filter(Author.slug == slug)
        if exclude_id:
            q = q.filter(Author.id != exclude_id)
        if not q.first():
            return slug
        slug = f"{base}-{counter}"
        counter += 1


def list_authors(db: Session, active_only: bool = False) -> list[Author]:
    q = db.query(Author)
    if active_only:
        q = q.filter(Author.is_active == True)
    return q.order_by(Author.sort_order, Author.name).all()


def get_author_by_id(db: Session, author_id: int) -> Optional[Author]:
    return db.query(Author).get(author_id)


def get_author_by_slug(db: Session, slug: str) -> Optional[Author]:
    return db.query(Author).filter(Author.slug == slug).first()


def create_author(db: Session, data: AuthorCreate) -> Author:
    slug = _unique_slug(db, data.name)
    author = Author(slug=slug, **data.model_dump())
    db.add(author)
    db.commit()
    db.refresh(author)
    return author


def update_author(db: Session, author_id: int, data: AuthorUpdate) -> Optional[Author]:
    author = db.query(Author).get(author_id)
    if not author:
        return None
    updates = data.model_dump(exclude_unset=True)
    if "name" in updates:
        author.slug = _unique_slug(db, updates["name"], exclude_id=author_id)
    for k, v in updates.items():
        setattr(author, k, v)
    db.commit()
    db.refresh(author)
    return author


def delete_author(db: Session, author_id: int) -> bool:
    author = db.query(Author).get(author_id)
    if not author:
        return False
    db.delete(author)
    db.commit()
    return True
