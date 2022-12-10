from flask import Flask

app = Flask(__name__)
content = "Кот это не хлеб, подумай, не ешь его, разработчик! Ай, ну я же просил"


@app.route('/', )
def page_index():
    return "index.html"


@app.route('/words/', )
def page_words():
    return "Слов: " + str(int(content.count(' ')) + 1)


@app.route('/spaces/', )
def page_spaces():
    return "Пробелов: " + str(int(content.count(' ')))


@app.route('/letters/', )
def page_letters():
    return str(len([word for word in content if word.isalpha()]))


app.run()
