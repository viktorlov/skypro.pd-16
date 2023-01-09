from flask import Flask, render_template, request

app = Flask(__name__)

PORT = 5005
app.config['JSON_AS_ASCII'] = False


def is_json(arg):
    ALLOWED_EXTENSIONS = {"json"}
    extension = arg.split(".")[-1]
    if extension in ALLOWED_EXTENSIONS:
        return True
    return False


@app.route('/')
def page_form():
    return render_template('form.html')


@app.route('/upload/', methods=['POST'])
def page_upload():
    json_file = request.files.get("file")
    data = json_file.stream.read()
    if is_json(json_file.filename):
        print(f'{data = }')
        return f'... это был json ...'
    else:
        return f"Это не json!"


if __name__ == '__main__':
    app.run(debug=True, port=PORT)
