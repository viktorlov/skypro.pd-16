from flask import Flask, render_template, abort

app = Flask(__name__)

PORT = 5001
CITIES = {1: "Самара", 2: "Краснодар", 3: "Сочи", 4: "Новосибирск", 5: "Вышгород"}


@app.route('/')
def index_page():
    return render_template('index.html')


@app.route('/city/<int:number>')
def city_page(number):
    if number in CITIES.keys():
        return render_template('city.html', arg=CITIES[number])
    else:
        abort(404)


if __name__ == '__main__':
    app.run(debug=True, port=PORT)
