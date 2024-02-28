
#models.py
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, func
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

BaseModel = declarative_base()

class User(BaseModel):
    """
    User model representing user information.
    """
    __tablename__ = 'Users'

    IDUser = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)
    created_at = Column(DateTime, default=func.now())
    last_login = Column(DateTime, nullable=True)
    profile_image = Column(String)
    bio = Column(String)
    is_verified = Column(Boolean, default=False)
    subscription_status = Column(String)

    videos = relationship('Video', back_populates='user', cascade='all, delete-orphan')
    likes = relationship('LikesDislikes', back_populates='user', cascade='all, delete-orphan')
    views = relationship('View', back_populates='user', cascade='all, delete-orphan')
    subscriptions = relationship('Subscription', back_populates='subscriber', cascade='all, delete-orphan')
    subscribers = relationship('Subscription', back_populates='channel', cascade='all, delete-orphan')

class Video(BaseModel):
    """
    Video model representing video information.
    """
    __tablename__ = 'Videos'

    IDVideo = Column(Integer, primary_key=True)
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
    likes = relationship('LikesDislikes', back_populates='video', cascade='all, delete-orphan')
    views = relationship('View', back_populates='video', cascade='all, delete-orphan')

class LikesDislikes(BaseModel):
    """
    LikesDislikes model representing user likes/dislikes for videos.
    """
    __tablename__ = 'LikesDislikes'

    like_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('Users.IDUser'))
    video_id = Column(Integer, ForeignKey('Videos.IDVideo'))
    like_status = Column(Integer)

    user = relationship('User', back_populates='likes')
    video = relationship('Video', back_populates='likes')

class View(BaseModel):
    """
    View model representing user views on videos.
    """
    __tablename__ = 'Views'

    view_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('Users.IDUser'))
    video_id = Column(Integer, ForeignKey('Videos.IDVideo'))
    view_date = Column(DateTime)

    user = relationship('User', back_populates='views')
    video = relationship('Video', back_populates='views')

class Subscription(BaseModel):
    """
    Subscription model representing user subscriptions to channels.
    """
    __tablename__ = 'Subscriptions'

    subscription_id = Column(Integer, primary_key=True)
    subscriber_id = Column(Integer, ForeignKey('Users.IDUser'))
    channel_id = Column(Integer, ForeignKey('Users.IDUser'))

    subscriber = relationship('User', foreign_keys=[subscriber_id], back_populates='subscriptions')
    channel = relationship('User', foreign_keys=[channel_id], back_populates='subscribers')
