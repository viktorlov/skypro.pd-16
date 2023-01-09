#
# Напишите вьюшку для запросов /get-some/<number> которая возвращает указанное количество букв или - если передан 0.
#
from flask import Flask, render_template

from data import alphabet

PORT = 5005

app = Flask(__name__)


@app.route('/')
def page_index():
    return render_template('index.html')


@app.route('/get_some/<int:number>/')
def page_get_some(number):
    arg = '-'
    if number in range(1, len(alphabet)):
        arg = alphabet[0:number]
    if number >= len(alphabet):
        arg = alphabet
    return render_template('get_some.html', arg=arg)


if __name__ == '__main__':
    app.run(debug=True, port=PORT)
