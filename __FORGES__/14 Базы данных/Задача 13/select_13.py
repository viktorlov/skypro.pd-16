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
            SELECT SUM(`kcal`) as "Сумма всех калорий"
            FROM grocery
            """
    print(*select(query), sep='\n')

    query = """
            SELECT MAX(`kcal`) as "Самая большая калория"
            FROM grocery
            """
    print(*select(query), sep='\n')

    query = """
            SELECT MIN(`kcal`) as "Самая маленькая калория"
            FROM grocery
            """
    print(*select(query), sep='\n')

    query = """
            SELECT `category`, AVG(`kcal`)
            FROM grocery
            GROUP BY `category`
            """
    print(*select(query), sep='\n')
