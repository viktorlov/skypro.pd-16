from flask import Flask

app = Flask(__name__)

with open('data6.txt', encoding='utf-8') as file6:
    data6 = file6.readlines()


@app.route('/', )
def page_index():
    return "index.html"


@app.route('/profile/<int:arg>', )
def page_profile(arg):
    return f'{data6[arg-1]}'


app.run()
