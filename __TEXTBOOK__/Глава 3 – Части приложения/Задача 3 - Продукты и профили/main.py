from flask import Flask, request

from products.views import products
from profiles.views import profiles

app = Flask(__name__)

app.register_blueprint(products, url_prefix='/products')
app.register_blueprint(profiles, url_prefix='/profiles')

@app.route('/')
def index():
    return f'{request.url}'

@app.errorhandler(404)
def error_404(error):
    return f'{request.url} Упало с ошибкой четыре сотни четыре', 404

if __name__ == '__main__':
    HOST = '127.0.0.3'
    PORT = 5003
    app.run(host=HOST, port=PORT, debug=True)
