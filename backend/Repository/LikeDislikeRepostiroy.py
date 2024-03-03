from sqlalchemy.orm import Session
import Models
from PydanticModels import LikesDislikesBase, LikesDislikes

def create_like_dislike(db: Session, like_dislike: LikesDislikesBase, user_id: int, video_id: int):
    db_like_dislike = Models.LikesDislikes(
        **like_dislike.dict(), user_id=user_id, video_id=video_id)
    db.add(db_like_dislike)
    db.commit()
    db.refresh(db_like_dislike)
    return db_like_dislike

def get_like_dislike(db: Session, like_id: int):
    return db.query(Models.LikesDislikes).filter(Models.LikesDislikes.like_id == like_id).first()

def get_likes_dislikes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Models.LikesDislikes).offset(skip).limit(limit).all()

def delete_like_dislike(db: Session, like_id: int):
    db.query(Models.LikesDislikes).filter(Models.LikesDislikes.like_id == like_id).delete()
    db.commit()
