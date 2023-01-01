from flask import Flask

app = Flask(__name__)


@app.route('/', )
def index():
    return "Hello World!"


@app.route('/detect/<arg>', )
def detect(arg):
    return "это число" if arg.isdigit() else "это не число"


if __name__ == "__main__":
    app.run(debug=True, port=5003)
