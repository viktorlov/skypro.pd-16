from datetime import datetime

from flask import Flask, jsonify, request

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

expense_list = [{"name": "milk", "unit_price": 50, "amount": 3, "total": 150},
                {"name": "sugar", "unit_price": 30, "amount": 3, "total": 90},
                {"name": "cookies", "unit_price": 50, "amount": 4, "total": 200},
                {"name": "corn-flakes", "unit_price": 70, "amount": 2, "total": 140},
                {"name": "nutella", "unit_price": 125, "amount": 1, "total": 250}, ]


@app.get('/')
def P__index():
    return jsonify({"url": request.url, "status": 200, "datetime": datetime.now()}), 200


@app.get('/api/1/expense/<product>')
def P__expense(product):
    output = {"error": f"no such product {product}"}
    for row in expense_list:
        if product == row['name']:
            output = row
            break
    return jsonify(output), 200


@app.get('/api/1/expense/')
def P__expense_all():
    return jsonify(expense_list), 200


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
    HOST = '127.0.0.5'
    PORT = 5005
    app.run(host=HOST, port=PORT, debug=True)
