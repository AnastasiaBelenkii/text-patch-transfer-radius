#!/usr/bin/env python3
"""Run the text-patch transfer-radius experiment."""

from __future__ import annotations

import argparse
import json
import os
import random
import sys
from pathlib import Path

from text_patch_transfer_radius.dataset import (
    build_cases,
    write_case_audit,
    write_cases_jsonl,
)
from text_patch_transfer_radius.metrics import (
    assign_profiles,
    compute_boundary_behavior_rows,
    compute_summary_rows,
    compute_surface_cue_rows,
    compute_targeted_rows,
    write_dataset_stats,
    write_summary_csv,
    write_summary_md,
)
from text_patch_transfer_radius.model_adapters import (
    MockPolicyClassifier,
    OpenAIPolicyClassifier,
)
from text_patch_transfer_radius.patches import get_patches, targeted_by_patch
from text_patch_transfer_radius.prompts import build_prompt, prompt_hash
from text_patch_transfer_radius.validation import validate_cases


DEFAULT_SEED = 2026


def main() -> int:
    args = parse_args()
    root = Path(__file__).resolve().parent
    data_path = root / "data" / "eval_cases.jsonl"
    audit_path = root / "data" / "case_audit.md"
    results_dir = root / "results"

    load_env_file(root / ".env")

    cases = build_cases()
    patches = get_patches()

    write_cases_jsonl(data_path, cases)
    write_case_audit(audit_path, cases)

    if not args.skip_validation:
        errors = validate_cases(cases, patches)
        if errors:
            print("Dataset validation failed:", file=sys.stderr)
            for error in errors:
                print(f"- {error}", file=sys.stderr)
            return 1

    write_dataset_stats(results_dir / "dataset_stats.md", cases, patches)

    try:
        adapter = build_adapter(args)
    except RuntimeError as exc:
        print(str(exc), file=sys.stderr)
        return 2

    try:
        records = run_evaluations(
            cases=cases,
            patches=patches,
            adapter=adapter,
            seed=args.seed,
        )
    except RuntimeError as exc:
        print(str(exc), file=sys.stderr)
        return 2

    write_raw_results(results_dir / "raw_results.jsonl", records)
    summary_rows = compute_summary_rows(records, patches)
    targeted_rows = compute_targeted_rows(records, patches)
    boundary_rows = compute_boundary_behavior_rows(records, patches)
    surface_rows = compute_surface_cue_rows(records, patches)
    profiles = assign_profiles(records, patches, targeted_rows, boundary_rows)

    write_summary_csv(
        results_dir / "summary.csv",
        summary_rows=summary_rows,
        targeted_rows=targeted_rows,
        boundary_rows=boundary_rows,
        surface_rows=surface_rows,
    )
    write_summary_md(
        results_dir / "summary.md",
        summary_rows=summary_rows,
        targeted_rows=targeted_rows,
        boundary_rows=boundary_rows,
        surface_rows=surface_rows,
        profiles=profiles,
    )

    print(f"Wrote {data_path.relative_to(root)}")
    print(f"Wrote {audit_path.relative_to(root)}")
    print(f"Wrote {results_dir.relative_to(root)}/raw_results.jsonl")
    print(f"Wrote {results_dir.relative_to(root)}/summary.csv")
    print(f"Wrote {results_dir.relative_to(root)}/summary.md")
    print(f"Wrote {results_dir.relative_to(root)}/dataset_stats.md")
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Measure transfer radius of short natural-language text patches."
    )
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument(
        "--mock",
        action="store_true",
        help="Use the deterministic rule-based simulator.",
    )
    mode.add_argument(
        "--model",
        type=str,
        help="OpenAI model name to evaluate with OPENAI_API_KEY.",
    )
    parser.add_argument(
        "--temperature",
        type=float,
        default=0.0,
        help="API temperature. The mock path ignores this.",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=DEFAULT_SEED,
        help="Fixed seed for evaluation condition order.",
    )
    parser.add_argument(
        "--skip-validation",
        action="store_true",
        help="Skip dataset validation before model evaluation.",
    )
    return parser.parse_args()


def build_adapter(args: argparse.Namespace):
    if args.model:
        return OpenAIPolicyClassifier(args.model, temperature=args.temperature)
    return MockPolicyClassifier()


def load_env_file(path: Path) -> None:
    """Load simple KEY=VALUE entries from .env without overriding the process env."""

    if not path.exists():
        return
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip("\"'")
        if key and key not in os.environ:
            os.environ[key] = value


def run_evaluations(
    cases: list[dict],
    patches: list[dict],
    adapter,
    seed: int,
) -> list[dict]:
    rng = random.Random(seed)
    records = []
    for case in cases:
        condition_order = list(patches)
        rng.shuffle(condition_order)
        for patch in condition_order:
            prompt = build_prompt(case, patch)
            prediction = adapter.predict(case, patch, prompt)
            records.append(
                {
                    "case_id": case["id"],
                    "patch_id": patch["patch_id"],
                    "distance_from_seed": case["distance_from_seed"],
                    "scenario_family": case["scenario_family"],
                    "surface_frame": case["surface_frame"],
                    "surface_cue": case["surface_cue"],
                    "cue_label_agreement": case["cue_label_agreement"],
                    "boundary_type": case["boundary_type"],
                    "boundary_risk": case["boundary_risk"],
                    "label": case["label"],
                    "prediction": prediction.prediction,
                    "correct": prediction.prediction == case["label"],
                    "model_name": adapter.model_name,
                    "mock_or_api": adapter.mode,
                    "prompt_hash": prompt_hash(prompt),
                    "condition_id": f"{case['id']}::{patch['patch_id']}",
                    "targeted_by_patch": targeted_by_patch(case, patch),
                    "raw_output": prediction.raw_output,
                }
            )
    return records


def write_raw_results(path: Path, records: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for record in records:
            f.write(json.dumps(record, sort_keys=True) + "\n")


if __name__ == "__main__":
    raise SystemExit(main())
