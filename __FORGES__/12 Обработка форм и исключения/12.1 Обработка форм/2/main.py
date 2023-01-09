from flask import Flask, render_template, request

app = Flask(__name__)

PORT = 5002


@app.route('/')
def add_form():
    return render_template('add.html')


@app.post('/add/')
def add_page():
    username = request.form['username']
    level = request.form['level']

    from datetime import datetime
    current_datetime = datetime.now()

    with open("records.txt", "a") as file:
        file.write(str(current_datetime) + " " + username + " " + level + '\n')

    return f'Информация записана'


if __name__ == '__main__':
    app.run(debug=True, port=PORT)
