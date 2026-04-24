"""Application settings — wczytuje .env, wymaga obecno\u015bci kluczowych sekret\u00f3w."""

import sys
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    APP_NAME: str = "Archaios SSG API"
    VERSION: str = "1.0.0"
    SITE_URL: str = "https://zdrowie.fit"

    # Sekrety \u2014 MUSZ\u0104 by\u0107 w .env
    SECRET_KEY: str
    ADMIN_USERNAME: str = "admin"
    ADMIN_PASSWORD: str

    DATABASE_URL: str = "sqlite:///./zdrowiefit.db"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 480  # 8h
    CORS_ORIGINS: list[str] = ["https://zdrowie.fit"]
    ARTICLES_PER_PAGE: int = 12


try:
    settings = Settings()
except Exception as exc:
    sys.stderr.write(
        "\n[config] Brak wymaganych zmiennych w .env: "
        f"{exc}\n"
        "Skopiuj .env.example do .env i uzupe\u0142nij SECRET_KEY oraz ADMIN_PASSWORD.\n\n"
    )
    raise

# Sprawdzenie: nie pozwalaj odpali\u0107 z domy\u015blnym has\u0142em w produkcji
if settings.ADMIN_PASSWORD in ("admin123", "zmien-mnie-silne-haslo-min-16-znakow", ""):
    sys.stderr.write(
        "[config] BLAD: Ustaw silne ADMIN_PASSWORD w .env przed uruchomieniem.\n"
    )
    raise SystemExit(1)
