from flask import Flask, render_template, request

app = Flask(__name__)

PORT = 5002


def is_filename_allowed(arg):
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
    extension = arg.split(".")[-1]
    if extension in ALLOWED_EXTENSIONS:
        return True
    return False


def filename_generator(length=6):
    from random import randint
    z = str()
    for _ in range(length):
        z += str(randint(0, 9))
    return z


@app.route('/')
def page_form():
    return render_template('form.html')


@app.route('/upload/', methods=['POST'])
def page_upload():
    file = request.files.get("file")
    full_filename = file.filename
    if is_filename_allowed(full_filename):
        new_filename = f'{filename_generator()}.{full_filename.split(".")[-1]}'
        file.save(f"./uploads/{new_filename}")
        return f"Загружен и сохранён файл {full_filename} под именем {new_filename}"
    else:
        extension = full_filename.split(".")[-1]
        return f"Тип файлов {extension} не поддерживается"


if __name__ == '__main__':
    app.run(debug=True, port=PORT)
