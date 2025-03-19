from contextlib import asynccontextmanager

from fastapi import APIRouter, Path, HTTPException, Query, Body, Depends

from schemas import PostResponse, PostCreate, UserCreate, User as DbUser
from typing import Optional, List, Dict, Annotated

from sqlalchemy.orm import Session
from database import session_local, engine
from models import Base, User, Post


router = APIRouter()

Base.metadata.create_all(bind=engine)


def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()
        print("Выключение DB")


@router.post("/user/add", response_model=DbUser)
async def create_user(
        user: UserCreate, db: Session = Depends(get_db)
) -> DbUser:
    db_user = User(name=user.name, age=user.age)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@router.post("/post/add", response_model=PostResponse)
async def create_post(
        post: PostCreate, db: Session = Depends(get_db)
) -> PostResponse:
    db_user = db.query(User).filter(User.id == post.author_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db_post = Post(title=post.title, body=post.body, author_id=post.author_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


@router.get("/posts", response_model=List[PostResponse])
async def get_posts(db: Session = Depends(get_db)):
    return db.query(Post).all()


