"""
Inicjalizacja świeżej bazy SQLite dla jednej domeny w CI (GitHub Actions).

Krok wymagany przed build.py w workflow .github/workflows/deploy.yml,
ponieważ backend/zdrowiefit.db nie jest w repo (jest w .gitignore).

Co robi:
1. Tworzy pusty plik backend/zdrowiefit.db
2. Importuje wszystkie modele i tworzy schemat (Base.metadata.create_all)
3. Czyta domains/<slug>.yaml i tworzy kategorie z tego pliku
4. Tworzy domyślnego autora 'marek-porycki' (używany przez wszystkie artykuły)
5. Nie wywołuje seed_service (który jest specyficzny dla zdrowie.fit)

Użycie:
    python scripts/init_ci_db.py <domain-slug>
    # np. python scripts/init_ci_db.py skanujfirme-pl
"""
from __future__ import annotations

import sys
from pathlib import Path

# Dodanie backend/ do PYTHONPATH żeby zaimportować app.*
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "backend"))

import yaml


def main():
    if len(sys.argv) < 2:
        print("Uzycie: python scripts/init_ci_db.py <domain-slug>", file=sys.stderr)
        sys.exit(1)

    domain_slug = sys.argv[1]
    yaml_path = ROOT / "domains" / f"{domain_slug}.yaml"
    if not yaml_path.exists():
        print(f"ERR: brak pliku {yaml_path}", file=sys.stderr)
        sys.exit(2)

    with open(yaml_path, encoding="utf-8") as f:
        dcfg = yaml.safe_load(f)

    # Import po skonfigurowaniu sys.path
    from app.core.database import Base, engine, SessionLocal  # noqa: E402
    # Import wszystkich modeli zeby Base.metadata znalo wszystkie tabele
    from app.models import (  # noqa: F401, E402
        admin_user, article, article_view, author, category, product,
        subscriber, api_key, webhook,
    )
    from app.models.category import Category  # noqa: E402
    from app.models.author import Author  # noqa: E402

    print(f"[init_ci_db] Tworze schemat bazy dla domeny: {domain_slug}")
    Base.metadata.create_all(engine)

    db = SessionLocal()
    try:
        # Kategorie z YAML
        cats = dcfg.get("categories", []) or []
        created_cats = 0
        for idx, c in enumerate(cats):
            name = c.get("name", "").strip()
            slug = c.get("slug", "").strip()
            if not name or not slug:
                continue
            if db.query(Category).filter_by(slug=slug).first():
                continue
            cat = Category(
                name=name,
                slug=slug,
                description="",
                icon=c.get("icon", "📝"),
                color=c.get("color", "#4a7c59"),
                sort_order=idx,
            )
            db.add(cat)
            created_cats += 1

        # Default author
        marek_slug = "marek-porycki"
        if not db.query(Author).filter_by(slug=marek_slug).first():
            db.add(Author(
                name="Marek Porycki",
                slug=marek_slug,
                credentials="psycholog, biegly sadowy, mediator, prorektor",
                bio_short=(
                    "Psycholog kliniczny, biegly sadowy, mediator. CEO Archaios.ai. "
                    "Autor publikacji naukowych i thrillerow psychologicznych."
                ),
                bio_long="",
                photo_url="",
                email="",
                linkedin="",
                twitter="",
                specializations="psychologia,mediacja,bezpieczenstwo,AI",
                sort_order=1,
            ))
            print(f"[init_ci_db] Utworzono autora: {marek_slug}")

        db.commit()
        print(f"[init_ci_db] Utworzono {created_cats} kategorii.")
        print(f"[init_ci_db] OK. Domena {domain_slug} gotowa do importu artykulow.")
    finally:
        db.close()


if __name__ == "__main__":
    main()
