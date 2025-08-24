# auth.py (Production-ready)

import os
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from dotenv import load_dotenv
from .models import User
from .database import SessionLocal
from .crud import get_user_by_key, verify_secret

# Load environment variables
load_dotenv()

JWT_SECRET = os.getenv("JWT_SECRET", "supersecurejwtsecret")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
JWT_EXPIRY_MINUTES = int(os.getenv("JWT_EXPIRY_MINUTES", 15))
JWT_REFRESH_DAYS = int(os.getenv("JWT_REFRESH_DAYS", 7))

bearer_scheme = HTTPBearer()

# Database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Authenticate user using hashed_secret
def authenticate_user(db: Session, client_key: str, secret_key: str):
    user = get_user_by_key(db, client_key)
    if user and verify_secret(secret_key, user.hashed_secret):
        return user
    return None


# Create JWT access token
def create_access_token(data: dict):
    to_encode = data.copy()
    if "sub" not in to_encode:
        raise ValueError("Access token requires 'sub'")
    expire = datetime.utcnow() + timedelta(minutes=JWT_EXPIRY_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, JWT_SECRET, algorithm=JWT_ALGORITHM)


# Create JWT refresh token
def create_refresh_token(data: dict):
    to_encode = data.copy()
    if "sub" not in to_encode:
        raise ValueError("Refresh token requires 'sub'")
    expire = datetime.utcnow() + timedelta(days=JWT_REFRESH_DAYS)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, JWT_SECRET, algorithm=JWT_ALGORITHM)


# Get current user from Bearer token
def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
    db: Session = Depends(get_db)
):
    token = credentials.credentials
    credentials_exception = HTTPException(status_code=401, detail="Not authenticated")
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        client_key = payload.get("sub")
        if client_key is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = db.query(User).filter(User.client_key == client_key).first()
    if user is None:
        raise credentials_exception
    return user
