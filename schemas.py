from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    age: int


class Post(BaseModel):
    id: int
    title: str
    body: Optional[str] = None
    author: User


class PostCreate(BaseModel):
    title: str
    body: Optional[str] = None
    author_id: int


