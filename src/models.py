# -----------------------------------------
# models.py — SQLAlchemy Models Definition
# -----------------------------------------

from sqlalchemy import Column, Integer, String
from database import Base  # Importing Base from our DB config

# -----------------------------------------
# SQLAlchemy model for the "users" table
# Inherits from Base, which tells SQLAlchemy this is a DB model
# -----------------------------------------
class User(Base):
    __tablename__ = "users"  # Table name in the DB

    # Columns in the table
    id = Column(Integer, primary_key=True, index=True)  # Unique user ID (Primary Key)
    username = Column(String, unique=True, index=True)  # Username must be unique
    email = Column(String, unique=True, index=True)     # Email must be unique
    hashed_password = Column(String)                    # Hashed password (not plain text)


# -----------------------------------------------
# 📘 Key Concepts Used in This File (For Freshers)
# -----------------------------------------------
# | Concept                 | Explanation                                                      |
# | ----------------------- | ---------------------------------------------------------------- |
# | `Base`                  | Base class from SQLAlchemy used to declare models                |
# | `__tablename__`         | Sets the table name in the actual database                       |
# | `Column()`              | Defines a column in the table                                    |
# | `Integer` / `String`    | Specifies data type of the column                                |
# | `primary_key=True`      | Marks the column as the primary key                              |
# | `unique=True`           | Ensures values in the column are unique                          |
# | `index=True`            | Creates an index on the column to speed up search queries        |
