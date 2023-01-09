from flask import Flask, request

from api.views import api
from pages.views import pages

app = Flask(__name__)

app.register_blueprint(api, url_prefix='/api/products')
app.register_blueprint(pages, url_prefix='/products')


@app.route('/')
def index():
    return f'{request.url}', 200


@app.errorhandler(404)
def error_404(error):
    return f'{request.url} Упало с ошибкой четыре сотни четыре', 404


if __name__ == '__main__':
    HOST = '127.0.0.5'
    PORT = 5005
    app.run(host=HOST, port=PORT, debug=True)
