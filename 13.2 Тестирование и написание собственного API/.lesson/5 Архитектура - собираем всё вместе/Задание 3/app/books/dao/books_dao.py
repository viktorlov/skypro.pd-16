import json


class BooksDAO:

    def __init__(self, path):
        self.path = path

    def load_data(self):
        with open(self.path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data

    def get_all(self):
        books = self.load_data()
        return books
