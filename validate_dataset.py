#!/usr/bin/env python3
"""Validate data/eval_cases.jsonl."""

from __future__ import annotations

import argparse
from pathlib import Path

from text_patch_transfer_radius.dataset import load_cases_jsonl
from text_patch_transfer_radius.patches import get_patches
from text_patch_transfer_radius.validation import validate_cases


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate the synthetic eval dataset.")
    parser.add_argument(
        "--path",
        type=Path,
        default=Path("data/eval_cases.jsonl"),
        help="Path to eval_cases.jsonl.",
    )
    args = parser.parse_args()

    cases = load_cases_jsonl(args.path)
    errors = validate_cases(cases, get_patches())
    if errors:
        print("Dataset validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Dataset validation passed: {len(cases)} cases")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
