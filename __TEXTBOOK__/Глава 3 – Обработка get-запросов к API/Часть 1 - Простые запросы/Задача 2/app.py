from datetime import datetime
from random import randint

from flask import Flask, jsonify, request, abort

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.get('/')
def Pindex():
    return jsonify({"url": request.url, "status": 200, "datetime": datetime.now()}), 200


@app.get('/api/1/random/')
def Prandom():
    try:
        from_ = int(request.args['from'])
        to_ = int(request.args['to'])
    except ValueError:
        abort(500)
    min_ = min([from_, to_])
    max_ = max([from_, to_])
    return jsonify({"number": randint(min_, max_)}), 200


@app.errorhandler(404)
def error_404(error):
    return jsonify({"url": request.url, "status": 404, "datetime": datetime.now()}), 404


@app.errorhandler(400)
def error_400(error):
    return jsonify({"url": request.url, "status": 400, "datetime": datetime.now()}), 404


@app.errorhandler(500)
def error_500(error):
    return jsonify({"url": request.url, "status": 500, "datetime": datetime.now()}), 404


if __name__ == '__main__':
    HOST = '127.0.0.2'
    PORT = 5002
    app.run(host=HOST, port=PORT, debug=True)
