from flask import Flask, render_template

app = Flask(__name__)

PORT = 5012


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/card/')
def card12():
    data = [{"postalZip": "71152",
             "address": "Ap #722-4909 Dictum Street"},
            {"postalZip": "65223-621",
             "address": "Ap #513-4641 Vitae Street"},
            {"postalZip": "44923",
             "address": "1763 Libero Street"}]
    return render_template('card12.html', arg=data)


if __name__ == '__main__':
    app.run(debug=True, port=PORT)
