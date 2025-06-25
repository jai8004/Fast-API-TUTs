# -----------------------------------------
# utils.py — Utility Functions for Auth
# -----------------------------------------

from passlib.context import CryptContext          # For password hashing
from datetime import datetime, timedelta          # For setting token expiry
from jose import JWTError, jwt                    # For JWT token encoding/decoding


# -----------------------------------------
# CryptContext for password hashing
# bcrypt is a strong hashing algorithm
# -----------------------------------------
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# -----------------------------------------
# JWT configuration constants
# These will be used to generate access tokens
# -----------------------------------------
SECRET_KEY = "your-secret-key"                    # Should be stored securely (e.g., env variable)
ALGORITHM = "HS256"                               # JWT signing algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = 30                  # Token expires after 30 minutes


# -----------------------------------------
# Function to hash a plain-text password
# Used when creating/storing user passwords securely
# -----------------------------------------
def hash_password(password: str):
    return pwd_context.hash(password)


# -----------------------------------------
# Function to verify password during login
# Compares plain password with hashed password from DB
# -----------------------------------------
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


# -----------------------------------------
# Function to create a JWT access token
# Includes expiry time in the payload
# -----------------------------------------
def create_access_token(data: dict):
    to_encode = data.copy()  # Copy payload data (like username)
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})  # Add expiry to token
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


# -----------------------------------------------
# 📘 Key Concepts Used in This File (For Freshers)
# -----------------------------------------------
# | Concept                      | Explanation                                                              |
# | ---------------------------- | ------------------------------------------------------------------------ |
# | `CryptContext`               | Manages password hashing schemes like bcrypt                             |
# | `bcrypt`                     | A secure hashing algorithm used for storing passwords                    |
# | `hash_password()`            | Hashes a plain password before saving to DB                              |
# | `verify_password()`          | Compares hashed DB password with user-entered password                   |
# | `create_access_token()`      | Generates a JWT token with username + expiry info                        |
# | `SECRET_KEY`                 | Used to sign JWT tokens securely                                         |
# | `HS256`                      | HMAC algorithm used to encode/decode JWTs                                |
# | `datetime.utcnow()`          | Gets current UTC time (used for expiry logic)                            |
