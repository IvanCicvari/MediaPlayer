from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from PydanticModels import *
from Repository.SubscriptionRepository import *
from database import SessionLocal

subscription_router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




# CRUD operations for Subscriptions
@subscription_router.post("/subscriptions/", tags=["Subscriptions"])
def create_subscription_api(subscription: SubscriptionCreate, subscriber_id: int, channel_id: int, db: Session = Depends(get_db)):
    return create_subscription(db, subscription, subscriber_id, channel_id)

@subscription_router.get("/subscriptions/{subscription_id}", tags=["Subscriptions"])
def read_subscription_api(subscription_id: int, db: Session = Depends(get_db)):
    db_subscription = get_subscription(db, subscription_id)
    if db_subscription is None:
        raise HTTPException(status_code=404, detail="Subscription not found")
    return db_subscription

@subscription_router.get("/subscriptions/", tags=["Subscriptions"])
def read_subscriptions_api(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_subscriptions(db, skip=skip, limit=limit)

@subscription_router.delete("/subscriptions/{subscription_id}", tags=["Subscriptions"])
def delete_subscription_api(subscription_id: int, db: Session = Depends(get_db)):
    db_subscription = delete_subscription(db, subscription_id)
    if db_subscription is None:
        raise HTTPException(status_code=404, detail="Subscription not found")
    return db_subscription

