# CHAB-2026: Protocol Deviations and Amendments Log

This document provides a transparent, chronological record of all modifications, structural clarifications, and statistical alignments applied to the Cardiology Humanoid AI Benchmark (CHAB-2026) protocol prior to final database freeze and manuscript submission.

## 1. Statistical Analysis Plan (SAP) Realignment
- **Amendment Date:** October 11, 2026
- **Original Protocol Specification:** The initial exploratory analysis draft incorporated Cochran's Q as a primary safety screening test alongside pairwise comparisons.
- **Revised Protocol Specification:** The primary safety endpoint is strictly restricted to six pairwise **Exact McNemar tests** evaluating the SEV-2/SEV-3 composite error rate across matching case IDs. Cochran's Q test ($Q = 17.65, P = 0.042$) has been formally re-allocated as a secondary, global exploratory check of cohort variance.
- **Scientific Rationale:** To prevent multi-group global testing statistics from being incorrectly interpreted as paired comparative inference, satisfying strict clinical trial reporting standards.

## 2. Segregation of Human Clinician Reference Cohorts
- **Amendment Date:** October 11, 2026
- **Original Protocol Specification:** Legacy analytical tables blended model metrics with junior resident and attending cardiology baselines inside a unified Friedman test framework with 4 or 5 degrees of freedom ($df=4$, $df=5$).
- **Revised Protocol Specification:** The primary omnibus analysis is strictly locked as a four-model comparison ($80\text{ cases} \times 4\text{ models} = 320\text{ observations}$) evaluated via a repeated-measures non-parametric Friedman test with three degrees of freedom ($df=3$), yielding a verified global statistic of $\chi^2(3) = 68.35, P < 0.001$. All human reference cohorts are completely removed from the primary omnibus step and isolated under separate secondary/exploratory descriptive partitions.
- **Scientific Rationale:** To ensure that model-to-model inference is completely unconfounded by human baseline variances, establishing a clean parametric machine learning evaluation boundary.

## 3. Case Complexity Index (CCI) Tier Synchronization
- **Amendment Date:** October 11, 2026
- **Original Protocol Specification:** Early repository library legends contained placeholder difficulty index cutoffs ($0\text{--}5 = \text{Tier 1}$, $6\text{--}10 = \text{Tier 2}$, $11\text{--}16 = \text{Tier 3}$).
- **Revised Protocol Specification:** The continuous Case Complexity Index is locked as an 8-domain, 0–16 framework. The operational difficulty tier thresholds are standardized and frozen as: **Tier 1 (CCI 5–6)**, **Tier 2 (CCI 7–10)**, and **Tier 3 (CCI 11–16)**, reflecting the true observed distribution of the clinical case corpus. Post-hoc case rebalancing or artificial tier shifting is prohibited.
- **Scientific Rationale:** Restores absolute mathematical continuity between the raw database entries, supplementary tables, and manuscript methods text.

## 4. Mitigation of Over-Interpretive Claims and Thresholds
- **Amendment Date:** October 11, 2026
- **Original Protocol Specification:** Draft graphics and text elements incorporated subjective vocabulary like "flawless safety" and marked a "critical failure zone at CCI $\ge 12$".
- **Revised Protocol Specification:** All subjective phrasing has been replaced with objective, guideline-concordant terms ("error-free case output rate", "SEV-0 compliance"). The unvalidated phrase "critical failure zone" has been completely struck from the text; continuous score degradation across the complexity spectrum is tracked purely via non-linear smoothed LOESS regression splines.
- **Scientific Rationale:** Adheres strictly to the conservative reporting requirements of high-impact medical journals.
