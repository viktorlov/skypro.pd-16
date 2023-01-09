from flask import Flask

from stats.views import stats
from users.views import users

app = Flask(__name__)

app.register_blueprint(stats, url_prefix='/stats')
app.register_blueprint(users, url_prefix='/users')

if __name__ == '__main__':
    HOST = '127.0.0.2'
    PORT = 5002
    app.run(host=HOST, port=PORT, debug=True)