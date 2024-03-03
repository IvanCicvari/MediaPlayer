from sqlalchemy.orm import Session
import Models
from PydanticModels import VideoTagBase, VideoTag

def create_video_tag(db: Session, video_tag: VideoTagBase):
    db_video_tag = Models.VideoTag(**video_tag.dict())
    db.add(db_video_tag)
    db.commit()
    db.refresh(db_video_tag)
    return db_video_tag

def get_video_tag(db: Session, video_id: int, tag_id: int):
    return db.query(Models.VideoTag).filter(Models.VideoTag.video_id == video_id, Models.VideoTag.tag_id == tag_id).first()

def get_video_tags(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Models.VideoTag).offset(skip).limit(limit).all()

def delete_video_tag(db: Session, video_id: int, tag_id: int):
    db.query(Models.VideoTag).filter(Models.VideoTag.video_id == video_id, Models.VideoTag.tag_id == tag_id).delete()
    db.commit()
