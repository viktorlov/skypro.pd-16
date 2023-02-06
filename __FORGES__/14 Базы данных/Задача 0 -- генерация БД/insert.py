import sqlite3


def insert():
    with sqlite3.connect('forges14.db') as connection:
        cursor = connection.cursor()
        query = """
                INSERT INTO grocery (object, category, kcal) 
                VALUES ('Apple green', 'fruit', 45),
                       ('Apple red', 'fruit', 50),
                       ('Banana', 'fruit', 95),
                       ('Avocado', 'fruit', 160),
                       ('Tomato', 'veggie', 20),
                       ('Broccoli', 'veggie', 35),
                       ('Carrot', 'veggie', 100),
                       ('Cookie', 'sweet', 515),
                       ('Donut', 'sweet', 300),
                       ('Cake', 'sweet', 400)
                """
        cursor.execute(query)


if __name__ == '__main__':
    insert()
