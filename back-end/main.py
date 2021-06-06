from fastapi import FastAPI, Depends

from routers.users import users

app = FastAPI()

app.include_router(users.router)
