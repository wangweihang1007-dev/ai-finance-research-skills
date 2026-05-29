# Finance Empirical Diagnosis Checklists

## Severity Levels

- High: invalid identification, wrong dependent/key variable, bad merge, duplicate expansion, fixed effects absorb treatment, post-treatment controls in baseline, impossible sample, unsupported causal claim.
- Medium: weak robustness, unexplained sample changes, clustering mismatch, unstable signs, missing mechanism logic, heterogeneity groups chosen after treatment.
- Low: formatting, unclear notes, missing variable labels, table order problems, wording too strong.

## Regression Table Checks

For each column:

- Model name and purpose.
- Dependent variable.
- Key coefficient and expected sign.
- Standard error type.
- Fixed effects included.
- Controls included.
- Observations.
- R-squared or relevant fit statistic.
- Clustering level.

Warnings:

- Key coefficient flips sign without specification explanation.
- Significance disappears after basic controls.
- Observations drop sharply after adding controls.
- R-squared changes implausibly.
- Fixed effects are listed but not actually included.
- Standard errors are too small due to no clustering.

## Data And Sample Checks

Ask whether:

- Entity-time rows are unique.
- Sample filters are applied before variable construction where required.
- Treatment and outcome are measured in the right time order.
- Lags are calculated within entity.
- Winsorization excludes dummies and identifiers.
- Missing values are not silently dropping most observations.
- Merge keys created duplicate observations.

## Model Specification Checks

Panel FE:

- Entity FE and time FE are usually expected.
- Key variable must vary within entity over time.
- Cluster at entity or treatment level.

DID:

- Treatment group and control group are defined before treatment.
- Parallel trends are tested.
- Policy timing is correct.
- Placebo timing or placebo groups are useful.
- Standard errors should reflect treatment assignment level.

IV:

- First-stage relevance is reported.
- Exclusion restriction is argued, not assumed.
- Weak instrument risk is discussed.
- Overidentification tests are interpreted carefully.

PSM:

- Matching variables are pre-treatment.
- Balance after matching is shown.
- Common support is checked.
- PSM does not solve unobservable selection by itself.

## Mechanism Diagnosis

A mechanism is weak if:

- The mechanism variable is just another outcome with no channel logic.
- The baseline controls already include the mechanism variable.
- `X` does not significantly affect `M`.
- The sign of `M` contradicts the theory.
- The thesis claims full mediation without sufficient evidence.

Better wording:

```text
The results are consistent with the proposed mechanism.
```

Avoid:

```text
This proves that the effect is caused by the mechanism.
```

## Heterogeneity Diagnosis

Check:

- Grouping variable is theory-based.
- Group is measured before treatment or lagged where needed.
- Subgroup sample sizes are adequate.
- Difference between groups is tested with an interaction when necessary.
- Interpretation does not overstate one significant subgroup and one insignificant subgroup as a proven difference.

## Robustness Diagnosis

A useful robustness test should target one threat:

- Measurement: alternative dependent/key variables.
- Outliers: winsorization or excluding extremes.
- Specification: fixed effects, clustering, controls.
- Sample: excluding special years, industries, or regions.
- Timing: lagged variables or alternative treatment windows.
- Placebo: fake outcomes, fake policy years, fake treatment groups.
- Selection: matching or balancing.

Weak robustness:

- Repeating the same model with cosmetic changes.
- Adding many controls without theory.
- Using alternative proxies that measure a different concept.

## Thesis Interpretation

If result is significant with expected sign:

```text
The coefficient is consistent with H1, suggesting that ...
```

If insignificant:

```text
The estimated coefficient has the expected sign but is not statistically significant, so the current evidence does not provide strong support for H1.
```

If wrong sign:

```text
The coefficient is opposite to the theoretical expectation, indicating that the hypothesis may not hold in this sample or that measurement/model specification requires further examination.
```

If causal identification is weak:

```text
The result should be interpreted as conditional association rather than definitive causal evidence.
```
