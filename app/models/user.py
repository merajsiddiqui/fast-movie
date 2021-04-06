from pydantic import BaseModel, EmailStr
from .response import Response
from .database import Base
from sqlalchemy import Column, Integer, String

'''
This model represents database 
'''


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, )  # User full name
    email = Column(String)  # User Email Id
    password = Column(Integer)  # User password


'''
The below Models are just used for schema and data conversion
'''


class UserResponseModel(BaseModel):
    name: str
    email: EmailStr


class LoginRequestBody(BaseModel):
    email: EmailStr
    password: str


class LoginResponseModel(Response):
    data: UserResponseModel
    token: str


class RegisterRequestBody(BaseModel):
    name: str
    email: EmailStr
    password: str
