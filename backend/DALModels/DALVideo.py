from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, NVARCHAR, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Video(Base):
    __tablename__ = 'Videos'
    IDVideo = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('Users.IDUser'))
    title = Column(NVARCHAR(255))
    description = Column(NVARCHAR(255))
    upload_date = Column(DateTime)
    thumbnail_url = Column(NVARCHAR(255))
    video_url = Column(NVARCHAR(255))
    duration = Column(Integer, nullable=True)
    categories = Column(NVARCHAR(255))
    privacy_setting = Column(NVARCHAR(255))
    total_likes = Column(Integer, default=0)
    total_views = Column(Integer, default=0)
    total_subscribers = Column(Integer, default=0)
    user = relationship('User', back_populates='videos')
