# CHAB-2026 Codebase Release Change Log

This file documents the version history, structural code modifications, and analytical database updates applied to this repository package.

## [v1.0.0] - 2026-10-11 (Authoritative Submission Release)
### Added
- Completed `benchmark/canonical_case_inventory.csv` containing the complete 80-case clinical taxonomy and continuous complexity score vectors.
- Implemented `analysis/analysis_code/sap_models.py` locking the primary Friedman omnibus test (df=3) and pairwise exact McNemar safety contrasts.
- Maintained `rubrics/reference_standard_and_adjudication.md` detailing expert panel qualifications and automated referee override thresholds.
- Created complete `execution/` and `governance/` administrative documentation tracking matrices.

### Changed
- Re-allocated Cochran's Q test (Q=17.65, P=0.042) strictly as an exploratory global check of macro-level safety variance, separating it from primary inference cells.
- Segregated all legacy junior resident and attending human reference datasets from primary four-model continuous omnibus pipelines to ensure unconvoluted machine learning testing bounds.
- Synchronized the operational difficulty tier boundaries to reflect the true observed index range of the corpus: Tier 1 (CCI 5–6), Tier 2 (CCI 7–10), and Tier 3 (CCI 11–16).
