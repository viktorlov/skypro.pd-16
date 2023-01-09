from flask import Flask, render_template, request

app = Flask(__name__)

PORT = 5003
LOGIN = 'nigol'
PASSWORD = 'drowssap'


@app.route('/')
def pair_form():
    return render_template('pair.html')


@app.route('/pair/', methods=['POST'])
def pair_page():

    username = request.form['username']
    password = request.form['password']

    if all([username == LOGIN, password == PASSWORD]):
        a = "Вход разрешен"
    else:
        a = "Вход запрещен"
    return a


if __name__ == "__main__":
    app.run(debug=True, port=PORT)
