# Licensed under the Apache License, Version 2.0 (the "License");
# ----------------------------------------------------------------
# ok
# ----------------------------------------------------------------
from contextlib import suppress
from typing import Any, Dict, List, Type

from sqlalchemy.exc import IntegrityError

from config import config
from models import Genre, Director, Movie, User
from server import create_app
from setup.db import db, models
from utils import read_json, debug


@debug
def load_data(data: List[Dict[str, Any]], model: Type[models.Base]) -> None:
    for item in data:
        item['id'] = item.pop('pk')
        db.session.add(model(**item))


@debug
def load_user(data: List[Dict[str, Any]], model: Type[models.Base]) -> None:
    for item in data:
        db.session.add(model(**item))


if __name__ == '__main__':
    fixtures: Dict[str, List[Dict[str, Any]]] = read_json("fixtures.json")

    app = create_app(config)

    with app.app_context():
        load_data(fixtures['genres'], Genre)
        load_data(fixtures['directors'], Director)
        load_data(fixtures['movies'], Movie)
        load_user(fixtures['users'], User)

        with suppress(IntegrityError):
            db.session.commit()
