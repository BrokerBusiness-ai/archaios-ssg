from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class AuthorCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=200)
    bio_short: str = Field(default="", max_length=500)
    bio_long: str = Field(default="")
    credentials: str = Field(default="", max_length=500)
    photo_url: str = Field(default="", max_length=500)
    email: str = Field(default="", max_length=200)
    linkedin: str = Field(default="", max_length=300)
    twitter: str = Field(default="", max_length=300)
    website: str = Field(default="", max_length=300)
    specializations: str = Field(default="", max_length=500)
    is_active: bool = True
    sort_order: int = 0


class AuthorUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=200)
    bio_short: Optional[str] = Field(None, max_length=500)
    bio_long: Optional[str] = None
    credentials: Optional[str] = Field(None, max_length=500)
    photo_url: Optional[str] = Field(None, max_length=500)
    email: Optional[str] = Field(None, max_length=200)
    linkedin: Optional[str] = Field(None, max_length=300)
    twitter: Optional[str] = Field(None, max_length=300)
    website: Optional[str] = Field(None, max_length=300)
    specializations: Optional[str] = Field(None, max_length=500)
    is_active: Optional[bool] = None
    sort_order: Optional[int] = None


class AuthorRead(BaseModel):
    id: int
    name: str
    slug: str
    bio_short: Optional[str] = ""
    bio_long: Optional[str] = ""
    credentials: Optional[str] = ""
    photo_url: Optional[str] = ""
    email: Optional[str] = ""
    linkedin: Optional[str] = ""
    twitter: Optional[str] = ""
    website: Optional[str] = ""
    specializations: Optional[str] = ""
    is_active: bool = True
    sort_order: int = 0
    created_at: datetime

    model_config = {"from_attributes": True}
