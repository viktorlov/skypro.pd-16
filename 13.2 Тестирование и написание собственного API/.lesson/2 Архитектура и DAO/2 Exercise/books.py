class Book:
    def __init__(self, book_id, title, pages):
        self.pk = book_id
        self.title = title
        self.pages = pages

    def __repr__(self):
        return f"{self.name}"
