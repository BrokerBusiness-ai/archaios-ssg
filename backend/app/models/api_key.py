"""ApiKey — autentykacja zewnętrznych aplikacji (n8n / Make / Zapier / GPT Actions / MCP).

Klucz jest hashowany SHA-256 przed zapisem. Przy auth check liczymy hash z headera
i porównujemy z key_hash w bazie. Plain key jest pokazywany użytkownikowi tylko raz —
po wygenerowaniu w admin panelu (analogicznie do GitHub PAT).

Scopes:
  read         — GET endpointy (artykuły, kategorie, statystyki)
  write        — POST/PUT/DELETE artykułów, kategorii, autorów, produktów
  admin        — zarządzanie API keys, webhooks, subscribers
  newsletter   — endpoint POST /api/newsletter (do form submitu z zewnętrznych integracji)
"""

import hashlib
import secrets
from datetime import datetime, timezone

from sqlalchemy import Column, Integer, String, DateTime, Boolean

from app.core.database import Base


class ApiKey(Base):
    __tablename__ = "api_keys"

    id = Column(Integer, primary_key=True, index=True)

    # SHA-256 hash klucza (key prefix `zfit_` + 32 bytes random base64)
    key_hash = Column(String(64), nullable=False, unique=True, index=True)

    # Pierwsze 8 znaków klucza widoczne w admin panelu (do identyfikacji)
    key_prefix = Column(String(16), nullable=False)

    name = Column(String(120), nullable=False)  # np. "n8n production"
    description = Column(String(500), nullable=True)

    # Scopes — CSV (read,write,admin,newsletter)
    scopes = Column(String(200), nullable=False, default="read")

    # Lifecycle
    is_active = Column(Boolean, default=True, nullable=False)
    expires_at = Column(DateTime, nullable=True)  # opcjonalna data wygaśnięcia
    last_used_at = Column(DateTime, nullable=True)
    last_used_ip = Column(String(45), nullable=True)

    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    created_by = Column(String(120), nullable=False)  # admin username

    revoked_at = Column(DateTime, nullable=True)

    # Rate limiting (per minute) — None = no limit
    rate_limit_per_min = Column(Integer, default=60, nullable=False)

    def __repr__(self):
        return f"<ApiKey {self.key_prefix}... name={self.name} scopes={self.scopes}>"

    @staticmethod
    def generate() -> tuple[str, str, str]:
        """Generuje nowy klucz. Zwraca (plain_key, key_hash, key_prefix).

        Plain key pokazujemy użytkownikowi RAZ. Hash zapisujemy w bazie.
        """
        random_part = secrets.token_urlsafe(32)
        plain = f"zfit_{random_part}"
        key_hash = hashlib.sha256(plain.encode()).hexdigest()
        key_prefix = plain[:12]  # "zfit_xxxx"
        return plain, key_hash, key_prefix

    @staticmethod
    def hash_key(plain_key: str) -> str:
        return hashlib.sha256(plain_key.encode()).hexdigest()

    def has_scope(self, scope: str) -> bool:
        """Sprawdza czy klucz ma dany scope."""
        if not self.scopes:
            return False
        scopes_list = [s.strip() for s in self.scopes.split(",")]
        return scope in scopes_list or "admin" in scopes_list  # admin = all
