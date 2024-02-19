from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from backend.BLModels import BLUser,BLVideo
class ViewBase(BaseModel):
    user_id: int
    video_id: int
    view_date: datetime

class ViewCreate(ViewBase):
    pass

class View(ViewBase):
    view_id: int
    user: BLUser
    video: BLVideo

    class Config:
        orm_mode = True
