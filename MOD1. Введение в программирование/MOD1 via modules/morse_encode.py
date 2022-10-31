import json
import requests

url = 'https://gist.githubusercontent.com/mohayonao/094c71af14fe4791c5dd/raw/8399262545d0d88507ce42069b0b50043f0eddbc/morse-code.json'
morse_code = json.loads(requests.get(url).text)


def morse_encode(arg):
    """
    функция для кодировки английских слов (и фраз) в азбуку Морзе
    """
    return ' '.join([' ' if letter == ' ' else morse_code[letter.lower()] for letter in str(arg)])
