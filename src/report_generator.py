def generator_final_report(
        ats_score,
        matched_skills,
        missing_skills,
        experience_analysis,
        recommendations
):
    report = f"""
===========================================================
                RESUME ANALYSIS REPORT
===========================================================

ATS MATCH SCORE: {ats_score}%

MATCHED SKILLS:
{", ".join(matched_skills) if matched_skills else "None"}

MISSING REQUIRED SKILLS:
{", ".join(missing_skills) if missing_skills else "None"}

EXPERIENCE ANALYSIS:
{experience_analysis["experience_status"]}

EXPERIENCE GAP:
{experience_analysis["experience_gap"]}

AI RECOMMENDATIONS:
{recommendations}

==============================================================

"""

    return report 

