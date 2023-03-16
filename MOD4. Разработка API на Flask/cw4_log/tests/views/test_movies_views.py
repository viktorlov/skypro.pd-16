# Licensed under the Apache License, Version 2.0 (the "License");
# ----------------------------------------------------------------
# ok
# ----------------------------------------------------------------
import pytest

from models import Movie


class TestMoviesView:
    @pytest.fixture
    def movie(self, db):
        obj = Movie(
            id=1,
            title="title1",
            description="description1",
            trailer="trailer1",
            year=2001,
            rating=1,
            genre_id=1,
            director_id=1
        )
        db.session.add(obj)
        db.session.commit()
        return obj

    def test_many(self, client, movie):
        response = client.get("/movies/")
        assert response.status_code == 200
        assert response.json == [{'description': 'description1',
                                  'director': {'id': None, 'name': None},
                                  'genre': {'id': None, 'name': None},
                                  'id': 1,
                                  'rating': 1.0,
                                  'title': 'title1',
                                  'trailer': 'trailer1',
                                  'year': 2001}]

    def test_movie_pages(self, client, movie):
        response = client.get("/movies/?page=1")
        assert response.status_code == 200
        assert len(response.json) == 1

        response = client.get("/movies/?page=2")
        assert response.status_code == 200
        assert len(response.json) == 0

    def test_movie(self, client, movie):
        response = client.get("/movies/1/")
        assert response.status_code == 200
        assert response.json == {'description': 'description1',
                                 'director': {'id': None, 'name': None},
                                 'genre': {'id': None, 'name': None},
                                 'id': 1,
                                 'rating': 1.0,
                                 'title': 'title1',
                                 'trailer': 'trailer1',
                                 'year': 2001}

    def test_movie_not_found(self, client, movie):
        response = client.get("/movies/2/")
        assert response.status_code == 404
