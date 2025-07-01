from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from . import models, schemas, crud
from .database import SessionLocal, engine, Base
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
Base.metadata.create_all(bind=engine)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/api/articles", response_model=schemas.Article)
def create_article(article: schemas.ArticleCreate, db: Session = Depends(get_db)):
    return crud.create_article(db=db, article=article)

@app.get("/api/articles", response_model=List[schemas.Article])
def read_articles(category_id: int = Query(None), db: Session = Depends(get_db)):
    if category_id is not None:
        articles = crud.get_articles_by_category_id(db, category_id=category_id)
    else:
        articles = crud.get_articles(db)
    return [schemas.Article.from_orm(article) for article in articles]

@app.get("/api/articles/slug/{slug}", response_model=schemas.Article)
def read_article_by_slug(slug: str, db: Session = Depends(get_db)):
    db_article = crud.get_article_by_slug(db, slug=slug)
    if db_article is None:
        raise HTTPException(status_code=404, detail="Article not found")
    return schemas.Article.from_orm(db_article)

@app.patch("/api/articles/{slug}", response_model=schemas.Article)
def update_article(slug: str, article: schemas.ArticleUpdate, db: Session = Depends(get_db)):
    db_article = crud.update_article(db, slug=slug, article=article)
    if db_article is None:
        raise HTTPException(status_code=404, detail="Article not found")
    return db_article

@app.delete("/api/articles/{slug}")
def delete_article(slug: str, db: Session = Depends(get_db)):
    success = crud.delete_article(db, slug=slug)
    if not success:
        raise HTTPException(status_code=404, detail="Article not found")
    return {"ok": True} 

@app.get("/api/articles/related")
def get_related_articles(category_id: int, exclude_slug: str, db: Session = Depends(get_db)):
    articles = crud.get_articles_by_category_id(db, category_id=category_id)
    filtered = [a for a in articles if a.slug != exclude_slug]
    filtered_sorted = sorted(filtered, key=lambda a: a.date, reverse=True)[:2]

    return filtered_sorted