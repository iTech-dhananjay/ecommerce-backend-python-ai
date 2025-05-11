from pydantic import BaseModel, EmailStr, constr
from typing import Optional

class UserBase(BaseModel):
    email: EmailStr
    full_name: str
    phone_number: Optional[constr(min_length=10, max_length=15)] = None

class UserCreate(UserBase):
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserOut(UserBase):
    id: int
    is_active: bool
    is_verified: bool
    user_role: str
    class Config:
        orm_mode = True

class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    phone_number: Optional[str] = None
    is_verified: Optional[bool] = None
    user_role: Optional[str] = None
    is_active: Optional[bool] = None