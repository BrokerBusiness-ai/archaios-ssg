"""Newsletter API — public endpoint dla formularza + confirmation/unsubscribe + admin stats."""

from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import RedirectResponse, HTMLResponse
from pydantic import BaseModel, EmailStr, Field
from sqlalchemy.orm import Session

from app.core.auth import get_admin_from_cookie
from app.core.database import get_db
from app.services import newsletter_service


router = APIRouter(prefix="/newsletter", tags=["newsletter"])


# ─── PUBLIC: form submit ──────────────────────────────────────────

class SignupPayload(BaseModel):
    email: EmailStr
    consent: bool = Field(..., description="RODO consent (must be True)")
    name: str | None = Field(None, max_length=120)
    source: str | None = Field("form", max_length=50)


@router.post("/")
async def signup(payload: SignupPayload, request: Request, db: Session = Depends(get_db)):
    """Form POST z frontu strony. Zapisuje subskrybenta i wysyła confirmation."""
    ip = request.client.host if request.client else None
    result = newsletter_service.signup(
        db,
        email=str(payload.email),
        consent=payload.consent,
        name=payload.name,
        ip=ip,
        source=payload.source or "form",
    )
    return result


# ─── PUBLIC: double opt-in confirmation ──────────────────────────

@router.get("/confirm/{token}", response_class=HTMLResponse)
async def confirm(token: str, db: Session = Depends(get_db)):
    """Klik z linka w confirmation email — aktywuje subskrybenta + wysyła welcome."""
    result = newsletter_service.confirm(db, token)

    if result["status"] in ("active", "already_active"):
        # Redirect na stronę "dziekujemy" (z parametrem dla GA4 tracking)
        return RedirectResponse(url="https://zdrowie.fit/dziekujemy.html?confirmed=1", status_code=302)

    # Błąd — pokaż prosty HTML
    return HTMLResponse(content=f"""
        <!DOCTYPE html><html lang="pl"><head><meta charset="UTF-8"><title>Błąd weryfikacji</title>
        <style>body{{font-family:Arial,sans-serif;max-width:600px;margin:48px auto;padding:32px;background:#fdfcf9;color:#3d3a35}}</style>
        </head><body>
        <h1 style="font-family:Georgia,serif">Coś poszło nie tak</h1>
        <p>{result["message"]}</p>
        <p><a href="https://zdrowie.fit/" style="color:#d9724a">Wróć na stronę główną</a></p>
        </body></html>
    """, status_code=400)


# ─── PUBLIC: unsubscribe ─────────────────────────────────────────

@router.get("/unsubscribe/{token}")
async def unsubscribe(token: str, db: Session = Depends(get_db)):
    """Klik z linka 'wypisz się' w stopce maila."""
    result = newsletter_service.unsubscribe(db, token)
    return RedirectResponse(url="https://zdrowie.fit/wypisano.html", status_code=302)


# ─── ADMIN: stats + lista ────────────────────────────────────────

def _require_admin(request: Request):
    admin = get_admin_from_cookie(request)
    if not admin:
        raise HTTPException(401, "Unauthorized")
    return admin


@router.get("/admin/stats")
async def admin_stats(request: Request, db: Session = Depends(get_db)):
    _require_admin(request)
    return newsletter_service.get_stats(db)


@router.get("/admin/list")
async def admin_list(request: Request, status: str | None = None, limit: int = 100,
                     db: Session = Depends(get_db)):
    _require_admin(request)
    subs = newsletter_service.list_subscribers(db, status=status, limit=limit)
    return [
        {
            "id": s.id,
            "email": s.email,
            "name": s.name,
            "status": s.status,
            "source": s.source,
            "tags": s.tags,
            "frequency": s.frequency,
            "created_at": s.created_at.isoformat(),
            "confirmed_at": s.confirmed_at.isoformat() if s.confirmed_at else None,
            "unsubscribed_at": s.unsubscribed_at.isoformat() if s.unsubscribed_at else None,
        }
        for s in subs
    ]
