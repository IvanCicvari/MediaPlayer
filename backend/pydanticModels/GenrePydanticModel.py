
from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel

# Genre Models
class GenreBase(BaseModel):
    genre_name: str

class GenreCreate(GenreBase):
    pass

class Genre(GenreBase):
    genre_id: int

    class Config:
        orm_mode = True