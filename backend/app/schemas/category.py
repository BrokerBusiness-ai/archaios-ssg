from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class CategoryCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    description: str = Field(default="", max_length=500)
    icon: str = Field(default="📝", max_length=10)
    color: str = Field(default="#4a7c59", pattern=r"^#[0-9a-fA-F]{6}$")
    sort_order: int = Field(default=0)


class CategoryUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    icon: Optional[str] = Field(None, max_length=10)
    color: Optional[str] = Field(None, pattern=r"^#[0-9a-fA-F]{6}$")
    sort_order: Optional[int] = None


class CategoryRead(BaseModel):
    id: int
    name: str
    slug: str
    description: str
    icon: str
    color: str
    sort_order: int
    article_count: int = 0
    created_at: datetime

    model_config = {"from_attributes": True}
