from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, func
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Subscription(Base):
    __tablename__ = 'Subscriptions'
    subscription_id = Column(Integer, primary_key=True, index=True)
    subscriber_id = Column(Integer, ForeignKey('Users.IDUser'))
    channel_id = Column(Integer, ForeignKey('Users.IDUser'))
    user = relationship('User', foreign_keys=[subscriber_id], back_populates='subscriptions')
    channel = relationship('User', foreign_keys=[channel_id], back_populates='subscribers')