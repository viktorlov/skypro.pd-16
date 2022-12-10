from flask import Flask

app = Flask(__name__)
words = ["@кот", "@хлеб", "не", "ешь", "@подумай", "теперь", "ешь"]


@app.route('/', )
def page_index():
    return "index.html"


@app.route('/mentions/', )
def page_mentions():
    return str(" ".join([word[1:] for word in words if word.startswith('@')]))


app.run()
