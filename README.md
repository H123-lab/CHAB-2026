# CHAB-2026: Cardiology Humanoid AI Benchmark

An open-science replication repository for the Cardiology Humanoid AI Benchmark (CHAB-2026). This repository hosts the canonical data matrices, standardized prompt profiles, and non-parametric statistical calculation code to ensure full reproducibility.

## Repository Directory Architecture
- **`CHAB-2026_Authoritative_Master_Audit_Workbook_FINAL.xlsx`**: Authoritative master evaluation datasets, independent double-blind reviewer matrices, and verified audit logs.
- **`analysis_pipeline.py`**: Python statistical script mapping the pre-registered non-parametric testing boundaries.
- **`README.md`**: Project overview and reproducibility documentation.

## Study Design & Specifications
- **Unit of Analysis**: Case-level paired observation preserving matched dependencies.
- **Primary Population Frame**: Exactly 80 canonical clinical cases (56 Guideline-Derived and 24 Published Case Reports).
- **Primary AI Models Evaluated**: GPT-5, Claude 3.5 Sonnet, Gemini 1.5 Pro, and DeepSeek-V3.
- **Primary Observation Pool**: Exactly 320 paired model-case observations.
- **Inter-Rater Reliability Pool**: Exactly 640 independent dual-reviewer grading records.
- **Open Science Framework (OSF) Registry Link**: https://osf.io

## Confirmatory Statistical Hierarchy
1. **Primary Continuous Performance (Composite CHAB Score, 0-100 scale)**: Evaluated via a repeated-measures non-parametric **Friedman test with three degrees of freedom (df = 3)**, yielding an omnibus statistic of χ²(3) = 68.35, P < 0.001. Post-hoc comparisons are processed via two-sided paired Wilcoxon signed-rank tests controlled via step-down **Holm-Bonferroni correction**.
2. **Primary Patient Safety Endpoint (SEV-2/SEV-3 Composite Error Rate)**: Evaluated strictly through six pairwise **Exact McNemar tests** on case-matched blocks to preserve model dependencies.
3. **Exploratory Cohort Variance Parameter**: Cochran's Q test (Q = 17.65, P = 0.042) is reclassified as a secondary, global exploratory check.

