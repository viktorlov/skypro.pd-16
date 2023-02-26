from dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session) -> None:
        self.session = session

    def get_one(self, mid) -> list:
        return self.session.query(Movie).get(mid)

    def get_all(self, filters: dict[str, str | None]) -> list:
        interim = self.session.query(Movie)
        if filters.get("director_id") is not None:
            interim = interim.filter(Movie.director_id == filters.get("director_id"))
        if filters.get("genre_id") is not None:
            interim = interim.filter(Movie.genre_id == filters.get("genre_id"))
        if filters.get("year") is not None:
            interim = interim.filter(Movie.year == filters.get("year"))
        return interim.all()

    def create(self, created_movie_data) -> Movie:
        created_movie: Movie = Movie(**created_movie_data)
        self.session.add(created_movie)
        self.session.commit()
        return created_movie

    def delete(self, mid) -> None:
        deleted_movie: list = self.get_one(mid)
        self.session.delete(deleted_movie)
        self.session.commit()

    def update(self, updated_movie_data):
        updated_movie: list = self.get_one(updated_movie_data.get("id"))

        updated_movie.title = updated_movie_data.get("title")
        updated_movie.description = updated_movie_data.get("description")
        updated_movie.trailer = updated_movie_data.get("trailer")
        updated_movie.year = updated_movie_data.get("year")
        updated_movie.rating = updated_movie_data.get("rating")
        updated_movie.genre_id = updated_movie_data.get("genre_id")
        updated_movie.director_id = updated_movie_data.get("director_id")

        # TODO Переделать на короткую запись через .update

        self.session.add(updated_movie)
        self.session.commit()
