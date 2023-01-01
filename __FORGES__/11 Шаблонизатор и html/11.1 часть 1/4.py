from flask import Flask

app = Flask(__name__)


@app.route('/', )
def index():
    return "Hello World!"


@app.route('/avg/', )
def avg():
    from statistics import mean
    numbers = [23, 16, 144, 72, 90, 11, 5]
    return str(mean(numbers))


if __name__ == "__main__":
    app.run(debug=True, port=5004)
