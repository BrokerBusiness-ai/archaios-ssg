"""Product / kampania promocyjna — do automatycznego lejka sprzedażowego w artykułach."""

from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime
from app.core.database import Base


class Product(Base):
    """
    Produkt lub usługa do promowania w artykułach.

    System automatycznie dobiera produkty do artykułu na podstawie:
    - target_category_slugs (po kategorii artykułu)
    - target_tags (po tagach artykułu)
    - priority (wyższa = wyżej na liście)
    - is_active + valid_from/valid_to (okno czasowe np. "promocja tygodnia")
    """
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False)
    slug = Column(String(200), unique=True, nullable=False, index=True)

    # Marka/producent (np. "Nurio", "ZdrowieFit", partner afiliacyjny)
    brand = Column(String(100), default="")

    tagline_short = Column(String(200), default="")   # "Psycholog AI 24/7"
    tagline_long = Column(String(500), default="")    # pełny opis 1-2 zdania
    description = Column(Text, default="")            # HTML, dłuższy opis

    # CTA
    cta_text = Column(String(100), default="Sprawdź")
    target_url = Column(String(500), nullable=False)
    utm_source = Column(String(100), default="zdrowie.fit")
    utm_medium = Column(String(100), default="article")

    # Grafika
    logo_url = Column(String(500), default="")
    hero_image = Column(String(500), default="")

    # Targetowanie
    target_category_slugs = Column(String(500), default="")  # "psychiczne,fitness" — puste = wszystkie
    target_tags = Column(String(500), default="")             # "lęk,stres,sen"

    # Placement: gdzie w artykule
    # "sidebar" = prawy pasek, "inline" = wtrącone w treść, "end" = CTA box na końcu
    placement = Column(String(20), default="end")

    # Widoczność
    is_active = Column(Boolean, default=True)
    priority = Column(Integer, default=50)  # 0-100, wyższa = wyżej
    valid_from = Column(DateTime, nullable=True)
    valid_to = Column(DateTime, nullable=True)

    # Typ — affiliate (z uwagą UOKiK), own (własne), partner
    kind = Column(String(20), default="own")
    affiliate_disclaimer = Column(String(200), default="")

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    @property
    def target_category_slugs_list(self) -> list[str]:
        return [s.strip() for s in (self.target_category_slugs or "").split(",") if s.strip()]

    @property
    def target_tags_list(self) -> list[str]:
        return [t.strip() for t in (self.target_tags or "").split(",") if t.strip()]

    def url_with_utm(self, campaign: str = "") -> str:
        """URL z parametrami UTM do śledzenia konwersji."""
        sep = "&" if "?" in self.target_url else "?"
        parts = [
            f"utm_source={self.utm_source}",
            f"utm_medium={self.utm_medium}",
        ]
        if campaign:
            parts.append(f"utm_campaign={campaign}")
        return f"{self.target_url}{sep}{'&'.join(parts)}"

    def matches(self, article) -> bool:
        """Czy ten produkt pasuje do danego artykułu."""
        if not self.is_active:
            return False
        now = datetime.utcnow()
        if self.valid_from and self.valid_from > now:
            return False
        if self.valid_to and self.valid_to < now:
            return False

        # Dopasowanie po kategorii
        cats = self.target_category_slugs_list
        if cats and (not article.category or article.category.slug not in cats):
            # Jeśli są kategorie ale nie pasuje — szukaj po tagach
            art_tags = [t.strip().lower() for t in (article.tags or "").split(",") if t.strip()]
            product_tags = [t.lower() for t in self.target_tags_list]
            if not any(pt in art_tags for pt in product_tags):
                return False
        return True
