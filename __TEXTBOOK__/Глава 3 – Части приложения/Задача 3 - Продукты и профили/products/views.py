from flask import Blueprint, request, jsonify

products = Blueprint('products', __name__)

products_all = [{"pk": 1, "name": "milk", "unit_price": 50},
                {"pk": 2, "name": "sugar", "unit_price": 30},
                {"pk": 3, "name": "cookies", "unit_price": 50},
                {"pk": 4, "name": "corn-flakes", "unit_price": 70},
                {"pk": 5, "name": "nutella", "unit_price": 125}, ]


@products.get('/')
def get():
    return f'{request.url}'


@products.get('/<int:id>')
def get_product(id):
    output = {}
    for row in products_all:
        if row['pk'] == id:
            output.update(row)
            break
    return jsonify(output)
