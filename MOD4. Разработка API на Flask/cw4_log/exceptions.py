# Licensed under the Apache License, Version 2.0 (the "License");
# ----------------------------------------------------------------
# ok
# ----------------------------------------------------------------
class BaseServiceError(Exception):
    code = 500


class ItemNotFound(BaseServiceError):
    code = 404
