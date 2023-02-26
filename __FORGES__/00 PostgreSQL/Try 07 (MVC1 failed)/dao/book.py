import json

from dao.model.book import Book


class BookDAO:

    def __init__(self, session):
        self.session = session

    def get_one(self, bid: int):
        book = self.session.query(Book).get(bid)
        def _print_():
            print('        DAO: get_one')
            print(f'        DAO INPUT {bid = }')
            print(f'        DAO INPUT {type(bid) = }')
            print(f'        DAO OUTPUT { book = }')
            print(f'        DAO OUTPUT {type(book) = }')

        _print_()
        return book

    def get_all(self):
        def _print_():
            print('        DAO: get_all')
            print(f'        DAO OUTPUT {self.session.query(Book).all() = }')
            print(f'        DAO OUTPUT {type(self.session.query(Book).all()) = }')

        _print_()
        return self.session.query(Book).all()

    def create(self, data: json):
        # noinspection PyArgumentList
        interim = Book(**data)
        self.session.add(interim)
        self.session.commit()
        return interim

    def update(self, data: json):
        # return
        pass

    def delete(self, bid):
        book = self.get_one(bid)
        self.session.delete(book)
        self.session.commit()
        return None
