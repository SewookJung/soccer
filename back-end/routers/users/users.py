from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException

from sqlalchemy.orm.session import Session

from database import get_db


from routers.users.auth import AuthHandler
from routers.users.models import User
from routers.users.schemas import CreateUserRequest, AuthDetails

from globals.responses import custom_exception


auth_handler = AuthHandler()


router = APIRouter(
    prefix="/users", tags=["users"], responses={404: {"discription": "Not Found"}}
)


@router.get("/{nickname}", status_code=status.HTTP_200_OK)
async def get_user(nickname: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.nickname == nickname).first()

    if not user:

        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail="Not found user",
        )

    return {"success": True, "user_id": user.id}


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_409_CONFLICT: {
            "description": "Conflict",
        }
    },
)
async def create_user(details: CreateUserRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == details.email).first()
    if user:
        HTTPException()
        raise HTTPException(status.HTTP_409_CONFLICT, detail="Conflict email")

    user = db.query(User).filter(User.nickname == details.nickname).first()
    if user:
        raise HTTPException(status.HTTP_409_CONFLICT, detail="Conflict nickname")

    hashed_password = auth_handler.get_password_hash(details.password)

    new_user = User(
        name=details.name,
        email=details.email,
        password=hashed_password,
        nickname=details.nickname,
    )
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
