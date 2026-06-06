from time import sleep

import streamlit as st

from .acoes_empresa import barra_acoes, botao_relatorio
from .cadastro_empresa import cadastrar_empresa
from .deletar_empresas import deletar_empresas
from .editar_empresa import editar_empresa
from .kpis import kpis
from .listar_empresas import listar_empresas
from database import conectar
from repositories import EmpresaRepository

from utils import (
    navegar_para,
    verificar_selecionadas,
    df_vazio
)


def dashboard():
    st.set_page_config(
        page_title="Dashboard",
        page_icon="📊",
        layout="wide",
    )

    st.title("Dashboard de Empresas")
    st.write("*Visualize indicadores e informações estratégicas para acompanhar o desempenho e a organização empresarial.*")

    conexao = conectar()

    try:
        empresas_repo = EmpresaRepository(conexao)
        df_empresas = empresas_repo.listar_empresas()

        kpis(df_empresas)

        st.write("")

        acoes = barra_acoes()

        termo_busca = acoes["buscar"].strip()

        if termo_busca:
            df_exibicao = empresas_repo.buscar_empresa(termo_busca)
            mensagem_vazia = "Nenhum resultado encontrado."
        else:
            df_exibicao = df_empresas
            mensagem_vazia = "Nenhuma empresa cadastrada."
    finally:
        conexao.close()

    empresas_selecionadas, mensagem = listar_empresas(df_exibicao, mensagem_vazia)

    if termo_busca and not df_vazio(df_exibicao):
        qtd_empresas = len(df_exibicao)
        texto_empresa = "empresa encontrada" if qtd_empresas == 1 else "empresas encontradas"
        mensagem.info(f"{qtd_empresas} {texto_empresa}.")

    if acoes["cadastrar"]:
        cadastrar_empresa()

    if acoes["deletar"]:
        if verificar_selecionadas(empresas_selecionadas, mensagem, "deletar"):
            deletar_empresas(empresas_selecionadas)

    if acoes["editar"]:
        if verificar_selecionadas(empresas_selecionadas, mensagem, "editar"):
            editar_empresa(empresas_selecionadas, df_empresas)

    if acoes["sair"]:
        sleep(2)
        navegar_para("entrada")

    botao_relatorio(df_empresas)
