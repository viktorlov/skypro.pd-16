#
# Напишите вьюшку для запросов /get-some/?limit=<limit>&offset=<offset>,
#   которая возвращает указанное количества с указанной позиции.
#   Если с таким отступом ничего нет или лимит нулевой – возвращает “-”.
#
from flask import Flask, render_template, request

from data import alphabet

PORT = 5006

app = Flask(__name__)


@app.route('/')
def page_index():
    return render_template('index.html')


@app.route('/get_some/')
def page_letter():
    limit = int(request.args.get('limit'))
    offset = int(request.args.get('offset'))
    arg = alphabet[offset:offset+limit]
    return render_template('get_some.html', arg=arg)


if __name__ == '__main__':
    app.run(debug=True, port=PORT)
