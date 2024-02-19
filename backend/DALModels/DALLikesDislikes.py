from sqlalchemy import Boolean, Column, DateTime, Integer, String, func,ForeignKey
from sqlalchemy.orm import relationship

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class LikesDislikes(Base):
    __tablename__ = 'LikesDislikes'
    like_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('Users.IDUser'))
    video_id = Column(Integer, ForeignKey('Videos.IDVideo'))
    like_status = Column(Integer)
    user = relationship('User', back_populates='likes_dislikes')
    video = relationship('Video', back_populates='likes_dislikes')