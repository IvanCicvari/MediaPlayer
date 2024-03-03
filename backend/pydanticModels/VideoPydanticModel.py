# Video Models

from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel
from UserPydanticModel import User
from backend.PydanticModels import LikesDislikes, View


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
    title: str
    description: str
    thumbnail_url: str
    video_url: str
    duration: Optional[int]
    categories: str
    class Config:
        orm_mode = True


class Video(VideoBase):
    IDVideo: int
    user_id: int
    user: User
    views: List['View'] = []
    likes: List['LikesDislikes'] = []

    class Config:
        orm_mode = True
