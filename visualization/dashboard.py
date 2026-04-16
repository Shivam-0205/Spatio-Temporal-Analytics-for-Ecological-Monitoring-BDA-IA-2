import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("city_day.csv")

city = st.selectbox("Select City", df["City"].unique())

city_df = df[df["City"] == city]

fig = px.line(city_df, x="Date", y="AQI")

st.plotly_chart(fig)
