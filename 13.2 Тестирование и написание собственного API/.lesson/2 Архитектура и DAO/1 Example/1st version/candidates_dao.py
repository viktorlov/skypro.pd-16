import json


class CandidatesDAO:

    def load_data(self):
        with open("candidates.json", "r", encoding="utf-8") as file:
            candidates = json.load(file)
        return candidates

    def get_all(self):
        return self.load_data()

    def get_by_skill(self, skill):
        candidates = self.load_data()
        skilled_candidates = []
        skill_lower = skill.lower()
        for candidate in candidates:
            candidate_skills = candidate["skills"].lower().split(", ")
            if skill_lower in candidate_skills:
                skilled_candidates.append(candidate)

        return skilled_candidates

    def get_by_id(self, candidate_id):
        candidates = self.load_data()
        for candidate in candidates:
            if candidate["id"] == candidate_id:
                return candidate
