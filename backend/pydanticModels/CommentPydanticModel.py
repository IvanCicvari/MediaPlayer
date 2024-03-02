
from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel

from backend.PydanticModels import User, Video


# Comment Models
class CommentBase(BaseModel):
    user_id: int
    video_id: int
    comment_text: str

class CommentCreate(CommentBase):
    pass

class Comment(CommentBase):
    comment_id: int
    comment_date: datetime
    user: 'User'
    video: 'Video'

    class Config:
        orm_mode = True

