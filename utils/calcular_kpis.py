from .validacao import df_vazio


def total_empresas(df):
    return len(df)


def faturamento_anual_total(df):
    return df["faturamento_anual"].sum()


def mediana_faturamento(df):
    if df_vazio(df):
        return 0
    else:
        return df["faturamento_anual"].median()


def maior_faturamento_ano(df):
    if df_vazio(df):
        return 0
    else:
        return df["faturamento_anual"].max()


def estado_lider_faturamento(df):
    if df_vazio(df):
        return "Nenhum"
    else:
        return df.groupby("estado")["faturamento_anual"].sum().idxmax()


def setor_lider_faturamento(df):
    if df_vazio(df):
        return "Nenhum"
    else:
        return df.groupby("setor_ti")["faturamento_anual"].sum().idxmax()


def setor_com_mais_empresas(df):
    if df_vazio(df):
        return "Nenhum"
    else:
        return df["setor_ti"].value_counts().idxmax()


def percentual_esg_ods(df):
    if df_vazio(df):
        return 0
    else:
        total_empresas = len(df)
        total_esg_ods = (df["praticas_esg_ods"] == 1).sum()

        return round((total_esg_ods / total_empresas) * 100)
