import streamlit as st
import pandas as pd

from utils import (
    converter_booleano,
    formatar_cnpj,
    formatar_moeda,
    df_vazio
)


def listar_empresas(df, mensagem_vazia="Nenhuma empresa cadastrada."):
    df_exibicao = df.copy()

    if not df_vazio(df):
        df_exibicao.insert(0, "selecionar", False)

        df_exibicao["cnpj"] = df_exibicao["cnpj"].apply(formatar_cnpj)
        df_exibicao["faturamento_anual"] = df_exibicao["faturamento_anual"].apply(formatar_moeda)
        df_exibicao["exporta"] = converter_booleano(df_exibicao["exporta"])
        df_exibicao["praticas_esg_ods"] = converter_booleano(df_exibicao["praticas_esg_ods"])

        mensagem = st.empty()

        df_editado = st.data_editor(
            df_exibicao,
            hide_index=True,
            use_container_width=True,
        )

        empresas_selecionadas = df_editado[df_editado["selecionar"]]

        return empresas_selecionadas, mensagem
    else:
        mensagem = st.empty()
        mensagem.info(mensagem_vazia)

        return pd.DataFrame(), mensagem
