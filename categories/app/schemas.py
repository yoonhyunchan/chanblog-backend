from pydantic import BaseModel

class SlugBody(BaseModel):
    slug: str

class CategoryBase(BaseModel):
    slug: str
    title: str
    image: str

class CategoryCreate(CategoryBase):
    pass

class CategoryUpdate(BaseModel):
    title: str | None = None
    image: str | None = None

class Category(CategoryBase):
    id: int
    class Config:
        orm_mode = True
