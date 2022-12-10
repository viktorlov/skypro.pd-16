from flask import Flask

from utilities import get_all, get_by_pk, get_by_skill

app = Flask(__name__)


@app.route("/")
def page_index():
    candidates = get_all()
    result = '<br>'
    for each in candidates:
        result += 'Имя кандидата - ' + each['name'] + '<br>'
        result += 'Позиция кандидата - ' + each['position'] + '<br>'
        result += 'Навыки кандидата - ' + each['skills'] + '<br>'
        result += '<br>'
    return f'<pre> {result} </pre>'


@app.route("/candidate/<int:pk>")
def page_candidates(pk):
    candidate = get_by_pk(pk)
    if not candidate:
        return f'Кандидат не найден'

    result = '<br>'
    result += 'Имя кандидата - ' + candidate['name'] + '<br>'
    result += 'Позиция кандидата - ' + candidate['position'] + '<br>'
    result += 'Навыки кандидата - ' + candidate['skills'] + '<br>'
    result += '<br>'
    return f'''
        <img src='{candidate['picture']}'>
        <pre> {result} </pre>
    '''


@app.route("/skill/<skill>")
def page_skills(skill):
    candidates = get_by_skill(skill)
    if not len(candidates):
        return f'Кандидат не найден'

    result = '<br>'
    for each in candidates:
        result += 'Имя кандидата - ' + each['name'] + '<br>'
        result += 'Позиция кандидата - ' + each['position'] + '<br>'
        result += 'Навыки кандидата - ' + each['skills'] + '<br>'
        result += '<br>'
    return f'<pre> {result} </pre>'


if __name__ == "__main__":
    app.run(debug=True)
