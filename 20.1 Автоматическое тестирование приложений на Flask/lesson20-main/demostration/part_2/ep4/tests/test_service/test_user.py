from unittest.mock import MagicMock

import pytest

from dao.model.user import User
from dao.user import UserDAO
from service.user import UserService
from setup_db import db


@pytest.fixture()
def user_dao():
    user_dao = UserDAO(db.session)

    jonh = User(id=1, name='jonh', age=30)
    kate = User(id=2, name='kate', age=31)
    max = User(id=3, name='max', age=32)

    user_dao.get_one = MagicMock(return_value=jonh)
    user_dao.get_all = MagicMock(return_value=[jonh, kate, max])
    user_dao.create = MagicMock(return_value=User(id=3))
    user_dao.delete = MagicMock()
    user_dao.update = MagicMock()
    return user_dao


class TestUserService:
    @pytest.fixture(autouse=True)
    def user_service(self, user_dao):
        self.user_service = UserService(dao=user_dao)

    def test_get_one(self):
        user = self.user_service.get_one(1)
        assert user != None
        assert user.id != None

    def test_get_all(self):
        users = self.user_service.get_all()
        assert len(users) > 0

    def test_create(self):
        user_d = {
            "name": "Ivan",
            "age": 39,
        }
        user = self.user_service.create(user_d)
        assert user.id != None

    def test_delete(self):
        self.user_service.delete(1)

    def test_update(self):
        user_d = {
            "id": 3,
            "name": "Ivan",
            "age": 39,
        }
        self.user_service.update(user_d)
