import prettytable
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app: Flask = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///../fruits.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db: SQLAlchemy = SQLAlchemy(app)

session = db.session()
cursor = session.execute("SELECT * from fruits WHERE kcal < 200").cursor
table = prettytable.from_db_cursor(cursor)
table.max_width = 30

if __name__ == '__main__':
    print(table)
