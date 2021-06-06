from pydantic import BaseModel, validator
from typing import Optional


class CreateUserRequest(BaseModel):
    name: str
    email: str
    password: str
    is_active: bool

    @validator("name")
    def check_name(cls, v):
        if not v:
            raise ValueError("Name is must be not a blank")

    @validator("email")
    def check_email(cls, v):
        if not v:
            raise ValueError("E-mail is must be not a blank")

    @validator("password")
    def check_password(cls, v):
        if not v:
            raise ValueError("Password is must be not a blank")


class UpdateUserRequest(BaseModel):
    id: int
    name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    is_active: bool


class AuthDetails(BaseModel):
    username: str
    password: str
    email: str
