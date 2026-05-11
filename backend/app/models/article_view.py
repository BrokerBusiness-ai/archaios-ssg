"""ArticleView — server-side tracker odsłon artykułów.

Każdy ping z frontu (article.js) tworzy jeden wpis. Łatwo agregowalny po dniach,
tygodniach, miesiącach, latach. Bez PII (IP hashowane, user-agent skrócony do typu).
RODO: zgodne z art. 6 ust. 1 lit. f (uzasadniony interes - statystyki własne, nie profilowanie).
"""

from datetime import datetime, timezone
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Index
from sqlalchemy.orm import relationship

from app.core.database import Base


class ArticleView(Base):
    __tablename__ = "article_views"

    id = Column(Integer, primary_key=True, index=True)

    # Powiązanie z artykułem — denormalizujemy slug (czytelność, niezmienność po zmianie ID)
    article_id = Column(Integer, ForeignKey("articles.id", ondelete="CASCADE"), nullable=True, index=True)
    article_slug = Column(String(200), nullable=False, index=True)

    # Czas — UTC, indexed dla agregatów
    viewed_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False, index=True)

    # Metadane (no PII):
    # ip_hash: SHA-256 z (IP + sól dnia) — anonimowe, ale stabilne w obrębie dnia (do unikalnych odsłon)
    ip_hash = Column(String(64), nullable=True, index=True)

    # session_id: cookie/sessionStorage z frontu — pozwala policzyć "ile sesji" vs "ile pageviews"
    session_id = Column(String(64), nullable=True, index=True)

    # device_type: mobile / tablet / desktop / bot
    device_type = Column(String(20), nullable=True)

    # referrer_host: tylko domena źródłowa (np. "google.com", "facebook.com", "direct")
    referrer_host = Column(String(120), nullable=True)

    # country: ISO-2 jeśli mamy GeoIP (na razie None — można dodać MaxMind/IP-API później)
    country = Column(String(2), nullable=True)

    # Powiązanie ORM
    article = relationship("Article", backref="view_records")

    __table_args__ = (
        Index("ix_article_views_slug_viewed", "article_slug", "viewed_at"),
        Index("ix_article_views_viewed_session", "viewed_at", "session_id"),
    )

    def __repr__(self):
        return f"<ArticleView slug={self.article_slug} at={self.viewed_at.isoformat()}>"
