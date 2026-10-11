# CHAB-2026 Case Adaptation and Curation Protocol

This document outlines the formalized operational protocol utilized by the investigator panel to select, transform, anonymize, and validate the 80 canonical clinical cases that constitute the Cardiology Humanoid AI Benchmark (CHAB-2026) corpus.

---

## 1. Objective and Core Scope
The case-construction pipeline was designed to build a high-density, multi-step cardiovascular simulation framework completely decoupled from public web training materials. Curation targeted critical decision nodes where secondary diagnostics, guideline-driven therapeutic choices, and safety-critical contraindication traps could be evaluated dynamically.

---

## 2. Source Track Eligibility Parameters

### 2.1 Guideline-Derived (GD) Track Curation (n = 56)
- **Selection Criteria:** Scenarios were synthetically generated using Class I, IIa, and III recommendations across 12 authoritative clinical practice guidelines published between 2018 and 2025 by the ESC, ACC, and AHA.
- **Adaptation Methodology:** Core recommendations were converted into clinical presentations by embedding standard clinical variables (e.g., specific chest pain profiles, dynamic ST-segment elevations, or potassium level vectors). Patient vignettes were structured to ensure that a model could not deduce the answer by simple pattern matching, requiring instead cross-axial data integration.

### 2.2 Published Case-Report (CR) Track Curation (n = 24)
- **Selection Criteria:** Real-world patient vignettes were compiled from peer-reviewed cardiology indexing journals (*European Heart Journal – Case Reports*, *JACC: Case Reports*, *Heart Rhythm*, *BMJ Case Reports*, and *NEJM*).
- **Adaptation Methodology:** To eliminate text-leakage risks while maintaining clinical realism, original published texts were systematically transformed using a structured rewriting protocol:
  * Proprietary institutional metadata, author names, geographic locations, and concrete dates were completely expunged.
  * Extraneous narrative clinical history unrelated to the cardiovascular presentation was pruned.
  * Numerical diagnostic markers (e.g., vital signs, cardiac enzymes, and specific ejection fractions) were preserved exactly to maintain clinical data integrity.
  * Case text was re-rendered using alternative clinical phrasing, syntax trees, and synonym matrices to break direct text memorization vectors.

---

## 3. Case Structure Standardization
Every included vignette string was forced into a rigid, standardized clinical layout before model deployment, containing exactly:
1.  **Chief Complaint & Presenting History:** Unstructured descriptions of current symptoms, duration, and baseline cardiac history.
2.  **Physical Examination Matrix:** Standardized physical parameters including initial jugular venous distension, cardiac auscultation fields, and peripheral perfusion signs.
3.  **Baseline Vital Signs:** Explicit values for blood pressure (mmHg), heart rate (bpm), respiratory rate, oxygen saturation, and body temperature.
4.  **Initial Diagnostic Markers:** Fixed numerical data arrays covering initial electrocardiogram (ECG) descriptions, bedside echocardiography estimates, and acute laboratory biomarkers (e.g., high-sensitivity troponin, NT-proBNP, and serum potassium vectors).

---

## 4. Quality Control & Quality Assurance Workflow
Before freezing the codebase on **August 15, 2026**, every candidate case block passed through a mandatory three-stage validation gate:
1.  **Independent Dual-Review Curation Check:** Two independent cardiology-trained investigators reviewed each case to ensure the clinical text was unconfounded, free of internal contradictions, and sufficiently specified to yield a definitive solution.
2.  **Gold-Standard Verification:** A defensible clinical reference standard was documented independently of model execution, tracing the expected management steps directly to a Class I or IIa guideline recommendation line.
3.  **Contamination & Code-C03 Audit:** All final vignette strings were processed through localized validation scripts to guarantee that direct guideline recommendation identifiers or numeric source text rows were isolated from the model-facing files.

---

## 5. Noncanonical Overflow Partitioning
Candidate profiles that met basic eligibility criteria but exceeded pre-registered domain sub-quotas were separated prior to freezing and allocated exclusively to the exploratory overflow array (n=4: `HF-GD-008`, `HF-GD-009`, `HF-GD-010`, `VHD/AORTA-LIT-004`). These data blocks are completely excluded from the primary 320-row evaluation dataset to maintain a strict, unconfounded analytical population boundary.
