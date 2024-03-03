# VideoTag Models

from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel

class VideoTagBase(BaseModel):
    video_id: int
    tag_id: int

class VideoTagCreate(VideoTagBase):
    pass

class VideoTag(VideoTagBase):
    class Config:
        orm_mode = True