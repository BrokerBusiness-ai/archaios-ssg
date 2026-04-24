from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class ArticleCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=300)
    excerpt: str = Field(default="", max_length=1000)
    content: str = Field(default="")
    category_id: Optional[int] = None
    author_id: Optional[int] = None
    author: str = Field(default="Zdrowie Fit Team", max_length=200)
    image_url: str = Field(default="", max_length=500)
    og_image_custom: str = Field(default="", max_length=500)
    icon: str = Field(default="📝", max_length=10)
    tags: str = Field(default="", max_length=500)
    reading_time: int = Field(default=5, ge=1, le=120)
    bibliography: str = Field(default="")
    related_slugs: str = Field(default="", max_length=500)
    product_slugs: str = Field(default="", max_length=500)
    is_published: bool = False
    is_featured: bool = False
    meta_title: str = Field(default="", max_length=300)
    meta_description: str = Field(default="", max_length=500)


class ArticleUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=300)
    excerpt: Optional[str] = Field(None, max_length=1000)
    content: Optional[str] = None
    category_id: Optional[int] = None
    author_id: Optional[int] = None
    author: Optional[str] = Field(None, max_length=200)
    image_url: Optional[str] = Field(None, max_length=500)
    og_image_custom: Optional[str] = Field(None, max_length=500)
    icon: Optional[str] = Field(None, max_length=10)
    tags: Optional[str] = Field(None, max_length=500)
    reading_time: Optional[int] = Field(None, ge=1, le=120)
    bibliography: Optional[str] = None
    related_slugs: Optional[str] = Field(None, max_length=500)
    product_slugs: Optional[str] = Field(None, max_length=500)
    is_published: Optional[bool] = None
    is_featured: Optional[bool] = None
    meta_title: Optional[str] = Field(None, max_length=300)
    meta_description: Optional[str] = Field(None, max_length=500)


class ArticleRead(BaseModel):
    id: int
    title: str
    slug: str
    excerpt: str
    content: str
    category_id: Optional[int]
    category_name: str = ""
    category_slug: str = ""
    author_id: Optional[int] = None
    author: str
    author_slug: str = ""
    image_url: str
    og_image_custom: str = ""
    icon: str
    tags: str
    reading_time: int
    bibliography: str = ""
    related_slugs: str = ""
    product_slugs: str = ""
    is_published: bool
    is_featured: bool
    meta_title: str
    meta_description: str
    views: int
    published_at: Optional[datetime]
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class ArticleListItem(BaseModel):
    id: int
    title: str
    slug: str
    excerpt: str
    category_id: Optional[int]
    category_name: str = ""
    category_slug: str = ""
    author_id: Optional[int] = None
    author: str
    author_slug: str = ""
    image_url: str
    icon: str
    tags: str
    reading_time: int
    is_published: bool
    is_featured: bool
    views: int
    published_at: Optional[datetime]
    created_at: datetime

    model_config = {"from_attributes": True}


class PaginatedArticles(BaseModel):
    items: list[ArticleListItem]
    total: int
    page: int
    per_page: int
    pages: int
