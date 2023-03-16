from typing import Optional

import jwt
from flask import current_app

from dao import UsersDAO
from exceptions import ItemNotFound
from models import User
from tools.security import generate_password_hash
from utils import debug


class UsersService:
    @debug
    def __init__(self, dao: UsersDAO) -> None:
        self.dao = dao

    @debug
    def get_item(self, pk: int) -> User:
        if user := self.dao.get_by_id(pk):
            return user
        raise ItemNotFound(f'User with pk={pk} not exists.')

    @debug
    def get_all(self, page: Optional[int] = None) -> list[User]:
        return self.dao.get_all(page=page)

    @debug
    def get_user_by_login(self, login):
        return self.dao.get_user_by_login(login)

    @debug
    def create_user(self, login, password):
        self.dao.create(login, generate_password_hash(password))

    @debug
    def partial_update(self, user_d):
        return self.dao.partial_update(user_d)

    @debug
    def get_user_by_token(self, token):
        data = jwt.decode(token,
                          current_app.config["SECRET_KEY"],
                          algorithms=[current_app.config["ALGORITHM"]])
        return self.get_user_by_login(data['login'])
