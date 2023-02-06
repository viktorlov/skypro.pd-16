# Cоздание таблицы
#
# Дана схема таблицы пациентов ветеринарной клиники:
#
# Id — идентификатор карты
# AnimalType — вид животного
# Sex — пол животного
# Name — кличка
# DateOfBirth — дата рождения
# Age — возраст (полных лет)
# Weight — вес (килограммы + граммы)
#
#
# Создайте таблицу в БД на основе этой схемы
import sqlite3
import prettytable

con = sqlite3.connect(":memory:")
cur = con.cursor()
sqlite_query = ("CREATE TABLE animals ("
                "Id INTEGER PRIMARY KEY AUTOINCREMENT, "
                "AnimalType VARCHAR(50) NOT NULL, "
                "Sex VARCHAR(10), "
                "Name VARCHAR(50) NOT NULL DEFAULT 'Noname', "
                "DateOfBirth DATE,"
                "Age INTEGER,"
                "Weight DECIMAL)")  # TODO составьте запрос на создание таблицы

# Не удаляйте код ниже, он используется
# для вывода заголовков созданной таблицы


def print_result(sqlite_query):
    cur.execute(sqlite_query)
    result_query = 'SELECT * FROM animals'
    table = cur.execute(result_query)
    mytable = prettytable.from_db_cursor(table)
    mytable.max_width = 30
    print(mytable)


if __name__ == '__main__':
    print_result(sqlite_query)
