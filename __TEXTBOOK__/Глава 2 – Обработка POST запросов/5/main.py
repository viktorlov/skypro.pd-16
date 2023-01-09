from flask import Flask, render_template, request, jsonify

from data import users

PORT = 5005

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.post('/')
def add_one():
    new_user = request.json
    if all([new_user.get("name", "") != "", new_user.get("phone", "") != ""]):
        new_row = {"pk": len(users) + 1,
                   "name": new_user["name"],
                   "phone": new_user["phone"], }
        users.append(new_row)
        return jsonify(users)
    else:
        errors = []
        if new_user.get("name", "") == "":
            user_error = "name missed"
            errors.append(user_error)
        if new_user.get("phone", "") == "":
            phone_error = "phone missed"
            errors.append(phone_error)
        return jsonify(errors)


if __name__ == '__main__':
    app.run(debug=True, port=PORT)
