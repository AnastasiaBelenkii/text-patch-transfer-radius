# Experiment Summary

Per-distance and per-family tables are the primary results. Any scalar summaries are informal diagnostics for comparing patch behavior under this fixed synthetic distribution.

Intervals are paired bootstrap 95% confidence intervals over examples for gain vs baseline. Small cells have wide intervals.

## Patch x Distance From Seed

| Patch | Distance | n | Accuracy | Gain vs baseline | 95% CI |
|---|---|---:|---:|---:|---:|
| Baseline prompt | frame_shift | 48 | 58.3% | +0.0% | +0.0%, +0.0% |
| Baseline prompt | lexical_near | 36 | 58.3% | +0.0% | +0.0%, +0.0% |
| Baseline prompt | seed | 21 | 71.4% | +0.0% | +0.0%, +0.0% |
| Baseline prompt | structural_analogy | 48 | 52.1% | +0.0% | +0.0%, +0.0% |
| Baseline prompt | unrelated | 63 | 93.7% | +0.0% | +0.0%, +0.0% |
| Length/style control | frame_shift | 48 | 66.7% | +8.3% | +2.1%, +16.7% |
| Length/style control | lexical_near | 36 | 58.3% | +0.0% | +0.0%, +0.0% |
| Length/style control | seed | 21 | 81.0% | +9.5% | +0.0%, +23.8% |
| Length/style control | structural_analogy | 48 | 54.2% | +2.1% | +0.0%, +6.2% |
| Length/style control | unrelated | 63 | 93.7% | +0.0% | +0.0%, +0.0% |
| Hidden-instruction targeted patch | frame_shift | 48 | 62.5% | +4.2% | +0.0%, +10.4% |
| Hidden-instruction targeted patch | lexical_near | 36 | 61.1% | +2.8% | +0.0%, +8.3% |
| Hidden-instruction targeted patch | seed | 21 | 85.7% | +14.3% | +0.0%, +28.6% |
| Hidden-instruction targeted patch | structural_analogy | 48 | 52.1% | +0.0% | +0.0%, +0.0% |
| Hidden-instruction targeted patch | unrelated | 63 | 93.7% | +0.0% | +0.0%, +0.0% |
| Credential targeted patch | frame_shift | 48 | 56.2% | -2.1% | -6.2%, +0.0% |
| Credential targeted patch | lexical_near | 36 | 61.1% | +2.8% | -5.6%, +13.9% |
| Credential targeted patch | seed | 21 | 76.2% | +4.8% | +0.0%, +14.3% |
| Credential targeted patch | structural_analogy | 48 | 50.0% | -2.1% | -6.2%, +0.0% |
| Credential targeted patch | unrelated | 63 | 93.7% | +0.0% | +0.0%, +0.0% |
| Rule-override targeted patch | frame_shift | 48 | 62.5% | +4.2% | +0.0%, +10.4% |
| Rule-override targeted patch | lexical_near | 36 | 66.7% | +8.3% | +0.0%, +16.7% |
| Rule-override targeted patch | seed | 21 | 76.2% | +4.8% | +0.0%, +14.3% |
| Rule-override targeted patch | structural_analogy | 48 | 60.4% | +8.3% | +2.1%, +16.7% |
| Rule-override targeted patch | unrelated | 63 | 93.7% | +0.0% | +0.0%, +0.0% |
| Overbroad caution patch | frame_shift | 48 | 62.5% | +4.2% | -14.6%, +22.9% |
| Overbroad caution patch | lexical_near | 36 | 58.3% | +0.0% | -25.0%, +22.2% |
| Overbroad caution patch | seed | 21 | 90.5% | +19.0% | +0.0%, +38.1% |
| Overbroad caution patch | structural_analogy | 48 | 62.5% | +10.4% | -8.3%, +27.1% |
| Overbroad caution patch | unrelated | 63 | 84.1% | -9.5% | -17.5%, -3.2% |

## Patch x Scenario Family

| Patch | Scenario family | n | Accuracy | Gain vs baseline | 95% CI |
|---|---|---:|---:|---:|---:|
| Baseline prompt | benign_instruction_discussion | 36 | 77.8% | +0.0% | +0.0%, +0.0% |
| Baseline prompt | credential_exfiltration | 24 | 20.8% | +0.0% | +0.0%, +0.0% |
| Baseline prompt | hidden_instruction_exfiltration | 24 | 25.0% | +0.0% | +0.0%, +0.0% |
| Baseline prompt | ordinary_help | 36 | 100.0% | +0.0% | +0.0%, +0.0% |
| Baseline prompt | public_security_education | 36 | 94.4% | +0.0% | +0.0%, +0.0% |
| Baseline prompt | rule_override | 24 | 37.5% | +0.0% | +0.0%, +0.0% |
| Baseline prompt | safety_policy_writing | 36 | 83.3% | +0.0% | +0.0%, +0.0% |
| Length/style control | benign_instruction_discussion | 36 | 77.8% | +0.0% | +0.0%, +0.0% |
| Length/style control | credential_exfiltration | 24 | 29.2% | +8.3% | +0.0%, +20.8% |
| Length/style control | hidden_instruction_exfiltration | 24 | 37.5% | +12.5% | +0.0%, +25.0% |
| Length/style control | ordinary_help | 36 | 100.0% | +0.0% | +0.0%, +0.0% |
| Length/style control | public_security_education | 36 | 94.4% | +0.0% | +0.0%, +0.0% |
| Length/style control | rule_override | 24 | 45.8% | +8.3% | +0.0%, +20.8% |
| Length/style control | safety_policy_writing | 36 | 83.3% | +0.0% | +0.0%, +0.0% |
| Hidden-instruction targeted patch | benign_instruction_discussion | 36 | 77.8% | +0.0% | +0.0%, +0.0% |
| Hidden-instruction targeted patch | credential_exfiltration | 24 | 20.8% | +0.0% | +0.0%, +0.0% |
| Hidden-instruction targeted patch | hidden_instruction_exfiltration | 24 | 50.0% | +25.0% | +8.3%, +41.7% |
| Hidden-instruction targeted patch | ordinary_help | 36 | 100.0% | +0.0% | +0.0%, +0.0% |
| Hidden-instruction targeted patch | public_security_education | 36 | 94.4% | +0.0% | +0.0%, +0.0% |
| Hidden-instruction targeted patch | rule_override | 24 | 37.5% | +0.0% | +0.0%, +0.0% |
| Hidden-instruction targeted patch | safety_policy_writing | 36 | 83.3% | +0.0% | +0.0%, +0.0% |
| Credential targeted patch | benign_instruction_discussion | 36 | 77.8% | +0.0% | +0.0%, +0.0% |
| Credential targeted patch | credential_exfiltration | 24 | 33.3% | +12.5% | +0.0%, +25.0% |
| Credential targeted patch | hidden_instruction_exfiltration | 24 | 25.0% | +0.0% | +0.0%, +0.0% |
| Credential targeted patch | ordinary_help | 36 | 100.0% | +0.0% | +0.0%, +0.0% |
| Credential targeted patch | public_security_education | 36 | 94.4% | +0.0% | +0.0%, +0.0% |
| Credential targeted patch | rule_override | 24 | 37.5% | +0.0% | +0.0%, +0.0% |
| Credential targeted patch | safety_policy_writing | 36 | 75.0% | -8.3% | -16.7%, +0.0% |
| Rule-override targeted patch | benign_instruction_discussion | 36 | 77.8% | +0.0% | +0.0%, +0.0% |
| Rule-override targeted patch | credential_exfiltration | 24 | 20.8% | +0.0% | +0.0%, +0.0% |
| Rule-override targeted patch | hidden_instruction_exfiltration | 24 | 25.0% | +0.0% | +0.0%, +0.0% |
| Rule-override targeted patch | ordinary_help | 36 | 100.0% | +0.0% | +0.0%, +0.0% |
| Rule-override targeted patch | public_security_education | 36 | 94.4% | +0.0% | +0.0%, +0.0% |
| Rule-override targeted patch | rule_override | 24 | 79.2% | +41.7% | +20.8%, +62.5% |
| Rule-override targeted patch | safety_policy_writing | 36 | 83.3% | +0.0% | +0.0%, +0.0% |
| Overbroad caution patch | benign_instruction_discussion | 36 | 55.6% | -22.2% | -36.1%, -8.3% |
| Overbroad caution patch | credential_exfiltration | 24 | 87.5% | +66.7% | +45.8%, +83.3% |
| Overbroad caution patch | hidden_instruction_exfiltration | 24 | 79.2% | +54.2% | +33.3%, +75.0% |
| Overbroad caution patch | ordinary_help | 36 | 94.4% | -5.6% | -13.9%, +0.0% |
| Overbroad caution patch | public_security_education | 36 | 52.8% | -41.7% | -58.3%, -27.8% |
| Overbroad caution patch | rule_override | 24 | 83.3% | +45.8% | +25.0%, +66.7% |
| Overbroad caution patch | safety_policy_writing | 36 | 55.6% | -27.8% | -41.7%, -13.9% |

## Targeted vs Non-Targeted

| Patch | Targeted n | Targeted acc | Targeted gain | Off-target n | Off-target acc | Off-target gain | Specificity |
|---|---:|---:|---:|---:|---:|---:|---:|
| Length/style control | 0 | NA | NA | 216 | 71.8% | +3.2% | NA |
| Hidden-instruction targeted patch | 24 | 50.0% | +25.0% | 192 | 74.0% | +0.0% | +25.0% |
| Credential targeted patch | 24 | 33.3% | +12.5% | 192 | 72.9% | -1.6% | +14.1% |
| Rule-override targeted patch | 24 | 79.2% | +41.7% | 192 | 72.4% | +0.0% | +41.7% |
| Overbroad caution patch | 72 | 83.3% | +55.6% | 144 | 64.6% | -24.3% | +79.9% |

## Boundary Behavior

Boundary cost is computed only on benign_boundary_allow cases: baseline accuracy minus patch accuracy.

| Patch | Benign boundary n | Benign boundary acc | Boundary cost | Hard boundary n | Hard boundary acc | Hard boundary gain |
|---|---:|---:|---:|---:|---:|---:|
| Baseline prompt | 36 | 77.8% | +0.0% | 24 | 25.0% | +0.0% |
| Length/style control | 36 | 77.8% | +0.0% | 24 | 33.3% | +8.3% |
| Hidden-instruction targeted patch | 36 | 77.8% | +0.0% | 24 | 29.2% | +4.2% |
| Credential targeted patch | 36 | 69.4% | +8.3% | 24 | 25.0% | +0.0% |
| Rule-override targeted patch | 36 | 77.8% | +0.0% | 24 | 33.3% | +8.3% |
| Overbroad caution patch | 36 | 16.7% | +61.1% | 24 | 66.7% | +41.7% |

## Surface-Cue Behavior

| Patch | Cue-label agreement | n | Accuracy | Gain vs baseline | 95% CI |
|---|---:|---:|---:|---:|---:|
| Baseline prompt | false | 60 | 56.7% | +0.0% | +0.0%, +0.0% |
| Baseline prompt | true | 156 | 73.1% | +0.0% | +0.0%, +0.0% |
| Length/style control | false | 60 | 60.0% | +3.3% | +0.0%, +8.3% |
| Length/style control | true | 156 | 76.3% | +3.2% | +0.6%, +6.4% |
| Hidden-instruction targeted patch | false | 60 | 58.3% | +1.7% | +0.0%, +5.0% |
| Hidden-instruction targeted patch | true | 156 | 76.3% | +3.2% | +0.6%, +6.4% |
| Credential targeted patch | false | 60 | 51.7% | -5.0% | -10.0%, +0.0% |
| Credential targeted patch | true | 156 | 75.0% | +1.9% | +0.0%, +4.5% |
| Rule-override targeted patch | false | 60 | 60.0% | +3.3% | +0.0%, +8.3% |
| Rule-override targeted patch | true | 156 | 78.2% | +5.1% | +1.9%, +9.0% |
| Overbroad caution patch | false | 60 | 36.7% | -20.0% | -36.7%, -1.7% |
| Overbroad caution patch | true | 156 | 84.0% | +10.9% | +3.2%, +19.2% |

| Patch | Surface cue | n | Accuracy | Gain vs baseline | 95% CI |
|---|---|---:|---:|---:|---:|
| Baseline prompt | allow_like | 69 | 68.1% | +0.0% | +0.0%, +0.0% |
| Baseline prompt | block_like | 84 | 50.0% | +0.0% | +0.0%, +0.0% |
| Baseline prompt | neutral | 63 | 93.7% | +0.0% | +0.0%, +0.0% |
| Length/style control | allow_like | 69 | 71.0% | +2.9% | +0.0%, +7.2% |
| Length/style control | block_like | 84 | 56.0% | +6.0% | +2.4%, +11.9% |
| Length/style control | neutral | 63 | 93.7% | +0.0% | +0.0%, +0.0% |
| Hidden-instruction targeted patch | allow_like | 69 | 69.6% | +1.4% | +0.0%, +4.3% |
| Hidden-instruction targeted patch | block_like | 84 | 56.0% | +6.0% | +1.2%, +11.9% |
| Hidden-instruction targeted patch | neutral | 63 | 93.7% | +0.0% | +0.0%, +0.0% |
| Credential targeted patch | allow_like | 69 | 68.1% | +0.0% | +0.0%, +0.0% |
| Credential targeted patch | block_like | 84 | 50.0% | +0.0% | -6.0%, +6.0% |
| Credential targeted patch | neutral | 63 | 93.7% | +0.0% | +0.0%, +0.0% |
| Rule-override targeted patch | allow_like | 69 | 71.0% | +2.9% | +0.0%, +7.2% |
| Rule-override targeted patch | block_like | 84 | 59.5% | +9.5% | +3.6%, +16.7% |
| Rule-override targeted patch | neutral | 63 | 93.7% | +0.0% | +0.0%, +0.0% |
| Overbroad caution patch | allow_like | 69 | 72.5% | +4.3% | -7.2%, +17.4% |
| Overbroad caution patch | block_like | 84 | 59.5% | +9.5% | -8.3%, +26.2% |
| Overbroad caution patch | neutral | 63 | 84.1% | -9.5% | -17.5%, -3.2% |

## Qualitative Patch Profiles

| Patch | Profile |
|---|---|
| Baseline prompt | dead patch |
| Length/style control | generic caution patch |
| Hidden-instruction targeted patch | targeted and specific patch |
| Credential targeted patch | local patch |
| Rule-override targeted patch | structural patch |
| Overbroad caution patch | overbroad patch |
