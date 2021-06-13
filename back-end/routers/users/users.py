from http.client import responses
from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException

from sqlalchemy.orm.session import Session
from sqlalchemy.orm import defer

from database import get_db
from globals.functions.response import reponses as res

from routers.users.auth import AuthHandler
from routers.users.models import User
from routers.users.schemas import CreateUserRequest, AuthDetails


auth_handler = AuthHandler()


router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.get(
    "/{nickname}",
    summary="Get user by nickname",
    responses={
        status.HTTP_404_NOT_FOUND: {"description": "User not found"},
        status.HTTP_200_OK: {
            "content": {
                "application/json": {
                    "example": {
                        "success": True,
                        "data": {
                            "name": "string",
                            "email": "string",
                            "nickname": "string",
                            "is_active": True,
                            "id": 0,
                        },
                    }
                }
            },
        },
    },
)
async def get_user(nickname: str, db: Session = Depends(get_db)):
    user = (
        db.query(User)
        .options(defer("password"))
        .filter(User.nickname == nickname)
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=res(success=False, msg=f"Not found user of {nickname}"),
        )
    return res(success=True, data=user)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_409_CONFLICT: {
            "description": "Conflict e-mail information",
        },
        status.HTTP_201_CREATED: {
            "content": {
                "application/json": {
                    "example": {
                        "success": True,
                        "data": {"user_id": 0},
                    }
                }
            },
        },
    },
    summary="Create new account",
)
async def create_user(details: CreateUserRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == details.email).first()
    if user:
        raise res(success=False, msg="Conflict of e-mail")

    hashed_password = auth_handler.get_password_hash(details.password)

    new_user = User(
        name=details.name,
        email=details.email,
        password=hashed_password,
    )
    db.add(new_user)
    db.commit()
    return res(success=True, data=new_user.id)


@router.post("/login", status_code=status.HTTP_200_OK)
async def login(details: AuthDetails, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == details.email).first()
    x = auth_handler.verify_password(details.password, user.password)
    print(x)

    if not user:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="User not found")

    return {"token": "token"}
