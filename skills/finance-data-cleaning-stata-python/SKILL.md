---
name: finance-data-cleaning-stata-python
description: Model-agnostic finance empirical data cleaning skill for any AI assistant or coding agent, including ChatGPT, Claude, Gemini, Codex, and other LLMs. Use when cleaning CSMAR, Wind, RESSET, WRDS, Compustat, CRSP, Excel, CSV, Stata, R, or Python datasets for finance master's theses, including identifier normalization, date parsing, panel construction, winsorization, lag variables, sample filters, merges, missing values, duplicates, variable construction, data validation, and reproducible Stata or Python workflows.
---

# Finance Data Cleaning Stata Python

## Core Rule

This is a model-agnostic working standard for ChatGPT, Claude, Gemini, Codex, and other AI assistants. Turn raw finance data into a clean, regression-ready dataset with visible, reproducible steps.

```text
raw data -> source cleaning -> identifiers/dates -> sample filters -> variable construction -> winsorization/lags -> merges -> validation -> final panel
```

Never overwrite raw data. Keep every transformation auditable.

## Universal Agent Rules

Apply these rules regardless of model, software, or interface:

1. Identify the observation unit and frequency before cleaning.
2. Preserve raw files and write cleaned outputs to a new location.
3. Normalize identifiers before merging, especially stock codes, firm IDs, fund IDs, bond IDs, city/province codes, and dates.
4. Record sample filters explicitly: financial firms, ST/*ST, missing values, IPO year, abnormal values, and period restrictions.
5. Check duplicates before and after each merge.
6. Build variables with named formulas, not anonymous transformations.
7. Apply winsorization, lags, and fixed-effect codes consistently.
8. Validate row counts, missing rates, merge rates, and summary statistics before regression.
9. Make outputs usable in Stata, Python, R, Excel, or thesis tables.
10. Report assumptions and any data quality risks.

## First Questions To Resolve

Infer cautiously if missing:

- Data source: CSMAR, Wind, RESSET, WRDS, Compustat, CRSP, annual reports, statistical yearbooks, manual collection.
- File format: `.xlsx`, `.csv`, `.dta`, `.sas7bdat`, `.parquet`, `.rds`, or database export.
- Unit and frequency: firm-year, firm-quarter, stock-day, fund-month, bond-year, city-year, province-year, event-window.
- Target software: Stata, Python, R, or software-neutral pseudocode.
- Final output: cleaned panel, regression-ready dataset, summary table, merge report, or reproducible script.

Ask only when missing information changes the cleaning logic.

## Output Shape

For cleaning plans or scripts, return:

1. Data lineage and target final dataset.
2. Required identifier and date normalization.
3. Sample filters.
4. Variable construction rules.
5. Merge sequence and keys.
6. Missing value and duplicate handling.
7. Winsorization and lag rules.
8. Validation checks.
9. Output filenames and formats.
10. Stata or Python implementation notes when requested.

For reviewing existing cleaning code, lead with risks: raw data overwrite, bad merge keys, duplicate expansion, post-treatment filters, inconsistent date units, silent missing drops, incorrect winsorization, or untracked sample loss.

## Software Defaults

Use the user's preferred software. If unspecified:

- Use Python for flexible file handling, validation, plots, and large CSV/Excel workflows.
- Use Stata for thesis-oriented panel regressions, winsorization, fixed effects, and `.dta` outputs.
- Keep formulas and cleaning logic software-neutral enough to translate across tools.

## Reference Use

Load `references/data_cleaning_checklists.md` when deeper detail is needed for:

- Stata and Python cleaning templates.
- Merge validation.
- Finance variable construction.
- Winsorization and lag rules.
- CSMAR/Wind-style identifier handling.
- Final panel validation.

## Quality Checks

Before finalizing:

- Confirm raw data are untouched.
- Confirm final data have a clear unit and frequency.
- Confirm each merge key is unique on the intended side or intentionally many-to-one.
- Confirm row counts before and after filters and merges.
- Confirm no obvious duplicate entity-time rows remain.
- Confirm missing key variables are handled explicitly.
- Confirm variable formulas match the thesis design.
- Confirm outputs are saved under clean, descriptive names.
