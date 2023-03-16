# Licensed under the Apache License, Version 2.0 (the "License");
# ----------------------------------------------------------------
# ok
# ----------------------------------------------------------------
import pytest

from models import Genre


class TestGenresView:
    @pytest.fixture
    def genre(self, db):
        obj = Genre(name="genre")
        db.session.add(obj)
        db.session.commit()
        return obj

    def test_many(self, client, genre):
        response = client.get("/genres/")
        assert response.status_code == 200
        assert response.json == [{"id": genre.id, "name": genre.name}]

    def test_genre_pages(self, client, genre):
        response = client.get("/genres/?page=1")
        assert response.status_code == 200
        assert len(response.json) == 1

        response = client.get("/genres/?page=2")
        assert response.status_code == 200
        assert len(response.json) == 0

    def test_genre(self, client, genre):
        response = client.get("/genres/1/")
        assert response.status_code == 200
        assert response.json == {"id": genre.id, "name": genre.name}

    def test_genre_not_found(self, client, genre):
        response = client.get("/genres/2/")
        assert response.status_code == 404
