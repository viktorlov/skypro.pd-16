from flask import Flask

app = Flask(__name__)


@app.route('/', )
def page_index():
    return "index.html"


@app.route('/to_kbytes/<int:arg>', )
def page_kbytes(arg):
    return str(arg * 1024)


@app.route('/to_bytes/<int:arg>', )
def page_bytes(arg):
    return str(arg * 1024 * 1024)


app.run()
