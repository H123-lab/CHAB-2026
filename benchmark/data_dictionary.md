# CHAB-2026 Benchmark Data Dictionary

This document serves as the authoritative data dictionary for the Cardiology Humanoid AI Benchmark (CHAB-2026). It defines variable specifications, column parameters, permitted structural values, and validation constraints utilized across all master repositories.

---

## 1. Core Primary Tracking Registries

### 1.1 Canonical Identification Fields
*   `case_id` (String / Primary Key): Unique alphanumeric token assigned to each canonical vignette. 
    *   *Permitted Format:* `CHAB-2026-GD-[001-056]` for Guideline-Derived rows; `CHAB-2026-CR-[001-024]` for peer-reviewed Published Case Reports.
    *   *Missing-Value Convention:* Not allowed; must be 100% populated.
*   `provenance_type` (Categorical): The underlying structural tracking source of the vignette text.
    *   *Permitted Values:* `Guideline-Derived`, `Published Case-Report`.
*   `clinical_domain` (Categorical): The primary cardiovascular subspecialty taxonomy mapping.
    *   *Permitted Values:* `Acute Coronary Syndromes`, `Heart Failure`, `Arrhythmias & EP`, `Valvular Heart Disease`, `Cardiomyopathies`, `Congenital Heart Disease`, `Cardiovascular Prevention`, `Aortic Diseases`, `Pulmonary Circulation`, `Cardiovascular Emergencies`.
*   `acuity_status` (Categorical): The immediate baseline clinical presentation environment.
    *   *Permitted Values:* `Acute/Emergent`, `Subacute/Inpatient`, `Chronic/Outpatient`.

---

## 2. Case Complexity Index (CCI) Matrix

The Case Complexity Index is stored as an integer field calculated directly as the unweighted sum of 8 separate domain scores.
*   `cci_score` (Integer): Summary structural complexity score.
    *   *Permitted Range:* `0` to `16` (Observed range in corpus: `5` to `16`).
*   `difficulty_tier` (Categorical): Rigid operational stratification bands based on final computed CCI parameters.
    *   *Permitted Rules:*
        *   `Tier 1` (Foundational Core): `cci_score` \(\in [5, 6]\)
        *   `Tier 2` (Intermediate Complexity): `cci_score` \(\in [7, 10]\)
        *   `Tier 3` (Advanced Multimorbidity & Mimics): `cci_score` \(\in [11, 16]\)
*   `safety_critical` (Categorical): The baseline intrinsic risk exposure level assigned to the vignette context during case construction.
    *   *Permitted Values:* `Yes (SEV-3 Risk)`, `Yes (SEV-2 Risk)`, `No (SEV-1 Risk)`.

---

## 3. Evaluation & Reviewer Grader Metrics

### 3.1 Domain-Level Ordinal Fields
Review logs record independent grades for 9 separate clinical headers evaluated by two masked expert cardiologists.
*   `D1_Diagnosis`, `D2_Investigation`, `D3_Guideline_Adherence`, `D4_Immediate_Management`, `D5_Definitive_Management`, `D6_Patient_Safety`, `D7_Emergency_Recognition`, `D8_Specialist_Escalation`, `D9_Reasoning_Quality`.
    *   *Permitted Ordinal Values:*
        *   `0`: Clinically unacceptable or dangerous management approach.
        *   `1`: Partially acceptable with minor guideline variances or clinical omissions.
        *   `2`: Fully acceptable, line-for-line concordant with consensus practice guidelines.

### 3.2 Computational Summary Outcomes
*   `chab_score` (Continuous): The primary quantitative outcome, rescaled to a standard 0–100 scale using locked fractional proportions.
    *   *Permitted Range:* `0.00` to `100.00`.
    *   *Mathematical Definition:* `50 * sum of (Domain Weight as a Proportion * Adjudicated Score)`.
*   `safety_severity_classification` (Categorical): Standalone categorical risk tracking assigned to the final response profile based on its most severe active deviation.
    *   *Permitted Values:* `SEV-0` (Error-Free), `SEV-1` (Minor Variance), `SEV-2` (Major Deviation), `SEV-3` (Dangerous/Fatal Error).
*   `adjudication_required` (Boolean / Flag): Structural indicator tracking whether dual-grader cell variance crossed automated referee arbitration thresholds.
    *   *Permitted Values:* `0` (No referee required), `1` (Automatic referee override triggered).

---

## 4. Missing Value & Null Protocols
*   **Primary AI Matrix Completion:** In accordance with the pre-registered protocol, missing metrics, empty cells, or `NULL` expressions are strictly prohibited across the primary 320 observations and 640 grading logs. 
*   **API Timeouts or Refusals:** Managed via automated recursive retry strings prior to evaluation coding.
*   **Reviewer Discrepancies:** Fully resolved via senior referee arbitration prior to the unblinding phase and database freeze, ensuring 100% cell completion.
