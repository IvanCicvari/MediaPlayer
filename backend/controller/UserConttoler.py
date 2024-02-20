from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from backend.DALModels import DALUser
from backend.BLModels import BLUser
from backend.repository.UserRepository import UserRepository
from backend.database import SessionLocal, engine

app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Dependency to get the UserRepository instance
def get_user_repository(db: Session = Depends(get_db)):
    return UserRepository(db)

# OAuth2PasswordBearer for authentication (you can replace this with your own authentication mechanism)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Example route for creating a user
@app.post("/users/", response_model=BLUser)
async def create_user(
    user: BLUser,
    user_repo: UserRepository = Depends(get_user_repository)
):
    return user_repo.create_user(user)

# Example route for getting a user by user_id
@app.get("/users/{user_id}", response_model=BLUser)
async def read_user(user_id: int, user_repo: UserRepository = Depends(get_user_repository)):
    user = user_repo.get_user_by_id(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Example route for getting all users
@app.get("/users/", response_model=BLUser)
async def read_all_users(user_repo: UserRepository = Depends(get_user_repository)):
    return user_repo.get_all_users()

# Example route for deleting a user by user_id or username
@app.delete("/users/{identifier}", response_model=bool)
async def delete_user(identifier: str, by_username: bool = True, user_repo: UserRepository = Depends(get_user_repository)):
    return user_repo.delete_user(identifier, by_username)
