from flask import Flask, render_template

app = Flask(__name__)

PORT = 5009


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/card/')
def card9():
    guests = ["Алиса", "Борис", "Марина", "Алишер"]
    return render_template('card9.html', arg=guests)


if __name__ == '__main__':
    app.run(debug=True, port=PORT)
