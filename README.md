# EthioClimate Analytics

## Project Overview

This repository contains the Week 0 challenge work for African climate trend analysis using NASA POWER data for Ethiopia, Kenya, Sudan, Tanzania, and Nigeria. The goal is to produce data-driven insights for COP32 framing, including country-level exploratory analysis, cross-country vulnerability comparisons, and an interactive Streamlit dashboard.

## Setup Instructions

1. Clone the repository.
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

## Repository Structure

- `app/` — Streamlit dashboard application code.
- `data/` — local raw and cleaned CSV files for analysis. **These files are ignored by Git and should not be committed.**
- `notebooks/` — EDA notebooks for each country and the cross-country comparison.
- `scripts/` — supporting scripts for generating notebooks and data analysis.
- `.github/workflows/ci.yml` — GitHub Actions workflow for dependency installation on push and PR.
- `requirements.txt` — Python package dependencies.
- `final_report.md` — narrative summary of the Week 0 deliverable and COP32 recommendations.

## Data Notes

- `data/<country>.csv` contains the raw NASA POWER dataset.
- `data/<country>_clean.csv` contains cleaned data after replacing `-999` values, parsing date fields, and applying quality checks.
- Both raw and cleaned CSV files are intentionally ignored in Git to comply with data handling guidance.

## Running the Notebooks

Open the notebooks in Jupyter Lab or Jupyter Notebook:
```bash
jupyter notebook
```
Then run the notebooks in the following order for reproducible analysis:

1. `notebooks/ethiopia_eda.ipynb`
2. `notebooks/kenya_eda.ipynb`
3. `notebooks/sudan_eda.ipynb`
4. `notebooks/tanzania_eda.ipynb`
5. `notebooks/nigeria_eda.ipynb`
6. `notebooks/compare_countries.ipynb`

## Streamlit Dashboard

Launch locally:
```bash
streamlit run app/main.py
```

Use the sidebar to select countries, filter by year range, and choose core climate variables for trend and distribution charts.

## CI / GitHub Actions

The GitHub Actions workflow is configured in `.github/workflows/ci.yml` to install dependencies on every push and pull request. This ensures the environment can be reprovisioned and the project dependencies are validated.
