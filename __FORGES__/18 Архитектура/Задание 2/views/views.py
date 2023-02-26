from flask import current_app as app, Blueprint

index = Blueprint('index', __name__)


@index.get('/')
def foo():
    return f'{app.config["TITLE"]}<br>{app.config["DESCRIPTION"]}'
