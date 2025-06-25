# -----------------------------------------
# main.py — Entry Point of the FastAPI App
# -----------------------------------------

# Import FastAPI core app
from fastapi import FastAPI

# Import routers (user and auth routes)
from routers import users, auth

# Import database base class and engine
from database import Base, engine

# Import models (this ensures SQLAlchemy sees model classes)
import models


# -----------------------------------------
# Create database tables
# This will create tables defined in models.py
# Only needs to run once during app startup
# -----------------------------------------
Base.metadata.create_all(bind=engine)


# -----------------------------------------
# Initialize the FastAPI app instance
# -----------------------------------------
app = FastAPI()


# -----------------------------------------
# Include route modules (modular routing)
# -----------------------------------------
app.include_router(auth.router)   # /auth endpoints (login, etc.)
app.include_router(users.router)  # /users endpoints (CRUD operations)


# -----------------------------------------------
# 📘 Key Concepts Used in This File (For Freshers)
# -----------------------------------------------
# | Concept                      | Explanation                                                        |
# | ---------------------------- | ------------------------------------------------------------------ |
# | `FastAPI()`                  | Creates an instance of the FastAPI app                             |
# | `Base.metadata.create_all()` | Auto-creates tables based on SQLAlchemy models                     |
# | `engine`                     | Database engine used to bind and connect to the DB                 |
# | `app.include_router()`       | Adds external route modules to keep project modular and clean      |
# | `routers.users` / `auth`     | Modules that handle user-related and authentication-related routes |
