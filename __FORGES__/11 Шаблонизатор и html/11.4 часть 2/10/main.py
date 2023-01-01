from flask import Flask, render_template

app = Flask(__name__)

PORT = 5010


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/card/')
def card10():
    expenses = [450, 850, 200, 430, 790, 310, 400]
    return render_template('card10.html', arg1=expenses, arg2=sum(expenses))


if __name__ == '__main__':
    app.run(debug=True, port=PORT)
