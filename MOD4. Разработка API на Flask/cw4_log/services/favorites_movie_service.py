from typing import Optional

from dao import FavoritesDAO
from exceptions import ItemNotFound
from models import FavoriteMovie
from utils import debug


class FavoritesMovieService:
    @debug
    def __init__(self, dao: FavoritesDAO) -> None:
        self.dao = dao

    @debug
    def get_item(self, pk: int) -> FavoriteMovie:
        if favorite_movie := self.dao.get_by_id(pk):
            return favorite_movie
        raise ItemNotFound(f'Favorite movie with pk={pk} not exists.')

    @debug
    def get_all(self, page: Optional[int] = None) -> list[FavoriteMovie]:
        return self.dao.get_all(page=page)

    @debug
    def add_movie(self, user_id, movie_id):
        self.dao.add_new(user_id, movie_id)

    @debug
    def delete_movie(self, user_id, movie_id):
        self.dao.delete(user_id, movie_id)
