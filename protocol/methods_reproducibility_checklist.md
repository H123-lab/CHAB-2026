# CHAB-2026: Methods and Reproducibility Verification Checklist

This checklist serves as the formal accountability and audit document for the Cardiology Humanoid AI Benchmark (CHAB-2026) open-science framework. It tracks compliance across all core design, execution, grading, and statistical reporting blocks.

***

## 1. Study Infrastructure & Baseline Constraints
- [x] **Primary Unit of Analysis Locked:** Every observation is a case-level paired entry.
- [x] **Canonical Sample Denominator Verified:** Exactly **80 canonical cases** are retained (`CHAB-001` through `CHAB-080`).
- [x] **Analytical Observations Total Blocked:** Exactly **320 paired model-case observations** (80 cases × 4 models).
- [x] **Reviewer Record Count Verified:** Exactly **640 primary dual-blind reviewer grades** (320 runs × 2 independent masked graders).
- [x] **Exploratory Data Partitioning Enforced:** Four overflow cases (`HF-GD-008`, `HF-GD-009`, `HF-GD-010`, `VHD/AORTA-LIT-004`) are fully isolated outside the canonical dataset and excluded from primary testing.
- [x] **Human Reference Cohort Segregation:** Legacy clinician evaluation records are restricted to secondary descriptive reference blocks to prevent primary pipeline contamination.

## 2. Case Selection & Provenance Layer Tracking
- [x] **Provenance Stratification Checked:** 56 Guideline-Derived cases (70.0%) and 24 peer-reviewed Published Case Reports (30.0%) are accurately registered.
- [x] **Source Timeline Bounds Verified:** Guideline reference documents span from **2018 to 2025** exactly.
- [x] **Targeted Screening Denominators Audited:** Curation tracking logs account for 105 total screened candidates, 21 protocol-defined exclusions, and 84 final eligible case structures.
- [x] **Source Citation Mapping Completed:** Verbatim recommendations, section paragraphs, and unique DOI anchors are permanently mapped across Supplementary Tables S1, S2, and S3.

## 3. Case Complexity Framework Audit
- [x] **CCI Domain Metric Standardized:** Case Complexity Index is fixed as an 8-dimension framework with ordinal item ranges from 0 to 2 (Total continuous range: 0–16).
- [x] **Difficulty Tier Boundaries Synchronized:** Tier thresholds are frozen as: **Tier 1 (CCI 5–6)**, **Tier 2 (CCI 7–10)**, and **Tier 3 (CCI 11–16)**.
- [x] **Observed Corpus Distribution Confirmed:** The natural observed distribution across the 80 cases is verified as: Tier 1 = 5; Tier 2 = 27; Tier 3 = 48 cases. Post-hoc artificial cell rebalancing is prohibited.

## 4. Model Execution & Environment Calibration
- [x] **Version Control Parameters Documented:** Exact runtime engine codes (`gpt-5-preview-2026-05`, `claude-3-5-sonnet-v1-2026`, `gemini-1.5-pro-exp-08`, `deepseek-v3-dense-06`) are recorded.
- [x] **Algorithmic Determinism Enforced:** Generation temperature is set to a strict **0.0** across all inference runs.
- [x] **Network Module Disabling Confirmed:** Upstream web-browsing capabilities, plugin integrations, and external tool dependencies were completely **DISABLED**.
- [x] **Response Matrix Denominators Validated:** Exactly 1 primary pass attempt occurred per model-case node, generating a 100% complete text dataset with zero model refusals or truncated entries.

## 5. Masking & Adjudication Pipeline Governance
- [x] **Double-Blind Integrity Confirmed:** Generation files were fully anonymized, stripped of vendor metadata, and randomly sequenced before reviewer distribution.
- [x] **Expert Grader Independence Verified:** Reviewers possess \(\ge 5\) years of post-fellowship cardiology experience and maintained 100% operational separation from case curation and prompt design tasks.
- [x] **Automated Trigger Constraints Checked:** Digital sheets automatically routed records to the senior referee if case-level score variance reached \(\ge 5.0\) points, domain delta reached \(\ge 1.0\) point, or any safety code conflict occurred.
- [x] **Adjudication Denominators Reconciled:** Database confirms that exactly **14.4% (46/320)** of multi-model execution blocks triggered referee arbitration, with zero unresolved scores left in the final database freeze.

## 6. Score Formulation & Safety Weight Controls
- [x] **Fractional Weight Scaling Checked:** Nine domain multipliers are stored strictly as proportions (e.g., `0.20`, `0.15`, `0.10`, `0.05`) and sum exactly to **1.000**.
- [x] **Composite Formula Integrity Verified:** The baseline scoring routine calculates the continuous metric using cell formula configurations matching the pre-registered framework: \(\text{CHAB Score} = 50 \times \sum (w_i \cdot D_i)\).
- [x] **Safety Code Independence Confirmed:** Case-level baseline clinical safety-criticality flags are kept entirely separate from the model response's observed observed safety-severity classifications (SEV-0 through SEV-3).

## 7. Statistical Analytical Hierarchy Validation
- [x] **Primary Continuous Outcome Omnibus Locked:** Overall performance variations are evaluated via a repeated-measures non-parametric **Friedman test (df=3)**, yielding the locked verification value: **\(\chi^2(3) = 68.35, P < 0.001\)**.
- [x] **Post-Hoc Multiplicity Controls Bound:** Cross-model continuous contrasts use two-sided paired Wilcoxon signed-rank tests adjusted via separate step-down **Holm-Bonferroni correction vectors**.
- [x] **Resampling Covariance Preserved:** Uncertainty boundaries and standard errors are derived uniformly using a **10,000-resample non-parametric bootstrap procedure clustered by unique Case ID**.
- [x] **Primary Patient Safety Contrast Verified:** Matched categorical safety proportions (SEV-2/SEV-3 composite error rate) are evaluated strictly through six pairwise **Exact McNemar tests**.
- [x] **Exploratory Metrics Reclassified:** Cochran's Q test (\(Q = 17.65, P = 0.042\)) is completely withheld from primary safety inference and cataloged strictly as a secondary global descriptive check of macro-level cohort variance.
- [x] **Linear Mixed-Effects (LME) Model Specified:** Case provenance interactions track REML estimations using random intercepts clustered by case ID and Kenward-Roger denominator degrees of freedom (\(F(1,78) = 28.40, P < 0.001\)).
- [x] **Data Missingness Verification Completed:** Database verification checks confirm a **100% complete evaluation matrix** across all 320 observation paths, rendering missing data imputations completely inapplicable.
