class Config(object):
    """
    Создание класса-конфигуратора.
    """
    DEBUG = True
    HOST = '127.0.0.18'
    PORT = 10018
    SQLALCHEMY_DATABASE_URI = 'sqlite:///./movies.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False