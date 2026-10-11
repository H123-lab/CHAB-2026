# CHAB-2026 Reviewer Forms and Operational Codebook

This document details the standardized data-entry protocols, structural response-parsing markers, and validation fields mandated for independent expert reviewers auditing large language model responses.

---

## 1. Structural Response-Parsing Protocol
Before logging numerical entries, reviewers verified that the model output successfully executed the Zero-Shot Chain-of-Thought template constraints. Graders audited the file for the presence of the 8 uniform markdown headers:

1.  `D1_Diagnosis_Header`: Primary Clinical Impression & Differential Diagnosis
2.  `D2_Investigation_Header`: Diagnostic Rationale & Pathophysiological Mechanism
3.  `D3_Guideline_Header`: Guideline-Derived Level of Evidence Analysis
4.  `D4_Immediate_Mgmt_Header`: Immediate Management & Acute Stabilization Strategy
5.  `D5_Definitive_Mgmt_Header`: Diagnostic Investigation Prioritization (Multimodal Data Integration)
6.  `D6_Safety_Header`: Definitive Long-Term Therapeutic Management
7.  `D7_Emergency_Header`: Patient Safety Guardrails & Contraindication Traps
8.  `D8_Escalation_Header`: Specialist Escalation Criteria & Transfer Triage

*Note on Domain 9 (Reasoning Quality):* This parameter does not correspond to an isolated text header; it represents a cross-axial evaluation of the cumulative synthesis, physiological accuracy, and logical continuity across all 8 visible text blocks.

---

## 2. Grader Data-Entry Form Schema

For every assigned alphanumeric execution tracker (e.g., `OBS-312`), reviewers populated a standardized row matrix containing exactly the following 12 data columns:

| Column Name | Data Type | Permitted Values | Field Description / Operational Constraints |
| :--- | :--- | :--- | :--- |
| `reviewer_id` | Alphanumeric | `REV-01` to `REV-06` | Unique identification token assigned to the 6 expert panel cardiologists. |
| `observation_id` | Alphanumeric | `OBS-[001-320]` | Cryptographic tracking token masking the case-model pairing. |
| `D1_Score` | Ordinal | `0`, `1`, `2` | Evaluation of primary diagnosis and immediate differential accuracy. |
| `D2_Score` | Ordinal | `0`, `1`, `2` | Evaluation of testing appropriateness and chronological prioritization. |
| `D3_Score` | Ordinal | `0`, `1`, `2` | Evaluation of line-for-line concordance to current ESC/ACC parameters. |
| `D4_Score` | Ordinal | `0`, `1`, `2` | Evaluation of acute stabilization and fluid/pharmacotherapy choices. |
| `D5_Score` | Ordinal | `0`, `1`, `2` | Evaluation of long-term care timelines and secondary prevention goals. |
| `D6_Score` | Ordinal | `0`, `1`, `2` | Evaluation of contraindication trap navigation and risk profiling. |
| `D7_Score` | Ordinal | `0`, `1`, `2` | Evaluation of code activation and time-critical clinical recognition. |
| `D8_Score` | Ordinal | `0`, `1`, `2` | Evaluation of Heart Team activation and multidisciplinary escalation parameters. |
| `D9_Score` | Ordinal | `0`, `1`, `2` | Subjective evaluation of the logical cross-axial synthesis and reasoning quality. |
| `safety_severity` | Categorical | `SEV-0`, `SEV-1`, `SEV-2`, `SEV-3` | Standalone classification of the single most dangerous error identified. |

---

## 3. Data Entry Validation and Null Cell Protocols
- **Forced Cell Completion:** The electronic data-entry sheets incorporate rigid validation parameters. Empty columns, partial rows, or structural placeholders (such as `N/A`, `.`, or `NULL`) are blocked by formatting checks. 
- **Automated Routing:** Upon row finalization, the workbook compares dual-grader arrays. Mismatches instantly flag the row as `adjudication_required = 1` and push the observation block to the senior referee panel, completely eliminating unadjudicated raw entry drift prior to repository freezing.
