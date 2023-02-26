from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from prettytable import prettytable

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:sql@localhost:5432/lesson15'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

session = db.session()

cursor = session.execute("SELECT * from public.authors").cursor
authors_table = prettytable.from_db_cursor(cursor)
authors_table.max_width = 30

cursor = session.execute("SELECT * from public.books").cursor
books_table = prettytable.from_db_cursor(cursor)
books_table.max_width = 30

if __name__ == '__main__':
    print(authors_table)
    print(books_table)
