import json

from books import Book


class BooksDAO:

    def load_data(self):

        with open("books.json", "r", encoding="utf-8") as file:
            books_data = json.load(file)
            books = []
            # Создаем список объектов класса Book
            for book in books_data:
                books.append(Book(book["pk"],
                                  book["title"],
                                  book["pages"], ))
        return books

    def get_all(self):
        return self.load_data()

    def get_by_id(self, book_id):
        books = self.load_data()
        for book in books:
            if book.pk == book_id:
                return book
