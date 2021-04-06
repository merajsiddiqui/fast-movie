from fastapi import APIRouter, Depends

router = APIRouter(
    prefix="/bookings",
    tags=["bookings"],
    responses={404: {"description": "Not found"}},
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


@router.delete("booking_id}/cancel")
def cancel_booking(booking_id: str):
    return {
        "api": "Post"
    }
