import json

from flask import Blueprint, render_template, jsonify

pages = Blueprint('pages', __name__, template_folder="templates")


def load_products():
    with open('prods.json', "r") as file:
        products_all = json.load(file)
    return products_all


@pages.get('/')
def index():
    return jsonify(load_products()), 200


@pages.get('/<int:id>/')
def get_product(id):
    output = {}
    for row in load_products():
        if row['pk'] == id:
            output.update(row)
            break
    if len(output) == 0:
        return f'no such product', 200
    return render_template('pages_product.html', arg=output), 200
