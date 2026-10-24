#!/usr/bin/env python3
"""Validation script for Tech & AI Weekly digest draft."""

import re
import sys
from pathlib import Path

FORBIDDEN_WORDS = [
    "主播", "视频", "节目", "录音", "转录", "字幕", "原文",
    "上述内容", "这期", "本期节目", "文中提到", "作者提到",
    "他说", "她说", "震撼发布", "彻底颠覆", "史诗级", "吊打",
]

REQUIRED_SECTIONS = [
    r"^## 0\s+",
    r"^## 1\s+",
    r"^## 2\s+",
    r"^## 3\s+",
]


def validate_text(text: str) -> list[str]:
    errors = []
    lines = text.strip().splitlines()

    # 1. Check Title (H1)
    h1_lines = [line for line in lines if line.startswith("# ")]
    if not h1_lines:
        errors.append("Missing H1 title (# Title).")
    else:
        title = h1_lines[0].strip()
        if not re.search(r"\b20\d{6}\b", title):
            errors.append(f"H1 title must end with target date in YYYYMMDD format (got: {title})")

    # 2. Check Required Sections
    for pattern in REQUIRED_SECTIONS:
        if not any(re.search(pattern, line) for line in lines):
            errors.append(f"Missing required section header matching: {pattern}")

    # 3. Check Forbidden words
    for word in FORBIDDEN_WORDS:
        count = text.count(word)
        if count > 0:
            errors.append(f"Found forbidden or sensationalist word '{word}' ({count} times).")

    # 4. First-person limit
    first_person_count = text.count("我") + text.count("我们")
    if first_person_count > 12:
        errors.append(f"First-person pronoun count exceeds limit: {first_person_count} > 12.")

    # 5. Length check
    char_count = len(re.sub(r"\s+", "", text))
    if char_count < 1200:
        errors.append(f"Article is too terse: {char_count} characters (minimum 1200 recommended).")

    return errors


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 validate_tech_weekly.py <markdown_file>")
        sys.exit(1)

    file_path = Path(sys.argv[1])
    if not file_path.exists():
        print(f"File not found: {file_path}")
        sys.exit(1)

    content = file_path.read_text(encoding="utf-8")
    errors = validate_text(content)

    if errors:
        print("Validation FAILED with the following errors:")
        for err in errors:
            print(f"  - {err}")
        sys.exit(1)
    else:
        print("Validation PASSED successfully.")
        sys.exit(0)


if __name__ == "__main__":
    main()
