import streamlit as st

from utils import navegar_para


def entrada():
    st.set_page_config(
        page_title="Portal de Entrada",
        page_icon="🏠",
        layout="centered"
    )

    st.title("Sistema de Gestão Empresarial")
    st.write("*Uma plataforma simples para gerenciar empresas e informações com eficiência.*")
    st.write("")

    with st.container(border=True):
        col1, col2, col3 = st.columns(3)

        with col1:
            st.info("🏢 Empresas")
            st.caption("Cadastre e gerencie empresas.")
        with col2:
            st.info("📊 Indicadores")
            st.caption("Acompanhe métricas relevantes.")
        with col3:
            st.info("👜 Gestão")
            st.caption("Centralize informações.")

    st.divider()
    st.write("**Selecione uma opção para prosseguir:**")
    st.write("")

    _, col2, _ = st.columns([1, 2, 1])

    with col2:
        if st.button("🔐 Acessar conta", use_container_width=True):
            navegar_para("login")

        if st.button("📋 Criar novo cadastro", use_container_width=True):
            navegar_para("cadastro")
