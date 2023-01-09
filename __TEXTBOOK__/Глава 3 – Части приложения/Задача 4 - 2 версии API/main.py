from flask import Flask, request

from api_1.views import api_1
from api_2.views import api_2

app = Flask(__name__)

app.register_blueprint(api_1, url_prefix='/api/1')
app.register_blueprint(api_2, url_prefix='/api/2')


@app.route('/')
def index():
    return f'{request.url}', 200


@app.errorhandler(404)
def error_404(error):
    return f'{request.url} Упало с ошибкой четыре сотни четыре', 404


if __name__ == '__main__':
    HOST = '127.0.0.4'
    PORT = 5004
    app.run(host=HOST, port=PORT, debug=True)
