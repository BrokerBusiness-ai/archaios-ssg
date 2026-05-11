"""Subscriber — model newslettera (RODO-compliant, double opt-in).

Cykl życia:
  pending → (klik confirmation link) → active → (klik unsubscribe) → unsubscribed
                                                                  → (60d bez akcji) → churned
"""

from datetime import datetime, timezone
from sqlalchemy import Column, Integer, String, DateTime, Boolean, Index
from app.core.database import Base


class Subscriber(Base):
    __tablename__ = "subscribers"

    id = Column(Integer, primary_key=True, index=True)

    email = Column(String(255), nullable=False, unique=True, index=True)
    name = Column(String(120), nullable=True)

    # status: pending / active / unsubscribed / churned / bounced
    status = Column(String(20), default="pending", nullable=False, index=True)

    # Tokeny — bezpieczne, jednorazowe URL-safe stringi
    confirmation_token = Column(String(64), nullable=True, index=True)
    unsubscribe_token = Column(String(64), nullable=True, index=True)

    # RODO — explicit consent
    opt_in_consent = Column(Boolean, default=False, nullable=False)
    opt_in_ip = Column(String(45), nullable=True)  # IPv4/IPv6 z zapisu (RODO art. 7 ust. 1 — proof of consent)
    opt_in_at = Column(DateTime, nullable=True)

    # Confirmation (klik w link aktywacyjny)
    confirmed_at = Column(DateTime, nullable=True)

    # Engagement (do segmentacji aktywności)
    last_engagement_at = Column(DateTime, nullable=True)

    # Tagi (preferencje content z welcome day 9): pref_ruch / pref_umysl / pref_dieta / pref_all
    tags = Column(String(200), default="", nullable=False)

    # Source (skąd przyszedł: form / exit-popup / ref / api)
    source = Column(String(50), default="form", nullable=False)

    # Lifecycle stage (do automation)
    lifecycle_stage = Column(String(30), default="welcome_series", nullable=False)
    welcome_step = Column(Integer, default=0, nullable=False)  # 0..5

    # Frequency (weekly / monthly)
    frequency = Column(String(20), default="weekly", nullable=False)

    # Timestamps
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc),
                        onupdate=lambda: datetime.now(timezone.utc), nullable=False)
    unsubscribed_at = Column(DateTime, nullable=True)

    __table_args__ = (
        Index("ix_subscribers_status_created", "status", "created_at"),
    )

    def __repr__(self):
        return f"<Subscriber {self.email} status={self.status}>"
