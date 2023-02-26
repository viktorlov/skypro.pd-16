from dao.author import AuthorDAO
from dao.book import BookDAO
# from services.author import AuthorService
from services.book import BookService
from setup_db import db

book_dao = BookDAO(session=db.session)
# author_dao = AuthorDAO(session=db.session)

book_service = BookService(dao=book_dao)
# author_service = AuthorService(dao=author_dao)
