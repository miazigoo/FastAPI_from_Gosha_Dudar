from fastapi import APIRouter
from schemas import Post, PostCreate
from typing import Optional, List, Dict
from fastapi import HTTPException


router = APIRouter()


users = [
    {'id': 1, 'name': "Sven", 'age': 321},
    {'id': 2, 'name': "Bella", 'age': 26},
    {'id': 3, 'name': "Toran", 'age': 217},
    {'id': 4, 'name': "Gardabon", 'age': 1612},
]


posts = [
    {'id': 1, 'title': 'News 1', 'body': 'Text 1', 'author': users[1]},
    {'id': 2, 'title': 'I am strong', 'body': 'Text 2', 'author': users[0]},
    {'id': 3, 'title': 'News 3', 'body': 'Text 3', 'author': users[3]},
    {'id': 4, 'title': 'News 4', 'body': 'Text 4', 'author': users[2]},
    {"id": 5, "title": "Сегодня я стану сильнее или умру...", "body": "Да пройдет битва между нами!", "author": users[1]}
]


@router.post("/items/add")
async def add_item(post: PostCreate) -> Post:
    author = next((user for user in users if user['id'] == post.author_id), None)
    if not author:
        raise HTTPException(status_code=404, detail="User not found")
    new_post_id = len(posts) + 1
    new_post = {
        'id': new_post_id,
        'title': post.title,
        'body': post.body,
        'author': author
    }
    posts.append(new_post)
    return Post(**new_post)


@router.put("/items/edit/{id}")
async def add_item(post: PostCreate) -> Post:
    author = next((user for user in users if user['id'] == post.author_id), None)
    if not author:
        raise HTTPException(status_code=404, detail="User not found")
    new_post_id = len(posts) + 1
    new_post = {
        'id': new_post_id,
        'title': post.title,
        'body': post.body,
        'author': author
    }
    posts.append(new_post)
    return Post(**new_post)


@router.get("/items")
async def get_items() -> List[Post]:
    return [Post(**post) for post in posts]


@router.get("/items/{id}")
async def get_item(id: int) -> Post:
    for post in posts:
        if post['id'] == id:
            return Post(**post)
    raise HTTPException(status_code=404, detail="Post not found")


@router.get("/search")
async def search_item(post_id: Optional[int] = None) -> Dict[str, Optional[Post]]:
    if post_id:
        for post in posts:
            if post['id'] == int(post_id):
                return {
                    'data': Post(**post)
                }
        raise HTTPException(status_code=404, detail="Post not found")
    else:
        return {'data': None}
