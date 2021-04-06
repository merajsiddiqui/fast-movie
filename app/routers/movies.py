from fastapi import APIRouter
from app.models.response import Response

router = APIRouter(
    prefix="/movies",
    tags=["movies"],
    responses={404: {'model': Response}},
)


@router.get("/{city}")
def get_movies(city: str):
    return {
        "api": "Post"
    }


@router.get("/{movie_id}")
def movie_details(movie_id: str):
    return {
        "api": "Post"
    }
