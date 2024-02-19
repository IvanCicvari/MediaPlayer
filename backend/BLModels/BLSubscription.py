# bl_models.py
from pydantic import BaseModel
from typing import List, Optional

class SubscriptionBase(BaseModel):
    subscriber_id: int
    channel_id: int

class SubscriptionCreate(SubscriptionBase):
    pass

class Subscription(SubscriptionBase):
    subscription_id: int

    class Config:
        orm_mode = True
