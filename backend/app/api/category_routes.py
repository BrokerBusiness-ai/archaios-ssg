"""Category CRUD."""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.auth import get_current_admin
from app.core.database import get_db
from app.schemas.category import CategoryCreate, CategoryRead, CategoryUpdate
from app.services import category_service as svc

router = APIRouter(prefix="/categories", tags=["categories"])


@router.get("/", response_model=list[CategoryRead])
def list_categories(db: Session = Depends(get_db)):
    return svc.list_categories(db)


@router.get("/{category_id}", response_model=CategoryRead)
def get_category(category_id: int, db: Session = Depends(get_db)):
    cat = svc.get_category(db, category_id)
    if not cat:
        raise HTTPException(404, "Kategoria nie znaleziona")
    return cat


@router.post("/", response_model=CategoryRead, status_code=201)
def create_category(data: CategoryCreate, db: Session = Depends(get_db), _: str = Depends(get_current_admin)):
    return svc.create_category(db, data)


@router.put("/{category_id}", response_model=CategoryRead)
def update_category(category_id: int, data: CategoryUpdate, db: Session = Depends(get_db), _: str = Depends(get_current_admin)):
    result = svc.update_category(db, category_id, data)
    if not result:
        raise HTTPException(404, "Kategoria nie znaleziona")
    return result


@router.delete("/{category_id}", status_code=204)
def delete_category(category_id: int, db: Session = Depends(get_db), _: str = Depends(get_current_admin)):
    if not svc.delete_category(db, category_id):
        raise HTTPException(404, "Kategoria nie znaleziona")
