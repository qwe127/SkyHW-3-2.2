import json


def load_candidates_from_json(path):
    with open(path, encoding='utf-8') as file:
        candidates = json.load(file)
    return candidates


def get_candidate(candidate_id):
    for candidate in load_candidates_from_json(data):
        if candidate['id'] == candidate_id:
            return candidate


def get_candidates_by_name(candidate_name):
    result = []
    for candidate in load_candidates_from_json(data):
        if candidate['name'] == candidate_name:
            result.append(candidate)
    return result


def get_candidates_by_skill(skill_name):
    result = []
    for candidate in load_candidates_from_json(data):
        if skill_name in candidate['skills'].lower().split(', '):
            result.append(candidate)
    return result


data = 'candidates.json'

print(get_candidates_by_skill('python'))
