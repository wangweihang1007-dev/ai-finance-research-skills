# Finance Thesis Methodology Checklists

## Model-Agnostic Use

These checklists are written for any AI model or assistant. The assistant should not depend on hidden platform features. It should produce plain empirical logic, equations, variable definitions, table plans, and implementation notes that can be used in Word, Stata, R, Python, or a thesis outline.

Universal rule:

```text
topic first, identification second, software last
```

Do not force every topic into DID or IV. Choose the simplest model that can answer the research question under the available data and identification constraints.

## Empirical Model Selection Checklist

- OLS: suitable for cross-sectional association or simple benchmark estimates; weak for causal claims.
- Panel fixed effects: suitable when unobserved time-invariant entity traits are important and variables vary over time.
- DID: suitable only with treatment/control groups and credible pre-treatment comparability.
- Staggered DID: requires extra care with timing, treatment-effect heterogeneity, and event-study interpretation.
- Event study: suitable for market reactions, policy dynamics, and treatment timing; needs clean event dates.
- IV/2SLS: suitable only with a strong instrument and a convincing exclusion restriction.
- PSM/matching: useful for balancing observables; does not solve unobservable selection by itself.
- Logit/probit: suitable for binary outcomes; report marginal effects when useful.
- Tobit: suitable for true censoring; do not use automatically for zero-heavy variables.
- Poisson/negative binomial: suitable for count outcomes such as patent counts or event counts.
- Fama-MacBeth: suitable for asset pricing cross-sectional return tests.
- Portfolio sorts: suitable for intuitive asset pricing or fund performance evidence.
- Factor models: suitable for abnormal returns, risk adjustment, and performance attribution.

## Variable Design

For every important variable, define:

- Role: dependent variable, key independent variable, control, mechanism, heterogeneity, moderator, or fixed effect.
- Economic meaning: what theoretical concept it proxies.
- Formula: numerator, denominator, transformation, lag, log, growth rate, dummy, or index construction.
- Data source: CSMAR, Wind, RESSET, WRDS, Compustat, CRSP, CNRDS, annual reports, local statistical yearbooks, manual collection, or other source.
- Frequency and unit: firm-year, firm-quarter, stock-day, bond-month, fund-month, bank-year, city-year, province-year, event-window.
- Expected sign: positive, negative, nonlinear, or ambiguous.
- Known limitations: measurement error, coverage bias, reporting lag, sample selection, or survivorship bias.

Avoid vague names like `finance`, `risk`, or `quality`. Prefer concrete names such as `FintechIndex`, `ESGScore`, `SAIndex`, `KZIndex`, `CrashRisk_NCSKEW`, `TobinQ`, `ROA`, `LEV`, `Size`, `Age`, `BM`, `Top1`, `SOE`, `Dual`, `BoardIndep`, or `AnalystCoverage`.

## Sample Construction

State these decisions explicitly:

- Market scope: A-share listed firms, banks, funds, bonds, cities, provinces, or international sample.
- Period: start year, end year, and why the period is chosen.
- Exclusions: financial firms, ST/*ST firms, missing key variables, IPO year, delisted firms, abnormal leverage or asset values.
- Merging keys: stock code, firm ID, year, quarter, trading date, city code, province code, fund ID, bond code.
- Treatment definition: policy city/province, pilot list, event date, affected industry, high-exposure group, or continuous exposure.
- Final panel: balanced or unbalanced, number of observations, number of entities, and summary of lost observations.

## Baseline Design

Common finance panel specification:

```text
Y_{i,t} = alpha + beta X_{i,t} + gamma Controls_{i,t} + mu_i + lambda_t + epsilon_{i,t}
```

Recommended explanations:

- `i` is the firm, fund, bank, city, province, or security.
- `t` is year, quarter, month, or day.
- `mu_i` controls time-invariant entity characteristics.
- `lambda_t` controls common macro or market shocks.
- `beta` is the coefficient of interest.
- Cluster standard errors at the entity level unless the treatment varies at a higher level.

Use lagged `X` or lagged controls when reverse causality is plausible and the data frequency supports it.

## DID And Event Study

Use DID only when there is a credible treatment group, control group, and policy/event timing.

Minimum DID checks:

- Treatment and control groups are defined before treatment.
- Post period starts after the actual policy/event date.
- Parallel trend can be shown with leads and lags.
- No obvious policy anticipation unless modeled.
- Treatment is not perfectly collinear with fixed effects.
- Standard errors are clustered at the treatment assignment level when appropriate.

Event-study template:

```text
Y_{i,t} = alpha + sum_k beta_k Treat_i x 1[t - T_i = k] + gamma Controls_{i,t} + mu_i + lambda_t + epsilon_{i,t}
```

Interpretation:

- Pre-treatment coefficients should be statistically close to zero for parallel trends.
- Post-treatment coefficients show dynamic treatment effects.
- Omit one pre-treatment period as the reference group.

## Endogeneity Strategy Menu

Match the strategy to the threat:

- Reverse causality: lag explanatory variables, use policy/event shocks, IV if credible, or dynamic panel only when justified.
- Omitted variables: richer fixed effects, industry-year FE, region-year FE, firm trends, additional controls, or placebo outcomes.
- Selection bias: PSM, entropy balancing, Heckman selection model, or matched DID.
- Measurement error: alternative proxies, index reconstruction, principal component analysis, or external validation.
- Simultaneity: lag structure, event timing, IV, or natural experiment design.
- Policy non-randomness: parallel trends, placebo policy years, matched control groups, city/industry trends, and pre-treatment covariate balance.

Do not recommend an IV unless it satisfies both relevance and exclusion. Always explain why the instrument affects `Y` only through `X`.

## Robustness Test Menu

Choose tests that target the design's actual fragility:

- Replace dependent variable proxy.
- Replace key independent variable proxy.
- Add or remove control variables carefully.
- Change fixed effects: industry FE, firm FE, year FE, industry-year FE, province-year FE.
- Change clustering level.
- Winsorization alternatives: 1%/99%, 5%/95%, or no winsorization.
- Alternative sample periods.
- Exclude special industries, crisis years, COVID years, financial firms, ST firms, or municipalities.
- Lag key independent variable.
- Placebo treatment group or placebo policy year.
- PSM or entropy-balanced sample.
- Parallel trend and dynamic effect tests for DID.
- Alternative model: logit/probit for binary outcomes, Tobit for censored variables, Poisson for counts, Fama-MacBeth for asset pricing panels.

## Heterogeneity Test Menu

Heterogeneity should be tied to theory, not arbitrary sample splitting.

Common finance dimensions:

- Ownership: SOE vs non-SOE.
- Financing constraints: high vs low SA/KZ/WW index.
- Information environment: analyst coverage, institutional ownership, Big Four audit, media attention.
- Governance: board independence, duality, ownership concentration, internal control quality.
- Region: marketization level, legal environment, financial development, digital finance, eastern/central/western China.
- Industry: high-tech vs traditional, heavily polluting vs non-polluting, competitive vs concentrated.
- Firm lifecycle: growth, maturity, decline.
- Size: large vs small firms.
- Risk level: high vs low volatility, high vs low leverage.

Report whether heterogeneity is tested by subgroup regressions, interaction terms, or both.

## Mechanism Test Menu

A mechanism test should answer "through what channel does X affect Y?"

Typical finance mechanisms:

- Financing constraint channel: SA index, KZ index, WW index, interest expense, credit access, debt maturity.
- Information asymmetry channel: analyst coverage, forecast dispersion, bid-ask spread, voluntary disclosure, media attention.
- Governance channel: agency cost, internal control, board independence, ownership concentration, executive incentives.
- Innovation channel: R&D intensity, patent applications, invention patents, green patents.
- Risk-taking channel: earnings volatility, leverage, investment volatility, stock return volatility, crash risk.
- Resource allocation channel: investment efficiency, overinvestment, underinvestment, capital expenditure.
- Market attention channel: turnover, institutional ownership, liquidity, investor sentiment.
- ESG/green channel: environmental investment, pollution fees, green patents, environmental disclosure.

Preferred mechanism structure:

1. Show `X` significantly affects mechanism variable `M`.
2. Show the sign of `M` is consistent with the theory when explaining `Y`.
3. Avoid overclaiming full mediation unless the design supports it.

## Common Problems And Fixes

- Problem: The hypothesis says "improves firm value" but the dependent variable is profitability.
  Fix: align the hypothesis with `TobinQ`, market value, ROA, or explain why profitability is the chosen dimension.

- Problem: Firm fixed effects absorb a time-invariant key variable.
  Fix: use interaction with time variation, DID, random effects only with justification, or change the key variable proxy.

- Problem: Controls include a mechanism variable.
  Fix: remove it from baseline controls and test it separately in the mechanism section.

- Problem: Heterogeneity groups are based on post-treatment values.
  Fix: define groups using pre-treatment or lagged characteristics.

- Problem: DID treatment group is chosen based on outcome performance.
  Fix: redefine treatment using policy exposure, geography, industry exposure, or pre-existing characteristics.

- Problem: Robustness tests are only "add more controls".
  Fix: include alternative proxies, alternative samples, placebo tests, and fixed-effect or clustering checks.

## Thesis Table Order

Recommended empirical chapter order:

1. Variable definitions table.
2. Descriptive statistics.
3. Correlation matrix.
4. Baseline regression.
5. Endogeneity or identification tests.
6. Robustness tests.
7. Heterogeneity analysis.
8. Mechanism tests.
9. Additional tests or economic significance.

## Writing Templates

Baseline model explanation:

```text
To test Hypothesis H1, this thesis estimates the following panel fixed-effects model: ...
The coefficient of interest is beta. If beta is significantly positive/negative, it indicates that ...
Firm fixed effects control for time-invariant firm characteristics, while year fixed effects control for macroeconomic shocks common to all firms.
Standard errors are clustered at the firm level.
```

Robustness explanation:

```text
To examine whether the baseline conclusion depends on measurement, sample selection, or model specification, this thesis conducts the following robustness tests: ...
The coefficient of the core explanatory variable remains consistent in sign and statistical significance, indicating that the main conclusion is robust.
```

Mechanism explanation:

```text
The previous results show that X affects Y. This section further examines whether the effect operates through M.
If X significantly affects M and M is associated with Y in the expected direction, the evidence supports the proposed mechanism.
```
