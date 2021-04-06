from .database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship


class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))  # User Id
    show_id = Column(Integer, ForeignKey("movie_shows.id"))  # Show Id
    ticket_code = Column(String)  # ticket code to be scanned
    deleted = Column(Boolean, default=False)  # if cancelled

    '''
    Relationships
    '''

    user = relationship("User", back_populates="users")

    show = relationship("MovieShows", back_populates="movie_shows")
