from flask import Flask, jsonify, request

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

books = [
    "Введение в Python",
    "Python для новичков",
    "Python  в схемах и мемах",
]


@app.route("/")
def get_books_json():
    s = request.args.get("s")

    books_found = []

    for book in books:
        if s in book.lower():
            books_found.append(book)

    return jsonify(books_found)


if __name__ == "__main__":
    app.run()
