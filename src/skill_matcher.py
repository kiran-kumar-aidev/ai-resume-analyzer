def compare_skills(candidate_skills, required_skills, preferred_skills):
    candidate_set = {
        skill.lower() for skill in candidate_skills
    }

    required_set = {
        skill.lower() for skill in required_skills
    }

    preferred_set = {
        skill.lower() for skill in preferred_skills
    }

    matched_skill = [
        skill for skill in required_skills
        if skill.lower() in candidate_set
    ]

    missing_skill = [
        skill for skill in required_skills
        if skill.lower() not in candidate_set
    ]

    matched_preferred = [
        skill for skill in preferred_skills
        if skill.lower() in candidate_set
    ]

    return {
        "matched_skills":matched_skill,
        "missing_skills":missing_skill,
        "matched_preferred_skill":matched_preferred,
        "required_skill_match_percentage": round (
            len(matched_skill) / len(required_set) * 100, 2
        ) if required_set else 0
    }

