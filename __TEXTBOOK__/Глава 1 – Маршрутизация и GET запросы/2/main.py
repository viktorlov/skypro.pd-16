#
# Напишите вьюшку для запросов типа /find/?letter=<letter>, которая возвращает букву на основе квери-параметра.
#
from flask import Flask, render_template, request

from data import alphabet

PORT = 5002

app = Flask(__name__)


@app.route('/')
def page_index():
    return render_template('index.html')


@app.route('/find/')
def page_letter():
    letter = request.args.get('letter')
    try:
        word = alphabet[letter.upper()]
    except KeyError:
        word = "Not a letter"
    return render_template('letter.html', arg=word)


if __name__ == '__main__':
    app.run(debug=True, port=PORT)
