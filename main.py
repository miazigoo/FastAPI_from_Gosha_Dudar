from typing import Optional
from fastapi import FastAPI, HTTPException
from contextlib import asynccontextmanager
from router import router as tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("База готова к работе")
    yield
    print("Выключение")


app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)

posts = [
    {'id': 1, 'title':'News 1', 'body':'Text 1'},
    {'id': 2, 'title':'News 2', 'body':'Text 2'},
    {'id': 3, 'title':'News 3', 'body':'Text 3'},
    {'id': 4, 'title':'News 4', 'body':'Text 4'},
]

@app.get("/items/{id}")
async def get_items(post_id:int) -> dict:
    for post in posts:
        if post['id'] == post_id:
            return post
    raise HTTPException(status_code=404, detail="Post not found")


@app.get("/search")
async def get_items(post_id: Optional[int] = None) -> dict:
    if post_id:
        for post in posts:
            if post['id'] == int(post_id):
                return post
        raise HTTPException(status_code=404, detail="Post not found")
    else:
        return {'data': 'No post id provided'}
