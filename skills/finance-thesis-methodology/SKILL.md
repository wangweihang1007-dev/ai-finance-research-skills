---
name: finance-thesis-methodology
description: Model-agnostic finance master's thesis methodology skill for any AI assistant or coding agent, including ChatGPT, Claude, Gemini, Codex, and other LLMs. Use when turning finance thesis research questions into executable empirical designs or evaluating methodology for OLS, panel regressions, DID, event studies, IV, PSM, mediation-style mechanism tests, heterogeneity analysis, robustness tests, endogeneity handling, variable definitions, sample construction, fixed effects, clustered standard errors, and thesis-ready methodology writing.
---

# Finance Thesis Methodology

## Core Rule

This is a model-agnostic working standard for ChatGPT, Claude, Gemini, Codex, and other AI assistants. Convert a finance thesis idea into an empirical design that can actually be estimated and defended. Always make the chain explicit:

```text
research question -> theory/mechanism -> hypotheses -> variables -> sample -> model -> identification -> tests -> thesis writing
```

Do not stop at generic suggestions. Produce concrete variable names, model equations, expected signs, sample requirements, fixed effects, clustering choices, and test tables whenever the user's topic allows it.

## Universal Agent Rules

Apply these rules regardless of the AI model, interface, or programming tool being used:

1. Start from the user's thesis topic, not from a preferred econometric model.
2. Identify the economic question before recommending OLS, panel FE, DID, event study, IV, PSM, or any other model.
3. Make all assumptions explicit when the topic lacks sample, period, variable, or data-source details.
4. Prefer defensible, thesis-ready empirical designs over technically fancy designs that the available data cannot support.
5. Separate baseline association, causal identification, robustness, heterogeneity, and mechanism tests.
6. Do not claim causality unless the identification strategy supports it.
7. Keep model equations, variable definitions, and table order concrete enough for Stata, R, Python, or manual thesis writing.
8. When writing code later, keep methodology decisions visible in comments, config files, or output notes.

## First Questions To Resolve

If the user has not provided them, infer cautiously and state assumptions:

- Dependent variable: what outcome is being explained.
- Key independent variable: the treatment, policy, shock, firm trait, market variable, or explanatory factor.
- Unit and frequency: firm-year, firm-quarter, stock-day, fund-month, province-year, bank-year, event-window, or portfolio-time.
- Sample and period: market, database, industry coverage, and years.
- Identification idea: OLS association, panel fixed effects, DID, event study, IV, PSM, mediation-style mechanism, or other design.

Ask a direct question only when the missing information changes the empirical design materially and cannot be reasonably inferred.

## Output Shape

For methodology design tasks, return:

1. A cleaned research question.
2. A theory and mechanism chain.
3. Testable hypotheses.
4. Variable table with dependent, key independent, controls, mechanism variables, heterogeneity variables, and fixed effects.
5. Baseline model equation with subscripts and expected coefficient sign.
6. Identification and endogeneity risks.
7. Robustness tests.
8. Heterogeneity tests.
9. Mechanism tests.
10. Suggested thesis section structure and table order.

For evaluating an existing design, lead with weaknesses and fixes: unclear causality, bad proxy variables, post-treatment controls, omitted fixed effects, clustering mismatch, weak mechanism logic, or tests that do not map to the hypothesis.

## Empirical Model Selection

Choose the model from the research design:

- Use OLS or panel fixed effects when the goal is conditional association and the key variable varies within entity over time.
- Use DID when there is a credible treatment group, control group, and treatment timing.
- Use event study when timing and dynamic effects are central, such as policy shocks, announcements, or market reactions.
- Use IV only when a credible instrument has both relevance and exclusion.
- Use PSM, entropy balancing, or matched samples when selection into treatment is a core concern.
- Use logit/probit when the dependent variable is binary.
- Use Tobit only when censoring is conceptually real, not merely because many observations are zero.
- Use Poisson or negative binomial models for count outcomes such as patent counts when appropriate.
- Use Fama-MacBeth, portfolio sorts, or factor models for asset pricing questions.
- Use mediation-style mechanism regressions when the thesis needs channel evidence, while avoiding overclaiming full mediation.

## Methodology Defaults

Use finance empirical conventions unless the user gives a school or advisor preference:

- Firm panel studies: include firm and year fixed effects by default; consider industry-year fixed effects when shocks vary by industry and year.
- City/province policy studies: include region and year fixed effects; for DID, consider region and year FE plus policy timing checks.
- Standard errors: cluster at the treatment or panel unit level by default; use two-way clustering when both entity and time dependence are credible and the sample supports it.
- Controls: use lagged controls when simultaneity is likely; avoid controls that are direct outcomes of the treatment unless explicitly testing channels.
- Continuous variables: winsorize common financial ratios at 1% and 99% if consistent with the dataset and thesis norm.
- Variable definitions: specify numerator, denominator, frequency, transformation, and data source.

## Model Patterns

Use compact equations and adapt them to the user's topic:

Baseline panel:

```text
Y_{i,t} = alpha + beta X_{i,t} + gamma Controls_{i,t} + mu_i + lambda_t + epsilon_{i,t}
```

DID:

```text
Y_{i,t} = alpha + beta Treat_i x Post_t + gamma Controls_{i,t} + mu_i + lambda_t + epsilon_{i,t}
```

Mechanism:

```text
M_{i,t} = alpha + beta X_{i,t} + gamma Controls_{i,t} + mu_i + lambda_t + epsilon_{i,t}
Y_{i,t} = alpha + beta X_{i,t} + theta M_{i,t} + gamma Controls_{i,t} + mu_i + lambda_t + epsilon_{i,t}
```

Heterogeneity:

```text
Y_{i,t} = alpha + beta1 X_{i,t} + beta2 X_{i,t} x Group_i + gamma Controls_{i,t} + mu_i + lambda_t + epsilon_{i,t}
```

Prefer subgroup regressions when they are easier for a master's thesis reader to interpret, but mention interaction models as a formal comparison.

## Reference Use

When the task requires deeper checks, load `references/methodology_checklists.md` for:

- Variable design standards.
- Endogeneity strategy selection.
- Robustness, heterogeneity, and mechanism test menus.
- Common finance thesis problems and fixes.
- Table ordering and thesis writing templates.

## Quality Checks

Before finalizing a methodology recommendation:

- Check that every hypothesis has at least one direct empirical test.
- Check that every model coefficient maps to a named hypothesis or mechanism.
- Check that the unit of observation matches the variable frequency.
- Check that fixed effects do not absorb the key variable.
- Check that mechanism variables are not merely alternative dependent variables without a channel story.
- Check that robustness tests test fragility instead of repeating the baseline with cosmetic changes.
- State residual limitations honestly, especially if identification is associative rather than causal.
