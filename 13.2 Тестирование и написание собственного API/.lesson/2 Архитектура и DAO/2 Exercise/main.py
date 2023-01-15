from datetime import datetime

from flask import Flask, request, jsonify, render_template

from books_dao import BooksDAO

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
books_dao = BooksDAO()


@app.route("/")
def page_index():
    books = books_dao.get_all()
    return render_template("index.html", books=books)


@app.route("/book/<int:uid>/")
def page_book(uid):
    book = books_dao.get_by_id(uid)
    return render_template("book.html", book=book)


@app.errorhandler(404)
def error_404(error):
    return jsonify({"url": request.url, "status": f'{error}', "datetime": datetime.now()}), 404


@app.errorhandler(400)
def error_400(error):
    return jsonify({"url": request.url, "status": f'{error}', "datetime": datetime.now()}), 400


@app.errorhandler(500)
def error_500(error):
    return jsonify({"url": request.url, "status": f'{error}', "datetime": datetime.now()}), 500


@app.errorhandler(ValueError)
def value_error(error):
    return jsonify({"url": request.url, "status": f'{error}', "datetime": datetime.now()}), 500


@app.errorhandler(KeyError)
def key_error(error):
    return jsonify({"url": request.url, "status": f'{error}', "datetime": datetime.now()}), 500


@app.errorhandler(TypeError)
def type_error(error):
    return jsonify({"url": request.url, "status": f'{error}', "datetime": datetime.now()}), 500


@app.errorhandler(NameError)
def name_error(error):
    return jsonify({"url": request.url, "status": f'{error}', "datetime": datetime.now()}), 500


if __name__ == '__main__':
    HOST = '127.0.0.9'
    PORT = 5009
    app.run(host=HOST, port=PORT, debug=True)
