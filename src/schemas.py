from pydantic import BaseModel, EmailStr

# Schema for user creation
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

# Schema for user response
class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        orm_mode = True

# Schema for login
class UserLogin(BaseModel):
    username: str
    password: str
