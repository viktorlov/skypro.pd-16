import sqlite3


def select(query):
    with sqlite3.connect('forges14.db') as connection:
        cursor = connection.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
    return data


if __name__ == '__main__':
    query = """SELECT * from grocery"""
    print(*select(query), sep='\n')
