from flask import Flask, render_template, request

app = Flask(__name__)

PORT = 5004


def is_picture(arg):
    PICTURE_EXTENSIONS = {"png", "jpg", "tiff", "svg"}
    extension = arg.split(".")[-1]
    if extension in PICTURE_EXTENSIONS:
        return True
    return False


def is_text(arg):
    TEXT_EXTENSIONS = {"txt", "doc", "rtf"}
    extension = arg.split(".")[-1]
    if extension in TEXT_EXTENSIONS:
        return True
    return False


@app.route('/')
def page_form():
    return render_template('form.html')


@app.route('/upload/', methods=['POST'])
def page_upload():
    file = request.files.get("file")
    filename = file.filename
    if is_picture(filename):
        return f"Файл {file.filename} это <b>картинка</b>"
    if is_text(filename):
        return f"Файл {file.filename} это <b>текст</b>"
    return f"Файл {file.filename} это <b>непонятно что</b>"


if __name__ == '__main__':
    app.run(debug=True, port=PORT)
