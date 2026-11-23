# CHAB-2026: Cardiology AI Benchmark

This repository contains the public benchmark materials and reproducibility code for the Cardiology Humanoid AI Benchmark (CHAB-2026).

## Registration

- **OSF pre-registration:** https://osf.io/237wu
- **OSF registration ID:** `237wu`

## Publicly available research assets

The public repository provides the 80-case benchmark corpus and case-provenance metadata, standardized system prompts, the nine-domain (D1–D9) scoring rubrics, and executable statistical analysis code in `analysis_pipeline.py`. These materials document the benchmark construction and analysis specification.

## Data availability and restriction notice

Individual row-level raw scoring sheets from the independent cardiology adjudication panel are **not publicly redistributed** because of post-study evaluator confidentiality and data-access restrictions. Aggregated benchmark summaries are reported in the manuscript.

The executable pipeline expects an authorized auditor to supply the restricted file locally at:

```
data/CHAB-2026_Restricted_Rater_Scores.csv
```

This restricted file is deliberately not included in the public repository. If it is absent, the pipeline stops with an explanatory message referring to this Data Availability Statement; it does not substitute placeholder data or hardcoded manuscript statistics.

## Analysis protocol

The pipeline computes the weighted nine-domain CHAB Score on a 0–100 scale using the prespecified weights:

| Domain | Weight |
|---|---:|
| D1 | 0.20 |
| D2 | 0.10 |
| D3 | 0.15 |
| D4 | 0.15 |
| D5 | 0.10 |
| D6 | 0.15 |
| D7 | 0.05 |
| D8 | 0.05 |
| D9 | 0.05 |

The primary analysis is restricted to the four AI model arms and the 80 canonical cases (56 Guideline-Derived; 24 Published Case Reports). Human-reference cohorts and the four noncanonical overflow cases are excluded from primary inference. The analysis includes descriptive statistics and 10,000-resample BCa confidence intervals, the repeated-measures Friedman test, six paired Wilcoxon tests with Holm adjustment and Cohen's dz, CCI Tier 3 subgroup summaries, six two-sided exact McNemar tests for the SEV-2/SEV-3 composite with Holm adjustment, and a case-level random-intercept linear mixed-effects provenance model.

## Repository layout

```
.
├── analysis_pipeline.py
├── analysis/
│   └── analysis_code/
│       └── sap_models.py
├── data/
│   ├── [public benchmark corpus and provenance metadata]
│   └── [restricted rater-score CSV supplied locally; not committed]
├── prompts/
│   ├── system_prompt.txt
│   └── zero_shot_cot_template.json
├── results/
│   └── verified_sap_outputs.json  # generated locally
├── Dockerfile
├── requirements.txt
└── README.md
```

## Run locally

Use Python 3.10.12 and install the pinned dependencies:

```bash
python3 -m pip install -r requirements.txt
python3 -m py_compile analysis_pipeline.py
python3 analysis_pipeline.py
```

A successful analysis writes computed results to `results/verified_sap_outputs.json`. Without the restricted auditor file, the script exits intentionally and explains the data-access restriction.

## Runtime and dependencies

The Dockerfile uses the pinned Python 3.10.12 slim image and installs the dependencies in `requirements.txt`.
