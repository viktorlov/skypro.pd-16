from dao.book import BookDAO


class BookService:
    def __init__(self, dao: BookDAO):
        self.dao = dao

    def get_one(self, bid: int):
        book = self.dao.get_one(bid)
        def _print_s1():
            print('    SERVICE: get_one')
            print(f'    SERVICE INPUT {bid = }')
            print(f'    SERVICE INPUT {type(bid) = }')
            print(f'    SERVICE OUTPUT { book = }')
            print(f'    SERVICE OUTPUT {type(book) = }')

        _print_s1()
        return book

    def get_all(self):
        def _print_s2():
            print('    SERVICE: get_all')
            print(f'    SERVICE OUTPUT {self.dao.get_all() = }')
            print(f'    SERVICE OUTPUT {type(self.dao.get_all()) = }')

        _print_s2()
        return self.dao.get_all()

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        # return self.dao.update(data)
        pass

    def delete(self, bid: int):
        self.dao.delete(bid)
        return None
