from flask import Flask, render_template

app = Flask(__name__)

SOMEDICT = {"username": "alexy_001", "email": "alexy@skyeng.ru", "phone": "+1555223311", }


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/card/')
def card():
    return render_template('card.html', arg=SOMEDICT)


if __name__ == '__main__':
    app.run(debug=True, port=5001)
