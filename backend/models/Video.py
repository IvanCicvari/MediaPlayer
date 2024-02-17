from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql import func

Base = declarative_base()

class Video(Base):
    __tablename__ = 'videos'
    video_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    title = Column(String)
    description = Column(String)
    upload_date = Column(DateTime)
    thumbnail_url = Column(String)
    video_url = Column(String)
    total_likes = Column(Integer, default=0)
    total_views = Column(Integer, default=0)
    total_subscribers = Column(Integer, default=0)