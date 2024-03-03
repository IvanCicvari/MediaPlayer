from sqlalchemy.orm import Session
import Models
from PydanticModels import ViewBase, View

def create_view(db: Session, view: ViewBase, user_id: int, video_id: int):
    db_view = Models.View(**view.dict(), user_id=user_id, video_id=video_id)
    db.add(db_view)
    db.commit()
    db.refresh(db_view)
    return db_view

def get_view(db: Session, view_id: int):
    return db.query(Models.View).filter(Models.View.view_id == view_id).first()

def get_views(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Models.View).offset(skip).limit(limit).all()

def delete_view(db: Session, view_id: int):
    db.query(Models.View).filter(Models.View.view_id == view_id).delete()
    db.commit()
