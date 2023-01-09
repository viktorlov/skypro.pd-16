#
# Напишите вьюшку для запросов `/letters` с  аргументами:
# `limit` – количество
# `offset` - отступ
# `sort` - порядок (asc / desc)
#
# Каждый из аргументов является необязательным.
#

from flask import Flask, render_template, request, abort

from data import alphabet

PORT = 5010

app = Flask(__name__)


@app.route('/')
def page_index():
    return render_template('index.html')


@app.route('/get/')
def page_get():
    if request.args.get('limit') is None:
        limit_ = 26
    else:
        try:
            limit_ = int(request.args.get('limit'))
            if limit_ > len(alphabet):
                raise ValueError
        except ValueError:
            abort(404)

    if request.args.get('offset') is None:
        offset_ = 0
    else:
        try:
            offset_ = int(request.args.get('offset'))
            if offset_ > len(alphabet):
                raise ValueError
        except ValueError:
            abort(404)

    if request.args.get('sort') is None:
        sort_ = 'asc'
    else:
        try:
            sort_ = request.args.get('sort')
            if sort_ not in ["asc", "desc"]:
                raise ValueError
        except ValueError:
            abort(404)
    if sort_ == 'desc':
        string_to_output = alphabet[::-1][offset_: offset_ + limit_]
    else:
        string_to_output = alphabet[offset_: offset_ + limit_]
    return render_template('get.html', arg=string_to_output)


@app.errorhandler(404)
def page_error_404(error):
    return f'Ошибка 404 по адресу {request.url}'


if __name__ == '__main__':
    app.run(debug=True, port=PORT)
