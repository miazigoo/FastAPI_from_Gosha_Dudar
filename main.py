from typing import Optional, List, Dict
from fastapi import FastAPI, HTTPException
from contextlib import asynccontextmanager

from sqlalchemy.testing.suite.test_reflection import users

from router import router as tasks_router
from schemas import Post


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("База готова к работе")
    yield
    print("Выключение")


app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)

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
]




# @app.get("/items")
# async def get_items() -> List[Post]:
#     post_objects = []
#     for post in posts:
#         post_objects.append(
#             Post(
#                 id=post["id"],
#                 title=post['title'],
#                 body=post["body"]
#             )
#         )
#     return post_objects

@app.get("/items")
async def get_items() -> List[Post]:
    return [Post(**post) for post in posts]


@app.get("/items/{id}")
async def get_item(id: int) -> Post:
    for post in posts:
        if post['id'] == id:
            return Post(**post)
    raise HTTPException(status_code=404, detail="Post not found")


@app.get("/search")
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
