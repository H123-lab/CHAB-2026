# CHAB-2026 Runtime Execution Protocol

This protocol documents the standardized software and networking conditions enforced during the automated evaluation sequence of the Cardiology Humanoid AI Benchmark.

## 1. Case Sequencing Order
To ensure absolute evaluation consistency, case vignettes were processed in a static, sequential linear order matching their unique identifiers exactly, starting from `CHAB-2026-GD-001` through `GD-056`, followed by `CHAB-2026-CR-001` through `CR-024`. Each model processed the identical sequence independently to eliminate variations caused by dynamic network conditions.

## 2. Input Presentation Format
Vignettes were formatted into a standardized JSON payload script where the case text was wrapped directly into the `{{CASE_VIGNETTE_TEXT_STRING}}` template slot inside `zero_shot_cot_template.json`. No conversational pre-conditioning or iterative multi-turn messaging was permitted; each case was executed as a isolated single-turn session pass.

## 3. Network and Tool Disabling Guardrails
Upstream web-browsing capabilities, interactive plugin connections, external digital tool integrations, and Retrieval-Augmented Generation (RAG) extensions were completely deactivated and blocked via script configurations across all 4 evaluated model arms. This design ensures that all text responses are generated purely from the models' static parametric memory.

## 4. Automation Error and Incomplete Response Handling
- **Network Dropouts / Timeouts:** The execution script utilized an automated recursive error-handling catch loop. Any connection timeout or API refusal instantly triggered an immediate retry loop using the identical case payload after a 5-second back-off delay.
- **Incomplete Responses / Truncation:** Responses were checked for structural integrity against a regex layout requiring at least 4 of the 8 pre-registered markdown headers. Zero generation crashes or text truncations occurred during the testing window, yielding a 100% complete text dataset across all 320 observations.
