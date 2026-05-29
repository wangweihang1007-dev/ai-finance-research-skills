# Finance Data Cleaning Checklists

## File And Data Lineage

Record these for every source:

- Source name and database.
- Original filename.
- Export date or download date.
- Original row and column counts.
- Unit and frequency.
- Key identifiers.
- Raw path and cleaned output path.
- Known source limitations.

Never edit raw files directly. Save cleaned source-level files before final merges.

## Identifier Normalization

Common finance identifiers:

- Stock code: preserve leading zeros; standardize exchange suffix separately if needed.
- Firm ID: distinguish stock code, listed company ID, accounting firm ID, and security ID.
- Year: integer fiscal year.
- Quarter/month/date: parse to real date types before merging.
- Industry: standardize CSRC, SIC, NAICS, or database-specific industry versions.
- Region: city/province names should be mapped to stable administrative codes.
- Fund/bond IDs: preserve leading zeros and suffixes.

Checks:

- No accidental numeric conversion of codes with leading zeros.
- No mixed date formats.
- No invisible whitespace or full-width characters in identifiers.
- Unique key checks before merges.

## Sample Filters

Common A-share filters:

- Exclude financial firms if the accounting structure is incompatible.
- Exclude ST/*ST firms when required by thesis convention.
- Exclude observations with missing dependent or key independent variables.
- Exclude observations with non-positive total assets when ratios use assets.
- Exclude IPO year or newly listed firms if justified.
- Restrict sample period to match policy, data availability, or research question.

Always report observation loss after each filter.

## Variable Construction

For each variable, record:

- Formula.
- Source fields.
- Unit and scale.
- Whether log transform is applied.
- Whether lagged value is used.
- Winsorization rule.
- Expected sign or role in model.

Common examples:

- `Size = ln(total_assets)`.
- `Lev = total_liabilities / total_assets`.
- `ROA = net_profit / total_assets`.
- `Growth = operating_revenue_growth`.
- `TobinQ = market_value / total_assets` or database-specific equivalent.
- `Cash = cash_and_equivalents / total_assets`.
- `Age = ln(current_year - listing_year + 1)`.
- `BoardIndep = independent_directors / board_size`.
- `Top1 = largest_shareholder_ownership`.
- `SOE = 1` if final controller is state-owned.

## Winsorization And Lags

Defaults:

- Winsorize continuous finance ratios at 1% and 99% unless the school or literature uses another standard.
- Do not winsorize dummy variables, identifiers, years, or categorical codes.
- Lag controls when simultaneity is likely.
- Build lags within entity after sorting by entity and time.
- Check gaps in panel before interpreting lags.

Stata-style pseudocode:

```stata
xtset firm_id year
gen L_size = L.size
winsor2 roa lev size growth, cuts(1 99) replace
```

Python-style pseudocode:

```python
df = df.sort_values(["firm_id", "year"])
df["L_size"] = df.groupby("firm_id")["size"].shift(1)
for col in ["roa", "lev", "size", "growth"]:
    lo, hi = df[col].quantile([0.01, 0.99])
    df[col] = df[col].clip(lo, hi)
```

## Merge Validation

Before merge:

- Check uniqueness of merge keys in each dataset.
- Decide merge type: one-to-one, many-to-one, one-to-many, or many-to-many.
- Avoid many-to-many unless it is explicitly intended and validated.

After merge:

- Report matched, left-only, and right-only counts.
- Check row expansion.
- Check missing values in newly merged variables.
- Spot-check several merged observations.

Stata-style checks:

```stata
duplicates report firm_id year
merge 1:1 firm_id year using controls.dta
tab _merge
```

Python-style checks:

```python
assert not left.duplicated(["firm_id", "year"]).any()
merged = left.merge(right, on=["firm_id", "year"], how="left", indicator=True)
merged["_merge"].value_counts()
```

## Final Panel Validation

Final dataset should include:

- Entity ID and time variable.
- Dependent variable.
- Key independent variable.
- Controls.
- Fixed-effect variables.
- Mechanism and heterogeneity variables when needed.
- Sample flags if useful.

Final checks:

- Unique entity-time rows.
- Reasonable min, max, mean, median, and missing rates.
- Expected sample period.
- Expected number of entities.
- No impossible values such as negative assets or leverage above a nonsensical threshold unless explained.
- Regression variables are numeric and not stored as strings.
