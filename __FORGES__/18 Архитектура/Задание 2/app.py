from flask import Flask

from config import Config
from views.views import index

app = Flask(__name__)

app_config = Config()
app.config.from_object(app_config)

app.register_blueprint(index)

if __name__ == '__main__':
    app.run()
