# from database import engine, new_session
# from schemas import UserCreate
#
#
# class UserCreateRepository:
#     @classmethod
#     async def add_one(cls, data: UserCreate):
#         async with new_session() as session:
#             task_dict = data.model_dump()
#             task = TaskOrm(**task_dict)
#             session.add(task)
#             await session.flush()
#             await session.commit()
#             return task.id