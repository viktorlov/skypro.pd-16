from random import randint

from flask import Flask

app = Flask(__name__)


@app.route('/', )
def page_index():
    return "index.html"


@app.route('/random/', )
def page_random():
    return str(randint(0, 10))


app.run()
