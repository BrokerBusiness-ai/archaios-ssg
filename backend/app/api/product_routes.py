"""Product CRUD."""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.auth import get_current_admin
from app.core.database import get_db
from app.schemas.product import ProductCreate, ProductRead, ProductUpdate
from app.services import product_service as svc

router = APIRouter(prefix="/products", tags=["products"])


@router.get("/", response_model=list[ProductRead])
def list_products(active_only: bool = False, db: Session = Depends(get_db)):
    return svc.list_products(db, active_only=active_only)


@router.get("/{product_id}", response_model=ProductRead)
def get_product(product_id: int, db: Session = Depends(get_db)):
    p = svc.get_product_by_id(db, product_id)
    if not p:
        raise HTTPException(404, "Produkt nie znaleziony")
    return p


@router.get("/slug/{slug}", response_model=ProductRead)
def get_by_slug(slug: str, db: Session = Depends(get_db)):
    p = svc.get_product_by_slug(db, slug)
    if not p:
        raise HTTPException(404, "Produkt nie znaleziony")
    return p


@router.post("/", response_model=ProductRead, status_code=201)
def create_product(data: ProductCreate, db: Session = Depends(get_db), _: str = Depends(get_current_admin)):
    return svc.create_product(db, data)


@router.put("/{product_id}", response_model=ProductRead)
def update_product(product_id: int, data: ProductUpdate, db: Session = Depends(get_db), _: str = Depends(get_current_admin)):
    r = svc.update_product(db, product_id, data)
    if not r:
        raise HTTPException(404, "Produkt nie znaleziony")
    return r


@router.delete("/{product_id}", status_code=204)
def delete_product(product_id: int, db: Session = Depends(get_db), _: str = Depends(get_current_admin)):
    if not svc.delete_product(db, product_id):
        raise HTTPException(404, "Produkt nie znaleziony")
