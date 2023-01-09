#
# Напишите вьюшку для запросов /between/?from=<letter>&to=<letter> ,
#   которая возвращает буквы в промежутке между указанными в любом направлении
#   или прочерк, если между указанными буквами ничего нет.
#
from flask import Flask, render_template, request

from data import alphabet

PORT = 5004

app = Flask(__name__)


@app.route('/')
def page_index():
    return render_template('index.html')


@app.route('/between/')
def page_letter():
    from_S = request.args.get('from')
    to_S = request.args.get('to')
    from_I = int(alphabet.find(from_S))
    to_I = int(alphabet.find(to_S))

    if all([from_S.isalpha(), to_S.isalpha(), abs(to_I - from_I) != 0]):
        arg = alphabet[min([from_I, to_I]):max([from_I, to_I])+1]
    else:
        arg = '-'
    return render_template('between.html', arg=arg)


if __name__ == '__main__':
    app.run(debug=True, port=PORT)
