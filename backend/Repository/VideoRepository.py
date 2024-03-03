from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
import Models
from PydanticModels import VideoBase, VideoCreate, Video

def create_video(db: Session, video: VideoBase, user_id: int):
    try:
        db_video = Models.Video(
            title=video.title,
            description=video.description,
            thumbnail_url=video.thumbnail_url,
            video_url=video.video_url,
            duration=video.duration,
            categories=video.categories,
        )
        db.add(db_video)
        db.commit()
        db.refresh(db_video)
        return Video.from_orm(db_video)
    except SQLAlchemyError as e:
        db.rollback()
        raise e

def get_video(db: Session, video_id: int):
    return db.query(Models.Video).filter(Models.Video.IDVideo == video_id).first()

def get_videos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Models.Video).offset(skip).limit(limit).all()

def update_video(db: Session, video_id: int, video: VideoCreate):
    db_video = db.query(Models.Video).filter(Models.Video.IDVideo == video_id).first()
    for key, value in video.dict(exclude_unset=True).items():
        if value is not None and value != "":
            setattr(db_video, key, value)
    db.commit()
    db.refresh(db_video)
    return db_video

def delete_video(db: Session, video_id: int):
    db.query(Models.Video).filter(Models.Video.IDVideo == video_id).delete()
    db.commit()
