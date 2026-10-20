# CHAB-2026 System Prompt Ablation and Strategy Analysis

This document outlines the exploratory prompt ablation testing used to establish the baseline execution protocol for the Cardiology AI Benchmark.

---

## 1. Prompt Architecture Formats Tested

Prior to freezing the primary evaluation repository, we conducted iterative pilot testing across three distinct prompt strategies to measure structural compliance and minimize formatting errors:

### Strategy A: Naive Plain Text (Standard Input-Output)
- **Design:** Directly ingested the clinical case text string and requested diagnostic/management conclusions without structural formatting boundaries or logical milestones.
- **Observed Behavior:** Highly fragmented output topologies. Models frequently omitted critical secondary comorbidity optimizations and exhibited a high rate of text truncation when processing long-context multimorbidity vignettes.

### Strategy B: Zero-Shot Chain-of-Thought (Locked CoT)
- **Design:** Injected explicit procedural directions requiring step-by-step clinical reasoning paths prior to generating final management actions.
- **Observed Behavior:** Marked improvements in multi-system pathophysiological reasoning. However, downstream parsing remained inconsistent due to models using variable, non-standardized section subheadings.

### Strategy C: Structured Zero-Shot CoT with Header Constraints (Frozen Baseline)
- **Design:** Combined Step-by-Step reasoning requirements with strict instructions mandating exactly 8 uniform Markdown headers (`D1_Diagnosis_Header` through `D8_Escalation_Header`).
- **Observed Behavior:** Optimal performance profile. Enforcing rigid header structures completely eliminated response truncation errors, stabilized cross-model evaluation lanes, and supported automated regex validation scoring without altering parametric memory.

---

## 2. Multi-Strategy Performance & Formatting Trajectory

The table below summarizes structural compliance and parsing stability logs captured during the pre-trial pilot runs across representative case strata:

| Prompt Strategy Array | Token Integrity Gates | Header Regex Compliance | Text Truncation Rate | Downstream Parsing Stability | Action Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Strategy A (Naive Plain)** | Passed | 0.0% (No Headers) | 8.8% (High Risk) | Unstable / Failed | Rejected |
| **Strategy B (Standard CoT)** | Passed | 45.2% (Variable) | 3.5% (Med Risk) | Suboptimal Variance | Rejected |
| **Strategy C (Structured CoT)** | Passed | 100.0% (Uniform) | 0.0% (Zero Drops) | Airtight Validation | **Frozen Protocol** |

---

## 3. Methodological Rule for Replicators
To preserve the unconfounded nature of the comparative continuous metrics, any replication attempt or expanded model benchmarking must utilize the identical system template strings archived in `/prompts/system_prompt.txt`. Introducing conversational pre-conditioning or interactive multi-turn variations outside these locked bounds will break the baseline structural constraints.
