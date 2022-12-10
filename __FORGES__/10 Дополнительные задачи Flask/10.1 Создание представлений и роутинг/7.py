import json

from flask import Flask

with open('data7.json') as file0:
    data7 = json.load(file0)

app = Flask(__name__)


@app.route('/', )
def page_index():
    return "index.html"


@app.route('/first/', )
def page_first():
    return str(data7[0])


@app.route('/last/', )
def page_last():
    return str(data7[-1])


@app.route('/sum/', )
def page_sum():
    return str(sum(data7))


app.run()
