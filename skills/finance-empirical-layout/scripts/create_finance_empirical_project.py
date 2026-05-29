#!/usr/bin/env python
"""Create a finance empirical research project directory layout."""

from __future__ import annotations

import argparse
import re
from datetime import date
from pathlib import Path


CORE_DIRS = [
    "config",
    "code/00_setup",
    "code/01_download",
    "code/02_clean",
    "code/03_construct_sample",
    "code/04_construct_variables",
    "code/05_descriptive_stats",
    "code/06_baseline_regression",
    "code/07_robustness",
    "code/08_heterogeneity",
    "code/09_mechanism",
    "code/utils",
    "data/raw",
    "data/external",
    "data/interim",
    "data/panel",
    "data/final",
    "outputs/tables/descriptive",
    "outputs/tables/baseline",
    "outputs/tables/robustness",
    "outputs/tables/heterogeneity",
    "outputs/tables/mechanism",
    "outputs/figures/descriptive",
    "outputs/figures/regression",
    "outputs/regressions/logs",
    "outputs/regressions/estimates",
    "outputs/logs",
    "reports",
]

OPTIONAL_DIRS = [
    "code/10_figures",
    "code/11_tables",
    "outputs/figures/sample",
    "outputs/regressions/diagnostics",
    "docs",
    "notebooks",
    "tests",
]


def slugify(name: str) -> str:
    slug = re.sub(r"[^A-Za-z0-9._-]+", "-", name.strip()).strip("-._")
    slug = re.sub(r"-{2,}", "-", slug).lower()
    if not slug:
        raise ValueError("Project name cannot be empty after slug normalization.")
    return slug


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create a standard finance empirical research project layout."
    )
    parser.add_argument("project_name", help="Project folder name, e.g. green-finance-did.")
    parser.add_argument(
        "--root",
        default=".",
        help="Parent directory where the project folder will be created. Default: current directory.",
    )
    parser.add_argument(
        "--full",
        action="store_true",
        help="Create optional docs, notebooks, tests, figure, and table-code folders.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Allow creating files inside an existing project folder.",
    )
    parser.add_argument(
        "--title",
        default="",
        help="Human-readable research title written into README.md.",
    )
    parser.add_argument(
        "--data-sources",
        default="",
        help="Comma-separated data sources, e.g. CSMAR,Wind,WRDS.",
    )
    parser.add_argument(
        "--sample-period",
        default="",
        help="Sample period written into README.md, e.g. 2007-2024.",
    )
    return parser.parse_args()


def write_if_missing(path: Path, content: str) -> None:
    if not path.exists():
        path.write_text(content, encoding="utf-8")


def create_readme(project_dir: Path, project_name: str, title: str, data_sources: str, sample_period: str) -> None:
    display_title = title or project_name.replace("-", " ").title()
    source_text = data_sources or "TBD"
    period_text = sample_period or "TBD"
    content = f"""# {display_title}

## Research Goal

TBD.

## Data Sources

- {source_text}

## Sample

- Unit of observation: TBD
- Sample period: {period_text}
- Key sample filters: see `config/sample_filters.yaml`

## Pipeline

1. `code/01_download/`
2. `code/02_clean/`
3. `code/03_construct_sample/`
4. `code/04_construct_variables/`
5. `code/05_descriptive_stats/`
6. `code/06_baseline_regression/`
7. `code/07_robustness/`
8. `code/08_heterogeneity/`
9. `code/09_mechanism/`

## Key Outputs

- Tables: `outputs/tables/`
- Figures: `outputs/figures/`
- Regression logs and estimates: `outputs/regressions/`

Created: {date.today().isoformat()}
"""
    write_if_missing(project_dir / "README.md", content)


def create_config(project_dir: Path) -> None:
    paths_yaml = """project_root: .
data:
  raw: data/raw
  external: data/external
  interim: data/interim
  panel: data/panel
  final: data/final
outputs:
  tables: outputs/tables
  figures: outputs/figures
  regressions: outputs/regressions
  logs: outputs/logs
"""
    filters_yaml = """sample_period:
  start: TBD
  end: TBD
unit_of_observation: TBD
filters:
  - name: TBD
    rule: TBD
winsorization:
  enabled: true
  lower: 0.01
  upper: 0.99
fixed_effects:
  - year
  - industry
clustered_standard_errors: TBD
"""
    write_if_missing(project_dir / "config" / "paths.yaml", paths_yaml)
    write_if_missing(project_dir / "config" / "sample_filters.yaml", filters_yaml)


def main() -> None:
    args = parse_args()
    project_name = slugify(args.project_name)
    root = Path(args.root).expanduser().resolve()
    project_dir = root / project_name

    if project_dir.exists() and not args.force:
        raise SystemExit(
            f"Project directory already exists: {project_dir}\n"
            "Use --force to add missing standard files and folders."
        )

    dirs = CORE_DIRS + (OPTIONAL_DIRS if args.full else [])
    for rel_path in dirs:
        (project_dir / rel_path).mkdir(parents=True, exist_ok=True)

    create_readme(project_dir, project_name, args.title, args.data_sources, args.sample_period)
    create_config(project_dir)

    print(f"Created finance empirical project layout: {project_dir}")
    print("Key folders:")
    for rel_path in dirs:
        print(f"  {rel_path}")


if __name__ == "__main__":
    main()
