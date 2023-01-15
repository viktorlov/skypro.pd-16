from flask import Flask

app = Flask(__name__)
app.config.from_pyfile("config.py")


@app.route('/')
def page_index():
    title = app.config.get("PROJECT_NAME")
    description = app.config.get("PROJECT_DESCRIPTION")
    return f"<h1>{title}</h1><p>{description}</p>"


if __name__ == '__main__':
    app.run()
