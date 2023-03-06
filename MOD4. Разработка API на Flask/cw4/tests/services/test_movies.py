# Licensed under the Apache License, Version 2.0 (the "License");
# ----------------------------------------------------------------
# TODO: test_get_movies
# ----------------------------------------------------------------
from unittest.mock import patch

import pytest

from exceptions import ItemNotFound
from models import Movie
from services import MoviesService


class TestMoviesService:

    @pytest.fixture()
    @patch('dao.MoviesDAO')
    def movies_dao_mock(self, dao_mock):
        m1 = Movie(id=1, title="title1", description="description1", trailer="trailer1",
                   year=2001, rating=1, genre_id=1, director_id=1)
        m2 = Movie(id=2, title="title2", description="description2", trailer="trailer2",
                   year=2002, rating=2, genre_id=2, director_id=2)
        dao = dao_mock()
        dao.get_by_id.return_value = m1
        dao.get_all.return_value = [m1, m2]
        return dao

    @pytest.fixture()
    def movies_service(self, movies_dao_mock):
        return MoviesService(dao=movies_dao_mock)

    @pytest.fixture
    def movie(self, db):
        obj = Movie(id=1, title="title1", description="description1", trailer="trailer1",
                    year=2001, rating=1, genre_id=1, director_id=1)
        db.session.add(obj)
        db.session.commit()
        return obj

    def test_get_movie(self, movies_service, movie):
        assert movies_service.get_item(movie.id)

    def test_movie_not_found(self, movies_dao_mock, movies_service):
        movies_dao_mock.get_by_id.return_value = None

        with pytest.raises(ItemNotFound):
            movies_service.get_item(1)

    # @pytest.mark.parametrize('page', [1, None], ids=['with page', 'without page'])
    # def test_get_movies(self, movies_dao_mock, movies_service, page):
    #     movies = movies_service.get_all(page=page)
    #     assert len(movies) == 2
    #     assert movies == movies_dao_mock.get_all.return_value
    #     movies_dao_mock.get_all.assert_called_with(page=page)
