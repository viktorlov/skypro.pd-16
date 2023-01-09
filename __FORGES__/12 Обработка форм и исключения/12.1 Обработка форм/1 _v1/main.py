from flask import Flask, request, render_template

app = Flask(__name__)

WS = ["платина", "стена", "халат", "блокнот", "косилка", "автобус", "базар", "биосфера", "грелка"]


@app.route('/')
def form_page():
    return render_template('form.html')


@app.route('/search/')
def search_page():
    s = request.args['s'].lower()
    a = [each for each in WS if s in each.lower()]
    if len(a) > 0:
        z = f""" Вы ввели слово {s}. <br> Оно встречается в словах: {a}. """
    else:
        z = f""" Вы ввели слово {s}. <br> Оно не встречается. """
    return z


if __name__ == '__main__':
    app.run(debug=True, port=5001)
