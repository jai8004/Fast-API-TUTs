from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import User
from schemas import UserLogin
from utils import verify_password, create_access_token

router = APIRouter(prefix="/auth", tags=["Auth"])

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Login route to generate token
@router.post("/login")
def login(user_cred: UserLogin, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == user_cred.username).first()
    if not user or not verify_password(user_cred.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid Credentials")
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}
