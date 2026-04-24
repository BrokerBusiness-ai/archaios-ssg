"""Author — dla E-E-A-T (Google ocenia kompetencje autora w YMYL)."""

from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime
from sqlalchemy.orm import relationship

from app.core.database import Base


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False)
    slug = Column(String(200), unique=True, nullable=False, index=True)
    bio_short = Column(String(500), default="")
    bio_long = Column(Text, default="")
    credentials = Column(String(500), default="")  # "dr n. med., psychoterapeuta"
    photo_url = Column(String(500), default="")
    email = Column(String(200), default="")
    linkedin = Column(String(300), default="")
    twitter = Column(String(300), default="")
    website = Column(String(300), default="")
    specializations = Column(String(500), default="")  # comma-separated
    is_active = Column(Boolean, default=True)
    sort_order = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)

    articles = relationship("Article", back_populates="author_obj")

    @property
    def specializations_list(self) -> list[str]:
        return [s.strip() for s in (self.specializations or "").split(",") if s.strip()]
