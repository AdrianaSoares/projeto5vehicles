# função para filtragem com base em um DF, condição e combustivel

def cond_fuel(df, cond, fuel):
    df_fuel = df[df['fuel'] == fuel]
    df_cond = df_fuel[df_fuel['condition'] == cond]

    return df


# função para remoção de colunas com dados faltantes escolhendo um limite

def dropar_dados_faltantes(df, coluna, limite_dados_faltantes):
    if df[coluna].isna().mean() > limite_dados_faltantes:
        df = df.dropna(subset=[coluna])

    return df


# função para limpeza outlier

def outlier(df, coluna):
    media = df[coluna].mean()  # calculo da média
    dp = df[coluna].std()  # desvio padrão
    ls = media + 2*dp  # limite superior
    li = media - 2*dp  # limite inferior
    df = df[(df[coluna] > li) & (df[coluna] < ls)]

    return df
