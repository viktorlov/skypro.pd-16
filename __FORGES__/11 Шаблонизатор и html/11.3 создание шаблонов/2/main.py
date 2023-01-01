from flask import Flask, render_template

app = Flask(__name__)

CITIES = {1: "Самара", 2: "Краснодар", 3: "Сочи", 4: "Новосибирск", 5: "Вышгород"}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/city/')
def city():
    return render_template('city.html', arg=CITIES)


if __name__ == '__main__':
    app.run(debug=True, port=5002)
