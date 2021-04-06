from pydantic import BaseModel, EmailStr
from .response import Response


class User(BaseModel):
    id: int
    name: str
    email: EmailStr
    password: str
    created_at: str
    updated_at: str


class UserResponseModel(BaseModel):
    name: str
    email: str


class LoginRequestBody(BaseModel):
    email: str
    password: str


class LoginResponseModel(Response):
    data: UserResponseModel
    token: str


class RegisterRequestBody(BaseModel):
    name: str
    email: str
    password: str
