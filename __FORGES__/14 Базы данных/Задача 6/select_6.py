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
            SELECT `id`, `object`, `kcal` 
            FROM grocery
            WHERE `category` = 'veggie'
            ORDER BY 2
            """
    print(*select(query), sep='\n')
