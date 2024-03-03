
# models.py
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, func
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

BaseModel = declarative_base()


class Video(BaseModel):
    """
    Video model representing video information.
    """
    __tablename__ = 'Videos'

    IDVideo = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('Users.IDUser'))
    title = Column(String)
    description = Column(String)
    upload_date = Column(DateTime)
    thumbnail_url = Column(String)
    video_url = Column(String)
    duration = Column(Integer, nullable=True)
    categories = Column(String)
    privacy_setting = Column(String)
    total_likes = Column(Integer, default=0)
    total_views = Column(Integer, default=0)
    total_subscribers = Column(Integer, default=0)

    user = relationship('User', back_populates='videos')
    likes = relationship(
        'LikesDislikes', back_populates='video', cascade='all, delete-orphan')
    views = relationship('View', back_populates='video',
                         cascade='all, delete-orphan')
