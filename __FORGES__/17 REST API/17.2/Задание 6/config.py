class ProjectConfig(object):
    DEBUG = True
    HOST = '127.0.0.66'
    PORT = 10066
    RESTX_JSON = {'ensure_ascii': False}
    JSON_SORT_KEYS = False
    JSON_AS_ASCII = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"
