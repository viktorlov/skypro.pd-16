from logistic_classes import Shop, Store, Request

if __name__ == '__main__':
    shop = Shop()
    shop.add("печеньки", 5)
    shop.add("вафли", 5)
    shop.add("помидоры", 5)
    shop.add("сок", 5)
    store = Store()
    store.add("печеньки_5", 5)

    user_str = input()
    user_str_list = user_str.split(" ")
    try:
        user_str_list[1] = int(user_str_list[1])
    except:
        print("введите число")
    if ("забрать" and "доставить") not in user_str_list[0].lower():
        print("Введите 'забрать/доставить'")
    elif ("магазин" and "склад") not in user_str_list[4].lower():
        print("введите место назначения")
    else:
        r = Request(user_str)
        print(r)
        if "магазин" in r.from_:
            print("Доставка возможна только со склада")
        elif "склад" in r.from_:
            if r.product in store.get_item():
                if r.amount <= store.get_item()[r.product]:
                    print("Нужное количество есть на складе")
                    print("Курьер везет со склад в магазин")
                    if sum(shop.get_item().values()) + int(r.amount) < shop.capacity:
                        print(f"Курьер доставил {r.amount} {r.product} в магазин")
                        store.remove(r.product, r.amount)
                        shop.add(r.product, r.amount)

                    else:
                        print("В магазин недостаточно места, попобуйте что-то другое")
                else:
                    print("Не хватает на складе, попробуйте заказать меньше")
            else:
                print("Такого товара нет на складе")

        print("В магазине хранится:")
        for key, value in shop.items.items():
            print(key, value)

        print("На складе хранится:")
        for key, value in store.items.items():
            print(key, value)
