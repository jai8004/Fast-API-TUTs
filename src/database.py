# -----------------------------------------
# database.py — SQLAlchemy DB Configuration
# -----------------------------------------

# Import required SQLAlchemy components
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# -----------------------------------------
# Define the database connection URL
# Using SQLite (a file-based DB)
# -----------------------------------------
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

# -----------------------------------------
# Create SQLAlchemy engine
# 'check_same_thread=False' is needed for SQLite when using it with FastAPI
# -----------------------------------------
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# -----------------------------------------
# Create a session factory
# - SessionLocal will be used to create DB sessions in routes
# - autocommit=False: changes are committed manually
# - autoflush=False: avoids automatic flushing of changes to DB
# -----------------------------------------
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# -----------------------------------------
# Create a base class for all models
# All SQLAlchemy models will inherit from this
# -----------------------------------------
Base = declarative_base()


# -----------------------------------------------
# 📘 Key Concepts Used in This File (For Freshers)
# -----------------------------------------------
# | Concept                  | Explanation                                                           |
# | ------------------------ | ---------------------------------------------------------------------- |
# | `create_engine()`        | Establishes connection to the SQLite database                         |
# | `check_same_thread`      | SQLite-specific config for multi-thread access in FastAPI             |
# | `sessionmaker()`         | Factory to create new DB sessions (used via `SessionLocal`)           |
# | `autocommit=False`       | Requires manual commit to save changes                                |
# | `autoflush=False`        | Avoids auto-sending of changes before queries                         |
# | `declarative_base()`     | Base class for declaring DB models (used in models.py)                |
