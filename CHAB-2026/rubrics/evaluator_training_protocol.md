# CHAB-2026 Grader Standardization Memo and Calibration Protocol

This operational directive details the mandatory multi-center calibration phase enforced to standardize independent expert reviewers prior to database logging.

---

## 1. Evaluator Eligibility and Background
The evaluation panel consists exclusively of six independent, board-certified clinical cardiologists with ≥ 5 years of post-fellowship tertiary care experience. All panel reviewers completed the calibration protocol to eliminate subjective grading drift and standardize scoring boundaries.

---

## 2. Calibration Reference Standards & Pilot Invariants
Before auditing the primary 320 text generation outputs, all six graders completed an independent scoring pass over a separate pilot vignette set (n = 5 noncanonical case blocks). 
- **The Benchmarking Standard:** Reviewers were required to map text segments line-for-line against ESC/ACC Class I consensus statements.
- **Score Anchor Alignment:** Graders were trained to enforce strict discrete definitions:
  * `Score 2`: 100% concordance with society recommendations.
  * `Score 1`: Partially acceptable response containing minor monitoring variances or minor non-harmful omissions.
  * `Score 0`: Deficient response containing guideline departures or medication omissions.

---

## 3. Post-Training Cohen's Kappa Concordance Gates
Following the independent pilot pass, initial rater arrays were audited using inter-rater reliability scripts. Reviewers were cleared to proceed to the main blinding registry only after achieving the pre-registered agreement thresholds:

[Grader Panel Pilot Run] ──► Audit via Fleiss' Kappa ──► Threshold Met? (κ ≥ 0.80) ──► Lock Panel

The panel achieved a pooled initial multi-class Fleiss' Kappa coefficient of $\kappa = 0.84$ on domain allocations, satisfying the strict data-entry quality gates and ensuring high inter-observer objectivity before database unblinding.
