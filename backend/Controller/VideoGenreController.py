from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from PydanticModels import *
from Repository.VideoGanareRepository import *
from database import SessionLocal

videoGenre_router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# CRUD operations for VideoGenres
@videoGenre_router.post("/video-genres/", tags=["VideoGenres"])
def create_video_genre_api(video_genre: VideoGenreCreate, db: Session = Depends(get_db)):
    return create_video_genre(db, video_genre)

@videoGenre_router.get("/video-genres/{video_genre_id}", tags=["VideoGenres"])
def read_video_genre_api(video_genre_id: int, db: Session = Depends(get_db)):
    db_video_genre = get_video_genre(db, video_genre_id)
    if db_video_genre is None:
        raise HTTPException(status_code=404, detail="VideoGenre not found")
    return db_video_genre

@videoGenre_router.get("/video-genres/", tags=["VideoGenres"])
def read_video_genres_api(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_video_genres(db, skip=skip, limit=limit)

@videoGenre_router.delete("/video-genres/{video_genre_id}", tags=["VideoGenres"])
def delete_video_genre_api(video_genre_id: int, db: Session = Depends(get_db)):
    db_video_genre = delete_video_genre(db, video_genre_id)
    if db_video_genre is None:
        raise HTTPException(status_code=404, detail="VideoGenre not found")
    return db_video_genre

