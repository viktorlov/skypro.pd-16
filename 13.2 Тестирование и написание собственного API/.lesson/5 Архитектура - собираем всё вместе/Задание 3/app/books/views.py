from flask import Blueprint, render_template

from .dao.books_dao import BooksDAO

# Создаем блупринт
books_blueprint = Blueprint('books_blueprint', __name__, template_folder="templates")

# Создаем DAO
books_dao = BooksDAO("./data/books.json")


# Создаем вьюшку для кандидатов
@books_blueprint.route('/books/')
def page_books_all():
    books = books_dao.get_all()
    return render_template("books_index.html", books=books)
