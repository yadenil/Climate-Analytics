import pandas as pd
import numpy as np
from scipy.stats import zscore

print("=== Ethiopia Data Profile ===")
df = pd.read_csv('../data/ethiopia.csv')

print(f"Initial shape: {df.shape}")

# Missing-Value Report (-999 replacement)
initial_neg_999 = (df == -999).sum().sum()
print(f"Count of -999 values: {initial_neg_999}")
df.replace(-999, np.nan, inplace=True)

# Duplicates
dup_count = df.duplicated().sum()
print(f"Duplicate rows: {dup_count}")
df.drop_duplicates(inplace=True)

# Missing values info
missing_pct = (df.isna().sum() / len(df)) * 100
print("\nMissing Values %:")
print(missing_pct[missing_pct > 0])

# Basic stats
print("\nSummary Statistics:")
print(df.describe().to_string())

# Outliers using Z-scores
cols_for_z = ['T2M', 'T2M_MAX', 'T2M_MIN', 'PRECTOTCORR', 'RH2M', 'WS2M', 'WS2M_MAX']
outlier_counts = {}
for col in cols_for_z:
    if col in df.columns:
        valid_mask = df[col].notna()
        z_scores = np.abs(zscore(df.loc[valid_mask, col]))
        outliers = (z_scores > 3).sum()
        outlier_counts[col] = outliers
print("\nOutlier Counts (|Z| > 3):")
print(outlier_counts)

# Correlations
print("\nTop Correlations:")
corr_matrix = df.select_dtypes(include=[np.number]).corr().abs()
upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))
top_corr = upper.unstack().sort_values(ascending=False).dropna().head(5)
print(top_corr)

# Basic cleanup for export
# Convert YEAR, DOY to Date
df['Date'] = pd.to_datetime(df['YEAR'] * 1000 + df['DOY'], format='%Y%j')
df['Month'] = df['Date'].dt.month
df['Country'] = 'Ethiopia'

# Forward fill weather variables
df.ffill(inplace=True)
df.to_csv('../data/ethiopia_clean.csv', index=False)
print("\nCleaned shape:", df.shape)
