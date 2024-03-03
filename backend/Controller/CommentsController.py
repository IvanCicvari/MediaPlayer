from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from PydanticModels import *
from Repository.CommentsRepository import *
from database import SessionLocal

comments_router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
# CRUD operations for Comments
@comments_router.post("/comments/", tags=["Comments"])
def create_comment_api(comment: CommentCreate, user_id: int, video_id: int, db: Session = Depends(get_db)):
    return create_comment(db, comment, user_id, video_id)

@comments_router.get("/comments/{comment_id}", tags=["Comments"])
def read_comment_api(comment_id: int, db: Session = Depends(get_db)):
    db_comment = get_comment(db, comment_id)
    if db_comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    return db_comment

@comments_router.get("/comments/", tags=["Comments"])
def read_comments_api(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_comments(db, skip=skip, limit=limit)

@comments_router.delete("/comments/{comment_id}", tags=["Comments"])
def delete_comment_api(comment_id: int, db: Session = Depends(get_db)):
    db_comment = delete_comment(db, comment_id)
    if db_comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    return db_comment


