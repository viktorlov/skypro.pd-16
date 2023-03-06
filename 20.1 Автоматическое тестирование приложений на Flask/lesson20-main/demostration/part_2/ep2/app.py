from unittest.mock import MagicMock


class ProductionClass:
    def m1(self):
        print("m1")

    def m2(self):
        print("m2")


if __name__ == '__main__':
    pc = ProductionClass()
    pc.m1 = MagicMock(return_value="123")
    print(pc.m1())

    pc.m2 = MagicMock(side_effect=Exception("oh no"))
    pc.m2()
