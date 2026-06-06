import streamlit as st

from services import gerar_relatorio_pdf
from utils import estilizar_inputs


def barra_acoes():
    with st.container(border=True):
        col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 4, 1])

        estilizar_inputs()

        with col1:
            cadastrar = st.button("➕ CADASTRAR", use_container_width=True)
        
        with col2:
            deletar = st.button("❌ DELETAR", use_container_width=True)

        with col3:
            editar = st.button("📝 EDITAR", use_container_width=True)

        with col4:
            buscar = st.text_input(
                "Buscar",
                placeholder="🔎 Busque por Razão Social, Nome Fantasia ou CNPJ",
                label_visibility="collapsed",
                key="busca_empresas",
            )

        with col5:
            sair = st.button("🚪 SAIR", use_container_width=True)

    return {
        "cadastrar": cadastrar,
        "deletar": deletar,
        "editar": editar,
        "buscar": buscar,
        "sair": sair
    }


def botao_relatorio(df):
    _, _, _, _, col5 = st.columns([1, 1, 1, 4, 1])

    with col5:
        pdf = gerar_relatorio_pdf(df)

        st.download_button(
            label="**📄 Baixar relatório PDF**",
            data=pdf,
            file_name="relatorio_empresas.pdf",
            mime="application/pdf",
            use_container_width=True
        )
