# PydanticModels.py

from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel

# User Models
class UserBase(BaseModel):
    first_name: str
    last_name: str
    username: str
    email: str
    password: str
    profile_image: Optional[str] = None
    bio: Optional[str] = None

class UserCreate(UserBase):
    pass

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

# Video Models
class VideoBase(BaseModel):
    title: str
    description: str
    upload_date: datetime
    thumbnail_url: str
    video_url: str
    duration: Optional[int]
    categories: str
    privacy_setting: str
    total_likes: int = 0
    total_views: int = 0
    total_subscribers: int = 0

class VideoCreate(VideoBase):
    pass

class Video(VideoBase):
    IDVideo: int
    user_id: int
    user: User
    views: List['View'] = []
    likes: List['LikesDislikes'] = []

    class Config:
        orm_mode = True

# LikesDislikes Models
class LikesDislikesBase(BaseModel):
    user_id: int
    video_id: int
    like_status: int

class LikesDislikesCreate(LikesDislikesBase):
    pass

class LikesDislikes(LikesDislikesBase):
    like_id: int
    user: User
    video: Video

    class Config:
        orm_mode = True

# View Models
class ViewBase(BaseModel):
    user_id: int
    video_id: int
    view_date: datetime

class ViewCreate(ViewBase):
    pass

class View(ViewBase):
    view_id: int
    user: User
    video: Video

    class Config:
        orm_mode = True

# Subscription Models
class SubscriptionBase(BaseModel):
    subscriber: int
    channel: int

class SubscriptionCreate(SubscriptionBase):
    pass

class Subscription(SubscriptionBase):
    subscription_id: int
    subscriber: User
    channel: User

    class Config:
        orm_mode = True
