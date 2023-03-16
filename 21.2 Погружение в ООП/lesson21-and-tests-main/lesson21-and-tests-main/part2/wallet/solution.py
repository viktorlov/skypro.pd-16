class Wallet:
    def __init__(self, gold=0, silver=0, bronze=0):
        self.gold = gold
        self.silver = silver
        self.bronze = bronze

    def bronze_converter(self):
        silver = 0
        gold = 0
        if self.silver:
            silver = self.silver * 100
        if self.gold:
            gold = self.gold * 1000
        return self.bronze + silver + gold

    def __repr__(self):
        return f'З: {self.gold}, С: {self.silver}, Б: {self.bronze}'

    def __eq__(self, other):
        return self.bronze_converter() == other.bronze_converter()

    def __ne__(self, other):
        return self.bronze_converter() != other.bronze_converter()

    def __gt__(self, other):
        return self.bronze_converter() > other.bronze_converter()

    def __ge__(self, other):
        return self.bronze_converter() >= other.bronze_converter()

    def __lt__(self, other):
        return self.bronze_converter() < other.bronze_converter()

    def __le__(self, other):
        return self.bronze_converter() <= other.bronze_converter()