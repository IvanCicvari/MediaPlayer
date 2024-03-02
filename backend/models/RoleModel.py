
# models.py
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, func
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

BaseModel = declarative_base()


class Role(BaseModel):
    """
    Role model representing user roles.
    """
    __tablename__ = 'Roles'

    role_id = Column(Integer, primary_key=True, autoincrement=True)
    role_name = Column(String, unique=True)

