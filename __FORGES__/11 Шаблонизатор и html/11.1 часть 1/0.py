from flask import Flask

app = Flask(__name__)


@app.route('/', )
def page_index():
    return "It works"


app.run()
