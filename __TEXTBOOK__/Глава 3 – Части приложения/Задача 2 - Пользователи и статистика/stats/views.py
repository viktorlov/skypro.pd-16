from flask import Blueprint

stats = Blueprint('stats', __name__)


@stats.get('/users/')
def get():
    from stats.utils import count_users
    return count_users()
