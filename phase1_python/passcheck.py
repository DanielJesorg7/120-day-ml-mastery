# passcheck.py
import argparse
import string
import secrets
import sys

parser = argparse.ArgumentParser(description="Password Strength Tester")

# Main password (required unless generating)
parser.add_argument("password", nargs="?", help="Password to check")

# Two modes: check strength or generate
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("--check", action="store_true", help="Check password strength")
group.add_argument("--generate", type=int, metavar="LENGTH", help="Generate secure password")

# Options
parser.add_argument("--strict", action="store_true", help="Use strict rules (12+ chars, all types required)")
parser.add_argument("--score", action="store_true", help="Show numeric score instead of text")

args = parser.parse_args()

# =============================================
# 1. Generate mode
# =============================================
if args.generate:
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*()"
    password = ''.join(secrets.choice(alphabet) for _ in range(args.generate))
    print(password)
    sys.exit(0)

# =============================================
# 2. Check mode (password given)
# =============================================
if not args.password:
    parser.error("Password is required when using --check")

pw = args.password
length = len(pw)
score = 0
feedback = []

# Length bonus
if length >= 12:
    score += 25
elif length >= 8:
    score += 15
elif length >= 6:
    score += 5

# Character type checks
has_lower = any(c.islower() for c in pw)
has_upper = any(c.isupper() for c in pw)
has_digit = any(c.isdigit() for c in pw)
has_special = any(c in "!@#$%^&*()" for c in pw)

if has_lower:   score += 15
if has_upper:   score += 20
if has_digit:   score += 20
if has_special: score += 20

# Strict mode
if args.strict:
    if length < 12:
        feedback.append("Too short (need 12+)")
    if not (has_lower and has_upper and has_digit and has_special):
        feedback.append("Missing required character types")

# Final strength
if args.score:
    print(score)
else:
    if args.strict:
        strength = "Strong" if score >= 90 and len(feedback) == 0 else "Weak"
    else:
        if score >= 85:
            strength = "Very Strong"
        elif score >= 70:
            strength = "Strong"
        elif score >= 50:
            strength = "Medium"
        else:
            strength = "Weak"
    print(strength)
    if feedback:
        for msg in feedback:
            print("  →", msg)