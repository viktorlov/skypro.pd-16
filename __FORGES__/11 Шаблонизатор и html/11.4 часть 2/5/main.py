from flask import Flask, render_template

app = Flask(__name__)

PORT = 5005

name = "Алиса"
position = "Senior Developer"
location = "Novosibirsk"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/card/')
def card5():
    return render_template('card5.html', arg1=name, arg2=position, arg3=location)


if __name__ == '__main__':
    app.run(debug=True, port=PORT)
