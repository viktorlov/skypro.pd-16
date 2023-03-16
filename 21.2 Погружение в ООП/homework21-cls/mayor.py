from clases import UserRequest, Shop, Store
from realizar_movimientos import moves, print_all


def función_principal():
    store = Store()
    shop = Shop()

    print("""
    Формат запроса: 'Доставить 1 яблоко со склада в магазин'.
    Товар должен быть в именительном падеже и единственном числе, например: 'яблоко', 'кабачок'.
    """)

    print_all(shop, store)

    while 1:

        user_input = input(f'\nВведите запрос (salida для выхода) ')

        _break = (
            'salida', 'ыфдшвф',
            'exit', 'учше',
            'выход', 'ds[jl',
            'стоп', 'cnjg',
            'stop', 'ыещз',
        )
        if user_input.lower() in _break:
            break

        try:
            request = UserRequest(user_input)
        except Exception as e:
            print('Wrong request >>> ', e)
        else:
            moves(request, shop, store)


if __name__ == "__main__":
    función_principal()
