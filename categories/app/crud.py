from sqlalchemy.orm import Session
from . import models, schemas
from fastapi import HTTPException
PROTECTED_CATEGORY_SLUGS = {'it', 'fashion', 'exhibition', 'must-try'}

def get_categories(db: Session):
    return db.query(models.Category).all()

def get_category_by_slug(db: Session, slug: str):
    return db.query(models.Category).filter(models.Category.slug == slug).first()

def create_category(db: Session, category: schemas.CategoryCreate):
    db_category = models.Category(**category.dict())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def update_category(db: Session, slug: str, updates: schemas.CategoryCreate):
    db_category = get_category_by_slug(db, slug)
    if not db_category:
        return None
    for key, value in updates.dict().items():
        setattr(db_category, key, value)
    db.commit()
    db.refresh(db_category)
    return db_category

def delete_category(db: Session, slug: str):
    db_category = get_category_by_slug(db, slug)
    if not db_category:
        return False
    if slug in PROTECTED_CATEGORY_SLUGS:
        raise HTTPException(status_code=403, detail="Can't Delete Default Category!")
    db.delete(db_category)
    db.commit()
    return True
