class Player:

    def __init__(self, name):
        if len(name) < 2:
            raise ValueError("Имя должно содержать по крайне мере 2 символа")
        self.name = name
        self.points = 0

    def change_name(self, new_name):
        if len(new_name) < 2:
            raise ValueError("Имя должно содержать по крайне мере 2 символа")
        self.name = new_name

    def add_points(self, number):
        if number <= 0:
            raise ValueError("Добавить можно неотрицательное число очков")
        if type(number) not in (int, float):
            raise TypeError("Очки должны быть числом")
        self.points += number

    def get_points(self):
        return self.points
