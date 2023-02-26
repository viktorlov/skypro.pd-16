from flask import Flask

from config import Config

app = Flask(__name__)

app.config.from_object(Config)


@app.get('/')
def foo():
    return f'{Config.TITLE}<br>{Config.DESCRIPTION}'


if __name__ == '__main__':
    app.run()