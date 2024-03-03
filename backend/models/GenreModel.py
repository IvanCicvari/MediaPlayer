

# models.py
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, func
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

BaseModel = declarative_base()

class Genre(BaseModel):
    """
    Genre model representing genres associated with videos.
    """
    __tablename__ = 'Genres'

    genre_id = Column(Integer, primary_key=True, autoincrement=True)
    genre_name = Column(String, unique=True)
