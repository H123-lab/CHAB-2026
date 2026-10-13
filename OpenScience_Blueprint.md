# CHAB-2026 Open-Science Pipeline & Architecture Blueprint

This blueprint outlines the data flow, prompt injection architecture, clinical evaluation framework, and statistical routing executed across the Cardiology Humanoid AI Benchmark (CHAB-2026) simulation trial.

---

## 1. Unified Pipeline System Topology

The diagram below maps the reproducible pipeline layout from initial data ingestion to unconfounded statistical output frames:

[Raw Case Selection Matrix]
│  (Curation tracks: 56 GD / 24 CR)
▼
[Anonymized Case Vignettes (N=80)]
│
▼  (Zero-Shot CoT Ingestion wrapper; Temperature = 0.0)
[Standardized Parallel API Runs]
│
▼  (Generates 320 text outputs stripped of metadata)
[Anonymized Response Sets]
│
▼  (Distributed to independent masked cardiologists)
[Double-Blind Dual Grading] ───► Mismatch? (Domain delta >= 1.0) ───► [Senior Referee Arbitration]
│                                                                      │
└───────────────────────────────────┬──────────────────────────────────┘
▼
[Adjudicated Score Registry]
│
▼ (Enforces df=3 complete-matrix boundary)
[Non-Parametric Statistical Engine]
│
┌──────────────────┴──────────────────┐
▼                                     ▼
[Friedman Omnibus χ²(3)]               [Exact Pairwise McNemar]
(Continuous CHAB Rank Order)           (Categorical Safety Matrix)

---

## 2. Text Ingestion & Execution Constraints

Future investigators replicating this execution environment must enforce the following runtime parameters to prevent environmental drift and generation confounding:
┌──────────────────────────────────────────┐
│      Standardized API Request Body       │
└─────────────────────┬────────────────────┘
│
┌──────────────────────────┼──────────────────────────┐
▼                          ▼                          ▼
[Temperature = 0.0]       [Max Tokens = 2048]       [Network Modules = OFF]
(Deterministic Logic Engine)  (Prevents Truncation)     (No Web/RAG Contamination)

---

## 3. Reference Extraction and Citation Anchor Mapping

To maintain perfect alignment between computational data structures and clinical reporting files, researchers utilizing this benchmark corpus should cite this framework using the metadata layout verified across our public channels:

### 3.1 Primary Repository Links
*   **Protocol Registry ID:** `237wu` (Open Science Framework: https://osf.io)
*   **Code Replication Hub:** https://github.com

### 3.2 Formal Bibliographic Template
> *CHAB-2026 Investigative Board. Clinical Evaluation of Humanoid Large Language Models in Multi-Step Cardiology Reasoning: A Case-Matched Simulation Trial (CHAB-2026). Open Science Framework & GitHub Code Repository. October 2026. Available at: https://github.com.*

### 3.3 Core Machine-Readable Metrics
```json
{
  "reproducibility_spec": {
    "canonical_case_count": 80,
    "paired_observation_count": 320,
    "eval_grading_records": 640,
    "continuous_omnibus_statistic": "Friedman chi-squared(3) = 68.35, P < 0.001",
    "categorical_safety_statistic": "Pairwise Exact McNemar Tests",
    "exploratory_safety_variance": "Cochran's Q = 17.65, P = 0.042"
  }
}
```
