from typing import Optional, Annotated

from pydantic import BaseModel, Field


class UserBase(BaseModel):
    name: str
    age: int

    # name: Annotated[
    #     str, Field(
    #         ..., title="Имя пользователя",
    #         min_length=2,
    #         max_length=40
    #     )
    # ]
    # age: Annotated[
    #     int, Field(
    #         ..., title="Возраст пользователя",
    #         ge=1, le=120
    #     )
    # ]


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class PostBase(BaseModel):
    title: str
    body: Optional[str] = None
    author_id: int


class PostResponse(PostBase):
    id: int
    author: User

    class Config:
        orm_mode = True


class PostCreate(PostBase):
    pass



