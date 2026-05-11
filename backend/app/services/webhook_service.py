"""Webhook dispatcher — wysyła POST do skonfigurowanych URL gdy zachodzi event.

HMAC-SHA256 signing — każdy POST ma header X-Signature: sha256=<hex>.
Odbiorca może zweryfikować autentyczność:
    expected = hmac.new(secret.encode(), body, hashlib.sha256).hexdigest()
    assert request.headers["X-Signature"] == f"sha256={expected}"

Retry: 3 próby z exponential backoff. Po failure_count >= auto_disable_after_failures
webhook automatycznie się wyłącza (is_active=False).

Wywoływane w services (np. article_service.create_article → after commit dispatch).
"""

import json
import hmac
import hashlib
import logging
from datetime import datetime, timezone
from typing import Any

import httpx
from sqlalchemy.orm import Session

from app.models.webhook import Webhook

log = logging.getLogger(__name__)

# Wersja schemy payload — gdy się zmieni, podbijamy
WEBHOOK_SCHEMA_VERSION = "1.0"


def dispatch(db: Session, event: str, payload: dict[str, Any]) -> dict:
    """Wyślij event do wszystkich aktywnych webhooków obsługujących ten event.

    Args:
        db: Session
        event: nazwa eventu, np. "article.published"
        payload: dane eventu (będzie wrappowane w envelope)

    Returns: {sent: N, skipped: N, failed: N}
    """
    webhooks = db.query(Webhook).filter(Webhook.is_active == True).all()
    matching = [w for w in webhooks if w.matches_event(event)]

    if not matching:
        log.debug(f"Webhook dispatch: no matching webhook for event {event}")
        return {"sent": 0, "skipped": 0, "failed": 0}

    envelope = {
        "schema_version": WEBHOOK_SCHEMA_VERSION,
        "event": event,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "data": payload,
    }
    body_json = json.dumps(envelope, ensure_ascii=False, default=str).encode("utf-8")

    sent = failed = 0
    for wh in matching:
        if _send_with_retry(wh, body_json, db):
            sent += 1
        else:
            failed += 1

    return {"sent": sent, "skipped": 0, "failed": failed}


def _send_with_retry(wh: Webhook, body: bytes, db: Session, retries: int = 2) -> bool:
    """Wysyła POST z body, retry przy 5xx errors."""
    signature = "sha256=" + hmac.new(wh.secret.encode(), body, hashlib.sha256).hexdigest()
    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "X-Signature": signature,
        "X-Schema-Version": WEBHOOK_SCHEMA_VERSION,
        "User-Agent": "ZdrowieFit-Webhook/1.0",
    }

    last_error = None
    last_status = None

    for attempt in range(retries + 1):
        try:
            with httpx.Client(timeout=10.0) as client:
                r = client.post(wh.url, content=body, headers=headers)
                last_status = r.status_code
                if 200 <= r.status_code < 300:
                    wh.last_triggered_at = datetime.now(timezone.utc)
                    wh.last_status_code = r.status_code
                    wh.last_response_body = (r.text or "")[:500]
                    wh.success_count = (wh.success_count or 0) + 1
                    wh.failure_count = 0  # reset po sukcesie
                    db.commit()
                    log.info(f"Webhook OK: {wh.name} → {wh.url[:50]} ({r.status_code})")
                    return True
                # 5xx → retry, 4xx → stop
                if r.status_code < 500 and attempt == 0:
                    break
                last_error = f"HTTP {r.status_code}"
        except httpx.RequestError as e:
            last_error = str(e)

    # Failed after retries
    wh.last_triggered_at = datetime.now(timezone.utc)
    wh.last_status_code = last_status
    wh.last_response_body = (last_error or "")[:500]
    wh.failure_count = (wh.failure_count or 0) + 1

    # Auto-disable po N kolejnych failach
    if wh.failure_count >= wh.auto_disable_after_failures:
        wh.is_active = False
        log.warning(f"Webhook AUTO-DISABLED: {wh.name} ({wh.failure_count} failures)")

    db.commit()
    log.error(f"Webhook FAIL: {wh.name} → {wh.url[:50]} ({last_error})")
    return False


# ── Wygodne funkcje do wywołania z services ─────────────────────

def emit_article_event(db: Session, event_type: str, article) -> dict:
    """event_type: created / published / updated / deleted"""
    return dispatch(db, f"article.{event_type}", {
        "id": article.id,
        "slug": article.slug,
        "title": article.title,
        "category_slug": getattr(article, "category_slug", None),
        "is_published": article.is_published,
        "url": f"https://zdrowie.fit/artykuly/{article.slug}.html",
        "published_at": article.published_at.isoformat() if article.published_at else None,
    })


def emit_subscriber_event(db: Session, event_type: str, subscriber) -> dict:
    """event_type: created (after confirmation) / unsubscribed"""
    return dispatch(db, f"subscriber.{event_type}", {
        "id": subscriber.id,
        "email": subscriber.email,
        "name": subscriber.name,
        "status": subscriber.status,
        "source": subscriber.source,
    })
