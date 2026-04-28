# Interim Report: Week 0 Climate Challenge

## Task 1: Git & Environment Setup

### Summary
- Initialized a clean repository structure for the climate analysis project.
- Created a `.gitignore` file to exclude local environment files, notebook checkpoints, and data files from version control.
- Set up `requirements.txt` with the project dependencies required for data analysis, visualization, notebook execution, and dashboard development.
- Added a GitHub Actions workflow at `.github/workflows/ci.yml` to install dependencies on every push and pull request.
- Documented the workflow and setup instructions clearly in `README.md`.

### Deliverables completed
- `.gitignore`
- `requirements.txt`
- `.github/workflows/ci.yml`
- `README.md`
- `final_report.md` (ongoing synthesis and documentation)

### Key points
- The repository structure now supports repeatable analysis and clean collaboration.
- The CI pipeline confirms the Python environment can be installed reliably on GitHub runners.
- Data handling policy was clarified by ignoring all local `data/` CSV files.

## Task 2: Data Profiling and Cleaning Approach

### Overall approach
- Prepared the climate dataset for analysis by using a consistent, repeatable cleaning pipeline.
- Conducted country-level exploratory data analysis for Ethiopia, Kenya, Sudan, Tanzania, and Nigeria.
- Focused on handling NASA POWER-specific data issues and ensuring each dataset is ready for cross-country comparison.

### Data cleaning steps
1. Loaded each country dataset from `data/<country>.csv`.
2. Replaced NASA sentinel values (`-999`) with `np.nan` across all columns before any summary statistics.
3. Converted `YEAR` and `DOY` into a proper datetime column using `pd.to_datetime(df['YEAR'] * 1000 + df['DOY'], format='%Y%j')`.
4. Added a `Month` column for seasonal analysis and a `Country` column for combined comparisons.
5. Checked for duplicates with `df.duplicated().sum()` and dropped any found duplicates.
6. Assessed missing values using `df.isna().sum()` and calculated percentage of missing values per column.
7. Detected outliers in key climate variables (`T2M`, `T2M_MAX`, `T2M_MIN`, `PRECTOTCORR`, `RH2M`, `WS2M`, `WS2M_MAX`) using Z-scores.
8. Applied forward-fill for remaining weather values and preserved rows unless more than 30% of values were missing.
9. Prepared cleaned datasets locally as `data/<country>_clean.csv` for further analysis.

### Analytical focus
- Created summary statistics and documented interpretations for each country dataset.
- Identified and noted any columns with more than 5% missing values.
- Flagged outliers and decided whether to retain or clean them based on climate signal and data quality.
- Ensured that each country notebook included time series analysis, correlation exploration, and distribution assessment.

### Current status
- Project setup and documentation are complete and staged.
- The country-level notebooks exist and are structured for consistent EDA and cleaning.
- The cleaning and profiling approach is ready for implementation across all datasets.
