from sqlalchemy.orm import Session
from Models import CommmentsModel  # Assuming your model is defined in Models.py
from PydanticModels import CommentBase

def create_comment(db: Session, comment: CommentBase, user_id: int, video_id: int):
    db_comment = CommmentsModel(**comment.dict(), user_id=user_id, video_id=video_id)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment

def get_comment(db: Session, comment_id: int):
    return db.query(CommmentsModel).filter(CommmentsModel.comment_id == comment_id).first()

def get_comments(db: Session, skip: int = 0, limit: int = 10):
    return db.query(CommmentsModel).offset(skip).limit(limit).all()

def delete_comment(db: Session, comment_id: int):
    db.query(CommmentsModel).filter(CommmentsModel.comment_id == comment_id).delete()
    db.commit()
