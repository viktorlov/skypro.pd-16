from flask import Flask, request, jsonify

import utils

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False


@app.route('/books/', methods=['GET'])
def read_books():
    books = utils.load_books_from_json()
    return jsonify(books)


@app.route('/books/<int:book_id>/', methods=['GET'])
def read_book(book_id):
    book = utils.get_book_by_id(book_id)
    return jsonify(book)


###

@app.route('/books/', methods=['POST'])
def create_book():
    book = {}
    post_data = request.json

    book["title"] = post_data.get("title")
    book["author"] = post_data.get("author")
    book["year"] = post_data.get("year")

    book_created = utils.add_book(book)

    return jsonify(book_created)


###

@app.route('/books/<int:book_id>/', methods=['PUT'])
def update_book(book_id):
    book = utils.get_book_by_id(book_id)
    post_data = request.json

    book["title"] = post_data.get("title")
    book["author"] = post_data.get("author")
    book["year"] = post_data.get("year")

    utils.update_book(book_id, book)

    return jsonify(book)


@app.route('/books/<int:book_id>/', methods=['DELETE'])
def delete_book(book_id):
    utils.delete_book(book_id)
    return ""

if __name__=='__main__':
    app.run(debug=True)
