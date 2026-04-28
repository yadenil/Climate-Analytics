# Final Report: African Climate Trend Analysis for COP32

## Executive Summary

This Week 0 challenge delivers a clean, reproducible climate analytics package for Ethiopia, Kenya, Sudan, Tanzania, and Nigeria using NASA POWER daily observations from 2015 through March 2026. The analysis includes country-specific EDA notebooks, a cross-country vulnerability comparison, and a Streamlit dashboard for interactive policy-facing exploration.

Key findings:
- Sudan is the most heat-stressed country in the dataset, with the highest mean daily temperature and the most extreme heat days above 35°C.
- Ethiopia appears to have the lowest average temperature among the five countries, making it comparatively cooler but still vulnerable to seasonal rainfall shocks.
- Nigeria and Tanzania show the largest precipitation variability, indicating high exposure to both heavy rainfall events and dry spells.
- Statistical testing confirms that temperature differences across the five countries are significant, making the comparative ranking robust.

## Task 1: Git & Environment Setup

### What was completed
- Initialized the repository structure with `app/`, `data/`, `notebooks/`, `scripts/`, and `tests/`.
- Created a Python virtual environment and documented setup steps in `README.md`.
- Built a GitHub Actions workflow at `.github/workflows/ci.yml` that installs dependencies on push and pull request.
- Added `.gitignore` rules for local environment files, notebook checkpoints, and CSV data files to ensure raw and cleaned datasets are not committed.

### Notes on branching and CI
- The repository contains feature branches for data cleaning, comparison analysis, and dashboard development, matching the challenge workflow.
- The CI workflow validates the Python environment by installing `requirements.txt` on every push and PR.

## Task 2: Data Profiling, Cleaning & EDA

### Approach
- Loaded each country dataset from `data/<country>.csv`.
- Replaced NASA sentinel values (`-999`) with `np.nan` across all columns before computing statistics.
- Parsed `YEAR` and `DOY` into a proper datetime column with `pd.to_datetime(df['YEAR'] * 1000 + df['DOY'], format='%Y%j')`.
- Added `Month` and `Country` columns for seasonal aggregation and comparison.
- Computed missing values, duplicate counts, summary statistics, and Z-score outliers for the key weather variables.
- Used forward-fill for remaining weather value gaps and kept rows with valid observations where possible.
- Exported cleaned data locally to `data/<country>_clean.csv`.

### Analytical coverage
- Time series analysis of monthly average temperature (`T2M`) and monthly total precipitation (`PRECTOTCORR`).
- Correlation matrices and scatter plots for `T2M`, `RH2M`, `T2M_RANGE`, and wind variables.
- Distribution analysis for precipitation, including skewness and a log-transformed histogram where needed.
- Country-specific interpretation notes in each notebook.

## Task 3: Cross-Country Comparison & Climate Vulnerability Ranking

### Approach
- Loaded cleaned country datasets from `data/*_clean.csv` and concatenated them into a combined DataFrame.
- Produced country-level summary tables comparing mean, median, and standard deviation for `T2M` and `PRECTOTCORR`.
- Visualized temperature trends for all five countries on a shared line chart.
- Built side-by-side boxplots for precipitation variability.
- Counted extreme heat days (`T2M_MAX > 35°C`) and annual dry-day frequency (`PRECTOTCORR < 1 mm`).
- Applied one-way ANOVA to test whether reported temperature differences between countries are statistically significant.

### Findings
- Sudan has the highest average temperature and the greatest count of extreme heat days, making it the top climate vulnerability candidate.
- Nigeria and Tanzania display the greatest precipitation variability, suggesting exposure to both flood and drought risks.
- Ethiopia’s climate profile is cooler and more stable in the dataset, but the country still faces strong seasonal rainfall variation and heat risk during peak months.
- The ANOVA test yields a p-value near zero, indicating the temperature differences across countries are statistically significant.

### Vulnerability ranking (data-driven)
1. Sudan — highest heat stress and extreme temperature frequency.
2. Nigeria — strong rainfall volatility and growing extreme-event exposure.
3. Tanzania — high precipitation variability plus seasonal instability.
4. Kenya — moderate warming with notable dry-season risk.
5. Ethiopia — lowest mean temperature but still vulnerable to rainfall seasonality.

## Time Management and Project Execution Reflection

### Task Prioritization
I prioritized the project by first establishing a stable technical foundation: environment setup, Git workflow, and CI. That allowed the later analytical tasks to proceed without repeated environment fixes. After setup, I split the work into two primary phases: country-level EDA and cross-country synthesis, because the challenge weights both detailed profiling and comparative vulnerability analysis.

### Task Allocation
I allocated time based on task complexity and deliverable value. The first 1–2 days were reserved for setup and notebook scaffolding. The next 2–3 days were dedicated to data cleaning and profiling for the five countries. The last phase was reserved for the cross-country comparison, dashboard refinement, and report writing.

### Strategic Decision-Making
A key strategic decision was to keep the analysis modular. Each country notebook contains the same cleaning and profiling logic, which made it easier to validate results and maintain consistency. Another strategic choice was to document decisions in the report as I worked, rather than leaving documentation for the very end.

### Time Management
I used a sprint-style approach: short, focused sessions for each country and larger blocks for synthesis and dashboard development. This structure helped prevent task switching overhead. By building the `README.md` and `final_report.md` in parallel with the analysis, I ensured that the final submission was complete and cohesive rather than a series of isolated outputs.

### Reflection on Process
Working on this project reinforced that good time management in data science is about process control, not speed alone. The environment setup and CI work were the highest-leverage tasks early on. The analytical work then became easier because the foundation was already in place. The final deliverable is stronger because I balanced execution with reflection, ensuring each step was documented and aligned with the challenge rubric.

## COP32-Framed Recommendations

1. **Warming fastest:** Sudan stands out with the strongest heat signal and should be highlighted as a priority case for extreme heat adaptation funding.
2. **Precipitation instability:** Nigeria and Tanzania both demonstrate highly unstable rainfall patterns, which supports calls for enhanced early warning systems and climate-smart water management.
3. **Extreme heat and drought stress:** Heat-day frequency and long dry spells reveal that the most urgent needs are cooling solutions, resilient agriculture, and loss-and-damage support.
4. **Ethiopia’s regional profile:** Ethiopia remains comparatively cooler, which strengthens its positioning as a data-informed host, but the country should still emphasize adaptation support for seasonal rainfall variability.
5. **COP32 finance priority:** Sudan should be championed for priority climate finance because the dataset shows the most intense combination of heat extremes and vulnerability across the five countries.

## Dashboard and Interactive Visualization

- Built `app/main.py` as a Streamlit dashboard with:
  - country multi-select filter
  - year range slider
  - variable selector for temperature, precipitation, and humidity
  - trend and distribution charts using Plotly
- The dashboard is ready to run locally with `streamlit run app/main.py`.

## How to Use This Repository

1. Activate the Python environment.
2. Install dependencies from `requirements.txt`.
3. Run the country EDA notebooks in `notebooks/`.
4. Open `notebooks/compare_countries.ipynb` for the cross-country vulnerability synthesis.
5. Run the Streamlit app for interactive exploration.

## Notes

- All raw and cleaned CSV files are intentionally kept local and ignored by Git.
- The notebooks contain the detailed analysis steps required by the Week 0 challenge.
- This repository is now aligned with the challenge requirements for structure, CI, and evidence-backed climate analytics.
