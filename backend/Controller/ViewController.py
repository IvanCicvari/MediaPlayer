from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from PydanticModels import *
from Repository.ViewRepository import *
from database import SessionLocal

view_router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# CRUD operations for Views
@view_router.post("/views/", tags=["Views"])
def create_view_api(view: ViewCreate, user_id: int, video_id: int, db: Session = Depends(get_db)):
    return create_view(db, view, user_id, video_id)

@view_router.get("/views/{view_id}", tags=["Views"])
def read_view_api(view_id: int, db: Session = Depends(get_db)):
    db_view = get_view(db, view_id)
    if db_view is None:
        raise HTTPException(status_code=404, detail="View not found")
    return db_view

@view_router.get("/views/", tags=["Views"])
def read_views_api(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_views(db, skip=skip, limit=limit)

@view_router.delete("/views/{view_id}", tags=["Views"])
def delete_view_api(view_id: int, db: Session = Depends(get_db)):
    db_view = delete_view(db, view_id)
    if db_view is None:
        raise HTTPException(status_code=404, detail="View not found")
    return db_view

