from typing import Optional

from dao.base import BaseDAO
from exceptions import ItemNotFound
from models import Genre
from utils import debug


class GenresService:
    @debug
    def __init__(self, dao: BaseDAO) -> None:
        self.dao = dao

    @debug
    def get_item(self, pk: int) -> Genre:
        if genre := self.dao.get_by_id(pk):
            return genre
        raise ItemNotFound(f'Genre with pk={pk} not exists.')

    @debug
    def get_all(self, page: Optional[int] = None) -> list[Genre]:
        return self.dao.get_all(page=page)
