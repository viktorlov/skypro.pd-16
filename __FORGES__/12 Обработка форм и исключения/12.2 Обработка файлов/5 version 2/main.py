from flask import Flask, render_template, request, jsonify

from os import mkdir, rmdir, remove

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


@app.post('/upload/')
def page_upload():
    json_file = request.files.get("file")
    if is_json(json_file.filename):
        filename = json_file.filename
        path = './temp/'
        try:
            mkdir(path)
        except OSError:
            pass
        json_file.save(f"{path}{filename}")
        with open(filename, encoding='utf-8') as f:
            data = f.read()
        print(f'{data = }')
        remove(path+filename)
        rmdir(path)
        return jsonify(data)
    else:
        return f"... не json ..."


if __name__ == '__main__':
    app.run(debug=True, port=PORT)
