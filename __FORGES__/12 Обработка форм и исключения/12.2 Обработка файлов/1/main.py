from flask import Flask, render_template, request

app = Flask(__name__)

PORT = 5001


def is_filename_allowed(arg):
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
    extension = arg.split(".")[-1]
    if extension in ALLOWED_EXTENSIONS:
        return True
    return False


@app.route('/')
def page_form():
    return render_template('form.html')


@app.route('/upload/', methods=['POST'])
def page_upload():
    file = request.files.get("file")
    filename = file.filename
    if is_filename_allowed(filename):
        file.save(f"./uploads/{filename}")
        return f"Загружен и сохранён файл {file.filename}"
    else:
        extension = filename.split(".")[-1]
        return f"Тип файлов {extension} не поддерживается"


if __name__ == '__main__':
    app.run(debug=True, port=PORT)
