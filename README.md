# CHAB-2026: Cardiology AI Benchmark

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

# CHAB-2026: Cardiology Humanoid AI Benchmark

An open-science replication codebase and audit registry for the Cardiology Humanoid AI Benchmark (CHAB-2026). This repository hosts the canonical evaluation registers, standardized clinical text prompt matrices, and executable non-parametric statistical models to guarantee absolute research integrity.

## Repository Directory Architecture
- **`data/CHAB-2026_Authoritative_Master_Audit_Workbook_FINAL.xlsx`**: Authoritative master workbook containing the complete case register (`SourceRegister`, n=80), execution logs (`ExecutionLog`, n=320), and dual-reviewer grading matrices (`ReviewLog`, n=640 records).
- **`prompts/system_prompt.txt`**: Verbatim tertiary-care consultant baseline system prompt instructing models to format answers into 8 uniform clinical headers.
- **`prompts/zero_shot_cot_template.json`**: Standardized JSON configuration wrapper forcing Zero-Shot Chain-of-Thought determinism.
- **`analysis_pipeline.py`**: Executable Python validation script running the locked primary and secondary statistical protocols.
- **`LICENSE`**: MIT open-source licensing agreement.

## Operational Protocol & Study Design
- **Primary Population Boundary**: Exactly 80 canonical clinical cases (56 Guideline-Derived [GD Track] and 24 peer-reviewed Published Case Reports [CR Track]).
- **Arm Allocation**: Paired case-matched design (within-subject). Each individual case serves as its own direct control across models.
- **Registered Model Arms**: Model Alpha (GPT-5), Model Beta (Claude 3.5 Sonnet), Model Gamma (Gemini 1.5 Pro), and Model Delta (DeepSeek-V3).
- **Continuous Primary Outcome**: Composite CHAB Score (0–100% scale) derived from an adjudicated 9-domain weighted linear combination.
- **Categorical Safety Endpoint**: Binary presence of a Major Safety Error defined under the prespecified SEV-2/SEV-3 composite endpoint.
- **Open Science Framework (OSF) Registry ID**: 237wu (URL: https://osf.io)

## Confirmatory Statistical Hierarchy (Primary SAP)
1. **Continuous Overall Analysis**: Global variance is analyzed strictly via a repeated-measures non-parametric **Friedman test with 3 degrees of freedom (df = 3)**, yielding the locked verification statistic of **χ²(3) = 68.35, P < 0.001**.
2. **Post-Hoc Pairwise Transformations**: Continuous cross-model deltas are evaluated via two-sided paired Wilcoxon signed-rank tests controlled for multiplicity via step-down **Holm-Bonferroni corrections** at familywise α = 0.05. Continuous uncertainty intervals are mapped via 10,000-resample non-parametric bias-corrected and accelerated (BCa) bootstrap vectors clustered by case ID.
3. **Safety Performance Inference**: Matched categorical error rates are analyzed strictly via **pairwise exact McNemar tests** utilizing identical case IDs across the six model pairs. Multiplicity is managed via a separate Holm-Bonferroni correction vector.

## Exploratory & Sensitivity Classifications
- **Cochran's Q Test**: The multi-group categorical statistic (Q = 17.65, P = 0.042) is re-allocated strictly as an exploratory global descriptive check.
- **Human Clinical Cohorts**: Junior Resident (74.20% ± 11.40%) and Attending Faculty (94.80% ± 4.20%) observations are isolated under secondary descriptive partitions to prevent primary df=3 inference contamination.
- **Complexity Tracking**: Point-by-point score degradation across the continuous 5–16 Case Complexity Index (CCI) range is tracked descriptively using smoothed LOESS non-linear regression splines. 

## Verification Execution
To verify data constants directly inside the repository workspace environment, run:
```bash
python3 analysis_pipeline.py
```

