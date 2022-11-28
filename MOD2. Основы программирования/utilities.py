from random import shuffle, randint

from requests import get

from basic_word import BasicWord


def load_random_word(arg: str):
    """
    Функция, которая:
        - получит список слов с внешнего ресурса,
        - выберет случайное слово,
        - создаст экземпляр класса `BasicWord`,
        - вернет этот экземпляр.

    :param arg: ссылка на json-файл
    :type arg: str
    :return: объект класса <BasicWord>
    :rtype: BasicWord
    """
    words_dictionary = get(arg).json()
    shuffle(words_dictionary)
    i = randint(0, len(words_dictionary) - 1)
    basic_word = BasicWord(word=words_dictionary[i]['word'],
                           subwords=words_dictionary[i]['subwords'])
    return basic_word
