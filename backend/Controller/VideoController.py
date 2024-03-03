from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from PydanticModels import *
from Repository.VideoRepository import *
from database import SessionLocal

video_router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CRUD operations for Videos
@video_router.post("/videos/", tags=["Videos"])
def create_video_api(video: VideoCreate, user_id: int, db: Session = Depends(get_db)):
    return create_video(db, video, user_id)

@video_router.get("/videos/{video_id}", tags=["Videos"])
def read_video_api(video_id: int, db: Session = Depends(get_db)):
    db_video = get_video(db, video_id)
    if db_video is None:
        raise HTTPException(status_code=404, detail="Video not found")
    return db_video

@video_router.get("/videos/", tags=["Videos"])
def read_videos_api(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_videos(db, skip=skip, limit=limit)

@video_router.put("/videos/{video_id}", tags=["Videos"])
def update_video_api(video_id: int, video: VideoCreate, db: Session = Depends(get_db)):
    db_video = update_video(db, video_id, video)
    if db_video is None:
        raise HTTPException(status_code=404, detail="Video not found")
    return db_video

@video_router.delete("/videos/{video_id}", tags=["Videos"])
def delete_video_api(video_id: int, db: Session = Depends(get_db)):
    db_video = delete_video(db, video_id)
    if db_video is None:
        raise HTTPException(status_code=404, detail="Video not found")
    return db_video
