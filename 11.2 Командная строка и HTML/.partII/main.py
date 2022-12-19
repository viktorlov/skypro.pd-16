from flask import Flask, render_template

from utilities import get_all, get_candidate, get_candidates_by_skill, get_candidates_by_name

app = Flask(__name__)


@app.route("/")
def page_index():
    candidates = get_all()
    return render_template('list.html', candidates=candidates)


@app.route("/candidate/<int:pk>")
def page_candidate(pk):
    candidate = get_candidate(pk)
    return render_template('single.html', candidate=candidate)


@app.route("/skill/<skill>")
def page_skills(skill):
    candidates = get_candidates_by_skill(skill)
    return render_template('skill.html', candidates=candidates, count_candidates=len(candidates), skill=skill)


@app.route("/search/<name>")
def page_names(name):
    candidates = get_candidates_by_name(name)
    return render_template('search.html', candidates=candidates, count_candidates=len(candidates))


if __name__ == "__main__":
    app.run(debug=True)
