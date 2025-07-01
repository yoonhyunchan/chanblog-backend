from sqlalchemy.orm import Session
from . import models, schemas
from typing import List, Optional

def get_articles(db: Session, skip: int = 0, limit: int = 10) -> List[models.Article]:
    return db.query(models.Article).offset(skip).limit(limit).all()

def get_articles_by_category_id(db: Session, category_id: int) -> List[models.Article]:
    return db.query(models.Article).filter(models.Article.category_id == category_id).all()

def get_article_by_slug(db: Session, slug: int) -> List[models.Article]:
    return db.query(models.Article).filter(models.Article.slug == slug).first()


def create_article(db: Session, article: schemas.ArticleCreate) -> models.Article:
    db_article = models.Article(**article.dict())
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article

def update_article(db: Session, slug: str, article: schemas.ArticleUpdate) -> Optional[models.Article]:
    db_article = db.query(models.Article).filter(models.Article.slug == slug).first()
    if db_article is None:
        return None
    for key, value in article.dict(exclude_unset=True).items():
        setattr(db_article, key, value)
    db.commit()
    db.refresh(db_article)
    return db_article

def delete_article(db: Session, slug: str) -> bool:
    db_article = db.query(models.Article).filter(models.Article.slug == slug).first()
    if db_article is None:
        return False
    db.delete(db_article)
    db.commit()
    return True

