from pydantic import Field, EmailStr, BaseModel
from typing import List


class NoteCreate(BaseModel):
  user_id: int = Field(...)
  category: str = Field(...)
  content: str = Field(...)


class NoteData(NoteCreate):
  id: int



class UserCreate(BaseModel):
  name: str = Field(..., min_length=5, max_length=20)
  age: int = Field(default=None)


class UserData(UserCreate):
  id: int
  notes: List[NoteData]


class UserOnly(UserCreate):
    id: int
