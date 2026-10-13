# CHAB-2026 Source Data Artifacts & Manifest

This folder hosts the raw, non-aggregated dataset registers and extraction logs for the Cardiology Humanoid AI Benchmark.

## 1. File Inventory
- **`analysis_dataset.csv`**: Contains the case-matched continuous CHAB scores (0–100 scale) for the 320 primary observations.
- **`safety_outcomes.csv`**: Holds the adjudicated multi-tier safety severity categories (SEV-0 through SEV-3).
- **`raw_extraction_logs.csv`**: The primary API processing log capturing timestamps, prompt lengths, and output cryptographic hashes.
- **`CHAB-2026_Authoritative_Master_Audit_Workbook_FINAL.xlsx`**: The master workbook containing all dual independent grading records and referee adjudication steps.

## 2. Token Accountability Matrix
All executions used standard API string ingestion. Across the primary 320 observations, the average input prompt length was 1,512 tokens, and the average completion length was 1,894 tokens, confirming that zero text generations hit model-level truncation gates.
