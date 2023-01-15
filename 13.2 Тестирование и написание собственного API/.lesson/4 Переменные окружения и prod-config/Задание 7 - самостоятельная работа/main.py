import os
from datetime import datetime

import dotenv
from flask import Flask, jsonify

from ehs.ehs import ehs  # blueprint "перехватчик ошибок"

app = Flask(__name__)

app.register_blueprint(ehs, url_prefix='/')

dotenv.load_dotenv(override=True)

if os.environ.get("APP_CONFIG") == "development":
    app.config.from_pyfile('config/development.py')
if os.environ.get("APP_CONFIG") == "production":
    app.config.from_pyfile('config/production.py')

title = app.config.get("TITLE")
description = app.config.get("DESCRIPTION")


@app.get('/')
def index():
    return jsonify({"ЧТО": f"{description}",
                    "ГДЕ": f"{title}",
                    "КОГДА": f"{datetime.now()}"})


if __name__ == '__main__':
    app.run(debug=app.config.get('DEBUG'),
            port=app.config.get('PORT'),
            host=app.config.get('HOST'))
