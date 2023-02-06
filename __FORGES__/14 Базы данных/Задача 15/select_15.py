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
            SELECT DISTINCT `category`,
                            ROUND(SUM(`kcal`)) AS "Сумма калорий",
                            ROUND(AVG(`kcal`)) AS "Средняя калорийность"
            FROM grocery
            GROUP BY `category`
            """
    print(*select(query), sep='\n')
