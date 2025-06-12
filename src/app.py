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

# Criando um histograma para o conjunto de dados de anúncios de vendas de carros

car_data = pd.read_csv(Path("data/vehicles.csv"))  # lendo os dados
hist_button = st.button('Criar histograma')  # criar um botão

if hist_button:  # se o botão for clicado
    # escrever uma mensagem
    st.write(
        'Criando um histograma para o conjunto de dados de anúncios de vendas de carros')

    # criar um histograma
    fig = px.histogram(car_data, x="odometer")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)


# criar uma caixa de seleção
build_histogram = st.checkbox('Criar um histograma')

if build_histogram:  # se a caixa de seleção for selecionada
    st.write('Criando um histograma para a coluna odometer')


ver_data = pd.read_csv(Path("data/vehicles.csv"))  # lendo os dados
chart_data = ver_data[ver_data['fuel'] == 'good']

st.bar_chart(chart_data)
