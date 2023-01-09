from datetime import datetime
from random import randint

from flask import Flask, jsonify, request

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.get('/')
def Pindex():
    return jsonify({"url": request.url, "status": 200, "datetime": datetime.now()}), 200


@app.get('/api/1/random/')
def Prandom():
    return jsonify({'number': randint(1, 10)})


@app.errorhandler(404)
def error_404(error):
    return jsonify({"url": request.url, "status": 404, "datetime": datetime.now()}), 404


if __name__ == '__main__':
    HOST = '127.0.0.1'
    PORT = 5001
    app.run(host=HOST, port=PORT, debug=True)
