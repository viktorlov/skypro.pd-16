import sqlite3


def select(query_: str):
    with sqlite3.connect('../forges14.db') as connection:
        connection.row_factory = sqlite3.Row
        data = []
        for i in connection.execute(query_).fetchall():
            data.append(dict(i))
    return data


if __name__ == '__main__':
    query = """
            SELECT COUNT(*) as "Общее количество фруктов"
            FROM grocery
            WHERE `category` = 'fruit'
            """
    print(*select(query), sep='\n')

    query = """
            SELECT COUNT(*) as "Общее количество продуктов с калорийностью меньше 200"
            FROM grocery
            WHERE `kcal` < 200
            """
    print(*select(query), sep='\n')
