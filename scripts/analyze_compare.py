import pandas as pd
import numpy as np
import scipy.stats as stats

countries = ['ethiopia', 'kenya', 'sudan', 'tanzania', 'nigeria']
dfs = []
for c in countries:
    df = pd.read_csv(f'../data/{c}_clean.csv')
    dfs.append(df)

all_df = pd.concat(dfs, ignore_index=True)

# Temperature
print("=== Temperature Options ===")
t2m_summary = all_df.groupby('Country')['T2M'].agg(['mean', 'median', 'std'])
print(t2m_summary)

# Precipitation
print("\n=== Precipitation ===")
prec_summary = all_df.groupby('Country')['PRECTOTCORR'].agg(['mean', 'median', 'std'])
print(prec_summary)

# Extreme Events
print("\n=== Extreme Heat (Days T2M_MAX > 35) ===")
heat_days = all_df[all_df['T2M_MAX'] > 35].groupby(['Country', 'YEAR']).size().groupby('Country').mean()
print(heat_days)

print("\n=== Extreme Dry (Consecutive Dry Days, approx by ratio) ===")
# Exact consecutive dry days calculation
dry_streaks_mean = {}
for name, group in all_df.groupby('Country'):
    group = group.sort_values('Date')
    is_dry = group['PRECTOTCORR'] < 1
    # Identify periods of consecutive True
    streaks = is_dry.groupby((~is_dry).cumsum())
    max_streaks_per_year = streaks.sum().to_frame(name='DryLength')
    max_streaks_per_year['YEAR'] = group.loc[streaks.apply(lambda x: x.index[0])]['YEAR'].values  # Just rough
    mean_longest_streak = 0
    
    # Actually just count total dry days per year and longest sequence per year
    yearly_streaks = []
    for year, y_group in group.groupby('YEAR'):
        y_is_dry = y_group['PRECTOTCORR'] < 1
        curr_streak = 0
        max_streak = 0
        for dry in y_is_dry:
            if dry:
                curr_streak += 1
                max_streak = max(max_streak, curr_streak)
            else:
                curr_streak = 0
        yearly_streaks.append(max_streak)
    dry_streaks_mean[name] = np.mean(yearly_streaks)
print(pd.Series(dry_streaks_mean))

# ANOVA
arrays = [group['T2M'].values for name, group in all_df.groupby('Country')]
f_val, p_val = stats.f_oneway(*arrays)
print(f"\nANOVA T2M p-value: {p_val}")
