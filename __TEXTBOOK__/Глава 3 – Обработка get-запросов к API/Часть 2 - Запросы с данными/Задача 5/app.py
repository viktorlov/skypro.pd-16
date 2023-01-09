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


@app.get('/api/1/product-stats/')
def P__product_stats():
    from statistics import mean
    kcals = []
    for row in data:
        kcals.append(row['kcal'])
    return jsonify({"count": len(data),
                    "kcal_avg": mean(kcals),
                    "kcal_max": max(kcals),
                    "kcal_min": min(kcals), }), 200


@app.errorhandler(404)
def error_404(error):
    return jsonify({"url": request.url, "status": f'{error}', "datetime": datetime.now()}), 404


@app.errorhandler(400)
def error_400(error):
    return jsonify({"url": request.url, "status": f'{error}', "datetime": datetime.now()}), 400


@app.errorhandler(500)
def error_500(error):
    return jsonify({"url": request.url, "status": f'{error}', "datetime": datetime.now()}), 500


@app.errorhandler(ValueError)
def value_error(error):
    return jsonify({"url": request.url, "status": f'{error}', "datetime": datetime.now()}), 500


@app.errorhandler(KeyError)
def key_error(error):
    return jsonify({"url": request.url, "status": f'{error}', "datetime": datetime.now()}), 500


@app.errorhandler(TypeError)
def type_error(error):
    return jsonify({"url": request.url, "status": f'{error}', "datetime": datetime.now()}), 500


@app.errorhandler(NameError)
def name_error(error):
    return jsonify({"url": request.url, "status": f'{error}', "datetime": datetime.now()}), 500


if __name__ == '__main__':
    HOST = '127.0.0.5'
    PORT = 5005
    app.run(host=HOST, port=PORT, debug=True)
