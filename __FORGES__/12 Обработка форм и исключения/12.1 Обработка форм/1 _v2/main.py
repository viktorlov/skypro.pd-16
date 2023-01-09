from flask import Flask, request, render_template, jsonify

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

WS = ["платина", "стена", "халат", "блокнот", "косилка", "автобус", "базар", "биосфера", "грелка"]


@app.route('/')
def form_page():
    return render_template('form.html')


@app.route('/search/')
def search_page():
    s = request.args['s'].lower()
    a = [each for each in WS if s in each.lower()]
    return jsonify(a)


if __name__ == '__main__':
    app.run(debug=True, port=5001)
