import pandas as pd
from pathlib import Path
import streamlit as st
import plotly_express as px

df = pd.read_csv(Path("data/vehicles.csv"))

st.title("Análise de Vendas de Automóveis")

fig = px.histogram(df, x='price', color='condition')

st.plotly_chart(fig)
