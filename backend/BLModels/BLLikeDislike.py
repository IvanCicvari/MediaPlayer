# bl_models.py
from pydantic import BaseModel
from typing import List, Optional

class LikeDislikeBase(BaseModel):
    user_id: int
    video_id: int
    like_status: int

class LikeDislikeCreate(LikeDislikeBase):
    pass

class LikeDislike(LikeDislikeBase):
    like_id: int

    class Config:
        orm_mode = True