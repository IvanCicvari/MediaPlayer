
# models.py
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, func
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

BaseModel = declarative_base()

class UsersRoles(BaseModel):
    """
    UsersRoles model representing the relationship between users and roles.
    """
    __tablename__ = 'UsersRoles'

    user_id = Column(Integer, ForeignKey('Users.IDUser'), primary_key=True)
    role_id = Column(Integer, ForeignKey('Roles.role_id'), primary_key=True)

    user = relationship('User', back_populates='roles')
    role = relationship('Role', back_populates='users')
