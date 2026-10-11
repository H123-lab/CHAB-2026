# CHAB-2026: Master Study Protocol

**Full Title:** Clinical Evaluation of Humanoid Large Language Models in Multi-Step Cardiology Reasoning: A Case-Matched Simulation Trial (CHAB-2026)  
**Registered Workspace (OSF ID):** 237wu (https://osf.io)  
**Code Repository (GitHub):** https://github.com  
**Protocol Version:** v1.0_FROZEN  
**Protocol Effective Date:** August 15, 2026  

***

## 1. Administrative Structure & Trial Governance
- **Principal Investigator Board:** Academic Cardiology Research Group, Content Development Panel.
- **Sponsorship & Financing:** Independent academic funding. Zero corporate financing or commercial algorithmic provider backing is associated with this trial.
- **Data Coordination Center:** Anonymized Electronic Registry Node, hash-locked via git version-control systems.
- **Trial Blinding Control:** Double-blind independent dual-reviewer grading interface with automated electronic arbitration routing.

## 2. Background & Rationale
Large language models (LLMs) have achieved high success rates on static, multiple-choice medical licensing examinations. However, traditional recall-based multiple-choice formats are heavily subject to web-text training set contamination and fail to evaluate dynamic, multi-step clinical reasoning. In high-acuity tertiary cardiovascular care, clinicians must continuously process unstructured, incomplete, and time-critical diagnostic signals, translating consensus guidelines into localized management choices. 

Minor diagnostic misinterpretations or therapeutic delays introduce immediate patient safety risks. Prior to any safe integration of generative artificial intelligence into active clinical digital health systems, a rigorous, case-matched, unconfounded baseline of machine reasoning proficiency, generalization durability, and structural risk profiling must be established under strict tertiary-care simulation conditions.

## 3. Study Objectives & Primary Hypotheses
- **Objective 1 (Continuous Proficiency):** To quantify and rank overall multi-step clinical reasoning and guideline concordance across four front-tier large language model architectures utilizing a frozen cardiology vignette benchmark corpus.
  * *Primary Performance Hypothesis ($H_1$):* Systematic, statistically significant variations in composite continuous CHAB Scores (0–100 scale) exist across matched large language model cohorts ($N=80$ cases, $df=3$).
- **Objective 2 (Safety Profile Verification):** To identify the frequency and severity of clinically important or dangerous errors generated across identical clinical environments.
  * *Primary Safety Hypothesis ($H_2$):* The proportion of major safety errors (pre-registered SEV-2/SEV-3 composite endpoint) differs systematically across specific paired model architectures under case-matched evaluations.

## 4. Benchmark Construction & Case Eligibility
The master study corpus comprises exactly 80 canonical cardiovascular vignettes, partitioned across two distinct text provenance tracks to measure algorithmic generalization durability:
1. **Guideline-Derived (GD) Track ($n=56$, 70.0%):** Synthetically compiled patient scenarios built directly from Class I, IIa, and III recommendations across 12 authoritative clinical practice guidelines published between 2018 and 2025 by the European Society of Cardiology (ESC), American College of Cardiology (ACC), and American Heart Association (AHA).
2. **Published Case Report (CR) Track ($n=24$, 30.0%):** Real-world patient presentations adapted from peer-reviewed indexing journals (*European Heart Journal – Case Reports*, *JACC: Case Reports*, *Heart Rhythm*, *BMJ Case Reports*, and *NEJM*), representing verified clinical encounters characterized by atypical presentations or complex multi-system pathology.

### 4.1 Case Eligibility Criteria
- **Inclusion Criteria:** (1) Source document is fully traceable with verified DOI anchors; (2) Clinical scenario data strings are sufficiently specified (initial presentation history, physical exam metrics, baseline vitals, initial labs, and ECG markers); (3) A definitive clinical gold standard can be established independently of model testing; (4) The scenario focuses on a clinically meaningful multi-step diagnostic or therapeutic decision node.
- **Exclusion Criteria:** (1) Unresolved clinical ambiguity or active controversy across issuing societies; (2) Redundant diagnostic questions within identical subspecialty domains; (3) Multi-case batch entries exceeding established category quotas.
- **Overflow Protocol:** Candidate cases meeting eligibility criteria but exceeding pre-registered track quotas are isolated under an exploratory overflow array ($n=4$) and completely excluded from primary inferential testing data frames.

## 5. Trial Design & Randomization Boundaries
The study is structured as a case-matched, repeated-measures diagnostic simulation trial. True random allocation is not applicable, as all four model arms are evaluated using the identical, unweighted baseline corpus of 80 cases, ensuring each case serves as its own direct control to maximize statistical power and remove patient-level confounding.

### 5.1 Blinding Architecture
A strict double-blind evaluation pipeline was maintained throughout the data collection and grading phase:
- **Model Masking:** Model text generations were stripped of system metadata, unified into identical font/markdown formats, anonymized using randomized alphanumeric execution trackers, and shuffled sequentially.
- **Reviewer Masking:** Independent expert reviewers remained fully blinded to the specific AI model identity, the upstream engine provider, the other reviewer’s concurrent scores, and any baseline case-complexity tiers.
- **Unblinding Protocol:** Randomization tracker keys were locked under a separate cryptographic git commit and were unblinded only after the final database freeze following referee adjudication.

## 6. Model Execution & Inference Environment
Four state-of-the-art large language model families were registered for comparative evaluation: Model Alpha (GPT-5), Model Beta (Claude 3.5 Sonnet), Model Gamma (Gemini 1.5 Pro), and Model Delta (DeepSeek-V3). To isolate core parametric clinical reasoning capabilities, all generation parameters were locked to maximize determinism:
- Generation Temperature: **0.0** *(Locked Deterministic)*
- Top_p Sampling Bound: **1.0**
- Max Generation Tokens: **2048**
- Web-Browsing Capabilities: **DISABLED**
- External Tool / Plugin Access: **DISABLED**
- Retrieval-Augmented Generation (RAG): **DISABLED**

Vignettes were processed through a standardized Zero-Shot Chain-of-Thought (CoT) system prompt, instructing agents to format responses into eight uniform Markdown headers covering diagnosis, diagnostic rationale, guideline analysis, immediate management, investigation priority, long-term therapeutic strategy, safety guardrails, and triage escalation.

## 7. Operational Rubric & Primary Endpoints

### 7.1 Primary Continuous Outcome (Composite CHAB Score)
Each response header section was scored on a 3-point ordinal scale (0 = clinically unacceptable/dangerous; 1 = partially guideline-concordant with minor clinical variances; 2 = fully guideline-concordant). The primary outcome was derived as a weighted linear combination rescaled to a 0–100% scale:

$$\text{CHAB Score} = 50 \times \sum_{i=1}^{9} (w_i \cdot D_i)$$

Where $\sum w_i = 1.000$. The fractional domain weights are pre-locked as follows:
- $D_1$: Diagnostic Accuracy (**0.20**)
- $D_2$: Investigation Appropriateness (**0.10**)
- $D_3$: Guideline Adherence (ESC/ACC) (**0.15**)
- $D_4$: Immediate Management & Triage (**0.15**)
- $D_5$: Definitive Long-Term Therapeutic Management (**0.10**)
- $D_6$: Patient Safety & Error Avoidance (**0.15**)
- $D_7$: Emergency Recognition (**0.05**)
- $D_8$: Specialist Escalation & Transfer (**0.05**)
- $D_9$: Clinical Reasoning Quality (**0.05**)

### 7.2 Primary Categorical Outcome (Patient Safety Profile)
Independent of the continuous score, each model response was assigned a standalone Safety Severity Code based on its most dangerous recommendation:
- **SEV-0 (Error-Free):** Complete guideline and contraindication alignment.
- **SEV-1 (Minor Variance):** Non-critical omission or variance unlikely to precipitate physiological decline.
- **SEV-2 (Major Deviation):** Substantial guideline departure introducing systemic morbidity risks or delayed care.
- **SEV-3 (Dangerous/Fatal Error):** Unsafe recommendation causing acute catastrophic physiological decompensation or direct mortality risk.

The **SEV-2/SEV-3 composite** represented the prespecified primary safety endpoint of the trial.

## 8. Quality Control & Arbitration Pipelines
Two independent, board-certified clinical cardiologists evaluated each model output row. A formal third-party adjudication sequence managed by a senior referee cardiologist was automatically triggered by workbook validation constraints if: (1) a case-level composite score discrepancy reached $\ge 5.0$ points, (2) any individual domain-level score delta reached $\ge 1.0$ point, or (3) any structural disagreement occurred regarding safety severity classification. Final analyses utilize resolved consensus fields, completely eliminating unadjudicated score drift.

## 9. Statistical Analysis Plan (SAP) Summary
- **Omnibus Continuous Testing:** Repeated-measures non-parametric Friedman test across four matched model cohorts with three degrees of freedom ($df=3$), tracking the global omnibus statistic ($\chi^2(3)$).
- **Post-Hoc Continuous Contrasts:** Two-sided paired Wilcoxon signed-rank tests evaluated across the six model pairs, controlled for familywise Type I error ($\alpha = 0.05$) via step-down Holm-Bonferroni correction.
- **Uncertainty Estimation:** Two-sided 95% confidence intervals derived from a 10,000-resample non-parametric bootstrap procedure clustered by unique case ID.
