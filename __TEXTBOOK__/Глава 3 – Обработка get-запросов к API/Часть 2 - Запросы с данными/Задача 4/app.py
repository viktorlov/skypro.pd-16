import json
from datetime import datetime

from flask import Flask, jsonify, request

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

with open('db.json', 'r', encoding='utf-8') as f:
    data = json.load(f)


@app.get('/')
def P__index():
    return jsonify(data), 200


@app.get('/api/1/categories/')
def P__categories():
    cats = []
    for row in data:
        cats.append(row['cat'])
    return jsonify(list(set(cats))), 200


@app.errorhandler(404)
def error_404(error):
    return jsonify({"url": request.url, "status": "404 NOT FOUND", "datetime": datetime.now()}), 404


@app.errorhandler(400)
def error_400(error):
    return jsonify({"url": request.url, "status": 400, "datetime": datetime.now()}), 400


@app.errorhandler(500)
def error_500(error):
    return jsonify({"url": request.url, "status": 500, "datetime": datetime.now()}), 500


@app.errorhandler(ValueError)
def value_error(error):
    return jsonify({"url": request.url, "status": "ValueError", "datetime": datetime.now()}), 500


@app.errorhandler(KeyError)
def key_error(error):
    return jsonify({"url": request.url, "status": "KeyError", "datetime": datetime.now()}), 500


@app.errorhandler(TypeError)
def key_error(error):
    return jsonify({"url": request.url, "status": "TypeError", "datetime": datetime.now()}), 500


if __name__ == '__main__':
    HOST = '127.0.0.4'
    PORT = 5004
    app.run(host=HOST, port=PORT, debug=True)
