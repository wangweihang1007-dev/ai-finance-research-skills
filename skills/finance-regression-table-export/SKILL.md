---
name: finance-regression-table-export
description: Export financial empirical regression results into thesis-ready Word three-line tables. Use when creating or formatting regression tables for master's theses, academic papers, finance empirical projects, baseline regressions, robustness tests, heterogeneity tests, mechanism tests, DID/event-study/factor-model/panel-regression outputs, or when converting CSV/Excel/Stata/R/Python regression results into .docx tables with coefficients, standard errors or t-statistics, significance stars, model statistics, and notes.
---

# Finance Regression Table Export

## Core Rule

Produce a Word `.docx` regression table that can be pasted directly into a master's thesis or finance empirical paper. Use a three-line table style: top rule, header-bottom rule, and bottom rule only. Do not export raw console output or messy DataFrame tables as the final result.

## Expected Output

Create a table with:

- A table title above the table, such as `Table 4-2 Baseline Regression Results` or a Chinese thesis title supplied by the user.
- Variables in rows and model specifications in columns.
- Coefficients with significance stars in the first row for each variable.
- Standard errors or t-statistics in parentheses in the second row.
- Model statistics at the bottom, such as controls, industry fixed effects, year fixed effects, observations, R-squared, and adjusted R-squared.
- Notes below the table explaining parentheses, clustering, fixed effects, and significance levels.
- File saved under an empirical output path such as `outputs/tables/baseline/`, `outputs/tables/robustness/`, `outputs/tables/heterogeneity/`, or `outputs/tables/mechanism/`.

Prefer `.docx`. If the user explicitly asks for legacy `.doc`, create `.docx` first and state that Word/WPS can save it as `.doc`.

## Workflow

1. Inspect the regression result source and identify model columns, variables, statistics, and notes.
2. Clean variable names into thesis-readable labels, for example `did` -> `DID`, `size` -> `Firm Size`, `lev` -> `Leverage`.
3. Decide whether parentheses contain standard errors, t-statistics, or p-values. Use standard errors by default for finance empirical tables unless the source clearly uses t-statistics.
4. Add significance stars using `***`, `**`, `*` for 1%, 5%, and 10% levels unless the user specifies another convention.
5. Export a Word three-line table with consistent font, alignment, borders, and notes.
6. Save the table in the correct finance empirical output subdirectory and report the exact path.

## Script

Use `scripts/export_regression_table_docx.py` when the regression results can be represented as a long CSV.

Required CSV columns:

```text
term,model,coef,se
```

Recommended optional columns:

```text
p,label,order,stat
```

Column meanings:

- `term`: variable or statistic key, such as `did`, `size`, `N`, `r2`.
- `model`: model column name, such as `(1)`, `(2)`, `Baseline`, `FE`.
- `coef`: coefficient or statistic value.
- `se`: standard error, t-statistic, or p-value to display in parentheses for coefficient rows.
- `p`: p-value used to generate significance stars.
- `label`: display label for the row.
- `order`: numeric order for variable rows.
- `stat`: set to `1`, `true`, or `yes` for statistic rows that should not get a second parentheses row.

Example:

```powershell
python C:\Users\zhuifeng\.codex\skills\finance-regression-table-export\scripts\export_regression_table_docx.py `
  --input outputs\regressions\estimates\baseline_long.csv `
  --output outputs\tables\baseline\table_4_2_baseline.docx `
  --title "Table 4-2 Baseline Regression Results" `
  --paren-label "clustered robust standard errors" `
  --note "All models include industry and year fixed effects."
```

If the source is a Stata, R, or Python model object, first convert it into the long CSV schema or write a small adapter that produces the same columns.

## Formatting Standards

Use these defaults unless the user gives a school template:

- Page orientation: portrait unless there are many model columns; use landscape for wide tables.
- Title: centered, Chinese font compatible with Word/WPS, 10.5-12 pt.
- Table body: centered model columns, left-aligned variable names, 10.5 pt.
- Borders: only top border, header-bottom border, and bottom border.
- Numbers: normally keep three decimals for coefficients and standard errors.
- Stars: attach to coefficient values, not to standard errors.
- Notes: smaller font below the table, left-aligned.

## Quality Checks

Before finalizing:

- Verify the Word file opens or is at least generated without script errors.
- Check that every model column has the same intended rows.
- Check that coefficient rows and parentheses rows are paired correctly.
- Check that statistics rows are not mistakenly formatted as coefficients.
- Check that the table path is under the correct `outputs/tables/...` folder.
- Mention any assumptions about standard errors, clustering, fixed effects, or stars.
