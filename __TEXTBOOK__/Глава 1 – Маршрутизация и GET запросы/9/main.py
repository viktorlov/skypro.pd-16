#
# Напишите вьюшку для запросов /get/?len=<length>
#   которая возвращает все слова указанной длины.
#   Если таких слов нет – напишите 404.
#
from flask import Flask, render_template, request, abort

from data import alphabet

PORT = 5009

app = Flask(__name__)


@app.route('/')
def page_index():
    return render_template('index.html')


@app.route('/get/')
def page_get():
    length_to_search = int(request.args.get('len'))
    string_to_output = *[_ for _ in alphabet.values() if len(_) == length_to_search],
    if len(string_to_output) == 0:
        abort(404)
    return render_template('get.html', arg=string_to_output)


if __name__ == '__main__':
    app.run(debug=True, port=PORT)
