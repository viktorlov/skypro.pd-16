# Licensed under the Apache License, Version 2.0 (the "License");
# ----------------------------------------------------------------
# ok
# ----------------------------------------------------------------
from .auth import auth_ns, user_ns
from .main import genres_ns, directors_ns, movies_ns, favorites_ns

__all__ = [
    'auth_ns',
    'genres_ns',
    'directors_ns',
    'movies_ns',
    'user_ns',
    'favorites_ns'
]
