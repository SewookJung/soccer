from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException

from sqlalchemy.orm.session import Session

from database import get_db
from routers.users.auth import AuthHandler
from routers.users.models import User
from routers.users.schemas import CreateUserRequest, AuthDetails

auth_handler = AuthHandler()

router = APIRouter(
    prefix="/users", tags=["users"], responses={404: {"discription": "Not Found"}}
)


@router.get("/{user_name}", status_code=status.HTTP_200_OK)
async def get_user(user_name: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.name == user_name).first()

    if not user:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Not found user")
    return {"success": True, "user_id": user.id}


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_409_CONFLICT: {
            "description": "Conflict Email",
        }
    },
)
async def create_user(details: CreateUserRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == details.email).first()
    if user:
        raise HTTPException(status.HTTP_409_CONFLICT, detail="Conflict email")

    hashed_password = auth_handler.get_password_hash(details.password)

    new_user = User(name=details.name, email=details.email, password=hashed_password)
    db.add(new_user)
    db.commit()

    return {"success": True, "user_id": new_user.id}


@router.post("/login", status_code=status.HTTP_200_OK)
async def login(details: AuthDetails, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == details.email).first()
    x = auth_handler.verify_password(details.password, user.password)
    print(x)

    if not user:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="User not found")

    return {"token": "token"}
