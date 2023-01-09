import json

from flask import Blueprint, request, jsonify

api_2 = Blueprint('api_2', __name__)


def load_products():
    with open('prods.json', "r") as file:
        products_all = json.load(file)
    return products_all


@api_2.get('/')
def index():
    return f'{request.url}', 200


@api_2.get('/products/')
def get_products():
    return jsonify(load_products()), 200
