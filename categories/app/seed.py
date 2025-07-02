from .database import SessionLocal
from . import models, schemas, crud

def init_db():
    db = SessionLocal()
    try:
        if db.query(models.Category).count() == 0:
            default_categories = [
                schemas.CategoryCreate(slug='it', title='IT', image='/images/categories/IT.jpg'),
                schemas.CategoryCreate(slug='fashion', title='Fashion', image='/images/categories/Fashion.jpg'),
                schemas.CategoryCreate(slug='exhibition', title='Exhibition', image='/images/categories/Exhibition.jpg'),
                schemas.CategoryCreate(slug='must-try', title='Must-Try', image='/images/categories/Must-Try.jpg'),
            ]
            for category in default_categories:
                crud.create_category(db, category)
            print("Success")
        else:
            print("Already DB Table")
    finally:
        db.close()