from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, func
from sqlalchemy.orm import relationship

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class View(Base):
    __tablename__ = 'Views'
    view_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('Users.IDUser'))
    video_id = Column(Integer, ForeignKey('Videos.IDVideo'))
    view_date = Column(DateTime)
    user = relationship('User', back_populates='views')
    video = relationship('Video', back_populates='views')