from datetime import datetime

from flask import Flask, jsonify, request

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

grocery_list = {"milk": 150,
                "sugar": 90,
                "cookies": 200,
                "corn-flakes": 140,
                "nutella": 250, }


@app.get('/')
def P__index():
    return jsonify({"url": request.url, "status": 200, "datetime": datetime.now()}), 200


@app.get('/api/1/grocery-stats/')
def P__grocery_stats():
    from statistics import mean
    grocery_stats = {"count": len(grocery_list),
                     "total": sum(grocery_list.values()),
                     "max": max(grocery_list.values()),
                     "min": min(grocery_list.values()),
                     "avg": mean(grocery_list.values()), }
    return jsonify(grocery_stats), 200


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
    HOST = '127.0.0.4'
    PORT = 5004
    app.run(host=HOST, port=PORT, debug=True)
