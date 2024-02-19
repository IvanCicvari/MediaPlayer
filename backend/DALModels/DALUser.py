# users.py
from sqlalchemy import Boolean, Column, DateTime, Integer, String, func
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class User(Base):
    __tablename__ = 'Users'
    user_id = Column(Integer, primary_key=True, index=True)
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
