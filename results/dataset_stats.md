# Dataset Statistics

Total cases: 216
Validation status: passed

## Counts by Scenario Family

| Scenario family | Cases |
|---|---:|
| benign_instruction_discussion | 36 |
| credential_exfiltration | 24 |
| hidden_instruction_exfiltration | 24 |
| ordinary_help | 36 |
| public_security_education | 36 |
| rule_override | 24 |
| safety_policy_writing | 36 |

## Counts by Distance From Seed

| Distance | Cases |
|---|---:|
| frame_shift | 48 |
| lexical_near | 36 |
| seed | 21 |
| structural_analogy | 48 |
| unrelated | 63 |

## Counts by Label

| Label | Cases |
|---|---:|
| ALLOW | 144 |
| BLOCK | 72 |

## Label Balance by Scenario Family

| Scenario family | ALLOW | BLOCK |
|---|---:|---:|
| benign_instruction_discussion | 36 | 0 |
| credential_exfiltration | 0 | 24 |
| hidden_instruction_exfiltration | 0 | 24 |
| ordinary_help | 36 | 0 |
| public_security_education | 36 | 0 |
| rule_override | 0 | 24 |
| safety_policy_writing | 36 | 0 |

## Label Balance by Distance From Seed

| Distance | ALLOW | BLOCK |
|---|---:|---:|
| frame_shift | 24 | 24 |
| lexical_near | 24 | 12 |
| seed | 9 | 12 |
| structural_analogy | 24 | 24 |
| unrelated | 63 | 0 |

## Counts by Boundary Type

| Boundary type | Cases |
|---|---:|
| benign_boundary_allow | 36 |
| hard_boundary_block | 24 |
| none | 156 |

## Counts by Surface Cue

| Surface cue | Cases |
|---|---:|
| allow_like | 69 |
| block_like | 84 |
| neutral | 63 |

## Counts by Cue-Label Agreement

| cue_label_agreement | Cases |
|---|---:|
| false | 60 |
| true | 156 |

## Contrast Counts

block_like ALLOW cases: 36
allow_like BLOCK cases: 24

The lexical_near, frame_shift, structural_analogy, boundary, and surface-cue categories are author-defined synthetic categories, not objective semantic distances.
