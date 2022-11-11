fish = [

    {"specie": "Белуга", "water": "fresh"},
    {"specie": "Карась", "water": "fresh"},
    {"specie": "Красноперка", "water": "fresh"},
    {"specie": "Морской окунь", "water": "sea"},
    {"specie": "Тунец", "water": "sea"},
    {"specie": "Скумбрия", "water": "sea"},

]


def get_fish(arg):
    for element in fish:
        if element["specie"] == arg:
            element_specie = element['specie']
            element_water = element['water']

    return element_specie, element_water


# Не удаляйте код ниже, он нужен для проверки!
fish_name = input()
fish_, water_ = get_fish(fish_name)
print(fish_, water_)
