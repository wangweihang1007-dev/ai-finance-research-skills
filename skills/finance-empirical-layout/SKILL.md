---
name: organize-code-artifacts
description: Enforce a model-agnostic finance empirical research project layout with correct code, data, table, figure, regression, and robustness-test directories. Use when any AI assistant or coding agent writes or modifies code for financial empirical analysis, asset pricing, corporate finance, event studies, panel regressions, factor models, portfolio sorts, difference-in-differences, data downloads, CSMAR/Wind/WRDS/Compustat/CRSP-style datasets, CSV/Excel/Stata outputs, regression tables, figures, logs, or research reports.
---

# Finance Empirical Project Organization

## Core Rule

This is a model-agnostic working standard for Gemini, Claude, Codex, ChatGPT, and other AI coding agents. Before writing code or downloading data for a finance empirical task, inspect the workspace and create or reuse a clearly named research project directory. The layout must make the empirical pipeline obvious: data source -> cleaning -> sample construction -> variable construction -> analysis -> tables/figures -> reports.

Use finance-specific names such as `stock-liquidity-panel`, `green-finance-did`, `earnings-announcement-event-study`, `fund-flow-performance`, or `analyst-coverage-returns`. Avoid vague folders like `test`, `new-code`, `data1`, `regression`, or `final-output`.

## Universal Agent Instructions

Apply these rules regardless of the model or tool being used:

1. Inspect the current directory before creating files.
2. If a suitable finance empirical project directory exists, reuse it.
3. If no suitable directory exists, create a descriptive project directory first.
4. Create code, data, output, and report subdirectories before writing files.
5. Put each script and artifact in the correct empirical-stage folder.
6. Never place generated CSVs, figures, regression logs, or datasets in the workspace root.
7. Keep paths centralized and make scripts create missing output folders automatically.
8. At the end, report the created or modified directory layout and key output paths.

## Required Layout

Use this structure for a new finance empirical project unless the repository already has a strict convention:

```text
project-name/
  README.md
  config/
    paths.yaml
    sample_filters.yaml
  code/
    00_setup/
    01_download/
    02_clean/
    03_construct_sample/
    04_construct_variables/
    05_descriptive_stats/
    06_baseline_regression/
    07_robustness/
    08_heterogeneity/
    09_mechanism/
    10_figures/
    11_tables/
    utils/
  data/
    raw/
    external/
    interim/
    panel/
    final/
  outputs/
    tables/
      descriptive/
      baseline/
      robustness/
      heterogeneity/
      mechanism/
    figures/
      sample/
      descriptive/
      regression/
    regressions/
      logs/
      estimates/
      diagnostics/
    logs/
  reports/
  docs/
  notebooks/
  tests/
```

Create only the folders needed for the current task, but keep their names compatible with this structure. Do not dump scripts, CSVs, figures, or regression output in the project root.

## Code Directory Rules

Place empirical code by stage:

- `code/00_setup/`: environment checks, path initialization, package setup, reproducibility seeds.
- `code/01_download/`: API/database download scripts, web collection, WRDS/CSMAR/Wind/export import scripts.
- `code/02_clean/`: source-specific cleaning, type fixes, identifier normalization, date parsing, duplicate handling.
- `code/03_construct_sample/`: sample filters, merge logic, panel balancing, event-window construction, treatment/control selection.
- `code/04_construct_variables/`: dependent variables, key independent variables, controls, winsorization, lags, industry/year definitions.
- `code/05_descriptive_stats/`: summary statistics, correlation matrices, sample distribution tables.
- `code/06_baseline_regression/`: main specifications, fixed effects, clustered standard errors, model exports.
- `code/07_robustness/`: alternative variable definitions, alternative samples, placebo tests, parallel trends, additional controls.
- `code/08_heterogeneity/`: subgroup regressions, interaction terms, cross-sectional splits.
- `code/09_mechanism/`: channel tests, mediation-style regressions, mechanism variables.
- `code/10_figures/`: plotting scripts for empirical figures.
- `code/11_tables/`: table formatting/export scripts when table generation is separate from estimation.
- `code/utils/`: shared path helpers, data validation helpers, regression/table utilities.

Use numbered script prefixes inside each stage when execution order matters, for example `01_download_prices.py`, `02_clean_firm_ids.py`, or `03_build_panel.py`.

## Data Directory Rules

Keep finance data lineage clear:

- `data/raw/`: untouched source exports or downloads, grouped by source when useful, such as `data/raw/csmar/`, `data/raw/wind/`, `data/raw/wrds/`, `data/raw/manual/`.
- `data/external/`: third-party mappings and reference files, such as industry codes, province codes, trading calendars, CPI/FF factor files, exchange calendars.
- `data/interim/`: cleaned source-level files before final merges.
- `data/panel/`: constructed firm-year, firm-quarter, stock-day, fund-month, event-window, or portfolio panels.
- `data/final/`: final regression-ready datasets used by tables and figures.

Never overwrite raw data. Save cleaned and merged data under new names with a clear frequency and unit, such as `firm_year_controls_2007_2024.parquet`, `stock_day_returns_2015_2025.csv`, or `event_window_car_m5_p5.dta`.

## Output Directory Rules

Save empirical outputs by use and specification:

- `outputs/tables/descriptive/`: summary statistics, correlations, sample distribution, balance tests.
- `outputs/tables/baseline/`: main regression tables.
- `outputs/tables/robustness/`: robustness and placebo tables.
- `outputs/tables/heterogeneity/`: subgroup and interaction tables.
- `outputs/tables/mechanism/`: mechanism/channel test tables.
- `outputs/figures/sample/`: sample coverage, missingness, event timeline, distribution by year/industry.
- `outputs/figures/descriptive/`: trends, binscatter, portfolio returns, factor or variable plots.
- `outputs/figures/regression/`: coefficient plots, event-study plots, parallel-trend plots.
- `outputs/regressions/logs/`: model logs, console output, Stata/R/Python regression logs.
- `outputs/regressions/estimates/`: serialized model results, coefficient files, intermediate estimation outputs.
- `outputs/regressions/diagnostics/`: VIF, residual checks, influence diagnostics, first-stage diagnostics.
- `outputs/logs/`: download logs, cleaning logs, run metadata, data validation reports.

Use deterministic file names that include the empirical object and specification, such as `table_2_baseline_fe_cluster_firm_year.xlsx`, `fig_parallel_trends_treat_policy_year.png`, or `robust_alt_winsor_1_99.csv`.

## Finance Empirical Code Standards

Keep code reproducible and auditable:

- Centralize paths in `config/paths.yaml`, a constants file, or a small path helper in `code/utils/`.
- Make every script create its required output directories before writing files.
- Keep raw data import, cleaning, sample construction, variable construction, and regression separate unless the task is truly tiny.
- Record sample filters explicitly in code or `config/sample_filters.yaml`.
- Preserve identifier logic: stock code, firm ID, fund ID, industry code, exchange, year, quarter, month, date.
- State the unit of observation in filenames and comments when constructing panels.
- Apply winsorization, lag construction, fixed effects, clustering, and sample restrictions in visible, named steps.
- Prefer Parquet or Stata files for large panel intermediates when the local stack supports them; CSV is acceptable for exchange and inspection.
- Keep notebooks exploratory. Move reusable empirical logic into `code/`.

## README Expectations

For non-trivial tasks, create or update `README.md` with:

- Research question or empirical goal.
- Data sources and download dates.
- Unit of observation and sample period.
- Pipeline order for scripts.
- Key outputs and where to find them.

Keep this concise. The README should orient the next empirical run, not become a paper draft.

## Existing Repositories

Respect an existing finance research repository layout if it is already consistent. If it uses names like `do/`, `ado/`, `rawdata/`, `temp/`, `processed/`, `results/`, `tables/`, or `figures/`, map the same empirical stages into those folders instead of imposing the default names.

Do not reorganize unrelated user files in a dirty worktree. For new tasks inside an existing repository, create a clearly scoped subdirectory or fit files into the existing empirical pipeline.
