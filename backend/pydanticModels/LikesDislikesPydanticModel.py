# LikesDislikes Models

from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel

from backend.PydanticModels import User, Video


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
