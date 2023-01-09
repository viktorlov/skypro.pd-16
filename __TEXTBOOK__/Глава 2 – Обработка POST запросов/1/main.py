from flask import Flask, render_template

from data import data

PORT = 5001

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.post('/')
def add_one():
    data["value"] += 1
    return f"{data['value']}"


if __name__ == '__main__':
    app.run(debug=True, port=PORT)
