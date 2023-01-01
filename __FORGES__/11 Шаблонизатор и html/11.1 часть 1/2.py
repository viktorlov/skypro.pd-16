from flask import Flask

app = Flask(__name__)


@app.route('/', )
def index():
    return "Hello World!"


@app.route('/random/', )
def random():
    from random import choice
    ALPHABET = "ABCDEFGHIKLMNOPQRSTVXYZ"
    return str(choice(ALPHABET))


if __name__ == "__main__":
    app.run(debug=True, port=5002)
