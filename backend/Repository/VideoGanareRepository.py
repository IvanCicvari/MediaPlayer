from sqlalchemy.orm import Session
import Models
from PydanticModels import VideoGenreBase, VideoGenre

def create_video_genre(db: Session, video_genre: VideoGenreBase):
    db_video_genre = Models.VideoGenre(**video_genre.dict())
    db.add(db_video_genre)
    db.commit()
    db.refresh(db_video_genre)
    return db_video_genre

def get_video_genre(db: Session, video_id: int, genre_id: int):
    return db.query(Models.VideoGenre).filter(Models.VideoGenre.video_id == video_id, Models.VideoGenre.genre_id == genre_id).first()

def get_video_genres(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Models.VideoGenre).offset(skip).limit(limit).all()

def delete_video_genre(db: Session, video_id: int, genre_id: int):
    db.query(Models.VideoGenre).filter(Models.VideoGenre.video_id == video_id, Models.VideoGenre.genre_id == genre_id).delete()
    db.commit()
