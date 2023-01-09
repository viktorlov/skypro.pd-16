from flask import Flask

from letteric.views import letteric
from numeric.views import numeric

app = Flask(__name__)

app.register_blueprint(letteric, url_prefix='/letteric')
app.register_blueprint(numeric, url_prefix='/numeric')

if __name__ == '__main__':
    HOST = '127.0.0.1'
    PORT = 5001
    app.run(host=HOST, port=PORT, debug=True)
