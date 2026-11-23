# Provenance registry audit — 2026-11-23

## Scope

Audited the public `main` branch of `H123-lab/CHAB-2026`, including the benchmark source register, canonical case inventory, data CSVs, JSON manifests, repository tree, and the root guideline case-construction workbook's presence and metadata.

## Verified counts

| Check | Observed | Expected | Result |
|---|---:|---:|---|
| Canonical case IDs in inventory (excluding stray header) | 80 | 80 | Pass |
| Unique canonical case IDs in inventory | 80 | 80 | Pass |
| GD cases in inventory | 56 | 56 | Pass |
| CR cases in inventory | 24 | 24 | Pass |
| Rows in `benchmark/source_register.csv` | 46 | 80 | Fail |
| Unique case IDs in source register | 46 | 80 | Fail |
| GD source-register rows | 46 | 56 | Fail |
| CR source-register rows | 0 | 24 | Fail |
| Duplicate DOI count among CR source-register rows | Not testable (no CR rows) | 0 | Not verifiable |

The inventory contained one malformed repeated header row beginning `box_id,` between CR-019 and CR-020. That stray row has been removed in this branch; the remaining inventory has 80 data rows and 80 unique case IDs.

## Provenance findings

- The source register stops at `CHAB-2026-GD-046`. It is missing GD-047 through GD-056 and all CR-001 through CR-024.
- `10.1093/eurheartj/ehad565` is repeated across several GD entries because they cite the same 2023 ESC acute coronary syndromes guideline. This is legitimate shared guideline provenance, not evidence that those case rows have distinct source documents.
- There are no CR rows in the current source register, so the requested 24-way CR DOI uniqueness test cannot be passed or meaningfully reported as zero duplicates.
- The source register schema does not contain the clinical-domain, acuity, complexity-tier, or CCI fields. Those are present in the canonical inventory, but the requested Supplementary Tables S1–S3 were not present as separate files in the inspected repository tree. Exact agreement with manuscript supplements therefore cannot be confirmed from repository contents alone.
- The requested strings `jaccas.2025.1023` and `ehad565` were not located in the other inspected text manifests through repository search; the source register itself contains `ehad565`.

## Workbook and nested directory

- `CHAB-2026_Guideline_Case_Construction_Workbook.xlsx` exists in the repository root (29,197 bytes). The GitHub file interface exposed its binary object metadata but not readable workbook sheets. Its record count and contents could not be independently confirmed, so it has not been moved into `data/`.
- A nested `CHAB-2026/` directory exists. It contains a separate reproducibility manifest, prompt JSON, safety-error audit CSV, and evaluator rubric. These files are not a byte-for-byte duplicate of the root structure based on the available tree listing; the directory was not deleted.

## Required author/source-document action

The missing 34 source records must be reconstructed from the actual frozen case-design source files and the cited published Supplementary Tables S2 and S3 (plus S1 for inventory alignment). Do not fabricate DOIs, guideline section numbers, article titles, or citations. Once the source documents are supplied or made available in the repository, re-audit every CR DOI against its publication and verify the GD section-level citations against the corresponding guideline editions.

This audit intentionally records the provenance registry as **incomplete and not yet publication-ready**. No missing citations have been invented or silently substituted.
