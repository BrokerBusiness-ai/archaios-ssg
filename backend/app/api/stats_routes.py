"""Stats API — publiczny endpoint do trackingu + admin endpoint do dashboard."""

import hashlib
import secrets
from datetime import datetime, timezone

from fastapi import APIRouter, Depends, Request, Response, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.core.auth import get_admin_from_cookie
from app.core.database import get_db
from app.services import stats_service


router = APIRouter(prefix="/stats", tags=["stats"])


# ─── PUBLIC: ping z JS przeglądarki ────────────────────────────────

class ViewPing(BaseModel):
    slug: str
    referer: str | None = None


@router.post("/view", status_code=204)
async def record_view(
    payload: ViewPing,
    request: Request,
    response: Response,
    db: Session = Depends(get_db),
):
    """JS pinguje ten endpoint po załadowaniu strony artykułu.

    - Zapisuje odsłonę z anonim metadanymi (IP hash, device, referer host)
    - Ustawia cookie session_id (sliding 30 min) jeśli nie ma
    - Inkrementuje Article.views counter
    """
    if not payload.slug or len(payload.slug) > 200:
        raise HTTPException(400, "invalid slug")

    # Session ID z cookie (lub generuj nowy)
    session_id = request.cookies.get("zf_session")
    if not session_id:
        session_id = secrets.token_urlsafe(16)
        response.set_cookie(
            "zf_session", session_id,
            max_age=1800,  # 30 min
            httponly=True, samesite="lax",
        )

    # IP hash — anonimowo, ale stabilne per dzień (sól z daty)
    client_ip = request.client.host if request.client else "0.0.0.0"
    salt = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    ip_hash = hashlib.sha256(f"{client_ip}|{salt}".encode()).hexdigest()

    # User-agent
    ua = request.headers.get("user-agent", "")

    # Referer
    referer = payload.referer or request.headers.get("referer", "")

    stats_service.record_view(
        db,
        article_slug=payload.slug,
        session_id=session_id,
        ip_hash=ip_hash,
        user_agent=ua,
        referer=referer,
    )
    return Response(status_code=204)


# ─── ADMIN: dashboard data (JSON) ──────────────────────────────────

def _require_admin(request: Request):
    admin = get_admin_from_cookie(request)
    if not admin:
        raise HTTPException(401, "Unauthorized")
    return admin


@router.get("/admin/overview")
async def admin_overview(request: Request, db: Session = Depends(get_db)):
    _require_admin(request)
    return stats_service.get_overview(db)


@router.get("/admin/daily")
async def admin_daily(request: Request, days: int = 30, db: Session = Depends(get_db)):
    _require_admin(request)
    return stats_service.get_daily_chart(db, days=days)


@router.get("/admin/top")
async def admin_top(request: Request, period: str = "month", limit: int = 10, db: Session = Depends(get_db)):
    _require_admin(request)
    return stats_service.get_top_articles(db, period=period, limit=limit)


@router.get("/admin/live")
async def admin_live(request: Request, db: Session = Depends(get_db)):
    _require_admin(request)
    return stats_service.get_live_readers(db)


@router.get("/admin/article/{slug}")
async def admin_article_stats(slug: str, request: Request, db: Session = Depends(get_db)):
    _require_admin(request)
    return stats_service.get_article_stats(db, slug)


@router.get("/admin/referrers")
async def admin_referrers(request: Request, days: int = 30, db: Session = Depends(get_db)):
    _require_admin(request)
    return stats_service.get_referrers(db, days=days)


@router.get("/admin/devices")
async def admin_devices(request: Request, days: int = 30, db: Session = Depends(get_db)):
    _require_admin(request)
    return stats_service.get_device_split(db, days=days)
