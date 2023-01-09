import json

from flask import Blueprint, request, jsonify

api_1 = Blueprint('api_1', __name__)


def load_products():
    with open('prods.json', "r") as file:
        products_all = json.load(file)
    return products_all


@api_1.get('/')
def index():
    return f'{request.url}', 200


@api_1.get('/products/')
def get_products():
    products_all = load_products()
    products_all_dict = {}
    for row in products_all:
        products_all_dict[str(row['pk'])] = row
    return jsonify(products_all_dict), 200
