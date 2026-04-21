from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Ecological Monitoring Dashboard", layout="wide")

DATA_PATH = (
    Path(__file__).resolve().parents[1]
    / "data"
    / "part-00000-78dc6448-dc38-4201-98e8-9d45eada4ea3-c000.snappy.parquet"
)

@st.cache_data
def load_data():
    return pd.read_parquet(DATA_PATH)

st.title("Spatio-Temporal Ecological Monitoring")
st.caption("Average AQI trends by city and year")

df = load_data()

cities = sorted(df["City"].dropna().unique())
selected_cities = st.multiselect(
    "Select cities",
    cities,
    default=cities[: min(5, len(cities))],
)

if not selected_cities:
    st.info("Select at least one city.")
    st.stop()

filtered_df = df[df["City"].isin(selected_cities)].sort_values(["City", "Year"])

fig = px.line(
    filtered_df,
    x="Year",
    y="Avg_AQI",
    color="City",
    markers=True,
    title="Average AQI Over Time",
)

st.plotly_chart(fig, use_container_width=True)
st.dataframe(filtered_df, use_container_width=True, hide_index=True)
