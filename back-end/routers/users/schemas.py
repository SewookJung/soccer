from pydantic import BaseModel, validator
from typing import Optional


class CreateUserRequest(BaseModel):
    name: str
    email: str
    password: str
    nickname: str

    @validator("name")
    def check_name(cls, v):
        if not v:
            raise ValueError("Name is a blank")
        return v

    @validator("email")
    def check_email(cls, v):
        if not v:
            raise ValueError("Email is blank")
        return v

    @validator("nickname")
    def check_nickname(cls, v):
        if not v:
            raise ValueError("Nickname is blank")
        return v

    @validator("password")
    def check_pw(cls, v):
        if not v:
            raise ValueError("Password is blank")
        return v


class AuthDetails(BaseModel):
    email: str
    password: str

    @validator("email")
    def check_email(cls, v):
        if not v:
            raise ValueError("Required email!")
        return v

    @validator("password")
    def check_password(cls, v):
        if not v:
            raise ValueError("Required password!")
        return v
