
# models.py
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, func
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

BaseModel = declarative_base()

class VideoGenre(BaseModel):
    """
    VideoGenre model representing the relationship between videos and genres.
    """
    __tablename__ = 'VideoGenres'

    video_id = Column(Integer, ForeignKey('Videos.IDVideo'), primary_key=True)
    genre_id = Column(Integer, ForeignKey('Genres.genre_id'), primary_key=True)

    video = relationship('Video', back_populates='genres')
    genre = relationship('Genre', back_populates='videos')


