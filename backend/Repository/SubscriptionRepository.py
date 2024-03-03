from sqlalchemy.orm import Session
import Models
from PydanticModels import SubscriptionBase, Subscription

def create_subscription(db: Session, subscription: SubscriptionBase, subscriber_id: int, channel_id: int):
    db_subscription = Models.Subscription(
        **subscription.dict(), subscriber_id=subscriber_id, channel_id=channel_id)
    db.add(db_subscription)
    db.commit()
    db.refresh(db_subscription)
    return db_subscription

def get_subscription(db: Session, subscription_id: int):
    return db.query(Models.Subscription).filter(Models.Subscription.subscription_id == subscription_id).first()

def get_subscriptions(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Models.Subscription).offset(skip).limit(limit).all()

def delete_subscription(db: Session, subscription_id: int):
    db.query(Models.Subscription).filter(
        Models.Subscription.subscription_id == subscription_id).delete()
    db.commit()
