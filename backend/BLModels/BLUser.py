from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class UserBase(BaseModel):
    first_name: str
    last_name: str
    username: str
    email: str
    password: str
    profile_image: Optional[str]
    bio: Optional[str]

class UserCreate(UserBase):
    pass

class User(UserBase):
    user_id: int
    created_at: datetime
    last_login: Optional[datetime]
    is_verified: bool
    subscription_status: str

    class Config:
        orm_mode = True