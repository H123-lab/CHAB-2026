#!/usr/bin/env python3
"""CHAB-2026 reproducible statistical analysis.

The restricted adjudicator-level input is intentionally not committed. An
authorized auditor may place it at data/CHAB-2026_Restricted_Rater_Scores.csv.
See the Data Availability section in README.md before running this pipeline.
"""
from __future__ import annotations

import itertools
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.formula.api as smf

ROOT = Path(__file__).resolve().parent
INPUT = ROOT / "data" / "CHAB-2026_Restricted_Rater_Scores.csv"
OUTPUT = ROOT / "results" / "verified_sap_outputs.json"
N_BOOT = 10_000
SEED = 20261123

DOMAIN_WEIGHTS = {
    "D1": 0.20, "D2": 0.10, "D3": 0.15, "D4": 0.15, "D5": 0.10,
    "D6": 0.15, "D7": 0.05, "D8": 0.05, "D9": 0.05,
}
MODELS = [
    "Model Alpha (GPT-5)",
    "Model Beta (Claude 3.5 Sonnet)",
    "Model Gamma (Gemini 1.5 Pro)",
    "Model Delta (DeepSeek-V3)",
]
MODEL_LABELS = {
    MODELS[0]: "GPT-5",
    MODELS[1]: "Claude 3.5 Sonnet",
    MODELS[2]: "Gemini 1.5 Pro",
    MODELS[3]: "DeepSeek-V3",
}
SEVERITIES = {"SEV-0", "SEV-1", "SEV-2", "SEV-3"}
OVERFLOW_IDS = {"HF-GD-008", "HF-GD-009", "HF-GD-010", "VHD/AORTA-LIT-004"}


def holm_adjust(p_values):
    """Return step-down Holm-adjusted p-values in their original order."""
    p = np.asarray(p_values, dtype=float)
    order = np.argsort(p)
    adjusted = np.empty(len(p), dtype=float)
    running = 0.0
    for rank, idx in enumerate(order):
        running = max(running, (len(p) - rank) * p[idx])
        adjusted[idx] = min(1.0, running)
    return adjusted.tolist()


def bca_interval(values, rng):
    values = np.asarray(values, dtype=float)
    result = stats.bootstrap(
        (values,), np.mean, confidence_level=0.95, n_resamples=N_BOOT,
        method="BCa", random_state=rng,
    )
    return [float(result.confidence_interval.low), float(result.confidence_interval.high)]


def load_canonical_data(path=INPUT):
    if not path.exists():
        raise FileNotFoundError(
            "Restricted row-level adjudicator scoring data were not found at "
            f"{path}. This file is not redistributed in the public repository "
            "because of evaluator confidentiality and data-access restrictions. "
            "An authorized auditor must supply data/CHAB-2026_Restricted_Rater_Scores.csv "
            "locally. See the Data Availability Statement in README.md."
        )
    frame = pd.read_csv(path)
    frame.columns = [str(c).strip() for c in frame.columns]
    aliases = {
        "Case_ID": "Case ID", "Model_Name": "Model Name",
        "Source_Type": "Source Type", "CCI_Score": "CCI Score",
        "Safety_Severity": "Safety Severity",
    }
    frame = frame.rename(columns={k: v for k, v in aliases.items() if k in frame.columns})
    required = {"Case ID", "Model Name", "Source Type", "CCI Score", "Safety Severity", *DOMAIN_WEIGHTS}
    missing = sorted(required - set(frame.columns))
    if missing:
        raise ValueError(f"Restricted score file is missing required columns: {missing}")

    frame["Case ID"] = frame["Case ID"].astype(str).str.strip()
    frame["Model Name"] = frame["Model Name"].astype(str).str.strip()
    frame["Source Type"] = frame["Source Type"].astype(str).str.strip()
    frame["Safety Severity"] = frame["Safety Severity"].astype(str).str.strip()

    # Human-reference rows are excluded by retaining only the four prespecified AI arms.
    frame = frame[frame["Model Name"].isin(MODELS)].copy()
    overflow_mask = frame["Case ID"].str.contains("OVERFLOW", case=False, na=False)
    overflow_mask |= frame["Case ID"].isin(OVERFLOW_IDS)
    frame = frame.loc[~overflow_mask].copy()

    if frame["Case ID"].nunique() != 80 or len(frame) != 320:
        raise ValueError(
            "Canonical primary cohort must contain exactly 80 cases and 320 "
            f"AI model-case rows after exclusions; found {frame['Case ID'].nunique()} "
            f"cases and {len(frame)} rows."
        )
    if frame.duplicated(["Case ID", "Model Name"]).any():
        raise ValueError("Duplicate canonical Case ID × Model Name rows detected.")
    counts = frame.groupby("Case ID")["Model Name"].nunique()
    if not (counts == 4).all():
        raise ValueError("Every canonical case must have exactly one row for each of four AI models.")
    provenance_counts = frame.groupby("Case ID")["Source Type"].nunique()
    if not (provenance_counts == 1).all():
        raise ValueError("Source Type must be constant within each case.")
    cases = frame[["Case ID", "Source Type"]].drop_duplicates()
    source_counts = cases["Source Type"].value_counts().to_dict()
    gd = sum(str(x).lower().startswith("guideline") or str(x).upper() == "GD" for x in cases["Source Type"])
    cr = sum("published" in str(x).lower() or "case report" in str(x).lower() or str(x).upper() == "CR" for x in cases["Source Type"])
    if gd != 56 or cr != 24:
        raise ValueError(f"Expected 56 Guideline-Derived and 24 Published Case Report cases; found GD={gd}, CR={cr}. Source counts: {source_counts}")

    for col in DOMAIN_WEIGHTS:
        numeric = pd.to_numeric(frame[col], errors="coerce")
        if numeric.isna().any() or not numeric.isin([0, 1, 2]).all():
            raise ValueError(f"{col} must contain only nonmissing integer ratings 0, 1, or 2.")
        if not np.equal(numeric, np.floor(numeric)).all():
            raise ValueError(f"{col} contains non-integer ratings.")
        frame[col] = numeric.astype(int)

    cci = pd.to_numeric(frame["CCI Score"], errors="coerce")
    if cci.isna().any() or not cci.between(0, 16).all() or not np.equal(cci, np.floor(cci)).all():
        raise ValueError("CCI Score must be a nonmissing integer on the prespecified 0–16 scale.")
    frame["CCI Score"] = cci.astype(int)
    frame["Safety Severity"] = frame["Safety Severity"].str.upper()
    if not frame["Safety Severity"].isin(SEVERITIES).all():
        raise ValueError(f"Safety Severity labels must be one of {sorted(SEVERITIES)}.")

    frame["CHAB Score"] = 50.0 * sum(frame[c] * w for c, w in DOMAIN_WEIGHTS.items())
    frame["Major Safety Error"] = frame["Safety Severity"].isin(["SEV-2", "SEV-3"]).astype(int)
    return cases, frame


def descriptive_results(pivot, rng):
    output = {}
    for model in MODELS:
        x = pivot[model].to_numpy(dtype=float)
        q1, q3 = np.percentile(x, [25, 75])
        output[MODEL_LABELS[model]] = {
            "n": int(len(x)), "mean": float(np.mean(x)),
            "sd": float(np.std(x, ddof=1)), "median": float(np.median(x)),
            "q1": float(q1), "q3": float(q3), "iqr": float(q3 - q1),
            "bca_95_ci_mean": bca_interval(x, rng),
        }
    return output


def run_analysis(cases, frame):
    rng = np.random.default_rng(SEED)
    pivot = frame.pivot(index="Case ID", columns="Model Name", values="CHAB Score").reindex(columns=MODELS)
    if pivot.isna().any().any():
        raise ValueError("Incomplete matched score matrix; all 80 cases need four model scores.")

    desc = descriptive_results(pivot, rng)
    friedman = stats.friedmanchisquare(*(pivot[m].to_numpy() for m in MODELS))

    pairwise = []
    raw_p = []
    for a, b in itertools.combinations(MODELS, 2):
        x, y = pivot[a].to_numpy(), pivot[b].to_numpy()
        diff = x - y
        test = stats.wilcoxon(x, y, alternative="two-sided", method="auto")
        sd = float(np.std(diff, ddof=1))
        pairwise.append({
            "model_1": MODEL_LABELS[a], "model_2": MODEL_LABELS[b],
            "mean_paired_difference": float(np.mean(diff)),
            "cohens_dz": float(np.mean(diff) / sd) if sd else None,
            "wilcoxon_statistic": float(test.statistic),
            "p_raw": float(test.pvalue),
            "difference_bca_95_ci": bca_interval(diff, rng),
        })
        raw_p.append(float(test.pvalue))
    for item, adjusted in zip(pairwise, holm_adjust(raw_p)):
        item["p_holm"] = adjusted

    cci_by_case = frame.groupby("Case ID")["CCI Score"].first()
    tier3_ids = set(cci_by_case[cci_by_case.between(11, 16)].index)
    if len(tier3_ids) != 48:
        raise ValueError(f"Expected 48 Tier 3 cases (CCI 11–16); found {len(tier3_ids)}.")
    tier3_pivot = pivot.loc[sorted(tier3_ids)]
    tier3 = {
        MODEL_LABELS[m]: {
            "n": int(tier3_pivot[m].count()),
            "mean": float(tier3_pivot[m].mean()),
            "sd": float(tier3_pivot[m].std(ddof=1)),
            "median": float(tier3_pivot[m].median()),
        } for m in MODELS
    }
    tier3_test = stats.friedmanchisquare(*(tier3_pivot[m].to_numpy() for m in MODELS))

    safety = frame.pivot(index="Case ID", columns="Model Name", values="Major Safety Error").reindex(columns=MODELS)
    safety_rates = {
        MODEL_LABELS[m]: {
            "events": int(safety[m].sum()), "n": int(len(safety)),
            "rate": float(safety[m].mean()),
        } for m in MODELS
    }
    safety_pairs, safety_raw = [], []
    for a, b in itertools.combinations(MODELS, 2):
        x, y = safety[a].to_numpy(), safety[b].to_numpy()
        b10 = int(np.sum((x == 1) & (y == 0)))
        b01 = int(np.sum((x == 0) & (y == 1)))
        discordant = b10 + b01
        p = float(stats.binomtest(min(b10, b01), n=discordant, p=0.5, alternative="two-sided").pvalue) if discordant else 1.0
        safety_pairs.append({
            "model_1": MODEL_LABELS[a], "model_2": MODEL_LABELS[b],
            "model_1_error_only": b10, "model_2_error_only": b01,
            "discordant_pairs": discordant, "p_exact_mcnemar": p,
        })
        safety_raw.append(p)
    for item, adjusted in zip(safety_pairs, holm_adjust(safety_raw)):
        item["p_holm"] = adjusted

    merged = frame.merge(cases, on=["Case ID", "Source Type"], how="left")
    merged = merged.rename(columns={"CHAB Score": "Score"})
    mixed = smf.mixedlm("Score ~ C(Q('Model Name')) * C(Q('Source Type'))", merged, groups=merged["Case ID"])
    mixed_fit = mixed.fit(reml=True, method="lbfgs")
    mixed_results = {
        "formula": "Score ~ Model * Provenance + (1 | Case_ID)",
        "n_cases": int(merged["Case ID"].nunique()), "n_observations": int(len(merged)),
        "converged": bool(mixed_fit.converged),
        "coefficients": {str(k): float(v) for k, v in mixed_fit.fe_params.items()},
        "p_values": {str(k): float(v) for k, v in mixed_fit.pvalues.items()},
        "aic": float(mixed_fit.aic) if np.isfinite(mixed_fit.aic) else None,
        "bic": float(mixed_fit.bic) if np.isfinite(mixed_fit.bic) else None,
    }

    return {
        "analysis_metadata": {
            "canonical_cases": 80, "ai_models": 4, "canonical_model_case_rows": 320,
            "guideline_derived_cases": 56, "published_case_report_cases": 24,
            "overflow_cases_excluded": 4, "human_reference_cohorts_excluded": True,
            "domain_weights": DOMAIN_WEIGHTS, "bootstrap_resamples": N_BOOT,
            "bootstrap_seed": SEED,
        },
        "descriptive_statistics": desc,
        "primary_friedman": {
            "test": "Repeated-measures Friedman", "df": 3,
            "statistic": float(friedman.statistic), "p_value": float(friedman.pvalue),
        },
        "pairwise_wilcoxon_holm": pairwise,
        "tier3_cci_11_16": {
            "n_cases": len(tier3_ids), "descriptives": tier3,
            "friedman": {"df": 3, "statistic": float(tier3_test.statistic), "p_value": float(tier3_test.pvalue)},
        },
        "safety_sev2_sev3": {"rates": safety_rates, "exact_mcnemar_pairs_holm": safety_pairs},
        "provenance_mixed_effects": mixed_results,
    }


def print_summary(results):
    print("\nCHAB-2026 VERIFIED STATISTICAL SUMMARY")
    print("=" * 92)
    print(f"{'Model':<24} {'Mean':>8} {'SD':>8} {'Median':>8} {'IQR':>8} {'BCa 95% CI':>24}")
    for model, d in results["descriptive_statistics"].items():
        lo, hi = d["bca_95_ci_mean"]
        print(f"{model:<24} {d['mean']:>8.2f} {d['sd']:>8.2f} {d['median']:>8.2f} {d['iqr']:>8.2f} [{lo:.2f}, {hi:.2f}]")
    f = results["primary_friedman"]
    print(f"\nPrimary Friedman: chi-square={f['statistic']:.4f}, df={f['df']}, p={f['p_value']:.6g}")
    print(f"Tier 3 Friedman: chi-square={results['tier3_cci_11_16']['friedman']['statistic']:.4f}, p={results['tier3_cci_11_16']['friedman']['p_value']:.6g}")
    print("\nPairwise Wilcoxon (Holm-adjusted)")
    for p in results["pairwise_wilcoxon_holm"]:
        print(f"  {p['model_1']} vs {p['model_2']}: dz={p['cohens_dz']:.3f}, p_adj={p['p_holm']:.6g}")
    print("\nSafety SEV-2/3 exact McNemar (Holm-adjusted)")
    for p in results["safety_sev2_sev3"]["exact_mcnemar_pairs_holm"]:
        print(f"  {p['model_1']} vs {p['model_2']}: p_adj={p['p_holm']:.6g}")
    print("\nProvenance mixed-effects model converged:", results["provenance_mixed_effects"]["converged"])


def main():
    cases, frame = load_canonical_data()
    results = run_analysis(cases, frame)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(results, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    print_summary(results)
    print(f"\nMachine-readable results written to: {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"ANALYSIS NOT RUN: {exc}", file=sys.stderr)
        sys.exit(1)
