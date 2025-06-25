from fastapi import FastAPI
from routers import users, auth
from database import Base, engine
import models

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include routers
app.include_router(auth.router)
app.include_router(users.router)
