from dao.author import AuthorDAO


class AuthorService:
    def __init__(self, dao: AuthorDAO):
        self.dao = dao

    def get_one(self, aid: int):
        return self.dao.get_one(aid)

    def get_all(self):
        return self.dao.get_all()
