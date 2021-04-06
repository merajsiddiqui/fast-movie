from fastapi import APIRouter, HTTPException
from app.models.user import LoginRequestBody, RegisterRequestBody, LoginResponseModel
from app.models.response import Response
from app.services.user import authenticate
from app.middleware.auth import signJWT
from typing import Dict
from fastapi.responses import JSONResponse

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={
        404: {'model': Response}
    },
)


@router.post("/login", response_model=LoginResponseModel)
def login_user(login: LoginRequestBody):
    authenticated_user = authenticate(login)
    if authenticated_user is None:
        authentication_error: Dict = {
            'code': 'AUTH_ERR',
            'message': 'Unable to Authenticate User'
        }
        return JSONResponse(status_code=404, content={"error": authentication_error})

    token = signJWT(authenticated_user['email'])
    print(token)
    return JSONResponse(status_code=200, content={
        'data': authenticated_user,
        'token': token
    })


@router.post("/register")
def register_user(user: RegisterRequestBody):
    return {
        "api": "Post"
    }
