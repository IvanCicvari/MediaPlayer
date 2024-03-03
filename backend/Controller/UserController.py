from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from PydanticModels import *
from Repository.UserRepository import *
from database import SessionLocal

user_router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CRUD operations for Users
@user_router.post("/users/", tags=["Users"])
def create_user_api(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

@user_router.get("/users/{user_id}", tags=["Users"])
def read_user_api(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@user_router.put("/users/{user_id}", tags=["Users"])
def update_user_api(user_id: int, user: UserBase, db: Session = Depends(get_db)):
    db_user = update_user(db, user_id, user)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@user_router.delete("/users/{user_id}", tags=["Users"], response_model=dict)
def delete_user_api(user_id: int, db: Session = Depends(get_db)):
    db_user = delete_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"status": "User deleted successfully"}

