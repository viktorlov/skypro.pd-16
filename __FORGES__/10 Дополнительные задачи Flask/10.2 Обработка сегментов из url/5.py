from flask import Flask

app = Flask(__name__)


@app.route('/', )
def page_index():
    return "index.html"


@app.route('/meal/<arg1>/<arg2>/<arg3>/', )
def page_meal(arg1, arg2, arg3):
    return f"""<pre>
{'На первое: ' + arg1}
{'На второе: ' + arg2}
{'На третье: ' + arg3}
                </pre>"""


app.run()
