# UsersRoles Models

from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel

class UsersRolesBase(BaseModel):
    user_id: int
    role_id: int

class UsersRolesCreate(UsersRolesBase):
    pass

class UsersRoles(UsersRolesBase):
    class Config:
        orm_mode = True

