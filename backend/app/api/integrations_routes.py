"""Integrations management — API keys + webhooks (admin only)."""

import secrets
from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from pydantic import BaseModel, HttpUrl
from sqlalchemy.orm import Session

from app.core.auth import get_admin_from_cookie
from app.core.database import get_db
from app.models.api_key import ApiKey
from app.models.webhook import Webhook


# Two routers: /api/integrations (JSON) + /admin/integrations (server-rendered)
api_router = APIRouter(prefix="/integrations", tags=["integrations-admin"])
admin_router = APIRouter(prefix="/admin/integrations", tags=["integrations-admin-ui"])


def _require_admin(request: Request):
    admin = get_admin_from_cookie(request)
    if not admin:
        raise HTTPException(401, "Unauthorized")
    return admin


def _require_admin_redirect(request: Request):
    admin = get_admin_from_cookie(request)
    if not admin:
        return None
    return admin


def _templates(request: Request):
    return request.app.state.templates


# ═══════════════════════════════════════════════════════════════
#                      API KEYS
# ═══════════════════════════════════════════════════════════════

class ApiKeyCreate(BaseModel):
    name: str
    description: str | None = None
    scopes: str = "read"  # CSV
    expires_days: int | None = None
    rate_limit_per_min: int = 60


@api_router.post("/api-keys", status_code=201)
async def create_api_key(
    payload: ApiKeyCreate,
    request: Request,
    db: Session = Depends(get_db),
):
    """Stworz API key. Plain key zwracany RAZ — kopiuj od razu."""
    admin = _require_admin(request)

    plain, key_hash, key_prefix = ApiKey.generate()

    expires_at = None
    if payload.expires_days:
        from datetime import timedelta
        expires_at = datetime.now(timezone.utc) + timedelta(days=payload.expires_days)

    api_key = ApiKey(
        key_hash=key_hash,
        key_prefix=key_prefix,
        name=payload.name,
        description=payload.description,
        scopes=payload.scopes,
        expires_at=expires_at,
        rate_limit_per_min=payload.rate_limit_per_min,
        created_by=admin.username,
    )
    db.add(api_key)
    db.commit()
    db.refresh(api_key)

    return {
        "id": api_key.id,
        "name": api_key.name,
        "scopes": api_key.scopes,
        "key": plain,  # ⚠️ pokazujemy RAZ — user musi skopiować
        "key_prefix": key_prefix,
        "expires_at": api_key.expires_at.isoformat() if api_key.expires_at else None,
        "warning": "Save this key NOW. It will never be shown again. Hashed in DB.",
    }


@api_router.get("/api-keys")
async def list_api_keys(request: Request, db: Session = Depends(get_db)):
    _require_admin(request)
    keys = db.query(ApiKey).order_by(ApiKey.created_at.desc()).all()
    return [{
        "id": k.id,
        "name": k.name,
        "key_prefix": k.key_prefix,
        "scopes": k.scopes,
        "is_active": k.is_active,
        "rate_limit_per_min": k.rate_limit_per_min,
        "last_used_at": k.last_used_at.isoformat() if k.last_used_at else None,
        "last_used_ip": k.last_used_ip,
        "expires_at": k.expires_at.isoformat() if k.expires_at else None,
        "revoked_at": k.revoked_at.isoformat() if k.revoked_at else None,
        "created_at": k.created_at.isoformat(),
        "created_by": k.created_by,
    } for k in keys]


@api_router.post("/api-keys/{key_id}/revoke")
async def revoke_api_key(key_id: int, request: Request, db: Session = Depends(get_db)):
    _require_admin(request)
    k = db.query(ApiKey).filter(ApiKey.id == key_id).first()
    if not k:
        raise HTTPException(404, "API key not found")
    k.is_active = False
    k.revoked_at = datetime.now(timezone.utc)
    db.commit()
    return {"status": "revoked"}


@api_router.delete("/api-keys/{key_id}", status_code=204)
async def delete_api_key(key_id: int, request: Request, db: Session = Depends(get_db)):
    _require_admin(request)
    k = db.query(ApiKey).filter(ApiKey.id == key_id).first()
    if not k:
        raise HTTPException(404)
    db.delete(k)
    db.commit()
    return


# ═══════════════════════════════════════════════════════════════
#                      WEBHOOKS
# ═══════════════════════════════════════════════════════════════

class WebhookCreate(BaseModel):
    name: str
    url: HttpUrl
    events: str = "*"  # CSV: "article.published,subscriber.created" or "*"
    auto_disable_after_failures: int = 10


@api_router.post("/webhooks", status_code=201)
async def create_webhook(payload: WebhookCreate, request: Request, db: Session = Depends(get_db)):
    admin = _require_admin(request)

    secret = secrets.token_urlsafe(32)
    wh = Webhook(
        name=payload.name,
        url=str(payload.url),
        events=payload.events,
        secret=secret,
        is_active=True,
        auto_disable_after_failures=payload.auto_disable_after_failures,
        created_by=admin.username,
    )
    db.add(wh)
    db.commit()
    db.refresh(wh)

    return {
        "id": wh.id,
        "name": wh.name,
        "url": wh.url,
        "events": wh.events,
        "secret": secret,  # ⚠️ pokazujemy RAZ — user musi skopiować dla HMAC verification
        "warning": "Save this secret NOW for HMAC signature verification. Won't be shown again.",
        "is_active": wh.is_active,
    }


@api_router.get("/webhooks")
async def list_webhooks(request: Request, db: Session = Depends(get_db)):
    _require_admin(request)
    whs = db.query(Webhook).order_by(Webhook.created_at.desc()).all()
    return [{
        "id": w.id,
        "name": w.name,
        "url": w.url,
        "events": w.events,
        "is_active": w.is_active,
        "last_triggered_at": w.last_triggered_at.isoformat() if w.last_triggered_at else None,
        "last_status_code": w.last_status_code,
        "success_count": w.success_count,
        "failure_count": w.failure_count,
        "created_at": w.created_at.isoformat(),
    } for w in whs]


@api_router.post("/webhooks/{webhook_id}/toggle")
async def toggle_webhook(webhook_id: int, request: Request, db: Session = Depends(get_db)):
    _require_admin(request)
    w = db.query(Webhook).filter(Webhook.id == webhook_id).first()
    if not w:
        raise HTTPException(404)
    w.is_active = not w.is_active
    if w.is_active:
        w.failure_count = 0  # reset
    db.commit()
    return {"id": w.id, "is_active": w.is_active}


@api_router.post("/webhooks/{webhook_id}/test")
async def test_webhook(webhook_id: int, request: Request, db: Session = Depends(get_db)):
    """Wyślij test event do webhook. Pomocny przy konfiguracji."""
    _require_admin(request)
    w = db.query(Webhook).filter(Webhook.id == webhook_id).first()
    if not w:
        raise HTTPException(404)

    from app.services import webhook_service
    result = webhook_service.dispatch(db, "test.ping", {
        "message": "This is a test from Zdrowie.fit admin panel",
        "webhook_id": w.id,
    })
    return result


@api_router.delete("/webhooks/{webhook_id}", status_code=204)
async def delete_webhook(webhook_id: int, request: Request, db: Session = Depends(get_db)):
    _require_admin(request)
    w = db.query(Webhook).filter(Webhook.id == webhook_id).first()
    if not w:
        raise HTTPException(404)
    db.delete(w)
    db.commit()
    return


# ═══════════════════════════════════════════════════════════════
#                      ADMIN UI (server-rendered)
# ═══════════════════════════════════════════════════════════════

@admin_router.get("/", response_class=HTMLResponse)
async def integrations_page(request: Request, db: Session = Depends(get_db)):
    admin = _require_admin_redirect(request)
    if not admin:
        return RedirectResponse("/admin/login", status_code=302)

    api_keys = db.query(ApiKey).order_by(ApiKey.created_at.desc()).all()
    webhooks = db.query(Webhook).order_by(Webhook.created_at.desc()).all()
    return _templates(request).TemplateResponse("admin/integrations.html", {
        "request": request, "admin": admin,
        "api_keys": api_keys, "webhooks": webhooks,
    })


@admin_router.post("/api-keys/new")
async def admin_create_api_key(
    request: Request,
    name: str = Form(...),
    description: str = Form(""),
    scopes: str = Form("read"),
    expires_days: int = Form(0),
    rate_limit_per_min: int = Form(60),
    db: Session = Depends(get_db),
):
    admin = _require_admin_redirect(request)
    if not admin:
        return RedirectResponse("/admin/login", status_code=302)

    plain, key_hash, key_prefix = ApiKey.generate()
    expires_at = None
    if expires_days > 0:
        from datetime import timedelta
        expires_at = datetime.now(timezone.utc) + timedelta(days=expires_days)

    k = ApiKey(
        key_hash=key_hash, key_prefix=key_prefix, name=name,
        description=description or None, scopes=scopes,
        expires_at=expires_at, rate_limit_per_min=rate_limit_per_min,
        created_by=admin.username,
    )
    db.add(k); db.commit(); db.refresh(k)

    # Pokazujemy plain key na osobnej stronie (RAZ)
    return _templates(request).TemplateResponse("admin/api_key_created.html", {
        "request": request, "admin": admin, "api_key": k, "plain_key": plain,
    })


@admin_router.post("/api-keys/{key_id}/revoke")
async def admin_revoke_api_key(key_id: int, request: Request, db: Session = Depends(get_db)):
    if not _require_admin_redirect(request):
        return RedirectResponse("/admin/login", status_code=302)
    k = db.query(ApiKey).filter(ApiKey.id == key_id).first()
    if k:
        k.is_active = False
        k.revoked_at = datetime.now(timezone.utc)
        db.commit()
    return RedirectResponse("/admin/integrations", status_code=302)


@admin_router.post("/api-keys/{key_id}/delete")
async def admin_delete_api_key(key_id: int, request: Request, db: Session = Depends(get_db)):
    if not _require_admin_redirect(request):
        return RedirectResponse("/admin/login", status_code=302)
    k = db.query(ApiKey).filter(ApiKey.id == key_id).first()
    if k:
        db.delete(k); db.commit()
    return RedirectResponse("/admin/integrations", status_code=302)


@admin_router.post("/webhooks/new")
async def admin_create_webhook(
    request: Request,
    name: str = Form(...),
    url: str = Form(...),
    events: str = Form("*"),
    auto_disable_after_failures: int = Form(10),
    db: Session = Depends(get_db),
):
    admin = _require_admin_redirect(request)
    if not admin:
        return RedirectResponse("/admin/login", status_code=302)
    secret = secrets.token_urlsafe(32)
    wh = Webhook(
        name=name, url=url, events=events, secret=secret,
        auto_disable_after_failures=auto_disable_after_failures,
        is_active=True, created_by=admin.username,
    )
    db.add(wh); db.commit(); db.refresh(wh)
    return _templates(request).TemplateResponse("admin/webhook_created.html", {
        "request": request, "admin": admin, "webhook": wh, "secret": secret,
    })


@admin_router.post("/webhooks/{webhook_id}/toggle")
async def admin_toggle_webhook(webhook_id: int, request: Request, db: Session = Depends(get_db)):
    if not _require_admin_redirect(request):
        return RedirectResponse("/admin/login", status_code=302)
    w = db.query(Webhook).filter(Webhook.id == webhook_id).first()
    if w:
        w.is_active = not w.is_active
        if w.is_active:
            w.failure_count = 0
        db.commit()
    return RedirectResponse("/admin/integrations", status_code=302)


@admin_router.post("/webhooks/{webhook_id}/test")
async def admin_test_webhook(webhook_id: int, request: Request, db: Session = Depends(get_db)):
    if not _require_admin_redirect(request):
        return RedirectResponse("/admin/login", status_code=302)
    w = db.query(Webhook).filter(Webhook.id == webhook_id).first()
    if w:
        from app.services import webhook_service
        webhook_service.dispatch(db, "test.ping", {
            "message": "Test from admin panel", "webhook_id": w.id,
        })
    return RedirectResponse("/admin/integrations", status_code=302)


@admin_router.post("/webhooks/{webhook_id}/delete")
async def admin_delete_webhook(webhook_id: int, request: Request, db: Session = Depends(get_db)):
    if not _require_admin_redirect(request):
        return RedirectResponse("/admin/login", status_code=302)
    w = db.query(Webhook).filter(Webhook.id == webhook_id).first()
    if w:
        db.delete(w); db.commit()
    return RedirectResponse("/admin/integrations", status_code=302)
