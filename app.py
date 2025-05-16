import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# Load your cleaned dataset with parsed dates
df = pd.read_csv("owid-covid-data.csv", parse_dates=['date'])

# Filter for East African countries
countries = ['Kenya', 'Tanzania', 'Uganda', 'Rwanda', 'Burundi']
df_EA = df[df['location'].isin(countries)]

st.title("COVID-19 Dashboard for East Africa")

# Country selector
country = st.selectbox("Select a country", countries)
country_df = df_EA[df_EA['location'] == country]

# Line chart for total cases
st.subheader(f"Total COVID-19 Cases Over Time in {country}")
fig = px.line(
    country_df,
    x='date',
    y='total_cases',
    title=f"Total Cases in {country}",
    labels={"total_cases": "Total Cases", "date": "Date"}
)
st.plotly_chart(fig)

# Choropleth map for latest date
st.subheader("Choropleth Map for Total Cases in East Africa")

# Ensure latest_date is a datetime object
latest_date = pd.to_datetime(df_EA['date'].max())
latest_data = df_EA[df_EA['date'] == latest_date]
choropleth_df = latest_data[['iso_code', 'location', 'total_cases']].dropna()

map_fig = px.choropleth(
    choropleth_df,
    locations='iso_code',
    color='total_cases',
    hover_name='location',
    color_continuous_scale='Reds',
    title=f'Total Cases on {latest_date.date()}'
)
st.plotly_chart(map_fig)
