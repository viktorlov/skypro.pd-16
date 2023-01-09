from flask import Flask, render_template, request, jsonify

from data import users

PORT = 5006

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.post('/')
def add_one():
    new_users = request.json
    users.extend(new_users)
    return jsonify({"users_count": len(users)})


if __name__ == '__main__':
    app.run(debug=True, port=PORT)
