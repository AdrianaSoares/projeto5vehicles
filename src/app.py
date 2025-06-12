# importando bibliotecas

import pandas as pd
from matplotlib import pyplot as plt
from pathlib import Path
import streamlit as st
import plotly_express as px
from src import funcoes

df = pd.read_csv(Path("data/vehicles.csv"))
df = funcoes.dropar_dados_faltantes(df, 'price', 0.1)
df = funcoes.cond_fuel(df, 'good', 'gas')
df = funcoes.outlier(df, 'price')


st.title("Análise de Vendas de Automóveis")

fig = px.histogram(df, x='price', color='condition')

st.plotly_chart(fig)
