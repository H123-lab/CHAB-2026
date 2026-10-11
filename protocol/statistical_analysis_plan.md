# CHAB-2026: Primary Statistical Analysis Plan (SAP) v1.0

**Study Title:** Cardiology Humanoid AI Benchmark (CHAB-2026)  
**Registered Repository (OSF):** https://osf.io  
**GitHub Repository:** https://github.com  
**Protocol Version:** v1.0_FROZEN (October 11, 2026)  

***

## 1. Study Framework and Unit of Analysis
The CHAB-2026 study utilizes a prospective, case-matched, repeated-measures simulation design to assess the multi-step clinical reasoning and guideline adherence of large language models. 
- **Primary Unit of Analysis:** Case-level paired observation. Every clinical vignette acts as its own dependent control across model arms to minimize baseline case variance.
- **Canonical Analytical Population:** Exactly 80 cases evaluated across 4 pre-registered language model architectures, yielding a primary sample size of exactly **320 matched model-case observations**.
- **Exclusion Boundaries:** All noncanonical overflow cases ($n=4$) and human clinical reference cohorts (Junior Residents and Attending Cardiologists) are strictly excluded from the primary inferential pipeline to guarantee an unconfounded machine learning evaluation boundary.

## 2. Primary Outcome Measure (Continuous Overall Performance)
The primary continuous outcome is the **Composite CHAB Score (0–100% scale)**, derived as a weighted linear combination across nine pre-registered clinical domains. Ordinal domain grades ($D_i \in \{0, 1, 2\}$) are determined by independent masked dual-reviewers and aggregated using locked fractional proportions:

$$\text{CHAB Score} = 50 \times \sum_{i=1}^{9} (w_i \cdot D_i)$$

Where $\sum w_i = 1.000$. The pre-specified proportions are defined as:
- Diagnosis Accuracy ($D_1$): **0.20**
- Guideline Adherence ($D_3$), Immediate Management ($D_4$), Patient Safety ($D_6$): **0.15 each**
- Investigation Appropriateness ($D_2$), Definitive Management ($D_5$): **0.10 each**
- Emergency Recognition ($D_7$), Specialist Escalation ($D_8$), Reasoning Quality ($D_9$): **0.05 each**

### 2.1 Confirmatory Statistical Testing Hierarchy
1. **Global Omnibus Significance:** Multi-group continuous score variance across the four matched model cohorts is evaluated utilizing the repeated-measures non-parametric **Friedman test with three degrees of freedom ($\text{df}=3$)**, establishing the primary global test statistic ($\chi^2(3)$).
2. **Post-Hoc Pairwise Transitions:** Localized model-to-model score deltas are calculated using **two-sided paired Wilcoxon signed-rank tests**. 
3. **Multiplicity Controls:** Familywise Type I error across the six primary performance comparisons is strictly controlled at a global threshold of $\alpha = 0.05$ via the step-down **Holm-Bonferroni procedure**.
4. **Uncertainty Estimation:** Standard deviations, standard errors, and two-sided 95% confidence intervals are derived utilizing a **10,000-resample non-parametric bias-corrected and accelerated (BCa) bootstrap procedure clustered by unique case ID**, preserving the within-case paired covariance structure.

## 3. Primary Patient Safety Endpoint (Categorical Risk Profiling)
The primary patient safety endpoint is a binary composite parameter tracking the presence or absence of a **Major Safety Error (the SEV-2/SEV-3 composite)** per case execution, evaluated independently of the continuous score.
- **Primary Inferential Test:** Matched categorical error proportions are analyzed strictly via **pairwise exact McNemar tests** evaluating matching case IDs across the six pre-specified model combinations.
- **Multiplicity Controls:** Type I error across the six localized safety hypotheses is managed independently via a separate, dedicated step-down Holm-Bonferroni correction vector to maintain familywise $\alpha = 0.05$.

## 4. Secondary and Exploratory Analytical Specifications
- **Global Safety Cohort Variance:** Cochran's Q test ($Q = 17.65, \text{df}=3, P = 0.042$) is classified strictly as a secondary, global exploratory check of macro-level cohort variance. No McNemar P-values shall be inferred or extrapolated from global Cochran's Q metrics.
- **Case Provenance Interactions:** Performance shifts across case construction tracks (56 synthetic Guideline-Derived scenarios vs. 24 peer-reviewed Published Case Reports) are evaluated descriptively and sensitive-tested utilizing a **linear mixed-effects (LME) model** (REML estimation, random intercept clustered by case ID, Kenward-Roger denominator degrees of freedom).
- **Complexity Trajectory Mapping:** Point-by-point score trajectories across the continuous 5–16 scale of the Case Complexity Index (CCI) are evaluated descriptively using non-linear smoothed **LOESS regression splines**. No post-hoc arbitrary threshold splits are utilized for confirmatory claims.
- **Inter-Rater Reliability:** Inter-observer scoring consistency prior to third-party referee intervention is quantified via continuous two-way random absolute agreement Intraclass Correlation Coefficients ($\text{ICC}(2,1)$) and quadratic-weighted Cohen's kappa ($\kappa$) vectors calculated across the 640 raw reviewer records.

## 5. Missing Data Handling Protocol
The evaluation design enforces complete data matrices. API configurations require complete text response rendering (fixed temperature = 0.0, web-browsing disabled) with script-level recursive retries for any transmission timeouts. Reviewer scoring logs prohibit empty entry fields, utilizing an automated third-party referee adjudication protocol to resolve localized grading drift prior to database unblinding and freezing. Missing data imputation techniques are not permitted.
