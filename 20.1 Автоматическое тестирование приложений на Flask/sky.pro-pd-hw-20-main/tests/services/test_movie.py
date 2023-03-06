import pytest
from unittest.mock import MagicMock

from app.dao.movie import MovieDAO
from app.dao.model.movie import Movie
from app.service.movie import MovieService

TEST_MOVIES_COUNT = 10


@pytest.fixture(scope="module")
def mocked_movie_dao():
    def create(data):
        pk = max(movies.keys()) + 1
        movie = Movie(
            id=pk,
            title=data["title"],
            description=data["description"],
            trailer=data["trailer"],
            year=data["year"],
            rating=data["rating"],
            genre_id=data["genre_id"],
            director_id=data["director_id"],
        )
        movies.update({
            pk: movie
        })

        return movie

    def update(data):
        model = movies.get(data.get("id"))
        model.title = data.get("title")
        model.description = data.get("description")
        model.trailer = data.get("trailer")
        model.year = data.get("year")
        model.rating = data.get("rating")
        model.genre_id = data.get("genre_id")
        model.director_id = data.get("director_id")

        return model

    movies = {i: Movie(
        id=i,
        title=f"title-{i}",
        description=f"description-{i}",
        trailer=f"trailer-{i}",
        year=2000 + i,
        rating=8.0 + i,
        genre_id=i,
        director_id=i,
    ) for i in range(1, TEST_MOVIES_COUNT + 1)}

    mocked_dao = MovieDAO(None)

    mocked_dao.get_one = MagicMock(side_effect=movies.get)
    mocked_dao.get_all = MagicMock(return_value=movies.values())
    mocked_dao.create = MagicMock(side_effect=create)
    mocked_dao.delete = MagicMock(side_effect=movies.pop)
    mocked_dao.update = MagicMock(side_effect=update)

    return mocked_dao


class TestMovieService:

    @pytest.fixture(autouse=True)
    def user_service(self, mocked_movie_dao):
        self.service = MovieService(mocked_movie_dao)

    @pytest.mark.parametrize("pk, title", [(i, f"title-{i}") for i in range(1, TEST_MOVIES_COUNT + 1)])
    def test_get_one(self, pk, title):
        assert self.service.get_one(pk).id == pk
        assert self.service.get_one(pk).title == title
        assert isinstance(self.service.get_one(pk), Movie)

    def test_get_all(self):
        models = self.service.get_all()
        assert len(models) == TEST_MOVIES_COUNT
        for model in models:
            assert isinstance(model, Movie)

    def test_create(self):
        model = self.service.create(dict(
            id=-100,
            title=f"movie-{TEST_MOVIES_COUNT + 1}",
            description=f"description-{TEST_MOVIES_COUNT + 1}",
            trailer=f"trailer-{TEST_MOVIES_COUNT + 1}",
            year=2000 + TEST_MOVIES_COUNT + 1,
            rating=8.0 + TEST_MOVIES_COUNT + 1,
            genre_id=TEST_MOVIES_COUNT + 1,
            director_id=TEST_MOVIES_COUNT + 1,
        ))
        assert model is not None
        assert model.id != -100
        assert isinstance(model, Movie)
        assert model.id > TEST_MOVIES_COUNT

    def test_delete(self):
        before_delete = self.service.get_all()
        before_len = len(before_delete)
        before_max_id = max([model.id for model in before_delete])

        self.service.delete(before_max_id)

        after_delete = self.service.get_all()
        after_len = len(after_delete)
        after_max_id = max([model.id for model in after_delete])

        assert before_len > after_len
        assert before_max_id > after_max_id
        assert self.service.get_one(before_max_id) is None

    def test_update(self):
        updated_model = self.service.update(dict(
            id=1,
            title="update_test",
            description=f"description_test",
            trailer=f"trailer_test",
            year=2000 + TEST_MOVIES_COUNT + 1,
            rating=8.0 + TEST_MOVIES_COUNT + 1,
            genre_id=TEST_MOVIES_COUNT + 1,
            director_id=TEST_MOVIES_COUNT + 1,
        ))
        assert 1 == updated_model.id
        assert "update_test" == updated_model.title

        get_model = self.service.get_one(1)
        assert get_model.id == updated_model.id
        assert "update_test" == get_model.title

    def test_partially_update(self):
        title_before_update = self.service.get_one(2).title
        updated_model = self.service.partially_update(dict(id=2))
        updated_model = self.service.partially_update(dict(id=2, title="partially_update_test"))
        assert updated_model.title == "partially_update_test"
        assert self.test_get_one(2).title == "partially_update_test"
