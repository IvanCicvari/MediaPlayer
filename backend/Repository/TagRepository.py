from sqlalchemy.orm import Session
import Models
from PydanticModels import TagBase, Tag

def create_tag(db: Session, tag: TagBase):
    db_tag = Models.Tag(**tag.dict())
    db.add(db_tag)
    db.commit()
    db.refresh(db_tag)
    return db_tag

def get_tag(db: Session, tag_id: int):
    return db.query(Models.Tag).filter(Models.Tag.tag_id == tag_id).first()

def get_tags(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Models.Tag).offset(skip).limit(limit).all()

def delete_tag(db: Session, tag_id: int):
    db.query(Models.Tag).filter(Models.Tag.tag_id == tag_id).delete()
    db.commit()
