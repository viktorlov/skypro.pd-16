# Licensed under the Apache License, Version 2.0 (the "License");
# ----------------------------------------------------------------
# ok
# ----------------------------------------------------------------
from .auth import api as auth_ns
from .user import api as user_ns

__all__ = [
    'auth_ns',
    'user_ns',
]
