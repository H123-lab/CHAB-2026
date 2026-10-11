# CHAB-2026 Model Output Data Sharing Statement

This statement provides an open-science declaration regarding the storage, dissemination, and redaction protocols for the raw textual language model outputs generated during this trial.

## 1. Data Availability & Storage Layout
The comprehensive, compiled grading parameters, independent domain scores, and safety classifications for all 320 model-case observations are permanently open-source and archived within our master dataset workbook: `/data/CHAB-2026_Authoritative_Master_Audit_Workbook_FINAL.xlsx`.

## 2. Sharing & Redaction Policy
- **Adjudicated Scoring Records:** 100% of the statistical rows, dual-reviewer metrics, and senior referee consensus overrides are shared completely and without redaction.
- **Raw API Text Generation Logs:** The raw text files containing the unformatted Markdown output responses are compiled into a compressed archive (`data/raw_json_api_logs.zip`) to protect data provenance. 
- **Exclusion Rationale:** Zero data fields or model text streams are withheld or obfuscated for proprietary or commercial reasons. No content was redacted, as the entire canonical evaluation dataset is completely de-identified and free of patient health numbers (PHI) or protected institutional metadata, fully satisfying open-access replication requirements.
