# Licensed under the Apache License, Version 2.0 (the "License");
# ----------------------------------------------------------------
# ok
# ----
from .directors import api as directors_ns
from .favorites import api as favorites_ns
from .genres import api as genres_ns
from .movies import api as movies_ns

__all__ = [
    'genres_ns',
    'directors_ns',
    'movies_ns',
    'favorites_ns',
]
