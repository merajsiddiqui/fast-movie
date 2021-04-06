from fastapi import FastAPI, HTTPException
from app.routers import users, movies, theaters, bookings
from app.models.response import Response

tags_metadata = [
    {
        "name": "users",
        "description": "Operations with users"
    },
    {
        "name": "movies",
        "description": "Operations with items"
    },
    {
        "name": "theaters",
        "description": "Operations with Theaters"
    }
]

app = FastAPI(
    title="FAST Movie API",
    description="Fast Movie API documentation to book movies",
    version="0.0.1",
    openapi_tags=tags_metadata
)


@app.get("/")
def read_root():
    return {
        'name': 'Fast Movie API',
        'version': "1.0",
        'error': None,
    }


# Including user api routes
app.include_router(users.router)
app.include_router(movies.router)
app.include_router(theaters.router)
app.include_router(bookings.router)