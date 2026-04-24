from pydantic import BaseModel, Field


class LoginRequest(BaseModel):
    username: str = Field(..., min_length=1)
    password: str = Field(..., min_length=1)


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class StatsResponse(BaseModel):
    total_articles: int
    published_articles: int
    draft_articles: int
    total_categories: int
    total_views: int
    featured_articles: int
