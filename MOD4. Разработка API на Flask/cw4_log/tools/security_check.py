# Licensed under the Apache License, Version 2.0 (the "License");
# ----------------------------------------------------------------
# ok
# ----------------------------------------------------------------
from run import app
from security import __generate_password_digest, generate_password_hash, compare_password

password_row: str = 'qwertyuiop'
password_bites: bytes = b'4\xb7E\xfc\xba,\xcar\xf9X\x85\xb4\xa1\x8f\xeb\xcf\xa5\x16cI\xaaT8\xb7|*V\xb8;\xbd@o'
password_hash: str = 'NLdF/LosynL5WIW0oY/rz6UWY0mqVDi3fCpWuDu9QG8='

if __name__ == '__main__':
    with app.app_context():
        print(__generate_password_digest(password_row))
        print(generate_password_hash(password_row))
        print(compare_password(password_hash,
                               password_row))

        pHa = "cervidae"  # harry
        pRo = "terrier"  # ron
        pHe = "lutra"  # hermione
        pDi = 'phoenix'  # director

        for each in (pHa, pRo, pHe, pDi):
            print(f'{each}: {generate_password_hash(each)}')
