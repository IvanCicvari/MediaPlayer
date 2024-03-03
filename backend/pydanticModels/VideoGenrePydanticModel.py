# VideoGenre Models

from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel

class VideoGenreBase(BaseModel):
    video_id: int
    genre_id: int

class VideoGenreCreate(VideoGenreBase):
    pass

class VideoGenre(VideoGenreBase):
    class Config:
        orm_mode = True