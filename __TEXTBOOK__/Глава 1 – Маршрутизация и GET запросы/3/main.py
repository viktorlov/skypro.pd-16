#
# Напишите вьюшку для запросов  /check/<letter>/<word> для проверки соответствия буквы ее расшифровке.
#
from flask import Flask, render_template

from data import alphabet

PORT = 5003

app = Flask(__name__)


@app.route('/')
def page_index():
    return render_template('index.html')


@app.route('/check/<string:letter>/<string:word_S>')
def page_check(letter, word_S):
    try:
        word_D = alphabet[letter.upper()]
    except KeyError:
        word_D = "Not a letter"
    sign = word_D == word_S
    return render_template('check.html', arg=sign)


if __name__ == '__main__':
    app.run(debug=True, port=PORT)
