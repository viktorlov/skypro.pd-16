from dao.model.author import Author


class AuthorDAO:

    def __init__(self, session):
        self.session = session

    def get_one(self, aid: int):
        return self.session.query(Author).get(aid)

    def get_all(self):
        return self.session.query(Author).all()
