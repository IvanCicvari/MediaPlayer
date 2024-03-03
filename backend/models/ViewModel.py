
# models.py
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, func
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

BaseModel = declarative_base()

class View(BaseModel):
    """
    View model representing user views on videos.
    """
    __tablename__ = 'Views'

    view_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('Users.IDUser'))
    video_id = Column(Integer, ForeignKey('Videos.IDVideo'))
    view_date = Column(DateTime)

    user = relationship('User', back_populates='views')
    video = relationship('Video', back_populates='views')


