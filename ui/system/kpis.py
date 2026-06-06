import streamlit as st

from utils import (
    formatar_moeda,
    total_empresas,
    faturamento_anual_total,
    mediana_faturamento,
    maior_faturamento_ano,
    estado_lider_faturamento,
    setor_lider_faturamento,
    setor_com_mais_empresas,
    percentual_esg_ods
)


def kpis(df):
    with st.container(border=True):
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                "**Total de empresas**",
                total_empresas(df),
                border=True
            )

            st.metric(
                "**Estado líder de faturamento**",
                estado_lider_faturamento(df),
                border=True
            )

        with col2:
            st.metric(
                "**Faturamento anual total**",
                formatar_moeda(faturamento_anual_total(df)),
                border=True
            )

            st.metric(
                "**Setor líder de faturamento**",
                setor_lider_faturamento(df),
                border=True
            )

        with col3:
            st.metric(
                "**Mediana de faturamento**",
                formatar_moeda(mediana_faturamento(df)),
                border=True
            )

            st.metric(
                "**Setor com mais empresas**",
                setor_com_mais_empresas(df),
                border=True
            )

        with col4:
            st.metric(
                "**Maior faturamento no ano**",
                formatar_moeda(maior_faturamento_ano(df)),
                border=True
            )

            st.metric(
                "**% Empresas com práticas ESG/ODS**",
                f"{percentual_esg_ods(df)}%",
                border=True
            )
