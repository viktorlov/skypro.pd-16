# Licensed under the Apache License, Version 2.
# ----------------------------------------------------------------
# ok
# ----------------------------------------------------------------
from dao import GenresDAO, MoviesDAO, DirectorsDAO, UsersDAO, FavoritesDAO

from services import GenresService, MoviesService, DirectorsService, UsersService
from services.auth_service import AuthService
from services.favorites_movie_service import FavoritesMovieService
from setup.db import db

# DAO
genre_dao = GenresDAO(db.session)
movie_dao = MoviesDAO(db.session)
director_dao = DirectorsDAO(db.session)
user_dao = UsersDAO(db.session)
favorite_movie_dao = FavoritesDAO(db.session)

# Services
genre_service = GenresService(dao=genre_dao)
movie_service = MoviesService(dao=movie_dao)
director_service = DirectorsService(dao=director_dao)
user_service = UsersService(dao=user_dao)
auth_service = AuthService(dao=user_dao)
favorite_movie_service = FavoritesMovieService(dao=favorite_movie_dao)
