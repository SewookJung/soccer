from fastapi import FastAPI
from fastapi.params import Depends
from sqlalchemy.orm import Session

from users.database import get_db
from users.schemas import (
    CreateUserRequest,
    GetUserRequest,
    UpdateUserRequest,
    DeleteUserRequest,
)
from users.models import User

app = FastAPI()


@app.get("/users/{user_id}")
async def get_user(details: GetUserRequest, db: Session = Depends(get_db)):
    get_user = db.query(User).filter(User.id == details.id).first()
    return get_user


@app.post("/users")
async def create_user(details: CreateUserRequest, db: Session = Depends(get_db)):
    new_user = User(name=details.name, email=details.email, password=details.password)
    db.add(new_user)
    db.commit()
    return {"success": True, "user_id": new_user.id}


@app.delete("/users/{user_id}")
async def delete_user(details: DeleteUserRequest, db: Session = Depends(get_db)):
    delete_user = db.query(User).filter(User.id == details.id).first()
    db.delete(delete_user)
    db.commit()
    return {"success": True}


@app.patch("/users/{user_id}")
async def update_user(details: UpdateUserRequest, db: Session = Depends(get_db)):
    get_user = db.query(User).filter(User.id == details.id).first()

    get_user.name = details.name
    get_user.email = details.email
    get_user.password = details.password
    get_user
