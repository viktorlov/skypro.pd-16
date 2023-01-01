from flask import Flask, render_template

app = Flask(__name__)

PORT = 5011


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/card/')
def card11():
    data = [{'name': "Brian Sparks",
             'phone': "(453) 207-8906",
             'email': "ipsum@yahoo.edu"},
            {'name': "Lacota Hughes",
             'phone': "1-835-268-7532",
             'email': "consectetuer.adipiscing.elit@outlook.org"},
            {'name': "Reuben Stafford",
             'phone': "1-813-687-6254",
             'email': "nec.mollis@yahoo.net"}]
    return render_template('card11.html', arg=data)


if __name__ == '__main__':
    app.run(debug=True, port=PORT)
