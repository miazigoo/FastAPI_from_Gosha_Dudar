from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    age: int


class Post(BaseModel):
    id: int
    title: Optional[str] = None
    body: Optional[str] = None
    author: User


