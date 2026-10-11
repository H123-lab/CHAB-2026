# CHAB-2026 Evaluation Framework & Domain Scoring Rubric

This document establishes the official scoring anchors, domain weights, and the mathematical formula used to calculate the continuous Composite CHAB Score.

---

## 1. Mathematical Score Equation
The continuous Composite CHAB Score is expressed on a 0–100 scale and calculated strictly from the adjudicated domain scores using pre-locked fractional proportions:

$$\text{CHAB Score} = 50 \times \sum_{i=1}^{9} (w_i \cdot D_i)$$

Where:
- $D_i$ represents the adjudicated score for domain $i$, with $D_i \in \{0, 1, 2\}$.
- $w_i$ represents the corresponding domain weight as a proportion, where $\sum_{i=1}^{9} w_i = 1.000$.

---

## 2. Pre-Locked Domain Weights
- **D1: Primary Diagnosis & Differential Accuracy:** 0.20 (20%)
- **D2: Investigation Appropriateness & Prioritization:** 0.10 (10%)
- **D3: Guideline Adherence (Concordance to ESC/ACC):** 0.15 (15%)
- **D4: Immediate Management & Stabilization:** 0.15 (15%)
- **D5: Definitive Long-Term Management:** 0.10 (10%)
- **D6: Patient Safety & Error Avoidance:** 0.15 (15%)
- **D7: Emergency Recognition & Time-Critical Triage:** 0.05 (5%)
- **D8: Specialist Escalation & Transfer Triage:** 0.05 (5%)
- **D9: Clinical Reasoning Quality & Synthesis:** 0.05 (5%)

---

## 3. General Scoring Anchors (0–2 Ordinal Scale)

For each of the nine domains, independent masked reviewers applied the following standardized scoring definitions:

### Score 2: Fully Guideline-Concordant / Competent
- The response meets all core clinical requirements for the specific domain.
- Recommended diagnostic pathways, testing prioritizations, and pharmacotherapies are line-for-line concordant with Class I or Class IIa consensus recommendations.
- No relevant omissions, systemic contradictions, or timing delays are present.

### Score 1: Partially Concordant / Minor Variance
- The response identifies the correct broad clinical direction but introduces minor procedural or pharmacotherapeutic variances.
- Includes non-critical diagnostic omissions (e.g., omitting an indicated non-invasive baseline marker) or non-harmful therapy delays that do not introduce immediate risks of physiological decline.
- Clinically acceptable alternative approaches backed by Class IIb society consensus are credited under this tier.

### Score 0: Clinically Unacceptable / Dangerous
- The response fails to address the primary clinical objective or introduces substantial guideline deviations (Class III interventions).
- Omits essential, life-saving therapies (e.g., failing to mandate emergent revascularization in STEMI) or directly recommends contraindicated pharmacotherapies.
- Recommends unsafe or unstable pathways that precipitate immediate patient risk or catastrophic clinical deterioration.
