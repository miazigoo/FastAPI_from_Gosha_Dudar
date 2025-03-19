from fastapi import FastAPI
from contextlib import asynccontextmanager

from router import router as tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("База готова к работе")
    yield
    print("Выключение")


app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)


