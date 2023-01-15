import pytest
from app.books.dao.books_dao import BooksDAO


@pytest.fixture()
def books_dao():
    books_dao_instance = BooksDAO("./data/books.json")
    return books_dao_instance


class TestBooksDao:

    def test_get_all(self, books_dao):
        books = books_dao.get_all()
        assert type(books) == list, "возвращается не список"
        assert len(books) > 0, "возвращается пустой список"
