# Password Analyzer – Day 1 of 120-Day ML Mastery

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Tests](https://img.shields.io/badge/Tests-22%2F22%20Passed-brightgreen)](https://github.com/DanielJesorg7/120-day-ml-mastery/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A CLI tool to **generate secure passwords** or **analyze strength** with scoring, feedback, and strict mode. Built with `argparse`, `secrets`, and pytest for 100% coverage. Part of my [120-Day ML Mastery](https://github.com/DanielJesorg7/120-day-ml-mastery) – Phase 1: Python fundamentals.

![Demo](demo.png)  
*(Carbon screenshot of combo command – add yours here for max impact.)*

## Features
- **Generate**: Cryptographically secure passwords (min 8 chars, all types).
- **Analyze**: Score (0-100) based on length + variety; levels (Weak → Very Strong).
- **Strict Mode**: Penalizes short/missing types (-40 points).
- **Combo**: Generate + auto-analyze in one command.
- **Tested**: 22/22 pytest green (see `test_analyzer.py`).

## Installation
```bash
git clone https://github.com/DanielJesorg7/120-day-ml-mastery.git
cd 120-day-ml-mastery/phase1_python/<img width="1952" height="4358" alt="carbon (3)" src="https://github.com/user-attachments/assets/d74569cc-d859-472b-bbbd-8f7a0d28d208" />
day01/password_analyzer
python analyzer.py --help
