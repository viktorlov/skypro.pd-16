from flask import Flask, redirect

app = Flask(__name__)

PORT = 5003


@app.route('/')
def index():
    return redirect('/next_level/', code=302)

@app.route('/next_level/')
def next_level():
    return redirect('/next_next_level', code=302)

@app.route('/next_next_level/')
def next_next_level():
    return f'Это третий уровень'


if __name__ == '__main__':
    app.run(debug=True, port=PORT)
