---
name: finance-empirical-diagnosis
description: Model-agnostic finance empirical diagnosis skill for any AI assistant or coding agent, including ChatGPT, Claude, Gemini, Codex, and other LLMs. Use when checking finance thesis regression results, empirical design, Stata/R/Python outputs, coefficient signs, significance, fixed effects, clustered standard errors, multicollinearity, sample changes, endogeneity tests, robustness tests, heterogeneity tests, mechanism tests, table consistency, and thesis interpretation risks.
---

# Finance Empirical Diagnosis

## Core Rule

This is a model-agnostic working standard for ChatGPT, Claude, Gemini, Codex, and other AI assistants. Diagnose whether finance empirical results are coherent, defensible, and thesis-ready.

```text
design -> data -> model -> output -> interpretation -> robustness -> thesis claim
```

Lead with problems and fixes. Do not merely describe regression tables.

## Universal Agent Rules

Apply these rules regardless of model, software, or interface:

1. Check whether the regression matches the stated hypothesis.
2. Check whether variable definitions and coefficient signs make economic sense.
3. Check fixed effects, clustering, sample size, and model statistics before interpreting significance.
4. Treat sudden sample changes across columns as a warning unless explained.
5. Distinguish insignificant results, wrong-sign results, unstable results, and economically small results.
6. Evaluate robustness tests by what threat they address.
7. Evaluate mechanism tests by whether they support the stated channel.
8. Evaluate heterogeneity tests by whether groups are theory-based and pre-determined.
9. Do not overclaim causality from associative regressions.
10. Provide concrete repair options: model change, variable change, sample check, extra test, or wording downgrade.

## First Questions To Resolve

Infer cautiously if missing:

- Research hypothesis and expected coefficient sign.
- Regression model type: OLS, panel FE, DID, event study, IV, PSM, logit/probit, Tobit, factor model.
- Unit and frequency.
- Dependent variable, key independent variable, controls, fixed effects, and clustering.
- Regression output source: table, Stata log, Python/R output, Excel, Word table, or screenshot text.

Ask only when the missing detail prevents diagnosis.

## Output Shape

For diagnosis tasks, return:

1. Overall judgment: usable, usable with revisions, risky, or not defensible.
2. Main problems ranked by severity.
3. Coefficient sign and significance interpretation.
4. Model specification checks.
5. Sample and data consistency checks.
6. Robustness/endogeneity/heterogeneity/mechanism assessment.
7. Suggested fixes and additional tests.
8. Thesis wording suggestions.

For code or table review, reference specific variables, columns, models, or output lines when available.

## Diagnosis Areas

Check these systematically:

- Hypothesis alignment: the coefficient tested is the coefficient required by the hypothesis.
- Variable validity: proxy matches the concept and frequency.
- Fixed effects: not omitted, excessive, or absorbing the key variable.
- Standard errors: clustered at a defensible level.
- Controls: not post-treatment mechanisms unless intended.
- Sample: filters are consistent and column-by-column N changes are explained.
- Multicollinearity: VIF or high correlations when signs/significance are unstable.
- Endogeneity: reverse causality, omitted variables, selection, simultaneity, measurement error.
- Robustness: alternative proxies, samples, fixed effects, clustering, placebo, lag structures.
- Mechanism: channel logic and empirical support.
- Heterogeneity: group definition and interaction/subgroup consistency.

## Reference Use

Load `references/diagnosis_checklists.md` when deeper detail is needed for:

- Regression red flags.
- Table-by-table diagnostic workflow.
- DID/event-study checks.
- IV and PSM diagnosis.
- Mechanism and heterogeneity assessment.
- Thesis interpretation wording.

## Quality Checks

Before finalizing:

- State what evidence is available and what cannot be diagnosed from it.
- Separate statistical significance from economic significance.
- Identify whether the result supports, partly supports, or fails to support each hypothesis.
- Recommend the minimum necessary fixes before broad redesign.
- Downgrade claims when identification is weak.
