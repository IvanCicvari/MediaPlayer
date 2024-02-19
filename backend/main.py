from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from sqlalchemy.orm import Session
from typing import Annotated
from database.database import engine, SessionLocal
import BLModels.BLUser

app = FastAPI()

BLModels.BLUser.Base.metadata.create_all(bind=engine)

class UserBase(BaseModel):
    username: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.post("/users/", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserBase, db: db_dependency):
    db_user = BLModels.BLUser.User(**user.dict())
    db.add(db_user)
    db.commit()
    return {"message": "User created successfully"}