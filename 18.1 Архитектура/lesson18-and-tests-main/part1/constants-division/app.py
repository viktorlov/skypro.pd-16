# У вас есть приложение с использованием REST X, 
# где все views, а также модель находятся в одном файле. 
# 
# Необходимо сделать рефакторинг архитектуры приложения.
# Структура приложения должна быть следующего вида:
#
# constants-division
# ├── ./app.py       - Основной фаил, здесь инициализируется приложение
# ├── ./constants.py - В этот файл переместите константы
# ├── ./models.py    - В этот фаил переместите модели
# ├── ./setup_db.    - в этом файле инициализируйте базу данных для Flask
# ├── ./test.py      - Это наши тесты, запустите после самостоятельной проверки
# └── ./views
#     ├── ./views/files.py        - В эти фаилы переместите необходимые
#     └── ./views/smartphones.py    для работы class based views.
# 
# Требования к выполнению задания:
# - Приложение должно соответствовать структуре выше.
# - В файле app.py не должно быть лишних переменных.
# - Приложение должно запускаться.
# - Запрос на эндпоинт должен возвращать корректный код.
#
# Менять значения, возвращаемые view-функциями, 
# а также url-адреаса в данном задании не требуется.
# Также задание содержит упрощенный вариант сериализации/десериализации
# которым мы пользуемся только в учебных целях для сокращения объема кода.


from flask import Flask
from flask_restx import Api

from models import SmartPhone, File
from setup_db import db
from views.files import files_ns
from views.smartphones import smartphones_ns


def create_app() -> Flask:
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    configure_app(app)
    return app


def configure_app(app: Flask) -> None:
    db.init_app(app)
    api = Api(app)
    api.add_namespace(smartphones_ns)
    api.add_namespace(files_ns)
    load_data(app)


def load_data(app):
    with app.app_context():
        db.create_all()
        f1 = File(id=1, name='config.cfg', path='/var/', size=500)
        f2 = File(id=2, name='run.exe', path='/var/lib/', size=500)
        sp1 = SmartPhone(id=1, name="iphone", price=100000)
        sp2 = SmartPhone(id=2, name="android", price=110000)
        with db.session.begin():
            db.session.add_all([f1, f2])
            db.session.add_all([sp1, sp2])


app = create_app()

if __name__ == '__main__':
    app.run(host="localhost", port=10001, debug=True)
