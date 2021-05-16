from pydantic import BaseModel
from pydantic.typing import is_callable_type


class CreateUserRequest(BaseModel):
    name: str
    email: str
    password: str
    is_active: bool


class GetUserRequest(BaseModel):
    id: int


class UpdateUserRequest(BaseModel):
    name: str
    email: str
    password: str
    is_active: bool


class DeleteUserRequest(BaseModel):
    id: int
