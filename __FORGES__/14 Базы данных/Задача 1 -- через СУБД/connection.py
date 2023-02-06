def connection2db(query: str):
    import psycopg2

    t0ken = {"db_host": "localhost",
             "db_name": "forges14",
             "db_password": "sql",
             "db_port": "5432",
             "db_user": "postgres"}

    connection = psycopg2.connect(database=t0ken['db_name'],
                                  user=t0ken['db_user'],
                                  password=t0ken['db_password'],
                                  host=t0ken['db_host'],
                                  port=t0ken['db_port'])

    cursor = connection.cursor()
    cursor.execute(query)
    groceries = cursor.fetchall()
    return groceries


if __name__ == '__main__':
    print(connection2db('SELECT object FROM grocery'))