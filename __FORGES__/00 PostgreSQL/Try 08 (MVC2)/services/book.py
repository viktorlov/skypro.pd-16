from dao.book import BookDAO


class BookService:
    def __init__(self, dao: BookDAO):
        self.dao = dao

    def get_one(self, bid: int):
        return self.dao.get_one(bid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data):
        self.dao.create(data)
        return None

    def update(self, data):
        self.dao.update(data)
        return None

    def delete(self, bid: int):
        self.dao.delete(bid)
        return None
