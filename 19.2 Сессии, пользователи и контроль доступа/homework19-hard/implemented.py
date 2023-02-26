# ----------------------------------------------------------------
# ok
# ----------------------------------------------------------------
from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.movie import MovieDAO
from dao.user import UserDAO
from service.auth import AuthService
from service.director import DirectorService
from service.genre import GenreService
from service.movie import MovieService
from service.user import UserService
from setup_db import db

director_dao: DirectorDAO = DirectorDAO(session=db.session)
genre_dao: GenreDAO = GenreDAO(session=db.session)
movie_dao: MovieDAO = MovieDAO(session=db.session)
user_dao: UserDAO = UserDAO(session=db.session)

director_service: DirectorService = DirectorService(dao=director_dao)
genre_service: GenreService = GenreService(dao=genre_dao)
movie_service: MovieService = MovieService(dao=movie_dao)
user_service = UserService(dao=user_dao)
auth_service = AuthService(user_service=user_service)
