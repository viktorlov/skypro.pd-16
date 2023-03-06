from typing import Optional

from dao import FavoritesDAO
from exceptions import ItemNotFound
from models import FavoriteMovie


class FavoritesMovieService:
    def __init__(self, dao: FavoritesDAO) -> None:
        self.dao = dao

    def get_item(self, pk: int) -> FavoriteMovie:
        if favorite_movie := self.dao.get_by_id(pk):
            return favorite_movie
        raise ItemNotFound(f'Favorite movie with pk={pk} not exists.')

    def get_all(self, page: Optional[int] = None) -> list[FavoriteMovie]:
        return self.dao.get_all(page=page)

    def add_movie(self, user_id, movie_id):
        self.dao.add_new(user_id, movie_id)

    def delete_movie(self, user_id, movie_id):
        self.dao.delete(user_id, movie_id)
