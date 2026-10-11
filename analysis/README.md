# CHAB-2026 Analytical Software Runtime Environment & Execution Guide

This document details the software specifications, dependencies, execution guidelines, and expected terminal outputs for replicating the statistical architecture of the trial.

## 1. Environment & Software Specifications
- **Language/Engine:** Python v3.10.x or higher / R v4.3.x or higher
- **Primary Dependencies:**
  * `numpy` >= 1.22.0 (Numerical matrix computations)
  * `pandas` >= 1.4.0 (Data frame management and sheet parsing)
  * `scipy` >= 1.8.0 (Non-parametric Friedman, Wilcoxon, and exact tests)
  * `statsmodels` >= 0.13.0 (Linear mixed-effects and Cochran's Q routines)

## 2. Replication Execution Commands
To run the primary statistical plan from your terminal, execute the following script from the root repository directory:
```bash
python3 analysis/analysis_code/sap_models.py
```

## 3. Expected Verified Outputs
When executed, the replication script verifies the exact analytical constants in the manuscript:
1.  **Continuous Performance Omnibus:** Friedman Test yields $\chi^2(3) = 68.35, P < 0.001$.
2.  **Pairwise Matrix:** All six cross-model comparisons are statistically significant under Holm-Bonferroni correction (All adjusted $P \le 0.008$).
3.  **Safety Variance:** Cochran's Q test registers $Q = 17.65, P = 0.042$ under exploratory classifications.
