#!/usr/bin/env python3
"""
Password Analyzer – Day 01 of 120-Day ML Mastery
Secure password generator + strength checker with strict mode and combo support.
"""

import argparse
import string
import secrets
import sys
from typing import Tuple

def generate_password(length: int) -> str:
    """Generate cryptographically secure password."""
    if length < 8:
        print("Error: Minimum length is 8", file=sys.stderr)
        sys.exit(1)
    
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(alphabet) for _ in range(length))

def analyze_password(password: str, strict: bool = False) -> Tuple[int, str, list]:
    """Return (score, level, feedback_list)."""
    score = 0
    feedback = []

    # Length
    if len(password) >= 12:
        score += 25
    elif len(password) >= 8:
        score += 15
    elif len(password) >= 6:
        score += 5
    else:
        feedback.append("Too short – aim for 12+ characters")

    # Character types
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    if has_lower:   score += 15
    else:           feedback.append("Add lowercase letters")
    if has_upper:   score += 20
    else:           feedback.append("Add uppercase letters")
    if has_digit:   score += 20
    else:           feedback.append("Add digits")
    if has_special: score += 20
    else:           feedback.append("Add symbols (!@#$ etc)")

    # Strict mode
    if strict and (len(password) < 12 or not all([has_lower, has_upper, has_digit, has_special])):
        score = max(0, score - 40)
        feedback.append("Strict mode failed: 12+ chars + all types required")

    # Level
    if score >= 90:
        level = "Very Strong"
    elif score >= 70:
        level = "Strong"
    elif score >= 50:
        level = "Medium"
    else:
        level = "Weak"

    return score, level, feedback

def main():
    parser = argparse.ArgumentParser(description="Password Analyzer – generate or check")
    parser.add_argument("password", nargs="?", help="Password to check")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-g", "--generate", type=int, metavar="LEN", help="Generate password")
    group.add_argument("-c", "--check", action="store_true", help="Check mode")
    parser.add_argument("--score", action="store_true", help="Show numeric score")
    parser.add_argument("--strict", action="store_true", help="Strict rules")

    args = parser.parse_args()

    if args.generate is not None:
        pwd = generate_password(args.generate)
        print(pwd)
        if args.score or args.strict:
            score, level, feedback = analyze_password(pwd, args.strict)
            if args.score:
                print(f"Score: {score}/100")
            print(level)
            if not feedback:
                print("   Perfect! No improvements needed.")
            else:
                for line in feedback:
                    print(f"   {line}")
    
    elif args.check:
        if not args.password:
            parser.error("Password required in check mode")
        score, level, feedback = analyze_password(args.password, args.strict)
        if args.score:
            print(f"Score: {score}/100")
        print(level)
        for line in feedback:
            print(f"   {line}")
        if not feedback:
            print("   Perfect! No improvements needed.")

if __name__ == "__main__":
    main()
    