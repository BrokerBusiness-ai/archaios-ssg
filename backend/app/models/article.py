from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from app.core.database import Base


class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(300), nullable=False)
    slug = Column(String(350), unique=True, nullable=False, index=True)
    excerpt = Column(Text, default="")
    content = Column(Text, default="")
    category_id = Column(Integer, ForeignKey("categories.id", ondelete="SET NULL"), nullable=True)

    # Autor — nowy: FK do Author (E-E-A-T). Stare pole `author` zachowane jako fallback.
    author_id = Column(Integer, ForeignKey("authors.id", ondelete="SET NULL"), nullable=True)
    author = Column(String(200), default="Zdrowie Fit Team")

    image_url = Column(String(500), default="")
    og_image_custom = Column(String(500), default="")  # opcjonalny custom OG (1200x630)
    icon = Column(String(10), default="📝")
    tags = Column(String(500), default="")          # comma-separated
    reading_time = Column(Integer, default=5)        # minutes

    # NOWE POLA:
    bibliography = Column(Text, default="")          # HTML z listą źródeł (PubMed, DOI, linki)
    related_slugs = Column(String(500), default="")  # comma-separated slugi artykułów (manual override)
    product_slugs = Column(String(500), default="")  # comma-separated slugi produktów do promocji (manual)

    is_published = Column(Boolean, default=False)
    is_featured = Column(Boolean, default=False)
    meta_title = Column(String(300), default="")
    meta_description = Column(String(500), default="")
    views = Column(Integer, default=0)
    published_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    category = relationship("Category", back_populates="articles")
    author_obj = relationship("Author", back_populates="articles")

    @property
    def tags_list(self) -> list[str]:
        return [t.strip() for t in self.tags.split(",") if t.strip()] if self.tags else []

    @property
    def related_slugs_list(self) -> list[str]:
        return [s.strip() for s in (self.related_slugs or "").split(",") if s.strip()]

    @property
    def product_slugs_list(self) -> list[str]:
        return [s.strip() for s in (self.product_slugs or "").split(",") if s.strip()]
