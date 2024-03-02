
# models.py
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, func
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

BaseModel = declarative_base()


class Subscription(BaseModel):
    """
    Subscription model representing user subscriptions to channels.
    """
    __tablename__ = 'Subscriptions'

    subscription_id = Column(Integer, primary_key=True, autoincrement=True)
    subscriber_id = Column(Integer, ForeignKey('Users.IDUser'))
    channel_id = Column(Integer, ForeignKey('Users.IDUser'))

    subscriber = relationship('User', foreign_keys=[
                              subscriber_id], back_populates='subscriptions')
    channel = relationship('User', foreign_keys=[
                           channel_id], back_populates='subscribers')

