import os
from pathlib import Path

BASE_DIR: Path = Path(__file__).resolve().parent

LOGS_FOLDER: Path = BASE_DIR.joinpath('logs')

PORT = 5016
HOST = "127.0.0.16"

class Config(object):
    DEBUG = True
    SECRET_KEY = os.urandom(12)
    JSON_SORT_KEYS = False
    JSON_AS_ASCII = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///lesson.db"
