from flask import Flask, render_template

from candidates_dao import CandidatesDAO

app = Flask(__name__)
candidates_dao = CandidatesDAO()


@app.route("/")
def page_index():
    candidates = candidates_dao.get_all()
    return render_template("index.html", candidates=candidates)


@app.route("/skill/<skill_name>/")
def page_skill(skill_name):
    candidates = candidates_dao.get_by_skill(skill_name)
    return render_template("skill.html", candidates=candidates)


@app.route("/candidate/<int:uid>/")
def page_candidate(uid):
    candidate = candidates_dao.get_by_id(uid)
    return render_template("templates/candidate.html", candidate=candidate)

if __name__=="__main__":
    app.run(debug=True)