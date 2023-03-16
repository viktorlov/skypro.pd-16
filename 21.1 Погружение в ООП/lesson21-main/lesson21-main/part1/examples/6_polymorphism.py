print('В данном примере видно, что класс с удобным интерфейсом можно использовать для реализации внутреннего объема '
      'как бензобака машины, так и для реализации банки варенья.\n')
print('\nТак же благодаря тому что и банка и бак машины поддерживают одинаковый интерфейс можно заставить бабушку '
      'мееедленно нацедить варенья в бак автомобиля и никаких сложностей не возникнет.\n')


class Tank:
    def __init__(self, capacity, fullness):
        self.capacity = capacity
        self.fullness = fullness
        self.is_open = False

    def open(self):
        self.is_open = True

    def close(self):
        self.is_open = False

    def check(self):
        return not self.is_open

    def fill(self, volume):
        if not self.is_open: raise Exception('Емкость закрыта')
        while self.capacity >= self.fullness + volume:
            print(f'В емкости {self.fullness}')
            self.fullness += volume
        print(f'В емкости {self.fullness}')

    def clear(self):
        self.fullness = 0


class Car:
    def __init__(self):
        self.tank = Tank(capacity=10, fullness=1)

    def fill(self, source):
        print('Заправка автомобиля начата')
        self.tank.open()
        self.tank.fill(source.get_volume())
        self.tank.close()
        assert self.tank.check(), True

    def clear(self):
        self.tank.clear()


class JamJar:
    def __init__(self):
        self.tank = Tank(capacity=1, fullness=0.1)

    def fill(self, source):
        print('Старая бабушка начала переливать варенье')
        self.tank.open()
        self.tank.fill(source.get_volume())
        self.tank.close()
        assert self.tank.check(), True

    def clear(self):
        self.tank.clear()


class Resource:
    def __init__(self):
        self.volume = 0

    def get_volume(self):
        return self.volume


class GasStation(Resource):
    def __init__(self):
        super(GasStation, self).__init__()
        self.volume = 2


class GrandMa(Resource):
    def __init__(self):
        super(GrandMa, self).__init__()
        self.volume = 0.1


gas_station = GasStation()
grand_ma = GrandMa()
car = Car()
jar = JamJar()
car.fill(gas_station)
print('=' * 20)
jar.fill(grand_ma)

print('\n В дело идет бабушка')
print('=' * 20)
car.clear()
car.fill(grand_ma)
