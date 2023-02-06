import sqlite3


def create_DB():
    with sqlite3.connect("forges14.db") as connection:
        cursor = connection.cursor()


if __name__ == '__main__':
    create_DB()
