from fastapi import APIRouter
from app.models.response import Response


router = APIRouter(
    prefix="/theaters",
    tags=["theaters"],
    responses={404: {'model': Response}},
)


@router.get("/{city}")
def get_theater_list(city: str):
    return {
        "api": "Post"
    }


@router.get("/{theater_id}")
def get_theater_details(theater_id: str):
    return {
        "api": "Post"
    }
