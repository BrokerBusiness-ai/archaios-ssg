from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class ProductCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=200)
    brand: str = Field(default="", max_length=100)
    tagline_short: str = Field(default="", max_length=200)
    tagline_long: str = Field(default="", max_length=500)
    description: str = Field(default="")
    cta_text: str = Field(default="Sprawdź", max_length=100)
    target_url: str = Field(..., min_length=1, max_length=500)
    utm_source: str = Field(default="zdrowie.fit", max_length=100)
    utm_medium: str = Field(default="article", max_length=100)
    logo_url: str = Field(default="", max_length=500)
    hero_image: str = Field(default="", max_length=500)
    target_category_slugs: str = Field(default="", max_length=500)
    target_tags: str = Field(default="", max_length=500)
    placement: str = Field(default="end", max_length=20)
    is_active: bool = True
    priority: int = Field(default=50, ge=0, le=100)
    valid_from: Optional[datetime] = None
    valid_to: Optional[datetime] = None
    kind: str = Field(default="own", max_length=20)
    affiliate_disclaimer: str = Field(default="", max_length=200)


class ProductUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=200)
    brand: Optional[str] = Field(None, max_length=100)
    tagline_short: Optional[str] = Field(None, max_length=200)
    tagline_long: Optional[str] = Field(None, max_length=500)
    description: Optional[str] = None
    cta_text: Optional[str] = Field(None, max_length=100)
    target_url: Optional[str] = Field(None, min_length=1, max_length=500)
    utm_source: Optional[str] = Field(None, max_length=100)
    utm_medium: Optional[str] = Field(None, max_length=100)
    logo_url: Optional[str] = Field(None, max_length=500)
    hero_image: Optional[str] = Field(None, max_length=500)
    target_category_slugs: Optional[str] = Field(None, max_length=500)
    target_tags: Optional[str] = Field(None, max_length=500)
    placement: Optional[str] = Field(None, max_length=20)
    is_active: Optional[bool] = None
    priority: Optional[int] = Field(None, ge=0, le=100)
    valid_from: Optional[datetime] = None
    valid_to: Optional[datetime] = None
    kind: Optional[str] = Field(None, max_length=20)
    affiliate_disclaimer: Optional[str] = Field(None, max_length=200)


class ProductRead(BaseModel):
    id: int
    name: str
    slug: str
    brand: str
    tagline_short: str
    tagline_long: str
    description: str
    cta_text: str
    target_url: str
    utm_source: str
    utm_medium: str
    logo_url: str
    hero_image: str
    target_category_slugs: str
    target_tags: str
    placement: str
    is_active: bool
    priority: int
    valid_from: Optional[datetime]
    valid_to: Optional[datetime]
    kind: str
    affiliate_disclaimer: str
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}
