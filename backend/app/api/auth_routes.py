"""Auth endpoints: login, me, stats."""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import func
from sqlalchemy.orm import Session

from app.core.auth import create_access_token, get_current_admin, verify_password
from app.core.database import get_db
from app.models.admin_user import AdminUser
from app.models.article import Article
from app.models.category import Category
from app.schemas.auth import LoginRequest, StatsResponse, TokenResponse

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login", response_model=TokenResponse)
def login(data: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(AdminUser).filter(AdminUser.username == data.username).first()
    if not user or not verify_password(data.password, user.password_hash):
        raise HTTPException(401, "Nieprawidłowy login lub hasło")
    token = create_access_token({"sub": user.username})
    return TokenResponse(access_token=token)


@router.get("/me")
def me(admin: str = Depends(get_current_admin)):
    return {"username": admin}


@router.get("/stats", response_model=StatsResponse)
def stats(db: Session = Depends(get_db), _admin: str = Depends(get_current_admin)):
    total = db.query(func.count(Article.id)).scalar() or 0
    published = db.query(func.count(Article.id)).filter(Article.is_published == True).scalar() or 0
    views = db.query(func.coalesce(func.sum(Article.views), 0)).scalar() or 0
    featured = db.query(func.count(Article.id)).filter(Article.is_featured == True).scalar() or 0
    cats = db.query(func.count(Category.id)).scalar() or 0
    return StatsResponse(
        total_articles=total, published_articles=published,
        draft_articles=total - published, total_categories=cats,
        total_views=views, featured_articles=featured,
    )
