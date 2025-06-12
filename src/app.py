import pandas as pd
from pathlib import Path
import streamlit as st

df = pd.read_csv(Path("../data/vehicles.csv"))

st.title("Análise de Vendas de Automóveis")
