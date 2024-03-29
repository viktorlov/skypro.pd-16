from unittest.mock import MagicMock

import pytest

from dao.model.movie import Movie
from dao.model.genre import Genre
from dao.model.director import Director

from dao.movie import MovieDAO
from service.movie import MovieService


# from setup_db import db


@pytest.fixture()
def movie_dao():
    # movie_dao = MovieDAO(db.session)
    movie_dao = MovieDAO(None)

    jonh = Movie(id=1, title="title1", description="description1", trailer="trailer1", year=1990, rating=3)
    kate = Movie(id=2, title="title2", description="description2", trailer="trailer2", year=1990, rating=3)
    max = Movie(id=3, title="title3", description="description3", trailer="trailer3", year=1990, rating=3)

    movie_dao.get_one = MagicMock(return_value=jonh)
    movie_dao.get_all = MagicMock(return_value=[jonh, kate, max])
    movie_dao.create = MagicMock(return_value=Movie(id=4))
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock()
    return movie_dao


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)
        assert movie != None
        assert movie.id != None

    def test_get_all(self):
        movies = self.movie_service.get_all()
        assert len(movies) > 0

    def test_create(self):
        created_movie = {
            "title": "title2049",
            "description": "description2049",
            "trailer": "trailer2049",
            "year": 2049,
            "rating": 20.49,
            "genre_id": 2,
            "director_id": 2
        }
        movie = self.movie_service.create(created_movie)
        assert movie.id != None

    def test_delete(self):
        self.movie_service.delete(1)

    def test_update(self):
        updated_movie = {
            "id": 2049,
            "title": "title2049_up",
            "description": "description2049_up",
            "trailer": "trailer2049_up",
            "year": 2049,
            "rating": 20.49,
            "genre_id": 2,
            "director_id": 2
        }
        self.movie_service.update(updated_movie)
