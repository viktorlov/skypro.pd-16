from flask import Flask, render_template

app = Flask(__name__)

PORT = 5007


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/card/')
def card7():
    user = {"id": 1,
            "first_name": "Rubie",
            "last_name": "Learoyd",
            "email": "rlearoyd0@wunderground.com",
            "ip_address": "152.119.234.83"}
    return render_template('card7.html', arg=user)


if __name__ == '__main__':
    app.run(debug=True, port=PORT)
