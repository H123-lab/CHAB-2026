# CHAB-2026 Case Complexity Index (CCI) Scoring Rubric

This document establishes the formal grading anchors and decision boundaries for the investigator-developed Case Complexity Index (CCI). The index aggregates structural clinical difficulty across eight predefined domains to classify cases into rigid difficulty tiers.

---

## 1. Mathematical Structure and Scale
The total CCI score is calculated as a direct, unweighted mathematical sum of all eight sub-component domain scores:

$$\text{Total CCI Score} = \sum_{i=1}^{8} \text{Domain Score}_i$$

- **Individual Domain Range:** 0, 1, or 2 points.
- **Theoretical CCI Range:** 0 to 16 points.
- **Observed Corpus Range:** 5 to 16 points.

---

## 2. Domain-Specific Scoring Anchors

### Domain 1: Diagnostic Complexity
*   **0 Points:** Straightforward single-disease presentation with classic pathognomonic findings.
*   **1 Point:** Presence of atypical symptoms or confounding baseline histories requiring secondary differential consideration.
*   **2 Points:** Complex diagnostic conundrum characterized by multiple overlapping diagnostic mimics or silent subclinical presentation modes.

### Domain 2: Management Complexity
*   **0 Points:** Single, standard guideline-mandated therapeutic intervention (e.g., standard pharmacotherapy initiation).
*   **1 Point:** Multi-drug optimization loops or interventions requiring acute clinical titration and active monitoring.
*   **2 Points:** High-complexity management involving conflicting organ system demands, urgent mechanical circulatory support staging, or high-risk surgical timelines.

### Domain 3: Differential Diagnosis Burden
*   **0 Points:** Narrow differential spectrum (< 2 plausible clinical causes).
*   **1 Point:** Moderate differential burden requiring active exclusion of 2 to 4 competitive cardiovascular pathologies.
*   **2 Points:** High differential density (> 4 distinct clinical entities) with high potential for diagnostic misdirection.

### Domain 4: Guideline Interpretation Burden
*   **0 Points:** Direct, singular guideline recommendation with definitive Class I status.
*   **1 Point:** Involves complex or overlapping recommendations across different society tracks (e.g., matching ESC vs. ACC/AHA variations).
*   **2 Points:** Requires resolution of lower-evidence recommendation classes (Class IIb) or managing populations explicitly under-represented in major clinical trials.

### Domain 5: Multimodal Information Burden
*   **0 Points:** Diagnostic resolution requires raw history and basic vitals only.
*   **1 Point:** Requires synthesis across two distinct diagnostic media (e.g., history matching an acute ECG profile or high-sensitivity lab trend).
*   **2 Points:** Advanced multi-system data integration matching clinical history with detailed laboratory metrics, dynamic ECG records, and complex cross-sectional imaging data (e.g., CMR, CTA, or Echo Doppler vectors).

### Domain 6: Sequential Decision Burden
*   **0 Points:** Static, single-step diagnostic or therapeutic decision node.
*   **1 Point:** Multi-step sequence where the subsequent clinical choice depends directly on the initial diagnostic output.
*   **2 Points:** Dynamic longitudinal pathway requiring rapid, sequential adjustments across acute stabilization, diagnostic prioritization, definitive therapy, and long-term care nodes.

### Domain 7: Patient Safety Criticality
*   **0 Points:** Routine care path with low immediate risk of acute decompensation.
*   **1 Point:** Moderate risk; medical omissions or delays introduce manageable systemic morbidity risks.
*   **2 Points:** Safety-critical environment where standard therapeutic missteps, delayed choices, or the presence of a strict contraindication trap poses an immediate, fatal risk to the patient.

### Domain 8: Emergency Recognition Requirement
*   **0 Points:** Scheduled outpatient or elective chronic care scenario.
*   **1 Point:** Subacute inpatient monitoring requiring routine ward workup or semi-urgent referral tracking.
*   **2 Points:** High-acuity, time-critical emergency node requiring immediate triage stabilization, code activation, or emergent subspecialty escalation.

---

## 3. Operational Difficulty Tier Boundaries

Cases are automatically stratified into three rigid operational tier bands based strictly on their computed summary scores. Post-hoc case shifting or manual category overrides are prohibited to prevent tier manipulation:

*   ==**Tier 1 (Foundational Core):**== $\text{CCI Score} \in [5, 6]$  
    *(Baseline corpus contains 5 cases)*
*   ==**Tier 2 (Intermediate Clinical Complexity):**== $\text{CCI Score} \in [7, 10]$  
    *(Baseline corpus contains 27 cases)*
*   ==**Tier 3 (Advanced Multimorbidity & Mimics):**== $\text{CCI Score} \in [11, 16]$  
    *(Baseline corpus contains 48 cases)*

---

## 4. Expert Override Regulation
Individual domain entries and summary scores are structurally locked following senior referee consensus. No post-hoc score adjustment or shifting of cases near threshold boundaries (e.g., shifting a case with a score of 10 to a score of 11) is permitted during the analysis pipeline to maintain absolute statistical and data architecture continuity.
