import sqlite3
from collections import Counter


def db_connect(db_name: str, query_str: str) -> list:
    """
    Функция для подключения к базе данных <<db_name>>,
    и поиска по запросу <<query_str>>.

    :param db_name: Файл с базой данных.
    :param query_str: Строка поиска.
    """

    con = sqlite3.connect(db_name)
    cursor = con.cursor()
    cursor.execute(query_str)
    data: list[dict] = cursor.fetchall()
    con.close()

    return data


def get_movie_by_title(movie_title: str) -> dict:
    """
    Реализуйте поиск по названию.
    Если таких фильмов несколько, выведите самый свежий.
    Затем напишите функцию, которая принимала бы title и возвращала бы данные.

    :param movie_title: Название фильма.
    """

    query_str = ("SELECT `show_id`, `title`, `country`, `release_year`, `listed_in`, `description` "
                 "FROM netflix "
                 f"WHERE LOWER(`title`) LIKE '%{movie_title.lower()}%' "
                 "AND `type`='Movie' "
                 "ORDER BY `release_year` DESC "
                 "LIMIT 1 ")

    data: dict = {"title": db_connect('netflix.db', query_str)[0][1],
                  "country": db_connect('netflix.db', query_str)[0][2],
                  "release_year": db_connect('netflix.db', query_str)[0][3],
                  "genre": db_connect('netflix.db', query_str)[0][4],
                  "description": db_connect('netflix.db', query_str)[0][5].replace('\n', '')}

    return data


def get_movies_by_years(start_date: int, end_date: int) -> list:
    """
    Сделайте поиск по диапазону лет выпуска.
    Сперва напишите SQL запрос. Фильмов будет много, так что ограничьте вывод 100 тайтлами.
    Затем напишите функцию, которая принимала бы два года и возвращала бы данные.

    :param start_date: Год начала поиска.
    :param end_date: Год конца поиска.
    """

    query_str = ("SELECT `show_id`, `title`, `release_year` "
                 "FROM netflix "
                 f"WHERE `release_year` BETWEEN '{start_date}' AND {end_date} "
                 "AND `type`='Movie' "
                 "ORDER BY `release_year` ASC "
                 "LIMIT 100 ")

    data: list[dict] = []

    for each in db_connect('netflix.db', query_str):
        data.append({"title": each[1],
                     "release_year": each[2]})

    return data


def get_movies_by_category(category: str):
    """
    Реализуйте поиск по рейтингу.
    Определите группы:
        - для детей,
        - для семейного просмотра,
        - для взрослых.
    """

    categories: dict = {'children': 'G',
                        'family': ('G', 'PG', 'PG-13'),
                        'adult': ('R', 'NC-17')}

    query_str = ("SELECT `show_id`, `title`, `rating`, `description` "
                 "FROM netflix "
                 f"WHERE `rating` IN {categories[category]}")

    if len(categories[category]) == 1:
        query_str = ("SELECT `show_id`, `title`, `rating`, `description` "
                     "FROM netflix "
                     f"WHERE `rating` == '{categories[category]}'")

    data: list[dict] = []

    for row in db_connect('netflix.db', query_str):
        data.append({'title': row[1],
                     'rating': row[2],
                     'description': row[3].replace('\n', '')})

    return data


def get_movies_by_genre(genre: str) -> list:
    """
    Напишите функцию, которая получает название жанра в качестве аргумента
    и возвращает 10 самых свежих фильмов в формате json.
    Сперва напишите SQL запрос.
    Затем напишите функцию, которая принимала бы `жанр` и возвращала данные.

    :param genre: Жанр поиска.
    """

    data: list[dict] = []

    query_str = ("SELECT `show_id`, `title`, `description` "
                 "FROM netflix "
                 f"WHERE LOWER(`listed_in`) LIKE '%{genre.lower()}%' "
                 "AND `type`='Movie' "
                 "ORDER BY `release_year` DESC "
                 "LIMIT 10 ")

    for row in db_connect('netflix.db', query_str):
        data.append({"title": row[1],
                     "description": row[2].replace('\n', '')})

    return data


def get_cast_located_with_2_actors(actor_1: str, actor_2: str) -> list:
    """
    Напишите функцию, которая получает в качестве аргумента имена двух актеров,
    сохраняет всех актеров из колонки cast, и возвращает список тех,
    кто играет с ними в паре больше 2 раз.

    :param actor_1: Актёр 1.
    :param actor_2: Актёр 2.
    """

    query_str = ("SELECT `cast` "
                 "FROM netflix "
                 f"WHERE LOWER(`cast`) LIKE '%{actor_1.lower()}%' "
                 f"AND LOWER(`cast`) LIKE '%{actor_2.lower()}%' ")

    data: list[dict] = db_connect('netflix.db', query_str)

    result_list: list[str] = []
    requested_actors: list[str] = []

    for row in data:
        actors_list: list[str] = row[0].split(', ')
        result_list.extend(actors_list)

    actors: dict = Counter(result_list)

    for name, number in actors.items():
        if number > 2 and name not in (actor_1, actor_2):
            requested_actors.append(name)

    return requested_actors


def get_movies_by_multiple(type_: str, year_: int, genre_: str) -> list:
    """
    Напишите функцию, с помощью которой можно будет передавать:
     - **тип** картины (фильм или сериал),
     - **год выпуска** и ее
     - **жанр** и получать на выходе список названий картин с их описаниями в JSON.
    Сперва напишите SQL запрос, затем напишите функцию, которая принимала бы `тип, год, жанр`.

    """

    data: list[dict] = []

    query_str = ("SELECT `show_id`, `title`, `description` "
                 "FROM netflix "
                 f"WHERE LOWER(`type`) = '{type_.lower()}' "
                 f"AND `release_year` = {year_} "
                 f"AND LOWER(`listed_in`) LIKE '%{genre_.lower()}%' ")

    for each in db_connect('netflix.db', query_str):
        data.append({"title": each[1],
                     "description": each[2].replace('\n', '')})

    return data
