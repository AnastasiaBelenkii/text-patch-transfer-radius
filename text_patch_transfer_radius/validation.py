"""Dataset validation for the contrast-set eval."""

from __future__ import annotations

import re
from collections import Counter

from text_patch_transfer_radius.dataset import (
    BOUNDARY_TYPE_VALUES,
    DISTANCE_VALUES,
    LABELS,
    MAJOR_SCENARIO_FAMILIES,
    SURFACE_CUE_VALUES,
)


REQUIRED_FIELDS = {
    "id",
    "text",
    "label",
    "scenario_family",
    "distance_from_seed",
    "surface_frame",
    "surface_cue",
    "cue_label_agreement",
    "boundary_type",
    "boundary_risk",
    "rationale",
}

UNSAFE_TEXT_PATTERNS = [
    (re.compile(r"sk-[A-Za-z0-9]{10,}"), "OpenAI-style API key"),
    (re.compile(r"AKIA[0-9A-Z]{16}"), "AWS-style access key"),
    (re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"), "private key block"),
    (re.compile(r"\b(password|token|api[_ -]?key)\s*=\s*['\"][^'\"]+['\"]", re.I), "credential assignment"),
    (re.compile(r"\bmalware\b", re.I), "malware instruction topic"),
    (re.compile(r"\bshellcode\b", re.I), "shellcode topic"),
    (re.compile(r"\bweapon\b|\bbomb\b", re.I), "weapon topic"),
]


def validate_cases(cases: list[dict], patches: list[dict]) -> list[str]:
    """Return validation errors. An empty list means the dataset passed."""

    errors: list[str] = []
    seen_texts: set[str] = set()
    seen_ids: set[str] = set()

    for index, case in enumerate(cases, start=1):
        missing = REQUIRED_FIELDS - set(case)
        if missing:
            errors.append(f"case {index} missing fields: {sorted(missing)}")
            continue

        case_id = case["id"]
        if case_id in seen_ids:
            errors.append(f"duplicate id: {case_id}")
        seen_ids.add(case_id)

        text = case["text"].strip()
        lowered_text = text.lower()
        if lowered_text in seen_texts:
            errors.append(f"duplicate text: {case_id}: {text}")
        seen_texts.add(lowered_text)

        if case["label"] not in LABELS:
            errors.append(f"{case_id}: invalid label {case['label']!r}")
        if case["distance_from_seed"] not in DISTANCE_VALUES:
            errors.append(
                f"{case_id}: invalid distance_from_seed {case['distance_from_seed']!r}"
            )
        if case["boundary_type"] not in BOUNDARY_TYPE_VALUES:
            errors.append(f"{case_id}: invalid boundary_type {case['boundary_type']!r}")
        if case["surface_cue"] not in SURFACE_CUE_VALUES:
            errors.append(f"{case_id}: invalid surface_cue {case['surface_cue']!r}")
        if not isinstance(case["cue_label_agreement"], bool):
            errors.append(f"{case_id}: cue_label_agreement must be boolean")
        if not isinstance(case["boundary_risk"], bool):
            errors.append(f"{case_id}: boundary_risk must be boolean")
        if case["boundary_risk"] != (case["boundary_type"] != "none"):
            errors.append(f"{case_id}: boundary_risk does not match boundary_type")
        if (
            case["boundary_type"] == "benign_boundary_allow"
            and case["label"] != "ALLOW"
        ):
            errors.append(f"{case_id}: benign_boundary_allow must have label ALLOW")
        if case["boundary_type"] == "hard_boundary_block" and case["label"] != "BLOCK":
            errors.append(f"{case_id}: hard_boundary_block must have label BLOCK")

        expected_agreement = _expected_cue_agreement(case["surface_cue"], case["label"])
        if case["cue_label_agreement"] != expected_agreement:
            errors.append(f"{case_id}: cue_label_agreement is inconsistent")

        for pattern, description in UNSAFE_TEXT_PATTERNS:
            if pattern.search(text):
                errors.append(f"{case_id}: possible unsafe content: {description}")

    errors.extend(_validate_coverage(cases, patches))
    return errors


def validation_status(cases: list[dict], patches: list[dict]) -> str:
    """Human-readable status for reports."""

    errors = validate_cases(cases, patches)
    if errors:
        return f"failed ({len(errors)} error(s))"
    return "passed"


def _validate_coverage(cases: list[dict], patches: list[dict]) -> list[str]:
    errors: list[str] = []
    boundary_counts = Counter(case["boundary_type"] for case in cases)
    family_counts = Counter(case["scenario_family"] for case in cases)

    if boundary_counts["benign_boundary_allow"] < 30:
        errors.append("expected at least 30 benign_boundary_allow cases")
    if boundary_counts["hard_boundary_block"] < 20:
        errors.append("expected at least 20 hard_boundary_block cases")

    for family in sorted(MAJOR_SCENARIO_FAMILIES):
        if family_counts[family] < 20:
            errors.append(f"scenario_family {family} has fewer than 20 cases")

    block_like_allow = sum(
        1 for case in cases if case["surface_cue"] == "block_like" and case["label"] == "ALLOW"
    )
    allow_like_block = sum(
        1 for case in cases if case["surface_cue"] == "allow_like" and case["label"] == "BLOCK"
    )
    if block_like_allow == 0:
        errors.append("expected at least one block_like ALLOW case")
    if allow_like_block == 0:
        errors.append("expected at least one allow_like BLOCK case")

    for patch in patches:
        if patch["is_control"]:
            continue
        targeted = [
            case
            for case in cases
            if case["scenario_family"] in patch["intended_scenario_families"]
        ]
        non_targeted = [
            case
            for case in cases
            if case["scenario_family"] not in patch["intended_scenario_families"]
        ]
        if len(targeted) < 20:
            errors.append(f"{patch['patch_id']} has fewer than 20 targeted cases")
        if len(non_targeted) < 20:
            errors.append(f"{patch['patch_id']} has fewer than 20 non-targeted cases")

    return errors


def _expected_cue_agreement(surface_cue: str, label: str) -> bool:
    if surface_cue == "neutral":
        return True
    return (surface_cue == "block_like" and label == "BLOCK") or (
        surface_cue == "allow_like" and label == "ALLOW"
    )
