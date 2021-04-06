from fastapi import APIRouter, Depends
from app.middleware.auth import JWTBearer
from app.models.response import Response

router = APIRouter(
    prefix="/bookings",
    dependencies=[Depends(JWTBearer())],
    tags=["bookings"],
    responses={404: {'model': Response}},
)


@router.get("/{show_id}")
def get_seats_available(show_id: str):
    return {
        "api": "Post"
    }


@router.get("/confirm")
def confirm_booking(theater_id: str):
    return {
        "api": "Post"
    }


@router.delete("/{booking_id}/cancel")
def cancel_booking(booking_id: str):
    return {
        "api": "Post"
    }
