"""Server-rendered admin panel using Jinja2."""

from datetime import datetime
from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.orm import Session

from app.core.auth import (
    create_access_token, get_admin_from_cookie, verify_password,
)
from app.core.database import get_db
from app.models.admin_user import AdminUser
from app.models.article import Article
from app.models.category import Category
from app.services import article_service, category_service, author_service, product_service, stats_service
from app.schemas.article import ArticleCreate, ArticleUpdate
from app.schemas.author import AuthorCreate, AuthorUpdate
from app.schemas.category import CategoryCreate, CategoryUpdate
from app.schemas.product import ProductCreate, ProductUpdate

router = APIRouter(prefix="/admin", tags=["admin-panel"])


def _templates(request: Request):
    return request.app.state.templates


def _require(request: Request):
    admin = get_admin_from_cookie(request)
    if not admin:
        return None
    return admin


def _dt(val: str) -> datetime | None:
    if not val:
        return None
    try:
        return datetime.fromisoformat(val)
    except ValueError:
        return None


# ── Login ────────────────────────────────────────────────────────

@router.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return _templates(request).TemplateResponse("admin/login.html", {"request": request, "error": ""})


@router.post("/login", response_class=HTMLResponse)
async def login_submit(request: Request, username: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    user = db.query(AdminUser).filter(AdminUser.username == username).first()
    if not user or not verify_password(password, user.password_hash):
        return _templates(request).TemplateResponse("admin/login.html", {"request": request, "error": "Nieprawidłowy login lub hasło"})
    token = create_access_token({"sub": user.username})
    resp = RedirectResponse("/admin/", status_code=302)
    resp.set_cookie("access_token", token, httponly=True, max_age=3600 * 8)
    return resp


@router.get("/logout")
async def logout():
    resp = RedirectResponse("/admin/login", status_code=302)
    resp.delete_cookie("access_token")
    return resp


# ── Dashboard ────────────────────────────────────────────────────

@router.get("/", response_class=HTMLResponse)
async def dashboard(request: Request, db: Session = Depends(get_db)):
    admin = _require(request)
    if not admin:
        return RedirectResponse("/admin/login", status_code=302)
    articles = db.query(Article).count()
    published = db.query(Article).filter(Article.is_published == True).count()
    categories = db.query(Category).count()
    from sqlalchemy import func
    views = db.query(func.coalesce(func.sum(Article.views), 0)).scalar()
    recent = db.query(Article).order_by(Article.updated_at.desc()).limit(10).all()

    # Live stats z trackera (server-side, niezależne od GA4)
    overview = stats_service.get_overview(db)
    daily_chart = stats_service.get_daily_chart(db, days=30)
    top_month = stats_service.get_top_articles(db, period="month", limit=5)
    live_readers = stats_service.get_live_readers(db)

    return _templates(request).TemplateResponse("admin/dashboard.html", {
        "request": request, "admin": admin,
        "articles": articles, "published": published, "drafts": articles - published,
        "categories": categories, "views": views, "recent": recent,
        "authors_count": db.query(__import__('app.models.author', fromlist=['Author']).Author).count(),
        "products_count": db.query(__import__('app.models.product', fromlist=['Product']).Product).count(),
        # Tracker stats:
        "stats_overview": overview,
        "stats_daily_chart": daily_chart,
        "stats_top_month": top_month,
        "stats_live_readers": live_readers,
    })


# ── Articles ─────────────────────────────────────────────────────

@router.get("/articles", response_class=HTMLResponse)
async def articles_list(request: Request, db: Session = Depends(get_db)):
    admin = _require(request)
    if not admin:
        return RedirectResponse("/admin/login", status_code=302)
    result = article_service.list_articles(db, per_page=100, published_only=False)
    return _templates(request).TemplateResponse("admin/articles.html", {
        "request": request, "admin": admin, "articles": result.items,
        "categories": category_service.list_categories(db),
    })


@router.get("/articles/new", response_class=HTMLResponse)
async def article_new(request: Request, db: Session = Depends(get_db)):
    admin = _require(request)
    if not admin:
        return RedirectResponse("/admin/login", status_code=302)
    return _templates(request).TemplateResponse("admin/article_form.html", {
        "request": request, "admin": admin, "article": None,
        "categories": category_service.list_categories(db),
        "authors": author_service.list_authors(db),
        "all_articles": article_service.list_articles(db, per_page=100).items,
        "all_products": product_service.list_products(db),
        "error": "",
    })


@router.post("/articles/new")
async def article_create(
    request: Request,
    title: str = Form(...), excerpt: str = Form(""), content: str = Form(""),
    category_id: int = Form(0), author_id: int = Form(0),
    author: str = Form("Zdrowie Fit Team"),
    image_url: str = Form(""), og_image_custom: str = Form(""),
    icon: str = Form("📝"), tags: str = Form(""),
    reading_time: int = Form(5),
    bibliography: str = Form(""),
    related_slugs: str = Form(""),
    product_slugs: str = Form(""),
    is_published: bool = Form(False),
    is_featured: bool = Form(False),
    meta_title: str = Form(""),
    meta_description: str = Form(""),
    db: Session = Depends(get_db),
):
    if not _require(request):
        return RedirectResponse("/admin/login", status_code=302)
    data = ArticleCreate(
        title=title, excerpt=excerpt, content=content,
        category_id=category_id if category_id else None,
        author_id=author_id if author_id else None,
        author=author, image_url=image_url, og_image_custom=og_image_custom,
        icon=icon, tags=tags, reading_time=reading_time,
        bibliography=bibliography, related_slugs=related_slugs, product_slugs=product_slugs,
        is_published=is_published, is_featured=is_featured,
        meta_title=meta_title, meta_description=meta_description,
    )
    article_service.create_article(db, data)
    return RedirectResponse("/admin/articles", status_code=302)


@router.get("/articles/{article_id}/edit", response_class=HTMLResponse)
async def article_edit(request: Request, article_id: int, db: Session = Depends(get_db)):
    admin = _require(request)
    if not admin:
        return RedirectResponse("/admin/login", status_code=302)
    article = article_service.get_article_by_id(db, article_id)
    if not article:
        return RedirectResponse("/admin/articles", status_code=302)
    return _templates(request).TemplateResponse("admin/article_form.html", {
        "request": request, "admin": admin, "article": article,
        "categories": category_service.list_categories(db),
        "authors": author_service.list_authors(db),
        "all_articles": [a for a in article_service.list_articles(db, per_page=100).items if a.id != article_id],
        "all_products": product_service.list_products(db),
        "error": "",
    })


@router.post("/articles/{article_id}/edit")
async def article_update(
    request: Request, article_id: int,
    title: str = Form(...), excerpt: str = Form(""), content: str = Form(""),
    category_id: int = Form(0), author_id: int = Form(0),
    author: str = Form("Zdrowie Fit Team"),
    image_url: str = Form(""), og_image_custom: str = Form(""),
    icon: str = Form("📝"), tags: str = Form(""),
    reading_time: int = Form(5),
    bibliography: str = Form(""),
    related_slugs: str = Form(""),
    product_slugs: str = Form(""),
    is_published: bool = Form(False),
    is_featured: bool = Form(False),
    meta_title: str = Form(""),
    meta_description: str = Form(""),
    db: Session = Depends(get_db),
):
    if not _require(request):
        return RedirectResponse("/admin/login", status_code=302)
    data = ArticleUpdate(
        title=title, excerpt=excerpt, content=content,
        category_id=category_id if category_id else None,
        author_id=author_id if author_id else None,
        author=author, image_url=image_url, og_image_custom=og_image_custom,
        icon=icon, tags=tags, reading_time=reading_time,
        bibliography=bibliography, related_slugs=related_slugs, product_slugs=product_slugs,
        is_published=is_published, is_featured=is_featured,
        meta_title=meta_title, meta_description=meta_description,
    )
    article_service.update_article(db, article_id, data)
    return RedirectResponse("/admin/articles", status_code=302)


@router.post("/articles/{article_id}/delete")
async def article_delete(request: Request, article_id: int, db: Session = Depends(get_db)):
    if not _require(request):
        return RedirectResponse("/admin/login", status_code=302)
    article_service.delete_article(db, article_id)
    return RedirectResponse("/admin/articles", status_code=302)


# ── Categories ───────────────────────────────────────────────────

@router.get("/categories", response_class=HTMLResponse)
async def categories_list(request: Request, db: Session = Depends(get_db)):
    admin = _require(request)
    if not admin:
        return RedirectResponse("/admin/login", status_code=302)
    return _templates(request).TemplateResponse("admin/categories.html", {
        "request": request, "admin": admin, "categories": category_service.list_categories(db),
    })


@router.post("/categories/new")
async def category_create(request: Request, name: str = Form(...), description: str = Form(""),
                          icon: str = Form("📝"), color: str = Form("#4a7c59"), db: Session = Depends(get_db)):
    if not _require(request):
        return RedirectResponse("/admin/login", status_code=302)
    category_service.create_category(db, CategoryCreate(name=name, description=description, icon=icon, color=color))
    return RedirectResponse("/admin/categories", status_code=302)


@router.post("/categories/{category_id}/delete")
async def category_delete(request: Request, category_id: int, db: Session = Depends(get_db)):
    if not _require(request):
        return RedirectResponse("/admin/login", status_code=302)
    category_service.delete_category(db, category_id)
    return RedirectResponse("/admin/categories", status_code=302)


# ── Authors ──────────────────────────────────────────────────────

@router.get("/authors", response_class=HTMLResponse)
async def authors_list(request: Request, db: Session = Depends(get_db)):
    admin = _require(request)
    if not admin:
        return RedirectResponse("/admin/login", status_code=302)
    return _templates(request).TemplateResponse("admin/authors.html", {
        "request": request, "admin": admin, "authors": author_service.list_authors(db),
    })


@router.get("/authors/new", response_class=HTMLResponse)
async def author_new_form(request: Request):
    admin = _require(request)
    if not admin:
        return RedirectResponse("/admin/login", status_code=302)
    return _templates(request).TemplateResponse("admin/author_form.html", {
        "request": request, "admin": admin, "author": None, "error": "",
    })


@router.post("/authors/new")
async def author_create(request: Request, name: str = Form(...), bio_short: str = Form(""),
                        bio_long: str = Form(""), credentials: str = Form(""),
                        photo_url: str = Form(""), email: str = Form(""),
                        linkedin: str = Form(""), twitter: str = Form(""), website: str = Form(""),
                        specializations: str = Form(""), is_active: bool = Form(True),
                        sort_order: int = Form(0), db: Session = Depends(get_db)):
    if not _require(request):
        return RedirectResponse("/admin/login", status_code=302)
    author_service.create_author(db, AuthorCreate(
        name=name, bio_short=bio_short, bio_long=bio_long, credentials=credentials,
        photo_url=photo_url, email=email, linkedin=linkedin, twitter=twitter, website=website,
        specializations=specializations, is_active=is_active, sort_order=sort_order,
    ))
    return RedirectResponse("/admin/authors", status_code=302)


@router.get("/authors/{author_id}/edit", response_class=HTMLResponse)
async def author_edit_form(request: Request, author_id: int, db: Session = Depends(get_db)):
    admin = _require(request)
    if not admin:
        return RedirectResponse("/admin/login", status_code=302)
    author = author_service.get_author_by_id(db, author_id)
    if not author:
        return RedirectResponse("/admin/authors", status_code=302)
    return _templates(request).TemplateResponse("admin/author_form.html", {
        "request": request, "admin": admin, "author": author, "error": "",
    })


@router.post("/authors/{author_id}/edit")
async def author_update(request: Request, author_id: int, name: str = Form(...), bio_short: str = Form(""),
                        bio_long: str = Form(""), credentials: str = Form(""),
                        photo_url: str = Form(""), email: str = Form(""),
                        linkedin: str = Form(""), twitter: str = Form(""), website: str = Form(""),
                        specializations: str = Form(""), is_active: bool = Form(True),
                        sort_order: int = Form(0), db: Session = Depends(get_db)):
    if not _require(request):
        return RedirectResponse("/admin/login", status_code=302)
    author_service.update_author(db, author_id, AuthorUpdate(
        name=name, bio_short=bio_short, bio_long=bio_long, credentials=credentials,
        photo_url=photo_url, email=email, linkedin=linkedin, twitter=twitter, website=website,
        specializations=specializations, is_active=is_active, sort_order=sort_order,
    ))
    return RedirectResponse("/admin/authors", status_code=302)


@router.post("/authors/{author_id}/delete")
async def author_delete(request: Request, author_id: int, db: Session = Depends(get_db)):
    if not _require(request):
        return RedirectResponse("/admin/login", status_code=302)
    author_service.delete_author(db, author_id)
    return RedirectResponse("/admin/authors", status_code=302)


# ── Products / kampanie ──────────────────────────────────────────

@router.get("/products", response_class=HTMLResponse)
async def products_list(request: Request, db: Session = Depends(get_db)):
    admin = _require(request)
    if not admin:
        return RedirectResponse("/admin/login", status_code=302)
    return _templates(request).TemplateResponse("admin/products.html", {
        "request": request, "admin": admin, "products": product_service.list_products(db),
    })


@router.get("/products/new", response_class=HTMLResponse)
async def product_new_form(request: Request, db: Session = Depends(get_db)):
    admin = _require(request)
    if not admin:
        return RedirectResponse("/admin/login", status_code=302)
    return _templates(request).TemplateResponse("admin/product_form.html", {
        "request": request, "admin": admin, "product": None,
        "categories": category_service.list_categories(db), "error": "",
    })


@router.post("/products/new")
async def product_create(
    request: Request, name: str = Form(...), brand: str = Form(""),
    tagline_short: str = Form(""), tagline_long: str = Form(""),
    description: str = Form(""), cta_text: str = Form("Sprawdź"),
    target_url: str = Form(...), utm_source: str = Form("zdrowie.fit"),
    utm_medium: str = Form("article"), logo_url: str = Form(""), hero_image: str = Form(""),
    target_category_slugs: str = Form(""), target_tags: str = Form(""),
    placement: str = Form("end"), is_active: bool = Form(True),
    priority: int = Form(50), valid_from: str = Form(""), valid_to: str = Form(""),
    kind: str = Form("own"), affiliate_disclaimer: str = Form(""),
    db: Session = Depends(get_db),
):
    if not _require(request):
        return RedirectResponse("/admin/login", status_code=302)
    product_service.create_product(db, ProductCreate(
        name=name, brand=brand, tagline_short=tagline_short, tagline_long=tagline_long,
        description=description, cta_text=cta_text, target_url=target_url,
        utm_source=utm_source, utm_medium=utm_medium, logo_url=logo_url, hero_image=hero_image,
        target_category_slugs=target_category_slugs, target_tags=target_tags,
        placement=placement, is_active=is_active, priority=priority,
        valid_from=_dt(valid_from), valid_to=_dt(valid_to),
        kind=kind, affiliate_disclaimer=affiliate_disclaimer,
    ))
    return RedirectResponse("/admin/products", status_code=302)


@router.get("/products/{product_id}/edit", response_class=HTMLResponse)
async def product_edit_form(request: Request, product_id: int, db: Session = Depends(get_db)):
    admin = _require(request)
    if not admin:
        return RedirectResponse("/admin/login", status_code=302)
    product = product_service.get_product_by_id(db, product_id)
    if not product:
        return RedirectResponse("/admin/products", status_code=302)
    return _templates(request).TemplateResponse("admin/product_form.html", {
        "request": request, "admin": admin, "product": product,
        "categories": category_service.list_categories(db), "error": "",
    })


@router.post("/products/{product_id}/edit")
async def product_update(
    request: Request, product_id: int,
    name: str = Form(...), brand: str = Form(""),
    tagline_short: str = Form(""), tagline_long: str = Form(""),
    description: str = Form(""), cta_text: str = Form("Sprawdź"),
    target_url: str = Form(...), utm_source: str = Form("zdrowie.fit"),
    utm_medium: str = Form("article"), logo_url: str = Form(""), hero_image: str = Form(""),
    target_category_slugs: str = Form(""), target_tags: str = Form(""),
    placement: str = Form("end"), is_active: bool = Form(True),
    priority: int = Form(50), valid_from: str = Form(""), valid_to: str = Form(""),
    kind: str = Form("own"), affiliate_disclaimer: str = Form(""),
    db: Session = Depends(get_db),
):
    if not _require(request):
        return RedirectResponse("/admin/login", status_code=302)
    product_service.update_product(db, product_id, ProductUpdate(
        name=name, brand=brand, tagline_short=tagline_short, tagline_long=tagline_long,
        description=description, cta_text=cta_text, target_url=target_url,
        utm_source=utm_source, utm_medium=utm_medium, logo_url=logo_url, hero_image=hero_image,
        target_category_slugs=target_category_slugs, target_tags=target_tags,
        placement=placement, is_active=is_active, priority=priority,
        valid_from=_dt(valid_from), valid_to=_dt(valid_to),
        kind=kind, affiliate_disclaimer=affiliate_disclaimer,
    ))
    return RedirectResponse("/admin/products", status_code=302)


@router.post("/products/{product_id}/delete")
async def product_delete(request: Request, product_id: int, db: Session = Depends(get_db)):
    if not _require(request):
        return RedirectResponse("/admin/login", status_code=302)
    product_service.delete_product(db, product_id)
    return RedirectResponse("/admin/products", status_code=302)
