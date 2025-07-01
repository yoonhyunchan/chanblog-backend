from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime

class ArticleBase(BaseModel):
    slug: str
    title: str
    subtitle: Optional[str] = None
    excerpt: Optional[str] = None
    intro: Optional[str] = None
    content: Optional[str] = None
    category_id: int
    date: Optional[str] = None
    image: Optional[str] = None
    tags: Optional[str] = None
    author_name: Optional[str] = None
    author_title: Optional[str] = None
    author_avatar_path: Optional[str] = None

class ArticleCreate(ArticleBase):
    pass

class ArticleUpdate(ArticleBase):
    title: str
    slug: str
    subtitle: Optional[str] = None
    excerpt: Optional[str] = None
    intro: Optional[str] = None
    content: Optional[str] = None
    category_id: int
    date: Optional[str] = None
    image: Optional[str] = None
    tags: Optional[str] = None
    author_name: Optional[str] = None
    author_title: Optional[str] = None
    author_avatar_path: Optional[str] = None

class Article(ArticleBase):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
        json_encoders = {
            date: lambda v: v.isoformat() if v else None
        } 