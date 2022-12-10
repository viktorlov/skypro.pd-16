from flask import Flask

app = Flask(__name__)
data = [23, 16, 144, 72, 90, 11, 5]


@app.route('/', )
def page_index():
    return "index.html"


@app.route('/first/', )
def page_first():
    return str(data[0])


@app.route('/last/', )
def page_last():
    return str(data[-1])


@app.route('/sum/', )
def page_sum():
    return str(sum(data))


app.run()
