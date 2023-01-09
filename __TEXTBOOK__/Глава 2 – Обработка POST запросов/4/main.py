from flask import Flask, render_template, request, jsonify

from data import users

PORT = 5004

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.post('/')
def add_one():
    new_user = request.json
    new_row = {"pk": len(users) + 1,
               "name": new_user["name"],
               "phone": new_user["phone"], }
    users.append(new_row)
    return jsonify(users)


if __name__ == '__main__':
    app.run(debug=True, port=PORT)
