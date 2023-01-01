from flask import Flask

app = Flask(__name__)


@app.route('/', )
def index():
    return "Hello World!"


@app.route('/python/', )
def python():
    return "это язык который мы учим"


@app.route('/java/', )
def java():
    return "а это мы не учим"


@app.route('/php/', )
def php():
    return "а это что такое вообще"

if __name__ =="__main__":
    app.run(debug=True, port=5001)

