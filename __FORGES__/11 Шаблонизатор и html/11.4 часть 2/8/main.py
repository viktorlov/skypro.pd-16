from flask import Flask, render_template

app = Flask(__name__)

PORT = 5008


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/card/')
def card8():
    car_info = {"location": "Guararema",
                "brand": "Toyota",
                "model": "Sequoia",
                "price": 10348.77,
                "owner": "Ambrosi McRitchie",
                "vin": "WAUMGAFL6DA818446"}
    return render_template('card8.html', arg=car_info)


if __name__ == '__main__':
    app.run(debug=True, port=PORT)
