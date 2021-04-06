from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    email: str
    password: str
    created_at: str
    updated_at: str


# class UserResponse(Response):

class LoginRequestBody(BaseModel):
    email: str
    password: str


class RegisterRequestBody(BaseModel):
    name: str
    email: str
    password: str
