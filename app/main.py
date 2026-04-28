import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="EthioClimate Dashboard", layout="wide", page_icon="🌍")

# Custom UI aesthetics
st.markdown("""
<style>
    .main-header {
        font-family: 'Inter', sans-serif;
        color: #2e7bcf;
        text-align: center;
        margin-bottom: 2rem;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='main-header'>🌍 EthioClimate Analytics Dashboard</h1>", unsafe_allow_html=True)

st.write("Welcome to the interactive exploration of NASA POWER climate data for key African countries. Use the sidebar to slice the data and uncover localized vulnerabilities.")

@st.cache_data
def load_data():
    countries = ['ethiopia', 'kenya', 'sudan', 'tanzania', 'nigeria']
    dfs = []
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    for c in countries:
        try:
            df = pd.read_csv(os.path.join(base_dir, 'data', f'{c}_clean.csv'))
            dfs.append(df)
        except Exception as e:
            st.error(f"Error loading {c}: {e}")
    if len(dfs) > 0:
        return pd.concat(dfs, ignore_index=True)
    return pd.DataFrame()

df = load_data()

if df.empty:
    st.error("Cleaned data not found. Please ensure the EDA data generation scripts have been run first.")
    st.stop()

# Interactive Sidebar
st.sidebar.header("🎯 Filter Controls")

selected_countries = st.sidebar.multiselect(
    "Select Country(ies):",
    options=df['Country'].unique(),
    default=df['Country'].unique()
)

min_year = int(df['YEAR'].min())
max_year = int(df['YEAR'].max())

year_range = st.sidebar.slider(
    "Select Year Range:",
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year)
)

var_options = {
    'Average Temperature (T2M)': 'T2M',
    'Max Temperature (T2M_MAX)': 'T2M_MAX',
    'Total Precipitation (PRECTOTCORR)': 'PRECTOTCORR',
    'Relative Humidity (RH2M)': 'RH2M'
}

selected_var = st.sidebar.selectbox("Select Core Variable for Trend Analysis:", list(var_options.keys()))
mapped_var = var_options[selected_var]

# Filtering Data
filtered_df = df[
    (df['Country'].isin(selected_countries)) &
    (df['YEAR'] >= year_range[0]) & 
    (df['YEAR'] <= year_range[1])
]

if filtered_df.empty:
    st.warning("No data matches selected filters.")
    st.stop()

# Laying out charts using columns
col1, col2 = st.columns(2)

with col1:
    st.subheader(f"📈 {selected_var} Trend")
    trend_df = filtered_df.groupby(['Country', 'YEAR'])[mapped_var].mean().reset_index()
    fig1 = px.line(trend_df, x='YEAR', y=mapped_var, color='Country', template="plotly_white", markers=True)
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.subheader(f"📊 {selected_var} Distribution")
    fig2 = px.box(filtered_df, x='Country', y=mapped_var, color='Country', template="plotly_white")
    st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")
st.subheader("💡 Key Diagnostic Observation")
st.info("These charts visualize how Sudan experiences dramatic extremes in max atmospheric heat and severe depression in precipitation. Comparatively, Ethiopia displays highly stable structural climate characteristics, cementing its foundational capacity for hosting the upcoming COP32 dialogues without immediate meteorological disruption risks.")
