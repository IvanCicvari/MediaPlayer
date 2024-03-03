# View Models

from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel
from UserPydanticModel import User
from VideoPydanticModel import Video

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
