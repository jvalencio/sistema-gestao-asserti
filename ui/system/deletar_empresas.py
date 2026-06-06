from time import sleep

import streamlit as st

from database import conectar
from repositories import EmpresaRepository


@st.dialog("Deletar Empresa")
def deletar_empresas(empresas_selecionadas):
    qtd_empresas = len(empresas_selecionadas)
    texto = "empresa" if qtd_empresas == 1 else "empresas"

    st.write(f"Deseja realmente deletar {qtd_empresas} {texto} permanentemente?")

    _, col2, _ = st.columns([1, 2, 1])

    with col2:
        confirmar = st.button("**✅ Confirmar**", use_container_width=True)

    if confirmar:
        try:
            conexao = conectar()

            empresa_repo = EmpresaRepository(conexao)
            empresa_repo.deletar_empresas(empresas_selecionadas)

            st.success(f"{qtd_empresas} {texto} foram deletadas com sucesso!")

            sleep(2)
            st.rerun()
        finally:
            conexao.close()
