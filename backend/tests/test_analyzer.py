from backend.analyzer import analyze_skills


def test_weighted_score_and_skill_lists():
    result = analyze_skills(
        {"programming": ["python"], "tools": ["git"]},
        {"programming": ["python", "java"], "tools": ["git"]},
    )

    assert result["score"] == 60
    assert result["matched_skills"] == ["git", "python"]
    assert result["missing_skills"] == ["java"]
    assert result["extra_skills"] == []


def test_score_is_zero_when_job_has_no_detected_skills():
    result = analyze_skills({"programming": ["python"]}, {})
    assert result["score"] == 0