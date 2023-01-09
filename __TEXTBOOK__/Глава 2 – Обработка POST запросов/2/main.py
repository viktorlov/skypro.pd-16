from flask import Flask, render_template, request, jsonify

from data import items

PORT = 5002

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.post('/')
def add_one():
    to_add = request.json
    items.extend(to_add)
    return jsonify(items)


if __name__ == '__main__':
    app.run(debug=True, port=PORT)
