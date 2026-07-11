# Task 3 — Cleaning Data (FIFA 21 Player Dataset)

*(Numbered per the internal project plan as Task 2 of 3 selected tasks; corresponds to Level 1 - Task 3 in the program's checklist. Confirm the exact submission file-naming number with your coordinator.)*

## Objective
Take a deliberately messy, real-world scraped dataset and systematically clean it into an analysis-ready dataset, documenting every decision made.

## Dataset
- **File:** `fifa21_raw_data.csv`
- **Rows:** 18,979 FIFA 21 player records
- **Columns:** 77 (player attributes, ratings, physical stats, contract info)
- **Source characteristics:** scraped directly from a player-ratings website, so many fields contain formatting artifacts (currency symbols, unit suffixes, star symbols, stray newlines)

## Tools & Libraries
- Python 3
- pandas
- numpy
- Jupyter Notebook

## What the Notebook Covers
1. Data quality report: nulls, duplicates, dtype issues
2. Missing value handling — `Loan Date End` converted to a proper `On Loan` boolean flag instead of fabricated imputation
3. Duplicate removal (1 row)
4. Standardisation of messy columns:
   - Height (`5'7"`) → `Height_cm`
   - Weight (`159lbs`) → `Weight_kg`
   - Value / Wage / Release Clause (`€67.5M`) → `_EUR` numeric columns
   - Star ratings (`4 ★`, `4★`) → `_num` integer columns
   - `Hits` — stray newlines and `K`-suffix values (e.g. `1.5K`) cleaned to numeric
   - `Team & Contract` split into `Club` and `Contract Status` (handles contracted players, players on loan, and free agents as 3 distinct patterns)
5. Outlier detection (IQR method) on Age, Value, Wage, Overall Rating — reviewed and deliberately retained since they represent real elite players, not errors
6. Final dtype corrections
7. Before/after summary table
8. Cleaned dataset saved to `fifa21_cleaned.csv`

## How to Run
1. Make sure `fifa21_raw_data.csv` is in the same folder as the notebook
2. Install dependencies: `pip install pandas numpy`
3. Open `YourName_Task2.ipynb` in Jupyter Notebook / JupyterLab
4. Run all cells top to bottom

## Key Findings
- Only one column (`Loan Date End`) had missing values, and this was structural (not-on-loan players), not a genuine data gap
- 1 duplicate row found and removed
- Nearly every numeric-seeming column was originally stored as formatted text and required parsing
- A naive regex-based approach to parsing `Team & Contract` and `Hits` initially failed silently on edge cases (non-ASCII club names, loan players, free agents, `K`-suffix hit counts) — verified and fixed by checking split/conversion success against the full dataset rather than just a preview

## Author
Submitted as part of the Data Analytics track — OIBSIP internship program.
