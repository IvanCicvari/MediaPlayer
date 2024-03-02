
# models.py
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, func
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

BaseModel = declarative_base()


class LikesDislikes(BaseModel):
    """
    LikesDislikes model representing user likes/dislikes for videos.
    """
    __tablename__ = 'LikesDislikes'

    like_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('Users.IDUser'))
    video_id = Column(Integer, ForeignKey('Videos.IDVideo'))
    like_status = Column(Integer)

    user = relationship('User', back_populates='likes')
    video = relationship('Video', back_populates='likes')


