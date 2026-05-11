"""Newsletter service — zapis, double opt-in, wypis, bulk.

Wszystkie publiczne metody są transakcyjne (commit/rollback) i bezpieczne.
Tokeny: secrets.token_urlsafe(32) — 256-bit random, URL-safe.
"""

import secrets
import logging
from datetime import datetime, timezone
from typing import Optional

from sqlalchemy.orm import Session

from app.models.subscriber import Subscriber
from app.services import brevo_service

log = logging.getLogger(__name__)

PUBLIC_BASE_URL = "https://zdrowie.fit"


def _gen_token() -> str:
    return secrets.token_urlsafe(32)


def signup(
    db: Session,
    *,
    email: str,
    consent: bool,
    name: Optional[str] = None,
    ip: Optional[str] = None,
    source: str = "form",
) -> dict:
    """Zapisz nowego subskrybenta lub re-aktywuj istniejącego.

    Returns dict z 'status' (created / resent / already_active / error) i 'message'.
    """
    email = email.strip().lower()
    if not email or "@" not in email:
        return {"status": "error", "message": "Niepoprawny adres email."}
    if not consent:
        return {"status": "error", "message": "Zgoda RODO jest wymagana."}

    existing = db.query(Subscriber).filter(Subscriber.email == email).first()

    if existing and existing.status == "active":
        return {"status": "already_active", "message": "Ten adres jest już aktywny."}

    now = datetime.now(timezone.utc)

    if existing:
        # Pending lub unsubscribed/churned — generuj nowy token, wyślij confirmation
        existing.confirmation_token = _gen_token()
        existing.unsubscribe_token = existing.unsubscribe_token or _gen_token()
        existing.opt_in_consent = True
        existing.opt_in_ip = ip
        existing.opt_in_at = now
        existing.status = "pending"
        existing.source = source
        existing.updated_at = now
        sub = existing
    else:
        sub = Subscriber(
            email=email,
            name=name,
            status="pending",
            confirmation_token=_gen_token(),
            unsubscribe_token=_gen_token(),
            opt_in_consent=True,
            opt_in_ip=ip,
            opt_in_at=now,
            source=source,
            tags="",
            lifecycle_stage="welcome_series",
            welcome_step=0,
            frequency="weekly",
        )
        db.add(sub)

    db.commit()
    db.refresh(sub)

    # Wyślij confirmation przez Brevo Transactional API
    confirm_url = f"{PUBLIC_BASE_URL}/api/newsletter/confirm/{sub.confirmation_token}"
    sent = brevo_service.send_confirmation(
        to_email=sub.email,
        confirmation_url=confirm_url,
        name=sub.name,
    )

    if not sent:
        log.warning("Confirmation email NOT sent for %s — Brevo API error or not configured.", sub.email)
        return {
            "status": "created_but_email_failed",
            "message": "Zapisaliśmy Cię, ale nie udało się wysłać emaila weryfikacyjnego. Skontaktuj się z nami.",
        }

    return {
        "status": "created" if not existing else "resent",
        "message": "Sprawdź skrzynkę — wysłaliśmy email z linkiem aktywacyjnym.",
    }


def confirm(db: Session, token: str) -> dict:
    """Aktywuj subskrybenta na podstawie tokenu confirmation."""
    if not token:
        return {"status": "error", "message": "Brak tokenu."}

    sub = db.query(Subscriber).filter(Subscriber.confirmation_token == token).first()
    if not sub:
        return {"status": "error", "message": "Token nieważny lub już wykorzystany."}

    if sub.status == "active":
        return {"status": "already_active", "message": "Subskrypcja już aktywna."}

    now = datetime.now(timezone.utc)
    sub.status = "active"
    sub.confirmed_at = now
    sub.confirmation_token = None  # jednorazowy
    sub.last_engagement_at = now
    sub.updated_at = now
    db.commit()
    db.refresh(sub)

    # Welcome email
    unsub_url = f"{PUBLIC_BASE_URL}/api/newsletter/unsubscribe/{sub.unsubscribe_token}"
    brevo_service.send_welcome(
        to_email=sub.email,
        unsubscribe_url=unsub_url,
        name=sub.name,
    )

    # Webhook event: subscriber.created (po confirmation = active)
    try:
        from app.services import webhook_service
        webhook_service.emit_subscriber_event(db, "created", sub)
    except Exception as e:
        log.error(f"Webhook emit failed for subscriber.created: {e}")

    return {"status": "active", "message": "Subskrypcja aktywowana. Sprawdź skrzynkę — wysłaliśmy welcome email."}


def unsubscribe(db: Session, token: str) -> dict:
    """Wypisz subskrybenta na podstawie tokenu unsubscribe."""
    if not token:
        return {"status": "error", "message": "Brak tokenu."}

    sub = db.query(Subscriber).filter(Subscriber.unsubscribe_token == token).first()
    if not sub:
        return {"status": "error", "message": "Token nieważny."}

    if sub.status == "unsubscribed":
        return {"status": "already_unsubscribed", "message": "Już jesteś wypisany/a."}

    now = datetime.now(timezone.utc)
    sub.status = "unsubscribed"
    sub.unsubscribed_at = now
    sub.updated_at = now
    db.commit()

    # Krótkie potwierdzenie wypisu
    brevo_service.send_unsubscribe_confirmation(to_email=sub.email, name=sub.name)

    # Webhook event
    try:
        from app.services import webhook_service
        webhook_service.emit_subscriber_event(db, "unsubscribed", sub)
    except Exception as e:
        log.error(f"Webhook emit failed for subscriber.unsubscribed: {e}")

    return {"status": "unsubscribed", "message": "Wypisano. Bez urazy."}


# ── Stats dla dashboard admin ────────────────────────────────────

def get_stats(db: Session) -> dict:
    """Statystyki subskrybentów dla admin panelu."""
    from sqlalchemy import func

    total = db.query(Subscriber).count()
    active = db.query(Subscriber).filter(Subscriber.status == "active").count()
    pending = db.query(Subscriber).filter(Subscriber.status == "pending").count()
    unsubscribed = db.query(Subscriber).filter(Subscriber.status == "unsubscribed").count()
    churned = db.query(Subscriber).filter(Subscriber.status == "churned").count()

    return {
        "total": total,
        "active": active,
        "pending": pending,
        "unsubscribed": unsubscribed,
        "churned": churned,
        "confirmation_rate": round(100 * active / total, 1) if total else 0,
    }


def list_subscribers(db: Session, status: Optional[str] = None, limit: int = 100) -> list[Subscriber]:
    q = db.query(Subscriber).order_by(Subscriber.created_at.desc())
    if status:
        q = q.filter(Subscriber.status == status)
    return q.limit(limit).all()
