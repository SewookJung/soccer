from fastapi import FastAPI, HTTPException, status
from fastapi.params import Depends
from sqlalchemy.orm import Session

from users.database import get_db
from users.schemas import (
    CreateUserRequest,
    UpdateUserRequest,
)
from users.models import User

app = FastAPI()


@app.get("/users/{user_id}", status_code=status.HTTP_200_OK)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User is not found!")
    return user


@app.post("/users", status_code=status.HTTP_201_CREATED)
async def create_user(details: CreateUserRequest, db: Session = Depends(get_db)):
    new_user = User(name=details.name, email=details.email, password=details.password)
    db.add(new_user)
    db.commit()
    return {"success": True, "user_id": new_user.id}


@app.delete("/users/{user_id}")
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    delete_user = db.query(User).filter(User.id == user_id).first()
    db.delete(delete_user)
    db.commit()
    return {"success": True}


@app.patch("/users/{user_id}")
async def update_user(details: UpdateUserRequest, db: Session = Depends(get_db)):
    update_user = db.query(User).filter(User.id == details.id).first()
    data = details.dict(exclude_unset=True)
    for key, value in data.items():
        setattr(update_user, key, value)
    db.commit()
    return {"success": True}
