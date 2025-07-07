from fastapi import FastAPI, Depends, HTTPException, status, Body
from sqlalchemy.orm import Session
from . import crud, models, schemas, seed
from .database import SessionLocal, engine, get_db, Base
from fastapi.middleware.cors import CORSMiddleware
from .schemas import SlugBody



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)
    seed.init_db()

@app.get("/api/categories", response_model=list[schemas.Category])
def read_categories(db: Session = Depends(get_db)):
    return crud.get_categories(db)

@app.get("/api/categories/{slug}", response_model=schemas.Category)
def get_category(slug: str, db: Session = Depends(get_db)):
    db_category = crud.get_category_by_slug(db, slug)
    if not db_category:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category

@app.post("/api/categories", response_model=schemas.Category, status_code=status.HTTP_201_CREATED)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    db_category = crud.create_category(db, category)
    return db_category

@app.patch("/api/categories", response_model=schemas.Category)
def update_category(
    slug: str = Body(...),
    updates: schemas.CategoryUpdate = Body(...),
    db: Session = Depends(get_db)
):
    db_category = crud.update_category(db, slug, updates)
    if not db_category:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category

@app.delete("/api/categories")
def delete_category(body: SlugBody, db: Session = Depends(get_db)):
    ok = crud.delete_category(db, body.slug)
    if not ok:
        raise HTTPException(status_code=404, detail="Category not found")
    return {"success": True}
