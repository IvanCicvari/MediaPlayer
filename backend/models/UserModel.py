
# models.py
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, func
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

BaseModel = declarative_base()


class User(BaseModel):
    """
    User model representing user information.
    """
    __tablename__ = 'Users'

    IDUser = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String)
    last_name = Column(String)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)
    created_at = Column(DateTime, default=func.now())
    last_login = Column(DateTime, nullable=True)
    profile_image = Column(String, nullable=True)
    bio = Column(String, nullable=True)
    is_verified = Column(Boolean, default=False)
    subscription_status = Column(String)

    videos = relationship('Video', back_populates='user',
                          cascade='all, delete-orphan')
    likes = relationship(
        'LikesDislikes', back_populates='user', cascade='all, delete-orphan')
    views = relationship('View', back_populates='user',
                         cascade='all, delete-orphan')
    subscriptions = relationship(
        'Subscription', foreign_keys="[Subscription.subscriber_id]", back_populates='subscriber', cascade='all, delete-orphan')
    subscribers = relationship(
        'Subscription', foreign_keys="[Subscription.channel_id]", back_populates='channel', cascade='all, delete-orphan')

