from flask import Flask, render_template

app = Flask(__name__)

PORT = 5006

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/card/')
def card6():
    title = "Умный светильник SkyLight r300"
    category = "Светильники"
    pic = "https://items.s1.citilink.ru/1422784_v01_b.jpg"
    price = 4400
    return render_template('card6.html', arg1=title, arg2=category, arg3=pic, arg4=price)


if __name__ == '__main__':
    app.run(debug=True, port=PORT)
