"""Brevo Transactional Email API client.

Używa Brevo SMTP API (https://api.brevo.com/v3/smtp/email) do wysyłania maili
transakcyjnych (confirmation, welcome, reactivation). Pomija Verified Sender
(używa Domain Authentication — DKIM/SPF z DNS, które już mamy zielone).

Wymaga BREVO_API_KEY w .env (xkeysib-...).
"""

import os
import logging
from pathlib import Path
from typing import Optional

import httpx

log = logging.getLogger(__name__)

BREVO_API_URL = "https://api.brevo.com/v3/smtp/email"
TEMPLATES_DIR = Path(__file__).resolve().parent.parent.parent.parent / "email-templates"


def _api_key() -> Optional[str]:
    return os.environ.get("BREVO_API_KEY")


def _is_configured() -> bool:
    return bool(_api_key())


def _load_template(name: str) -> str:
    """Wczytaj szablon HTML z folderu email-templates/."""
    path = TEMPLATES_DIR / name
    if not path.exists():
        log.error(f"Email template not found: {path}")
        return ""
    return path.read_text(encoding="utf-8")


def _render(template: str, vars: dict) -> str:
    """Prosty render — podmiana {{ key }} → vars[key]. Wystarczy dla naszych potrzeb."""
    out = template
    for k, v in vars.items():
        # Obsługuj zarówno {{ key }} jak i {{key}}, oraz nested {{ params.key }}
        out = out.replace("{{ " + k + " }}", str(v))
        out = out.replace("{{" + k + "}}", str(v))
    # Usuń nieobsłużone Jinja-like placeholdery (np. {% if %} bloki)
    import re
    out = re.sub(r'\{%[^}]*%\}', '', out)
    out = re.sub(r'\{\{[^}]*\}\}', '', out)
    return out


def send_email(
    *,
    to_email: str,
    to_name: Optional[str] = None,
    subject: str,
    html_content: str,
    sender_name: str = "Zdrowie.fit",
    sender_email: str = "kontakt@zdrowie.fit",
    reply_to: Optional[str] = None,
    tags: Optional[list[str]] = None,
) -> bool:
    """Wyślij pojedynczy mail przez Brevo Transactional API.

    Returns True jeśli sukces, False jeśli błąd (loguje szczegóły).
    """
    if not _is_configured():
        log.warning("BREVO_API_KEY not set — email not sent (dev mode). Recipient: %s", to_email)
        return False

    payload = {
        "sender": {"name": sender_name, "email": sender_email},
        "to": [{"email": to_email, "name": to_name} if to_name else {"email": to_email}],
        "subject": subject,
        "htmlContent": html_content,
    }
    if reply_to:
        payload["replyTo"] = {"email": reply_to}
    if tags:
        payload["tags"] = tags

    headers = {
        "accept": "application/json",
        "api-key": _api_key(),
        "content-type": "application/json",
    }

    try:
        with httpx.Client(timeout=15.0) as client:
            r = client.post(BREVO_API_URL, json=payload, headers=headers)
            if r.status_code in (200, 201):
                log.info("Brevo: sent %s → %s (msgId=%s)", subject, to_email, r.json().get("messageId"))
                return True
            log.error("Brevo API error %d: %s — payload to=%s", r.status_code, r.text, to_email)
            return False
    except httpx.RequestError as e:
        log.error("Brevo network error: %s — payload to=%s", e, to_email)
        return False


# ── Wysyłka konkretnych typów maili ──────────────────────────────

def send_confirmation(
    *,
    to_email: str,
    confirmation_url: str,
    name: Optional[str] = None,
) -> bool:
    """Double opt-in confirmation."""
    template = _load_template("confirmation.html")
    if not template:
        return False
    html = _render(template, {
        "doubleoptin": confirmation_url,
        "contact.NAME": name or "",
        "params.year": _current_year(),
    })
    return send_email(
        to_email=to_email,
        to_name=name,
        subject="Potwierdź zapis na newsletter Zdrowie.fit",
        html_content=html,
        tags=["confirmation"],
    )


def send_welcome(
    *,
    to_email: str,
    unsubscribe_url: str,
    name: Optional[str] = None,
) -> bool:
    """Welcome po confirm."""
    template = _load_template("welcome.html")
    if not template:
        return False
    html = _render(template, {
        "unsubscribe": unsubscribe_url,
        "contact.NAME": name or "",
        "params.year": _current_year(),
    })
    return send_email(
        to_email=to_email,
        to_name=name,
        subject="Witaj w Zdrowie.fit — co dalej",
        html_content=html,
        tags=["welcome"],
    )


def send_unsubscribe_confirmation(
    *,
    to_email: str,
    name: Optional[str] = None,
) -> bool:
    """Krótkie potwierdzenie wypisu (RODO best practice)."""
    html = f"""
    <div style="font-family:Arial,sans-serif;max-width:600px;margin:0 auto;padding:32px;background:#fdfcf9">
        <h2 style="color:#2d2a26;font-family:Georgia,serif">Wypisany/a. Bez urazy.</h2>
        <p>Twoja subskrypcja newslettera Zdrowie.fit została zakończona. Twój adres email zostanie trwale usunięty z naszej bazy w ciągu 30 dni (suppression list — RODO compliance).</p>
        <p>Dziękujemy, że byłeś/aś z nami. Jeśli zmienisz zdanie — możesz zapisać się ponownie w dowolnym momencie na <a href="https://zdrowie.fit/#newsletter" style="color:#d9724a">zdrowie.fit</a>.</p>
        <p style="font-size:12px;color:#8a857d;margin-top:32px">© {_current_year()} Zdrowie.fit</p>
    </div>
    """
    return send_email(
        to_email=to_email,
        to_name=name,
        subject="Wypisałeś/aś się z newslettera Zdrowie.fit",
        html_content=html,
        tags=["unsubscribe-confirm"],
    )


def _current_year() -> int:
    from datetime import datetime
    return datetime.utcnow().year


# ── Bulk send (do weekly digest itp.) ────────────────────────────

def send_bulk(
    *,
    recipients: list[dict],  # [{email, name?}, ...]
    subject: str,
    html_content: str,
    sender_name: str = "Zdrowie.fit",
    sender_email: str = "kontakt@zdrowie.fit",
    tags: Optional[list[str]] = None,
) -> dict:
    """Bulk send — Brevo API obsługuje do 50 odbiorców per call.

    Zwraca {sent: N, failed: N, errors: [...]}.
    """
    if not _is_configured():
        return {"sent": 0, "failed": len(recipients), "errors": ["BREVO_API_KEY not set"]}

    sent = 0
    failed = 0
    errors = []

    # Brevo API: 'to' może być listą, ale wtedy każdy odbiorca dostaje ten sam mail (bez personalizacji).
    # Lepiej: pojedyncze wywołania per odbiorca (do 1000/dzień na free tier).
    for r in recipients:
        ok = send_email(
            to_email=r["email"],
            to_name=r.get("name"),
            subject=subject,
            html_content=html_content,
            sender_name=sender_name,
            sender_email=sender_email,
            tags=tags,
        )
        if ok:
            sent += 1
        else:
            failed += 1
            errors.append(r["email"])
    return {"sent": sent, "failed": failed, "errors": errors[:10]}  # max 10 błędów w response
