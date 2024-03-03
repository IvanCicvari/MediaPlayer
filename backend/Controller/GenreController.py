from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from PydanticModels import *
from Repository.GenereRepository import *
from database import SessionLocal

genre_router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CRUD operations for Genres
@genre_router.post("/genres/", tags=["Genres"])
def create_genre_api(genre: GenreCreate, db: Session = Depends(get_db)):
    return create_genre(db, genre)

@genre_router.get("/genres/{genre_id}", tags=["Genres"])
def read_genre_api(genre_id: int, db: Session = Depends(get_db)):
    db_genre = get_genre(db, genre_id)
    if db_genre is None:
        raise HTTPException(status_code=404, detail="Genre not found")
    return db_genre

@genre_router.get("/genres/", tags=["Genres"])
def read_genres_api(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_genres(db, skip=skip, limit=limit)

@genre_router.delete("/genres/{genre_id}", tags=["Genres"])
def delete_genre_api(genre_id: int, db: Session = Depends(get_db)):
    db_genre = delete_genre(db, genre_id)
    if db_genre is None:
        raise HTTPException(status_code=404, detail="Genre not found")
    return db_genre

