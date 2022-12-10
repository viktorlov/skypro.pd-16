from flask import Flask

app = Flask(__name__)
records = []


@app.route('/', )
def page_index():
    return "index.html"


@app.route('/add/<arg>', )
def page_add(arg):
    records.append(arg)
    return f'Слово {arg} добавлено в список'


@app.route('/show/', )
def page_show():
    return str(', '.join(records))


app.run()
