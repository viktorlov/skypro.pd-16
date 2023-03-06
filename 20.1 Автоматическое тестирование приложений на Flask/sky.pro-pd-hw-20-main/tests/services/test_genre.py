import pytest
from unittest.mock import MagicMock

from app.dao.genre import GenreDAO
from app.dao.model.genre import Genre
from app.service.genre import GenreService

TEST_GENRES_COUNT = 10


@pytest.fixture(scope="module")
def mocked_genre_dao():
    def create(data):
        pk = max(genres.keys()) + 1
        genre = Genre(id=pk, name=data["name"])
        genres.update({
            pk: genre
        })

        return genre

    def update(data):
        model = genres.get(data.get("id"))
        model.name = data.get("name")
        return model

    genres = {i: Genre(id=i, name=f"genre-{i}") for i in range(1, TEST_GENRES_COUNT + 1)}

    mocked_dao = GenreDAO(None)

    mocked_dao.get_one = MagicMock(side_effect=genres.get)
    mocked_dao.get_all = MagicMock(return_value=genres.values())
    mocked_dao.create = MagicMock(side_effect=create)
    mocked_dao.delete = MagicMock(side_effect=genres.pop)
    mocked_dao.update = MagicMock(side_effect=update)

    return mocked_dao


class TestGenreService:

    @pytest.fixture(autouse=True)
    def user_service(self, mocked_genre_dao):
        self.service = GenreService(mocked_genre_dao)

    @pytest.mark.parametrize("pk, name", [(i, f"genre-{i}") for i in range(1, TEST_GENRES_COUNT + 1)])
    def test_get_one(self, pk, name):
        assert self.service.get_one(pk).id == pk
        assert self.service.get_one(pk).name == name
        assert isinstance(self.service.get_one(pk), Genre)

    def test_get_all(self):
        models = self.service.get_all()
        assert len(models) == TEST_GENRES_COUNT
        for model in models:
            assert isinstance(model, Genre)

    def test_create(self):
        model = self.service.create(dict(id=-100, name=f"director-{TEST_GENRES_COUNT + 1}"))
        assert model is not None
        assert model.id != -100
        assert isinstance(model, Genre)
        assert model.id > TEST_GENRES_COUNT

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
        updated_model = self.service.update(dict(id=1, name="update_test"))
        assert 1 == updated_model.id
        assert "update_test" == updated_model.name

        get_model = self.service.get_one(1)
        assert get_model.id == updated_model.id
        assert "update_test" == get_model.name

    def test_partially_update(self):
        name_before_update = self.service.get_one(2).name
        updated_model = self.service.partially_update(dict(id=2))
        assert updated_model.name == name_before_update
        updated_model = self.service.partially_update(dict(id=2, name="partially_update_test"))
        assert updated_model.name == "partially_update_test"
        assert self.test_get_one(2).name == "partially_update_test"
