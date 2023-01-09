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


@app.get('/api/1/product/')
def P__product_name():
    from_ = request.args.get('from')
    to_ = request.args.get('to')
    if any([from_ is None,
            to_ is None,
            not from_.isdecimal(),
            not to_.isdecimal, ]):
        return jsonify(data), 200
    else:
        output = []
        for row in data:
            if min(int(from_), int(to_)) <= row['kcal'] <= max(int(from_), int(to_)):
                output.append(row)
        if len(output) == 0:
            return jsonify({"sorry": "no such category"}), 200
        else:
            return jsonify(output), 200


@app.errorhandler(404)
def error_404(error):
    return jsonify({"url": request.url, "status": 404, "datetime": datetime.now()}), 404


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


if __name__ == '__main__':
    HOST = '127.0.0.3'
    PORT = 5003
    app.run(host=HOST, port=PORT, debug=True)
