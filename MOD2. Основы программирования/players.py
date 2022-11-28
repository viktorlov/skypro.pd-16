class Player:
    """
    Создаёт и инициализирует класс <Player>.

    Поля:
        - имя пользователя,
        - использованные слова пользователя.
    Методы:
        - получение количества использованных слов (возвращает int);
        - добавление слова в использованные слова (ничего не возвращает);
        - проверка использования данного слова до этого (возвращает bool).
    """

    def __init__(self, name: str, used_words=None):
        if used_words is None:
            used_words: list[str] = []
        self.name = name
        self.used_words = used_words

    def __repr__(self):
        return "<Player>"

    def get_count_used_words(self):
        return len(self.used_words)

    def add_used_word(self, word: str):
        self.used_words.append(word)

    def check_word(self, word: str):
        return word in self.used_words
