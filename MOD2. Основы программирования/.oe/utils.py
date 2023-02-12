import random

import requests

from basic_word import BasicWord


def load_random_word(words_url):
    """
    The function receives a list of words from an external resource,
    picks a random word creates an instance of the `BasicWord` class.
    :return: an instance of the `BasicWord` class
    """
    dict_words_json = requests.get(words_url)
    dict_words = dict_words_json.json()
    random_word = [word for word in dict_words]
    random.shuffle(random_word)
    basic_word = [BasicWord(word['word'], word['subwords']) for word in random_word]
    return basic_word[0]

