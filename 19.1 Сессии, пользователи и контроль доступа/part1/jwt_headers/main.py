# Напишите декоратор `auth_required` который проверяет 
# наличие в запросе заголовка 
# Authorization (содержание заголовка может быть любым)
from flask import Flask, request, abort

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.url_map.strict_slashes = False


def auth_required(func):
    def wrapper():
        if "Authorization" not in request.headers:
            abort(401)
        return func()

    return wrapper


@app.route("/")  # Для самопроверки запустите приложение
@auth_required  # и попробуйте отправить GET-запросы
def get_page():  # C заголовком Authorization и без
    return "", 200


if __name__ == "__main__":
    app.run()
