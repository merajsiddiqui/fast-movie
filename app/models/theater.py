from .database import Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship


class Theater(Base):
    __tablename__ = "theaters"

    '''
    Columns
    '''
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, )  # Name of the cinema
    city = Column(String)  # City where the cinema is located

    '''
    Relationships
    '''
    shows = relationship("MovieShows", back_populates="movie_shows")


class MovieShows(Base):
    __tablename__ = "movie_shows"

    '''
    Columns
    '''
    id = Column(Integer, primary_key=True, index=True)
    theater_id = Column(Integer, ForeignKey("theaters.id"))
    movie_id = Column(Integer, ForeignKey("movies.id"))
    show_time = Column(String)  # Show Time which can be further improved
    hall_name = Column(String)  # Hall name where show is going on
    ticket_cost = Column(Float)  # cost per show
    capacity = Column(Integer)  # Maximum tickets which can be booked

    '''
    Relationships
    '''

    theater = relationship("Theater", back_populates="theaters")

    movies = relationship("Movies", back_populates="movies")
