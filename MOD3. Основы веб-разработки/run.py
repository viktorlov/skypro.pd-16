from flask import Flask

from app.bp_api.bp_api_views import api_blueprint
from app.bp_errorhandlers.bp_errorhandlers_views import errorhandlers
from app.bp_posts.bp_posts_views import posts_blueprint

app = Flask(__name__)

app.config.from_pyfile('config/config.py')

app.register_blueprint(errorhandlers)
app.register_blueprint(api_blueprint)
app.register_blueprint(posts_blueprint)

if __name__ == '__main__':
    app.run(host=app.config.get('HOST'),
            port=app.config.get('PORT'),
            debug=app.config.get('DEBUG'))
