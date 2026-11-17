from datetime import datetime
from sqlalchemy.orm import Session
from typing import List
from fastapi import FastAPI, status, Depends
from. import models, schemas
from.database import engine, SessionLocal, Base

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

@app.post("/api/entries", response_model=schemas.EntriesResponse, status_code=status.HTTP_201_CREATED)
def add_entry(entry: schemas.CreateEntry, db: Session = Depends(get_db)):
    created_at = datetime.now().strftime("%d/%m/%Y %H:%M")

    db_item = models.Item(content=entry.content, created_at=created_at)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.get("/api/entries", response_model=List[schemas.EntriesResponse])
def get_entries(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = db.query(models.Item).offset(skip).limit(limit).all()
    return items
