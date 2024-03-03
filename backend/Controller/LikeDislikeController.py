from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from PydanticModels import *
from Repository.LikeDislikeRepostiroy import *
from database import SessionLocal

likeDislike_router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        

# CRUD operations for Likes/Dislikes
@likeDislike_router.post("/likes-dislikes/", tags=["Likes/Dislikes"])
def create_like_dislike_api(like_dislike: LikesDislikesCreate, user_id: int, video_id: int, db: Session = Depends(get_db)):
    return create_like_dislike(db, like_dislike, user_id, video_id)

@likeDislike_router.get("/likes-dislikes/{like_id}", tags=["Likes/Dislikes"])
def read_like_dislike_api(like_id: int, db: Session = Depends(get_db)):
    db_like_dislike = get_like_dislike(db, like_id)
    if db_like_dislike is None:
        raise HTTPException(status_code=404, detail="Like/Dislike not found")
    return db_like_dislike

@likeDislike_router.get("/likes-dislikes/", tags=["Likes/Dislikes"])
def read_likes_dislikes_api(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_likes_dislikes(db, skip=skip, limit=limit)

@likeDislike_router.delete("/likes-dislikes/{like_id}", tags=["Likes/Dislikes"])
def delete_like_dislike_api(like_id: int, db: Session = Depends(get_db)):
    db_like_dislike = delete_like_dislike(db, like_id)
    if db_like_dislike is None:
        raise HTTPException(status_code=404, detail="Like/Dislike not found")
    return db_like_dislike
