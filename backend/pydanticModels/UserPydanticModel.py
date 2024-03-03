# User Models

from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel

from backend.PydanticModels import LikesDislikes, Subscription, Video, View


class UserBase(BaseModel):
    first_name: str
    last_name: str
    username: str
    email: str
    password: str
    profile_image: Optional[str] = None
    bio: Optional[str] = None
    subscription_status: str


class UserCreate(UserBase):
    first_name: str
    last_name: str
    username: str
    email: str
    password: str
    profile_image: str
    bio: str
    subscription_status: str

    class Config:
        orm_mode = True


class UserUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    username: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    profile_image: Optional[str] = None
    bio: Optional[str] = None
    subscription_status: Optional[str] = None

    class Config:
        orm_mode = True


class User(UserBase):
    IDUser: int
    created_at: datetime
    last_login: Optional[datetime]
    is_verified: bool
    subscription_status: str
    videos: List['Video'] = []
    likes: List['LikesDislikes'] = []
    views: List['View'] = []
    subscriptions: List['Subscription'] = []

    class Config:
        orm_mode = True