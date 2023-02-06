import sqlite3


def create_TABLE():
    with sqlite3.connect("forges14.db") as connection:
        cursor = connection.cursor()
        query = """
                CREATE TABLE grocery (`id` INTEGER PRIMARY KEY AUTOINCREMENT,
                                      `object` VARCHAR(20), 
                                      `category` VARCHAR(20),
                                      `kcal` integer)
                """
        cursor.execute(query)


if __name__ == "__main__":
    create_TABLE()
