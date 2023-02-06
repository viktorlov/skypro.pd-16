### импортируем специальную библиотеку для подключения к базам данных
import psycopg2

### импортируем из файла to_ken.py информацию для подключения
from to_ken import to_ken

### устанавливаем соединение с базой данных forges14
connection = psycopg2.connect(database=to_ken['db_name'],
                              user=to_ken['db_user'],
                              password=to_ken['db_password'],
                              host=to_ken['db_host'],
                              port=to_ken['db_port'])

### создаём специальный метод для парсинга данных из базы данных
cursor = connection.cursor()

### пишем запрос на SQL, и выполняем его с помощью созданного метода
### берём данные из таблицы film
query = """SELECT * FROM grocery"""
cursor.execute(query)

### парсим все данные по нашему запросу
groceries = cursor.fetchall()

print(groceries)
