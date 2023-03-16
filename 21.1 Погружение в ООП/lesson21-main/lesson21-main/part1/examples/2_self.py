print('self - обращение к переменным и методам конкретного объекта')


class SomeClass:
    def __init__(self, var1: str, var2: str):
        self.var1 = var1
        self.var2 = var2

    def print(self) -> None:
        print(self._concat())

    def _concat(self) -> str:
        return f'{self.var1} {self.var2}'


cats = SomeClass(var1='слава', var2='котикам')
foxes = SomeClass(var1='позор', var2='лисичкам')
cats.print()
foxes.print()

print('\nПри модификации одного из методов с хорошим или злым умыслом - остальные объекты не пострадают\n')


def sabotage(*args, **kwargs):
    return 'саботаж'


foxes._concat = sabotage

cats.print()
foxes.print()

print('\nНо при этом в самом классе шаблон метода остался без изменений\n')

dogs = SomeClass(var1='позор', var2='песикам')
dogs.print()
