#!/usr/bin/env python3
"""Run the text-patch transfer-radius experiment."""

from __future__ import annotations

import argparse
import json
import random
import sys
from pathlib import Path

from text_patch_transfer_radius.dataset import build_cases, write_cases_jsonl
from text_patch_transfer_radius.metrics import (
    assign_profiles,
    compute_boundary_cost_rows,
    compute_summary_rows,
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


DEFAULT_SEED = 2026


def main() -> int:
    args = parse_args()
    root = Path(__file__).resolve().parent
    data_path = root / "data" / "eval_cases.jsonl"
    results_dir = root / "results"

    cases = build_cases()
    patches = get_patches()

    write_cases_jsonl(data_path, cases)
    write_dataset_stats(results_dir / "dataset_stats.md", cases)

    try:
        adapter = build_adapter(args)
    except RuntimeError as exc:
        print(str(exc), file=sys.stderr)
        return 2

    records = run_evaluations(
        cases=cases,
        patches=patches,
        adapter=adapter,
        seed=args.seed,
    )

    write_raw_results(results_dir / "raw_results.jsonl", records)
    summary_rows = compute_summary_rows(records, patches)
    targeted_rows = compute_targeted_rows(records, patches)
    boundary_rows = compute_boundary_cost_rows(records, patches)
    profiles = assign_profiles(records, patches, boundary_rows)

    write_summary_csv(results_dir / "summary.csv", summary_rows)
    write_summary_md(
        results_dir / "summary.md",
        summary_rows=summary_rows,
        targeted_rows=targeted_rows,
        boundary_rows=boundary_rows,
        profiles=profiles,
    )

    print(f"Wrote {data_path.relative_to(root)}")
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
    return parser.parse_args()


def build_adapter(args: argparse.Namespace):
    if args.model:
        return OpenAIPolicyClassifier(args.model, temperature=args.temperature)
    return MockPolicyClassifier()


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
                    "split": case["split"],
                    "scenario_family": case["scenario_family"],
                    "surface_frame": case["surface_frame"],
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
