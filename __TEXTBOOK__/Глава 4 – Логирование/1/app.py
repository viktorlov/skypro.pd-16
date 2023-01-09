import logging

from flask import Flask, render_template, jsonify, abort, request

from csl import create_and_set_loggers

create_and_set_loggers()

logger = logging.getLogger("basic")

PORT = 5001

app = Flask(__name__)

DATA = [{"pk": 1, "name": "milk", "unit_price": 50},
        {"pk": 2, "name": "sugar", "unit_price": 30},
        {"pk": 3, "name": "cookies", "unit_price": 50},
        {"pk": 4, "name": "corn-flakes", "unit_price": 70},
        {"pk": 5, "name": "nutella", "unit_price": 125}, ]


@app.errorhandler(400)
def error_400(error):
    logger.error('____ Error ____ : %s', error)
    return f'{request.url} Упало с ошибкой четыре сотни', 400


@app.errorhandler(404)
def error_404(error):
    logger.error('____ Error ____ : %s', error)
    return f'{request.url} Упало с ошибкой четыре сотни четыре', 404


@app.errorhandler(500)
def error_500(error):
    logger.error('____ Error ____ : %s', error)
    return f'{request.url} Упало с ошибкой пять сотен', 500


@app.route('/')
def index():
    logger.debug(f'____ Debug ____ : get {request.url} done')
    return render_template('index.html', arg='index'), 200


@app.route('/products/')
def products_index():
    logger.debug(f'____ Debug ____ : get {request.url} done')
    return jsonify(DATA), 200


@app.route('/products/<int:id>/')
def product_get(id):
    if not str(id).isdigit():
        abort(404)
    if id not in [_['pk'] for _ in DATA]:
        abort(404)
    logger.debug(f'____ Debug ____ : get {request.url} done')
    return jsonify([_ for _ in DATA if _['pk'] == id]), 200


@app.post('/products/')
def product_add():
    new_product = request.json
    if all([new_product.get("name", "") != "", new_product.get("unit_price", "") != ""]):
        new_row = {"pk": max([_['pk'] for _ in DATA]) + 1,
                   "name": new_product["name"],
                   "unit_price": new_product["unit_price"], }
        DATA.append(new_row)
        logger.debug(f'____ Debug ____ : post {new_row} done')
        return jsonify(new_row), 200
    else:
        errors = []
        if new_product.get("name", "") == "":
            user_error = "name missed"
            errors.append(user_error)
        if new_product.get("unit_price", "") == "":
            phone_error = "unit_price missed"
            errors.append(phone_error)
        logger.debug(f'____ Debug ____ : warning {errors} done')
        return jsonify(errors), 200


@app.delete('/products/<int:id>/')
def product_delete(id):
    if not str(id).isdigit():
        abort(400)
    if id not in [_['pk'] for _ in DATA]:
        abort(400)
    for index_, product_ in enumerate(DATA):
        if product_["pk"] == id:
            del DATA[index_]
            break
    logger.debug(f'____ Debug ____ : delete {request.url} done')
    return jsonify(DATA), 200


if __name__ == '__main__':
    app.run(debug=True, port=PORT)
