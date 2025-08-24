from sqlalchemy.orm import Session
from . import models
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_user_by_key(db: Session, client_key: str):
    return db.query(models.User).filter(models.User.client_key == client_key).first()

def create_user(db: Session, client_key: str, secret_key: str):
    hashed = pwd_context.hash(secret_key)
    user = models.User(client_key=client_key, hashed_secret=hashed)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def verify_secret(plain_secret: str, hashed_secret: str):
    return pwd_context.verify(plain_secret, hashed_secret)
