from clases.verificar_entrada import check_user_input


class UserRequest:
    """
    Класс запрос пользователя
    Пример: <<Доставить 3 печеньки со склада в магазин>>
    """

    def __init__(self, user_request):
        self._data = check_user_input(user_request)
        self.amount_ = self._data.get('amount')
        self.product_ = self._data.get('product')
        self.from_ = self._data.get('from')
        self.to_ = self._data.get('to')

    def __repr__(self):
        return f'From - {self.from_}' \
               f'\nTo - {self.to_}' \
               f'\nProduct - {self.product_}' \
               f'\nAmount - {self.amount_}'

    def get_data(self):
        return {'amount': self.amount_,
                'product': self.product_,
                'from': self.from_,
                'to': self.to_
                }
