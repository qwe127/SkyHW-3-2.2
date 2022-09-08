from flask import Flask, render_template

from utils import load_candidates_from_json, get_candidate, get_candidates_by_name, get_candidates_by_skill

app = Flask(__name__)


@app.route("/")
def home():
    candidates = load_candidates_from_json(path)
    return render_template('list.html', candidates=candidates)


@app.route("/candidate/<int:id>")
def candidate_card(id):
    candidate = get_candidate(id)
    if not candidate:
        return "Nothing found"
    return render_template('card.html', candidate=candidate)


@app.route("/search/<candidate_name>")
def candidate_search(candidate_name):
    candidates = get_candidates_by_name(candidate_name)
    return render_template('search.html', candidates=candidates)


@app.route("/skill/<skill_name>")
def skill_search(skill_name):
    candidates = get_candidates_by_skill(skill_name)
    return render_template('skill.html', skill=skill_name, candidates=candidates)


path = 'candidates.json'
app.run()

print(load_candidates_from_json(path))
