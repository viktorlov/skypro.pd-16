# Licensed under the Apache License, Version 2.0 (the "License");
# ----------------------------------------------------------------
# ok
# ----------------------------------------------------------------
from config import config
from server import create_app
from setup.db import db

if __name__ == '__main__':
    with create_app(config).app_context():
        db.drop_all()
        db.create_all()
