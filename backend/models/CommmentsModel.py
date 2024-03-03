
# models.py
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, func
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

BaseModel = declarative_base()

class Comment(BaseModel):
    """
    Comment model representing user comments on videos.
    """
    __tablename__ = 'Comments'

    comment_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('Users.IDUser'))
    video_id = Column(Integer, ForeignKey('Videos.IDVideo'))
    comment_text = Column(String)
    comment_date = Column(DateTime, default=func.now())

    user = relationship('User', back_populates='comments')
    video = relationship('Video', back_populates='comments')
