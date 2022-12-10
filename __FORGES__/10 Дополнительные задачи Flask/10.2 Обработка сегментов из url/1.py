from flask import Flask

app = Flask(__name__)

text = """На крыльце сидел котейка
Мимо шел казах Андрейка
Будет завтра у Андрейки
из котейки тюбетейка"""


@app.route('/', )
def page_index():
    return "index.html"


@app.route('/find/<arg>/', )
def page_find(arg):
    return 'YES' if arg in text else 'NO'


app.run()
