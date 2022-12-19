from typing import Optional
from pydantic import EmailStr

from sqlmodel import SQLModel, Field

class UserBase(SQLModel):
  name: str = Field(title='full name')
  email: EmailStr = Field(title='user email')
  phone: str = Field(max_length=15)

class User(UserBase, table=True):
  id: int = Field(default=None, primary_key=True)
  password: str


class UserCreate(UserBase):
  password: str
  class Config:
    schema_extra = {
      "example": {
        "name": "John Doe",
        "email": "john@mail.com",
        "phone": "0707853729",
        "password": "password"
      }
  }

class UserProfile(UserBase):
  pass


class LoginIn(SQLModel):
  email: str
  password: str

class JwtUser(UserBase):
  access_token: str
  refresh_token: str