#
# Напишите вьюшку для запросов /get-some/page/<page_number>
#   которая выводила бы по пять элементов, причем, если страница не указана,
#   выводятся первые 5 элементов, если же для указанной страницы не хватает элементов,
#   возвращается статус-код 404.
#
from flask import Flask, render_template, abort

from data import alphabet

PORT = 5007

app = Flask(__name__)


@app.route('/')
def page_index():
    return render_template('index.html')


@app.route('/get_some/')
def page_get_some():
    return render_template('get_some.html', arg=alphabet[0:5])


@app.route('/get_some/page/<int:number>')
def page_page(number):
    if number > 1 + len(alphabet) // 5:
        raise abort(404)
    to_ = number * 5
    from_ = to_ - 5
    return render_template('get_some.html', arg=alphabet[from_:to_])


if __name__ == '__main__':
    app.run(debug=True, port=PORT)
