from flask import Flask, render_template, request

app = Flask(__name__)

PORT = 5003


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
    folder = request.form.get("folder")
    from os import mkdir
    try:
        mkdir(folder)
    except FileExistsError:
        pass
    filename = file.filename
    if is_filename_allowed(filename):
        file.save(f"./{folder}/{filename}")
        return f"Загружен и сохранён файл {filename} в папку {folder}"
    else:
        extension = filename.split(".")[-1]
        return f"Тип файлов {extension} не поддерживается"


if __name__ == '__main__':
    app.run(debug=True, port=PORT)
