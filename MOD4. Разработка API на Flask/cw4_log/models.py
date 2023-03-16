# Licensed under the Apache License, Version 2.0 (the "License");
# ----------------------------------------------------------------
# ok
# ----------------------------------------------------------------
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

from setup.db import models


class Genre(models.Base):
    __tablename__ = 'genres'

    name = Column(String(100), unique=True, nullable=False)


class Director(models.Base):
    __tablename__ = 'directors'

    name = Column(String(100), unique=True, nullable=False)


class Movie(models.Base):
    __tablename__ = 'movies'

    title = Column(String(100), nullable=False)
    description = Column(String(255), nullable=False)
    trailer = Column(String(255), nullable=False)
    year = Column(Integer, nullable=False)
    rating = Column(Float, nullable=False)
    genre_id = Column(Integer, ForeignKey(f'{Genre.__tablename__}.id'), nullable=False)
    genre = relationship('Genre')
    director_id = Column(Integer, ForeignKey(f'{Director.__tablename__}.id'), nullable=False)
    director = relationship('Director')


class User(models.Base):
    __tablename__ = 'users'

    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), unique=False, nullable=False)
    name = Column(String(255))
    surname = Column(String(255))
    favorite_genre_id = Column(Integer, ForeignKey(f'{Genre.__tablename__}.id'))
    favorite_genre = relationship("Genre")


class FavoriteMovie(models.Base):
    __tablename__ = 'favorite_movie'

    user_id = Column(Integer, ForeignKey(f'{User.__tablename__}.id'))
    movie_id = Column(Integer, ForeignKey(f'{Movie.__tablename__}.id'))
    user = relationship("User")
    movie = relationship("Movie")
