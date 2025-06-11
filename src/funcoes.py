def cond_fuel(df, cond, fuel):
    df_fuel = df[df['fuel'] == fuel]
    df_cond = df_fuel[df_fuel['condition'] == cond]

    return df


def dropar_dados_faltantes(df, coluna, limite_dados_faltantes):
    if df[coluna].isna().mean() > limite_dados_faltantes:
        df = df.dropna(subset=[coluna])

    return df


def outlier(df, coluna):
    media = df[coluna].mean()  # calculo da média
    dp = df[coluna].std()  # desvio padrão
    ls = media + 2*dp  # limite superior
    li = media - 2*dp  # limite inferior
    df = df[(df[coluna] > li) & (df[coluna] < ls)]

    return df
