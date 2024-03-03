# Subscription Models

from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel

from backend.PydanticModels import User


class SubscriptionBase(BaseModel):
    subscriber: int
    channel: int


class SubscriptionCreate(SubscriptionBase):
    pass


class Subscription(SubscriptionBase):
    subscription_id: int
    subscriber: User
    channel: User

    class Config:
        orm_mode = True
from typing import List
from datetime import datetime
from pydantic import BaseModel