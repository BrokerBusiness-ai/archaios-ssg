"""API Key authentication — dla zewnętrznych integracji.

Użycie:
    @router.get("/protected")
    async def endpoint(api_key: ApiKey = Depends(require_api_key("read"))):
        ...

Nagłówek: X-API-Key: zfit_xxxxxxxxxxxxxx
"""

from datetime import datetime, timezone
from fastapi import Depends, HTTPException, Header, Request
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.api_key import ApiKey


def require_api_key(scope: str = "read"):
    """Factory tworzący FastAPI dependency wymagający API key z danym scope.

    Returns: ApiKey instance jeśli auth OK, raise HTTPException 401/403 w innym przypadku.
    """
    def _check(
        request: Request,
        x_api_key: str | None = Header(None, alias="X-API-Key"),
        db: Session = Depends(get_db),
    ) -> ApiKey:
        if not x_api_key:
            raise HTTPException(401, detail="X-API-Key header required")

        if not x_api_key.startswith("zfit_"):
            raise HTTPException(401, detail="Invalid API key format")

        key_hash = ApiKey.hash_key(x_api_key)
        api_key = db.query(ApiKey).filter(ApiKey.key_hash == key_hash).first()

        if not api_key:
            raise HTTPException(401, detail="Invalid API key")

        if not api_key.is_active or api_key.revoked_at:
            raise HTTPException(401, detail="API key revoked")

        if api_key.expires_at and api_key.expires_at < datetime.now(timezone.utc):
            raise HTTPException(401, detail="API key expired")

        if not api_key.has_scope(scope):
            raise HTTPException(
                403,
                detail=f"API key missing required scope: {scope} (has: {api_key.scopes})",
            )

        # Update last used metadata
        api_key.last_used_at = datetime.now(timezone.utc)
        api_key.last_used_ip = request.client.host if request.client else None
        db.commit()

        return api_key

    return _check


# Convenience aliases
require_read = require_api_key("read")
require_write = require_api_key("write")
require_admin_api = require_api_key("admin")
require_newsletter_scope = require_api_key("newsletter")
