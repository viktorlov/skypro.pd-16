#
# Напишите вьюшку для запросов типа /letter/<letter>, которая возвращает букву.
#
from flask import Flask, render_template

from data import alphabet

PORT = 5001

app = Flask(__name__)


@app.route('/')
def page_index():
    return render_template('index.html')


@app.route('/letter/<string:letter>')
def page_letter(letter):
    try:
        word = alphabet[letter.upper()]
    except KeyError:
        word = "Not a letter"
    return render_template('letter.html', arg=word)


if __name__ == '__main__':
    app.run(debug=True, port=PORT)
