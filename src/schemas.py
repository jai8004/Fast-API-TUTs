# -----------------------------------------
# schemas.py — Pydantic Schemas for Request & Response Models
# -----------------------------------------

from pydantic import BaseModel, EmailStr  # EmailStr validates email format


# -----------------------------------------
# Schema for creating a new user (used in POST request body)
# -----------------------------------------
class UserCreate(BaseModel):
    username: str              # Username as plain text
    email: EmailStr            # Validated email string
    password: str              # Plain text password (to be hashed later)


# -----------------------------------------
# Schema for returning user info in API responses
# This omits sensitive data like password
# -----------------------------------------
class UserOut(BaseModel):
    id: int                    # User ID from the database
    username: str              # Username
    email: EmailStr            # Email address

    class Config:
        orm_mode = True        # Allows compatibility with SQLAlchemy ORM objects


# -----------------------------------------
# Schema for login request body
# Only username and password are needed
# -----------------------------------------
class UserLogin(BaseModel):
    username: str              # Username for login
    password: str              # Password for login (plain text)


# -----------------------------------------------
# 📘 Key Concepts Used in This File (For Freshers)
# -----------------------------------------------
# | Concept               | Explanation                                                            |
# | --------------------- | ---------------------------------------------------------------------- |
# | `BaseModel`           | Base class from Pydantic used to define data validation schemas        |
# | `EmailStr`            | Pydantic field type that ensures the string is a valid email format    |
# | `UserCreate`          | Input schema for creating new users                                    |
# | `UserOut`             | Output schema for returning user data without password                 |
# | `orm_mode = True`     | Enables Pydantic to work with SQLAlchemy ORM objects (e.g., models)    |
# | `UserLogin`           | Input schema for login that requires only username and password        |
