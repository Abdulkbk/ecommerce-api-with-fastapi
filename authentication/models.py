from typing import Optional

from sqlmodel import SQLModel, Field

class UserBase(SQLModel):
  name: str
  email: str
  password: str
  phone: str

class User(UserBase, table=True):
  id: int = Field(default=None, primary_key=True)


class UserCreate(UserBase):
  pass