from typing import Optional

from dao import MoviesDAO
from exceptions import ItemNotFound
from models import Movie
from utils import debug


class MoviesService:
    @debug
    def __init__(self, dao: MoviesDAO) -> None:
        self.dao = dao

    @debug
    def get_item(self, pk: int) -> Movie:
        if movie := self.dao.get_by_id(pk):
            return movie
        raise ItemNotFound(f'Movie with pk={pk} not exists.')

    @debug
    def get_all(self, filter=None, page: Optional[int] = None) -> list[Movie]:
        return self.dao.get_all_order_by(page=page, filter=filter)
