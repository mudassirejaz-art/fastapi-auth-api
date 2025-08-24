# main.py (Production-ready)

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, auth, crud
from .database import engine, SessionLocal
# from sqlalchemy.orm import Session
from . import crud, auth

# Create all tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI Auth Production-ready")


# Auto-create test user if DB empty
def create_test_user():
    db: Session = next(auth.get_db())
    user = crud.get_user_by_key(db, "myclient123")
    if not user:
        crud.create_user(db, client_key="myclient123", secret_key="mysecret456")
        print("✅ Test user created: myclient123 / mysecret456")
    db.close()

# call this once app starts
create_test_user()

@app.get("/")
def root():
    return {"message": "Welcome to FastAPI Auth!"}


@app.post("/login", response_model=schemas.Token)
def login(request: schemas.LoginRequest, db: Session = Depends(auth.get_db)):
    user = auth.authenticate_user(db, request.client_key, request.secret_key)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token_data = {"sub": user.client_key}
    return schemas.Token(
        access_token=auth.create_access_token(token_data),
        refresh_token=auth.create_refresh_token(token_data),
        token_type="bearer",
        user_id=user.id
    )


@app.get("/me", response_model=schemas.UserOut)
def read_me(current_user: models.User = Depends(auth.get_current_user)):
    return schemas.UserOut(
        id=current_user.id,
        client_key=current_user.client_key,
        created_at=current_user.created_at
    )


@app.get("/secure-data")
def secure_data(current_user: models.User = Depends(auth.get_current_user)):
    return {"message": f"Welcome {current_user.client_key}, secure access granted!"}
