class BasicWord:
    """
    Создаёт и инициализирует класс <BasicWord>.

    Поля:
        - исходное слово,
        - набор допустимых подслов.
    Методы:
        - проверка введенного слова в списке допустимых подслов (вернет bool),
        - подсчет количества подслов (вернет int).
    """

    def __init__(self, word: str, subwords: list[str]):
        self.word = word
        self.subwords = subwords

    def __repr__(self):
        return "<BasicWord>"

    def is_correct(self, arg: str):
        return arg in self.subwords

    def subwords_count(self):
        return len(self.subwords)
