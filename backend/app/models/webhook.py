"""Webhook — outgoing notifications dla zewnętrznych integracji.

Backend wysyła POST do skonfigurowanego URL gdy zachodzi event.
Body: JSON z payload eventu. Header X-Signature: HMAC-SHA256 z secret.

Eventy supportowane:
  article.created          - nowy artykuł stworzony (draft lub published)
  article.published        - artykuł opublikowany (is_published: false → true)
  article.updated          - artykuł edytowany
  article.deleted          - artykuł usunięty
  subscriber.created       - nowy subscriber (po confirmation, status=active)
  subscriber.unsubscribed  - subscriber się wypisał
  comment.created          - (gdy będą komentarze, na razie placeholder)
"""

from datetime import datetime, timezone
from sqlalchemy import Column, Integer, String, DateTime, Boolean

from app.core.database import Base


class Webhook(Base):
    __tablename__ = "webhooks"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(120), nullable=False)
    url = Column(String(500), nullable=False)

    # CSV listy eventów: "article.published,subscriber.created"
    # "*" = wszystkie eventy
    events = Column(String(500), nullable=False, default="*")

    # Secret — używany do HMAC signing (header X-Signature)
    secret = Column(String(64), nullable=False)

    is_active = Column(Boolean, default=True, nullable=False)

    # Statystyki
    last_triggered_at = Column(DateTime, nullable=True)
    last_status_code = Column(Integer, nullable=True)
    last_response_body = Column(String(500), nullable=True)
    failure_count = Column(Integer, default=0, nullable=False)
    success_count = Column(Integer, default=0, nullable=False)

    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    created_by = Column(String(120), nullable=False)

    # Auto-disable po N kolejnych failach (default 10)
    auto_disable_after_failures = Column(Integer, default=10, nullable=False)

    def __repr__(self):
        return f"<Webhook {self.name} url={self.url[:40]}...>"

    def matches_event(self, event: str) -> bool:
        """Sprawdza czy webhook obsługuje dany event."""
        if not self.events:
            return False
        if self.events.strip() == "*":
            return True
        configured = {e.strip() for e in self.events.split(",")}
        if event in configured:
            return True
        # Wildcard typu "article.*"
        prefix = event.split(".")[0] + ".*"
        return prefix in configured
