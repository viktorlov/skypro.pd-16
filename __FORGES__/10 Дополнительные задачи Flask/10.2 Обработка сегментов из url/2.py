from flask import Flask

app = Flask(__name__)

dictionary = {1: "Самара",
              2: "Краснодар",
              3: "Сочи",
              4: "Новосибирск",
              5: "Вышгород"}


@app.route('/', )
def page_index():
    return "index.html"


@app.route('/city/<int:arg>/', )
def page_find(arg):
    return dictionary[arg]


app.run()
