# Import required modules from FastAPI
from fastapi import APIRouter, Depends, HTTPException

# Import Session class for database connection
from sqlalchemy.orm import Session

# Import the database session creator
from database import SessionLocal

# Import the User model (i.e., the users table from the database)
from models import User

# Import the schema to validate login request data
from schemas import UserLogin

# Import helper functions for password verification and JWT token generation
from utils import verify_password, create_access_token

# Create a router for authentication-related routes
# prefix="/auth" means all routes here will start with /auth
# tags=["Auth"] helps organize the Swagger documentation
router = APIRouter(prefix="/auth", tags=["Auth"])

# -----------------------------
# Dependency to get a DB session
# -----------------------------
# This function will be called automatically by FastAPI to provide a database session
# It ensures that a session is created and properly closed after use
def get_db():
    db = SessionLocal()  # Create a new DB session
    try:
        yield db         # Provide the DB session to the calling function
    finally:
        db.close()       # Close the session after the request is completed

# -----------------------------
# Route: POST /auth/login
# -----------------------------
# This endpoint is used to log in a user and return a JWT token
# It expects a username and password in the request body
@router.post("/login")
def login(user_cred: UserLogin, db: Session = Depends(get_db)):
    """
    Login endpoint to authenticate the user and return an access token.

    Parameters:
    - user_cred: UserLogin - Pydantic model with username and password fields
    - db: Session - Database session injected by FastAPI using Depends

    Returns:
    - JSON containing access token and token type
    """
    
    # Step 1: Search for the user in the database by username
    user = db.query(User).filter(User.username == user_cred.username).first()

    # Step 2: If user is not found or password is incorrect, raise an error
    if not user or not verify_password(user_cred.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid Credentials")

    # Step 3: Create a JWT token with the username embedded in it
    access_token = create_access_token(data={"sub": user.username})

    # Step 4: Return the token as a response
    return {
        "access_token": access_token,
        "token_type": "bearer"  # Indicates the token type for Authorization header
    }
