from dao.model.book import Book


class BookDAO:

    def __init__(self, session):
        self.session = session

    def get_one(self, bid: int):
        return self.session.query(Book).get(bid)

    def get_all(self):
        return self.session.query(Book).all()

    def create(self, data: dict):
        # noinspection PyArgumentList
        interim = Book(**data)
        self.session.add(interim)
        self.session.commit()
        return None

    def update(self, data: dict):
        self.session.query(Book).filter(Book.book_id == data.get('book_id')).update(data)
        self.session.commit()
        return None

    def delete(self, bid):
        book = self.get_one(bid)
        self.session.delete(book)
        self.session.commit()
        return None
