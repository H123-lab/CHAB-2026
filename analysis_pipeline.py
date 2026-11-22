#!/usr/bin/env python3
"""
CHAB-2026: Cardiology AI Benchmark
Authoritative Statistical Analysis Plan (SAP) Execution Engine
Reads raw case-level domain ratings from the Master Audit Workbook and computes
all primary and secondary inferential statistics dynamically.
"""

import os
import sys
import warnings
import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.api as sm
import statsmodels.formula.api as smf

warnings.filterwarnings("ignore")

# Prespecified Domain Weights (Must sum to 1.000)
DOMAIN_WEIGHTS = {
    "D1": 0.20,  # Diagnostic Accuracy
    "D2": 0.10,  # Investigation Appropriateness
    "D3": 0.15,  # Guideline Adherence
    "D4": 0.15,  # Immediate Management & Triage
    "D5": 0.10,  # Definitive Long-Term Management
    "D6": 0.15,  # Patient Safety & Error Avoidance
    "D7": 0.05,  # Emergency Recognition
    "D8": 0.05,  # Specialist Escalation
    "D9": 0.05,  # Clinical Reasoning Quality
}

MODELS = [
    "Model Alpha (GPT-5)",
    "Model Beta (Claude 3.5 Sonnet)",
    "Model Gamma (Gemini 1.5 Pro)",
    "Model Delta (DeepSeek-V3)",
]


def load_and_validate_workbook(filepath: str):
    """Loads raw sheets and enforces canonical cohort boundaries (N=80, n=320)."""
    if not os.path.exists(filepath):
        # Fallback check for root directory placement
        alt_path = os.path.basename(filepath)
        if os.path.exists(alt_path):
            filepath = alt_path
        else:
            raise FileNotFoundError(f"Master workbook not found at {filepath}")

    xl = pd.ExcelFile(filepath)
    sheet_names = xl.sheet_names

    # Identify source, execution, and adjudicated score sheets
    source_df = pd.read_excel(xl, sheet_name=sheet_names[0])
    scores_df = pd.read_excel(xl, sheet_name=sheet_names[-1])

    # Normalize column names
    source_df.columns = [c.strip() for c in source_df.columns]
    scores_df.columns = [c.strip() for c in scores_df.columns]

    # Filter strictly to canonical 80 cases (exclude overflow & human cohorts)
    canonical_sources = source_df[
        source_df["Case ID"].astype(str).str.contains("GD-|CR-", regex=True)
    ].copy()
    canonical_sources = canonical_sources[
        ~canonical_sources["Case ID"].astype(str).str.contains("OVERFLOW|HF-GD-008|HF-GD-009|HF-GD-010|LIT-004", regex=True)
    ]

    valid_case_ids = set(canonical_sources["Case ID"].unique())
    df = scores_df[scores_df["Case ID"].isin(valid_case_ids)].copy()

    # Keep primary 4 AI models only
    df = df[df["Model Name"].isin(MODELS)].copy()

    return canonical_sources, df


def compute_chab_scores(df: pd.DataFrame) -> pd.DataFrame:
    """Computes composite 0-100 CHAB Score from D1-D9 adjudicated domain ratings."""
    domain_cols = [f"D{i}" for i in range(1, 10)]
    missing_cols = [c for c in domain_cols if c not in df.columns]

    if missing_cols:
        raise ValueError(
            f"DATA INTEGRITY ERROR: Missing required domain columns {missing_cols} in scoring sheet. "
            "All 9 domains (D1-D9) must be present to compute the weighted CHAB score."
        )

    weighted_sum = sum(df[col].astype(float) * DOMAIN_WEIGHTS[col] for col in domain_cols)
    df["Computed_CHAB_Score"] = 50.0 * weighted_sum
    return df


def bootstrap_bca_ci(data: np.ndarray, n_resamples: int = 10000, seed: int = 42):
    """Computes exact 95% BCa bootstrap confidence intervals."""
    rng = np.random.default_rng(seed)
    res = stats.bootstrap(
        (data,),
        np.mean,
        n_resamples=n_resamples,
        confidence_level=0.95,
        method="BCa",
        random_state=rng,
    )
    return res.confidence_interval.low, res.confidence_interval.high


def holm_bonferroni(p_values: list) -> list:
    """Applies step-down Holm-Bonferroni multiplicity correction."""
    m = len(p_values)
    indexed = sorted(enumerate(p_values), key=lambda x: x[1])
    adjusted = [0.0] * m
    prev_max = 0.0
    for rank, (orig_idx, p) in enumerate(indexed):
        adj_p = min(1.0, max(prev_max, p * (m - rank)))
        adjusted[orig_idx] = adj_p
        prev_max = adj_p
    return adjusted


def run_primary_analysis(sources: pd.DataFrame, df: pd.DataFrame):
    """Executes all confirmatory and secondary statistical tests."""
    print("=========================================================================")
    print("        CHAB-2026 AUTHORITATIVE STATISTICAL EXECUTION REPORT             ")
    print("=========================================================================\n")

    n_cases = df["Case ID"].nunique()
    n_obs = len(df)
    print(f"[COHORT VERIFIED] Canonical Cases: N = {n_cases} | Primary Observations: n = {n_obs}\n")

    if n_cases != 80 or n_obs != 320:
        raise AssertionError(f"Expected N=80 cases and n=320 rows, found N={n_cases}, n={n_obs}")

    # Pivot to Case x Model matrix (80 x 4)
    pivot_scores = df.pivot(index="Case ID", columns="Model Name", values="Computed_CHAB_Score")[MODELS]

    # 1. Descriptive Summary & 95% BCa CIs
    print("--- 1. OVERALL CONTINUOUS PERFORMANCE (CHAB SCORE 0-100) ---")
    for model in MODELS:
        vals = pivot_scores[model].dropna().values
        mean_val = np.mean(vals)
        sd_val = np.std(vals, ddof=1)
        med_val = np.median(vals)
        q25, q75 = np.percentile(vals, [25, 75])
        ci_low, ci_high = bootstrap_bca_ci(vals)
        print(
            f"{model:<32} | Mean: {mean_val:6.2f} ± {sd_val:5.2f} | "
            f"Median: {med_val:6.2f} (IQR: {q25:5.2f}-{q75:5.2f}) | "
            f"95% BCa CI: [{ci_low:6.2f}, {ci_high:6.2f}]"
        )

    # 2. Primary Omnibus Test: Repeated-Measures Friedman Test (df = 3)
    friedman_stat, friedman_p = stats.friedmanchisquare(
        pivot_scores[MODELS[0]],
        pivot_scores[MODELS[1]],
        pivot_scores[MODELS[2]],
        pivot_scores[MODELS[3]],
    )
    print(f"\n[PRIMARY OMNIBUS] Friedman Test (df = 3): chi^2(3) = {friedman_stat:.4f}, P = {friedman_p:.4e}\n")

    # 3. Post-Hoc Pairwise Wilcoxon Signed-Rank + Holm-Bonferroni
    print("--- 2. POST-HOC PAIRWISE MODEL CONTRASTS (WILCOXON + HOLM-BONFERRONI) ---")
    pairs = []
    raw_pvals = []
    for i in range(len(MODELS)):
        for j in range(i + 1, len(MODELS)):
            m1, m2 = MODELS[i], MODELS[j]
            diff = pivot_scores[m1].values - pivot_scores[m2].values
            mean_diff = np.mean(diff)
            sd_diff = np.std(diff, ddof=1)
            dz = mean_diff / sd_diff if sd_diff > 0 else 0.0
            ci_l, ci_h = bootstrap_bca_ci(diff)
            w_stat, p_val = stats.wilcoxon(pivot_scores[m1], pivot_scores[m2])
            pairs.append((m1, m2, mean_diff, ci_l, ci_h, dz, w_stat, p_val))
            raw_pvals.append(p_val)

    adj_pvals = holm_bonferroni(raw_pvals)
    for idx, (m1, m2, m_diff, ci_l, ci_h, dz, w_stat, p_raw) in enumerate(pairs):
        print(
            f"{m1} vs. {m2}:\n"
            f"   Delta = {m_diff:+6.2f} (95% BCa CI: [{ci_l:+6.2f}, {ci_h:+6.2f}]) | "
            f"Cohen's dz = {dz:.3f} | W = {w_stat:.1f} | P_raw = {p_raw:.4e} | P_adj = {adj_pvals[idx]:.4f}"
        )

    # 4. Primary Composite Safety Analysis (SEV-2 / SEV-3 Exact McNemar)
    print("\n--- 3. PRIMARY SAFETY ANALYSIS (SEV-2 / SEV-3 EXACT MCNEMAR) ---")
    df["Major_Safety_Error"] = df["Safety Error (SEV)"].isin(["SEV-2", "SEV-3"]).astype(int)
    pivot_safety = df.pivot(index="Case ID", columns="Model Name", values="Major_Safety_Error")[MODELS]

    for model in MODELS:
        err_count = pivot_safety[model].sum()
        print(f"{model:<32} | SEV-2/3 Errors: {err_count}/80 ({err_count / 80 * 100:.2f}%)")

    safety_pairs = []
    safety_raw_p = []
    for i in range(len(MODELS)):
        for j in range(i + 1, len(MODELS)):
            m1, m2 = MODELS[i], MODELS[j]
            s1, s2 = pivot_safety[m1].values, pivot_safety[m2].values
            # Discordant pairs: b (m1=1, m2=0), c (m1=0, m2=1)
            b = np.sum((s1 == 1) & (s2 == 0))
            c = np.sum((s1 == 0) & (s2 == 1))
            n_disc = b + c
            p_exact = stats.binomtest(min(b, c), n=n_disc, p=0.5).pvalue if n_disc > 0 else 1.0
            safety_pairs.append((m1, m2, b, c, p_exact))
            safety_raw_p.append(p_exact)

    safety_adj_p = holm_bonferroni(safety_raw_p)
    for idx, (m1, m2, b, c, p_raw) in enumerate(safety_pairs):
        print(
            f"{m1} vs. {m2}: Discordant (b={b}, c={c}) | "
            f"Exact McNemar P_raw = {p_raw:.4f} | P_adj = {safety_adj_p[idx]:.4f}"
        )

    # 5. Case Provenance Linear Mixed-Effects Model (GD vs. CR)
    print("\n--- 4. CASE PROVENANCE MIXED-EFFECTS MODEL (GD vs. CR) ---")
    merged = df.merge(sources[["Case ID", "Source Type"]], on="Case ID", how="left")
    merged = merged.rename(columns={"Computed_CHAB_Score": "Score", "Model Name": "Model", "Source Type": "Provenance"})
    lme = smf.mixedlm("Score ~ C(Model) * C(Provenance)", merged, groups=merged["Case ID"])
    lme_fit = lme.fit(reml=True)
    print(lme_fit.summary().tables[1])


if __name__ == "__main__":
    WORKBOOK_PATH = "data/CHAB-2026_Authoritative_Master_Audit_Workbook_FINAL.xlsx"
    try:
        sources_data, ratings_data = load_and_validate_workbook(WORKBOOK_PATH)
        scored_data = compute_chab_scores(ratings_data)
        run_primary_analysis(sources_data, scored_data)
    except Exception as exc:
        print(f"\n[EXECUTION HALTED] {exc}", file=sys.stderr)
        sys.exit(1)

        
   
   

