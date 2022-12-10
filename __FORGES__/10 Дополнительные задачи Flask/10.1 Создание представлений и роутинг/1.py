from flask import Flask

app = Flask(__name__)


@app.route('/', )
def page_index():
    return "index.html"


@app.route('/hello/', )
def page_hello():
    return "Hello!"


@app.route('/goodbye/', )
def page_goodbye():
    return "Googbye!"


@app.route('/seeyou/', )
def page_seeyou():
    return "See you!"


app.run()
