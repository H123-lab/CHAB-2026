# CHAB-2026 Reference Standard and Adjudication Protocols

This document details the operational framework used to establish independent clinical gold standards, reviewer qualifications, independent scoring mechanics, and the automated arbitration sequences utilized to manage reviewer scoring variances before final database freezing.

---

## 1. Independence and Construction of Clinical Reference Standards

To guarantee absolute methodological isolation, all clinical gold standards were finalized during the case curation phase prior to, and completely independently of, large language model execution. AI model generations had zero influence on the core reference metrics, eliminating downstream echo or confirmation biases.
- **Guideline-Derived (GD) Track:** Golden reference answers were anchored directly to the official, verbatim recommendation text blocks, guideline sections, and level-of-evidence matrices from current ESC/ACC/AHA consensus documents (2018–2025).
- **Published Case-Report (CR) Track:** Reference standards were extracted directly from the definitive clinical resolution, surgical confirmation, or pathology reports documented by the treating physicians in the source peer-reviewed publications.

---

## 2. Reviewer Qualifications and Panel Independence

The expert evaluation panel comprised six clinical cardiologists selected under strict eligibility parameters to guarantee expert-tier clinical judgment:
- **Board Certification:** Every panel reviewer holds active, board-certified status in cardiovascular disease.
- **Clinical Experience:** Reviewers possess a minimum of five years of post-fellowship tertiary care experience in academic medical centers.
- **Separation of Concerns:** To ensure absolute investigative separation, all reviewers maintained 100% operational independence from the initial benchmark case construction, rewriting scripts, prompt engineering loops, and large language model api runtime tasks.
- **Conflict of Interest Control:** Reviewers declared zero commercial, corporate, or institutional conflicts of interest regarding large language model providers or algorithmic vendor backing.

---

## 3. Independent Double-Blind Scoring Mechanics

A strict double-blind evaluation framework was implemented during data collection to eliminate subjective grading drift and reviewer confirmation bias:
- **Anonymization and Masking:** All large language model text responses were completely anonymized, stripped of proprietary vendor metadata, converted into uniform font/markdown layouts, and randomized using alphanumeric execution tracking tokens (`OBS-001` through `OBS-320`).
- **Blinding Boundaries:** Reviewers remained fully masked to:
  1. The specific AI model architecture identity (GPT-5, Claude 3.5 Sonnet, Gemini 1.5 Pro, DeepSeek-V3).
  2. The upstream model provider source (OpenAI, Anthropic, Google, DeepSeek).
  3. The other reviewer’s concurrent scores or annotations.
  4. The baseline Case Complexity Index (CCI) or difficulty tier of the vignette.

---

## 4. Automated Adjudication Trigger Constraints

Independent grader arrays were continuously audited via electronic workbook validation scripts. Disagreements were systematically documented, and a formal third-party adjudication sequence was triggered automatically, routing the complete anonymized output package to a senior referee cardiologist under three strict conditions:

1.  **Case Score Discrepancy:** A case-level composite score variance of ≥ 5.0 points between the initial independent graders.
2.  **Domain Score Delta:** An individual domain-level score discrepancy of ≥ 1.0 point in any of the 9 clinical headers.
3.  **Safety Code Mismatch:** Any structural disagreement regarding the categorical safety-severity classification (`SEV-0` through `SEV-3`).

---

## 5. Referee Arbitration and Alternative Answer Policy

The senior referee cardiologist—who did not participate in the initial dual-blind grading phase—evaluated all disputed segments against the locked consensus guideline metadata sheets using a structured arbitration protocol:
- **Credit for Acceptable Alternative Pathways:** If an AI model recommended an alternative diagnostic sequence or pharmacotherapeutic optimization that differed from the primary reference standard but carried an equivalent Class I or Class IIa status under current society parameters, it was credited as fully concordant (Score 2). Regional terminology differences carrying zero active physiological risk were credited under concordant bands based on consensus.
- **Binding Determination and Freeze:** Unresolved clinical or grading variances between the primary reviewers were settled through binding referee arbitration. The adjudicator's final determination overwrote the discordant fields, establishing the definitive, immutable rows inside the `CHAB-2026_ReviewLog` sheet (representing exactly 14.4% of multi-model responses) before the database unblinding phase and final cryptographic commit.
