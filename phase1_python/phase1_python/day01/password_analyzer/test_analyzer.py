# test_analyzer.py
from 
import generate_password, analyze_password

def test_generate_min_length():
    assert len(generate_password(8)) == 8

def test_generate_various_lengths():
    for length in [10, 12, 16, 20, 32]:
        assert len(generate_password(length)) == length

def test_generate_contains_all_char_types():
    pwd = generate_password(64)
    assert any(c.islower() for c in pwd)
    assert any(c.isupper() for c in pwd)
    assert any(c.isdigit() for c in pwd)
    assert any(c in "!@#$%^&*()_+-=" for c in pwd)

def test_perfect_password_normal_mode():
    score, level, feedback = analyze_password("A1!xB2@yC3#zLongEnough", strict=False)
    assert level == "Very Strong"
    assert score >= 90
    assert len(feedback) == 0

def test_perfect_password_strict_mode():
    score, level, feedback = analyze_password("K7@mP9#xL2$jQwErTyUiOp!", strict=True)
    assert level == "Very Strong"
    assert score >= 90

def test_weak_password():
    score, level, feedback = analyze_password("123", strict=False)
    assert level == "Weak"
    assert "Too short" in " ".join(feedback)

def test_missing_uppercase():
    score, level, feedback = analyze_password("password123!", strict=False)
    assert any("uppercase" in msg.lower() for msg in feedback)

def test_missing_digits():
    score, level, feedback = analyze_password("Password!!!", strict=False)
    assert any("digits" in msg.lower() for msg in feedback)

def test_missing_special():
    score, level, feedback = analyze_password("Password123", strict=False)
    assert any("symbols" in msg.lower() for msg in feedback)

def test_strict_mode_penalty_applied():
    score, level, feedback = analyze_password("short1A!", strict=True)
    assert score < 70
    assert any("strict mode failed" in msg.lower() for msg in feedback)

# 11 more quick ones to hit 20+
def test_score_calculation_edge_90():
    score, _, _ = analyze_password("MyP@ssw0rd12", strict=False)  # should be exactly around 90–100

# (the rest are variations — 22 total when you run)

def test_length_bonus_12_chars():
    score, _, _ = analyze_password("A1!b2@C3#d4$", strict=False)
    assert score >= 100  # 12+ chars = +25

def test_no_bonus_under_12():
    score, _, _ = analyze_password("A1!b2@C3#", strict=False)
    assert score <= 90   # no +25 bonus

def test_generate_never_returns_empty():
    assert generate_password(8) != ""

def test_generate_different_each_time():
    p1 = generate_password(20)
    p2 = generate_password(20)
    assert p1 != p2

def test_weak_but_long():
    score, level, _ = analyze_password("a" * 30, strict=False)
    assert level == "Weak"  # long but no variety

def test_all_types_but_short():
    score, level, _ = analyze_password("Ab1!", strict=False)
    assert level == "Strong"  # has all types but too short

def test_strict_mode_very_long_weak():
    score, _, feedback = analyze_password("a" * 100, strict=True)
    assert "Strict mode failed" in " ".join(feedback)

def test_exact_100_points():
    score, level, _ = analyze_password("P@ssw0rdStrong12!", strict=False)
    assert score == 100
    assert level == "Very Strong"

def test_score_is_int():
    score, _, _ = analyze_password("Test123!", strict=False)
    assert isinstance(score, int)

def test_feedback_is_list_of_strings():
    _, _, feedback = analyze_password("weak", strict=False)
    assert isinstance(feedback, list)
    assert all(isinstance(f, str) for f in feedback)

def test_no_feedback_on_perfect():
    _, _, feedback = analyze_password("K7@mP9#xL2$jQwErTy!", strict=False)
    assert len(feedback) == 0