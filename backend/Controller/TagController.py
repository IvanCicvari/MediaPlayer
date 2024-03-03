from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from PydanticModels import *
from Repository.TagRepository import *
from database import SessionLocal

tag_router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CRUD operations for Tags
@tag_router.post("/tags/", tags=["Tags"])
def create_tag_api(tag: TagCreate, db: Session = Depends(get_db)):
    return create_tag(db, tag)

@tag_router.get("/tags/{tag_id}", tags=["Tags"])
def read_tag_api(tag_id: int, db: Session = Depends(get_db)):
    db_tag = get_tag(db, tag_id)
    if db_tag is None:
        raise HTTPException(status_code=404, detail="Tag not found")
    return db_tag

@tag_router.get("/tags/", tags=["Tags"])
def read_tags_api(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_tags(db, skip=skip, limit=limit)

@tag_router.delete("/tags/{tag_id}", tags=["Tags"])
def delete_tag_api(tag_id: int, db: Session = Depends(get_db)):
    db_tag = delete_tag(db, tag_id)
    if db_tag is None:
        raise HTTPException(status_code=404, detail="Tag not found")
    return db_tag
