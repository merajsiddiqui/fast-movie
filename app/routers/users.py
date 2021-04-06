from fastapi import APIRouter, Depends
from app.models.user import LoginRequestBody, RegisterRequestBody

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@router.post("/login")
def login_user(login: LoginRequestBody):
    return {
        "api": "Post"
    }


@router.post("/register")
def register_user(user: RegisterRequestBody):
    return {
        "api": "Post"
    }
