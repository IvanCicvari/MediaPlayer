from pydantic import BaseModel, List, Optional
from datetime import datetime
from backend.BLModels import BLUser, BLView

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
    user: BLUser
    views: List[BLView] 

    class Config:
        orm_mode = True
