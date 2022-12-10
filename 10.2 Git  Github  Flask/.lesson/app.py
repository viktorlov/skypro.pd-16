from flask import Flask

app = Flask(__name__)


@app.route("/")
def page_index():
    return "Главная страничка"


@app.route("/profile/")
def page_profile():
    return "Профиль пользователя"


@app.route("/feed/")
def page_feed():
    return "Лента пользователя"


@app.route("/messages/")
def page_messages():
    return "Сообщения пользователя"


@app.route('/users/<uid>')
def page_profile_users(uid):
    return f'<h1>Профиль {uid}</h1>'


@app.route('/catalog/items/<itemid>')
def page_profile_items(itemid):
    return f'<h1>Страничка товара {itemid}</h1>'


if __name__ == "__main__":
    app.run()
