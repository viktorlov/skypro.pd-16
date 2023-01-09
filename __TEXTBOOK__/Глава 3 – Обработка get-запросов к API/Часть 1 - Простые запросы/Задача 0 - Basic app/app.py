from datetime import datetime

from flask import Flask, jsonify, request

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.get('/')
def Pindex():
    return jsonify({"url": request.url, "status": 200, "datetime": datetime.now()}), 200


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
    HOST = '127.0.0.1'
    PORT = 5000
    app.run(host=HOST, port=PORT, debug=True)
