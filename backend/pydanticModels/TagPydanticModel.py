# Tag Models

from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel

class TagBase(BaseModel):
    tag_name: str

class TagCreate(TagBase):
    pass

class Tag(TagBase):
    tag_id: int

    class Config:
        orm_mode = True
