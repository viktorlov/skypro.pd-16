from flask import Flask

app = Flask(__name__)
words = {"one": "один", "two": "два", "three": "три"}


@app.route('/', )
def page_index():
    return "index.html"


@app.route('/one/', )
def page_one():
    return str(words['one'])


@app.route('/two/', )
def page_two():
    return str(words['two'])


@app.route('/three/', )
def page_three():
    return str(words['three'])


app.run()
