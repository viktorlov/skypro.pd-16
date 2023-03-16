from typing import Optional

from dao.base import BaseDAO
from exceptions import ItemNotFound
from models import Director
from utils import debug


class DirectorsService:
    @debug
    def __init__(self, dao: BaseDAO) -> None:
        self.dao = dao

    @debug
    def get_item(self, pk: int) -> Director:
        if director := self.dao.get_by_id(pk):
            return director
        raise ItemNotFound(f'Director with pk={pk} not exists.')

    @debug
    def get_all(self, page: Optional[int] = None) -> list[Director]:
        return self.dao.get_all(page=page)
