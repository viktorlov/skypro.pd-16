#
# Напишите вьюшку для запросов /search/?s=<s> которая бы выводила слова,
#   в которых содержится указанная подстрока. Если ничего не нашлось – верните 404.
#
from flask import Flask, render_template, request, abort

from data import alphabet

PORT = 5008

app = Flask(__name__)


@app.route('/')
def page_index():
    return render_template('index.html')


@app.route('/search/')
def page_search():
    string_to_search = request.args.get('s').lower()
    string_to_output = *[_ for _ in alphabet.values() if string_to_search in _.lower()],
    if len(string_to_output) == 0:
        abort(404)
    return render_template('search.html', arg=string_to_output)


if __name__ == '__main__':
    app.run(debug=True, port=PORT)
