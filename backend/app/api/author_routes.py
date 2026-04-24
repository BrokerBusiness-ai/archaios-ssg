"""Author CRUD."""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.auth import get_current_admin
from app.core.database import get_db
from app.schemas.author import AuthorCreate, AuthorRead, AuthorUpdate
from app.services import author_service as svc

router = APIRouter(prefix="/authors", tags=["authors"])


@router.get("/", response_model=list[AuthorRead])
def list_authors(active_only: bool = False, db: Session = Depends(get_db)):
    return svc.list_authors(db, active_only=active_only)


@router.get("/{author_id}", response_model=AuthorRead)
def get_author(author_id: int, db: Session = Depends(get_db)):
    a = svc.get_author_by_id(db, author_id)
    if not a:
        raise HTTPException(404, "Autor nie znaleziony")
    return a


@router.get("/slug/{slug}", response_model=AuthorRead)
def get_by_slug(slug: str, db: Session = Depends(get_db)):
    a = svc.get_author_by_slug(db, slug)
    if not a:
        raise HTTPException(404, "Autor nie znaleziony")
    return a


@router.post("/", response_model=AuthorRead, status_code=201)
def create_author(data: AuthorCreate, db: Session = Depends(get_db), _: str = Depends(get_current_admin)):
    return svc.create_author(db, data)


@router.put("/{author_id}", response_model=AuthorRead)
def update_author(author_id: int, data: AuthorUpdate, db: Session = Depends(get_db), _: str = Depends(get_current_admin)):
    r = svc.update_author(db, author_id, data)
    if not r:
        raise HTTPException(404, "Autor nie znaleziony")
    return r


@router.delete("/{author_id}", status_code=204)
def delete_author(author_id: int, db: Session = Depends(get_db), _: str = Depends(get_current_admin)):
    if not svc.delete_author(db, author_id):
        raise HTTPException(404, "Autor nie znaleziony")
