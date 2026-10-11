# CHAB-2026 Prompts and System Instructions Matrix

This directory hosts the exact prompts and structural templates utilized to evaluate large language model multi-step cardiology clinical reasoning.

## 1. Primary Prompts & Configuration Mapping
The precise, verbatim system prompts and runtime configuration profiles are permanently archived and accessible in the root directory to maintain an unconfounded execution chain:
- **System Instructions File:** Refer to `/prompts/system_prompt.txt` in the root folder for the expert cardiologist senior consultant baseline rules and the 8 mandated markdown section headers.
- **Inference Template File:** Refer to `/prompts/zero_shot_cot_template.json` in the root folder for the Zero-Shot Chain-of-Thought json configuration, locked temperature values, and API hyperparameter controls.

## 2. Prompt Sharing and Recoverability Status
All execution prompts are 100% unredacted, recoverable, open-source, and fully shareable under our open-science protocol. No proprietary, hidden, or dynamically updating meta-prompts were utilized during the evaluation testing window.
