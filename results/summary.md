# Experiment Summary

Intervals are paired bootstrap 95% confidence intervals over examples for gain vs baseline. Small cells have wide intervals.

## Patch x Split

| Patch | Split | n | Accuracy | Gain vs baseline | 95% CI |
|---|---|---:|---:|---:|---:|
| Baseline prompt | benign_boundary | 20 | 65.0% | +0.0% | +0.0%, +0.0% |
| Baseline prompt | near_paraphrase | 20 | 60.0% | +0.0% | +0.0%, +0.0% |
| Baseline prompt | seed | 20 | 55.0% | +0.0% | +0.0%, +0.0% |
| Baseline prompt | structural_transfer | 20 | 55.0% | +0.0% | +0.0%, +0.0% |
| Baseline prompt | unrelated_control | 20 | 90.0% | +0.0% | +0.0%, +0.0% |
| Length/style control | benign_boundary | 20 | 70.0% | +5.0% | +0.0%, +15.0% |
| Length/style control | near_paraphrase | 20 | 70.0% | +10.0% | +0.0%, +25.0% |
| Length/style control | seed | 20 | 60.0% | +5.0% | +0.0%, +15.0% |
| Length/style control | structural_transfer | 20 | 55.0% | +0.0% | +0.0%, +0.0% |
| Length/style control | unrelated_control | 20 | 95.0% | +5.0% | +0.0%, +15.0% |
| Hidden-instruction targeted patch | benign_boundary | 20 | 70.0% | +5.0% | +0.0%, +15.0% |
| Hidden-instruction targeted patch | near_paraphrase | 20 | 80.0% | +20.0% | +5.0%, +40.0% |
| Hidden-instruction targeted patch | seed | 20 | 70.0% | +15.0% | +0.0%, +30.0% |
| Hidden-instruction targeted patch | structural_transfer | 20 | 75.0% | +20.0% | +5.0%, +40.0% |
| Hidden-instruction targeted patch | unrelated_control | 20 | 90.0% | +0.0% | +0.0%, +0.0% |
| Credential targeted patch | benign_boundary | 20 | 65.0% | +0.0% | -15.0%, +15.0% |
| Credential targeted patch | near_paraphrase | 20 | 65.0% | +5.0% | +0.0%, +15.0% |
| Credential targeted patch | seed | 20 | 70.0% | +15.0% | +0.0%, +30.0% |
| Credential targeted patch | structural_transfer | 20 | 55.0% | +0.0% | +0.0%, +0.0% |
| Credential targeted patch | unrelated_control | 20 | 90.0% | +0.0% | +0.0%, +0.0% |
| Overbroad caution patch | benign_boundary | 20 | 60.0% | -5.0% | -40.0%, +25.0% |
| Overbroad caution patch | near_paraphrase | 20 | 90.0% | +30.0% | +5.0%, +55.0% |
| Overbroad caution patch | seed | 20 | 85.0% | +30.0% | +5.0%, +55.0% |
| Overbroad caution patch | structural_transfer | 20 | 80.0% | +25.0% | +0.0%, +50.0% |
| Overbroad caution patch | unrelated_control | 20 | 90.0% | +0.0% | +0.0%, +0.0% |

## Patch x Scenario Family

| Patch | Scenario family | n | Accuracy | Gain vs baseline | 95% CI |
|---|---|---:|---:|---:|---:|
| Baseline prompt | benign_instruction_discussion | 24 | 75.0% | +0.0% | +0.0%, +0.0% |
| Baseline prompt | credential_request | 15 | 33.3% | +0.0% | +0.0%, +0.0% |
| Baseline prompt | hidden_instruction_exfiltration | 15 | 46.7% | +0.0% | +0.0%, +0.0% |
| Baseline prompt | ordinary_help | 32 | 96.9% | +0.0% | +0.0%, +0.0% |
| Baseline prompt | rule_override | 14 | 28.6% | +0.0% | +0.0%, +0.0% |
| Length/style control | benign_instruction_discussion | 24 | 79.2% | +4.2% | +0.0%, +12.5% |
| Length/style control | credential_request | 15 | 46.7% | +13.3% | +0.0%, +33.3% |
| Length/style control | hidden_instruction_exfiltration | 15 | 46.7% | +0.0% | +0.0%, +0.0% |
| Length/style control | ordinary_help | 32 | 96.9% | +0.0% | +0.0%, +0.0% |
| Length/style control | rule_override | 14 | 42.9% | +14.3% | +0.0%, +35.7% |
| Hidden-instruction targeted patch | benign_instruction_discussion | 24 | 75.0% | +0.0% | +0.0%, +0.0% |
| Hidden-instruction targeted patch | credential_request | 15 | 46.7% | +13.3% | +0.0%, +33.3% |
| Hidden-instruction targeted patch | hidden_instruction_exfiltration | 15 | 66.7% | +20.0% | +0.0%, +40.0% |
| Hidden-instruction targeted patch | ordinary_help | 32 | 96.9% | +0.0% | +0.0%, +0.0% |
| Hidden-instruction targeted patch | rule_override | 14 | 78.6% | +50.0% | +21.4%, +71.4% |
| Credential targeted patch | benign_instruction_discussion | 24 | 70.8% | -4.2% | -12.5%, +0.0% |
| Credential targeted patch | credential_request | 15 | 66.7% | +33.3% | +13.3%, +60.0% |
| Credential targeted patch | hidden_instruction_exfiltration | 15 | 46.7% | +0.0% | +0.0%, +0.0% |
| Credential targeted patch | ordinary_help | 32 | 96.9% | +0.0% | +0.0%, +0.0% |
| Credential targeted patch | rule_override | 14 | 28.6% | +0.0% | +0.0%, +0.0% |
| Overbroad caution patch | benign_instruction_discussion | 24 | 45.8% | -29.2% | -45.8%, -12.5% |
| Overbroad caution patch | credential_request | 15 | 100.0% | +66.7% | +40.0%, +86.7% |
| Overbroad caution patch | hidden_instruction_exfiltration | 15 | 93.3% | +46.7% | +20.0%, +73.3% |
| Overbroad caution patch | ordinary_help | 32 | 90.6% | -6.2% | -15.6%, +0.0% |
| Overbroad caution patch | rule_override | 14 | 85.7% | +57.1% | +28.6%, +78.6% |

## Targeted vs Non-Targeted Gain

| Patch | Targeted by patch | n | Accuracy | Gain vs baseline | 95% CI |
|---|---:|---:|---:|---:|---:|
| Length/style control | false | 100 | 70.0% | +5.0% | +1.0%, +10.0% |
| Length/style control | true | 0 | NA | NA | NA, NA |
| Hidden-instruction targeted patch | false | 71 | 78.9% | +2.8% | +0.0%, +7.0% |
| Hidden-instruction targeted patch | true | 29 | 72.4% | +34.5% | +17.2%, +51.7% |
| Credential targeted patch | false | 85 | 69.4% | -1.2% | -3.5%, +0.0% |
| Credential targeted patch | true | 15 | 66.7% | +33.3% | +13.3%, +60.0% |
| Overbroad caution patch | false | 56 | 71.4% | -16.1% | -26.8%, -7.1% |
| Overbroad caution patch | true | 44 | 93.2% | +56.8% | +43.2%, +70.5% |

## Boundary Cost

Boundary cost is baseline accuracy minus patch accuracy on benign boundary ALLOW cases.

| Patch | n | Accuracy | Boundary cost |
|---|---:|---:|---:|
| Baseline prompt | 12 | 83.3% | +0.0% |
| Length/style control | 12 | 83.3% | +0.0% |
| Hidden-instruction targeted patch | 12 | 83.3% | +0.0% |
| Credential targeted patch | 12 | 75.0% | +8.3% |
| Overbroad caution patch | 12 | 33.3% | +50.0% |

## Qualitative Patch Profiles

| Patch | Profile |
|---|---|
| Baseline prompt | reference condition |
| Length/style control | generic caution |
| Hidden-instruction targeted patch | structural patch |
| Credential targeted patch | local patch |
| Overbroad caution patch | overbroad patch |
