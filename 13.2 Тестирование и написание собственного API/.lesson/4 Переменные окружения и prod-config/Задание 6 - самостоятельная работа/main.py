import os

import dotenv
from flask import Flask

from ehs.ehs import ehs

app = Flask(__name__)

app.register_blueprint(ehs, url_prefix='/')

dotenv.load_dotenv(override=True)
location = os.environ.get('LOCATION')


@app.get('/', )
def index():
    if location == 'home':
        return f"Приложение запушено на домашнем сервере"
    if location == 'work':
        return f"Приложение запушено на рабочем сервере"


if __name__ == '__main__':
    app.run(debug=True)
