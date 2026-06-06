from time import sleep

import streamlit as st

from .formulario_empresa import (
    campos_identificacao_empresa,
    campos_localizacao_empresa,
    campos_perfil_empresa
)

from database import conectar
from models import Empresa
from repositories import EmpresaRepository
from utils import validar_empresa


def formulario_editar_empresa(empresa_selecionada, df_original):
    with st.form(f"form_editar_empresa"):
        dados_empresa_editados = {
            **campos_identificacao_empresa(dados_empresa=empresa_selecionada),
            **campos_localizacao_empresa(dados_empresa=empresa_selecionada),
            **campos_perfil_empresa(dados_empresa=empresa_selecionada)
        }

        _, col2, _ = st.columns([1, 2, 1])

        with col2:
            editar = st.form_submit_button("**Salvar alterações**", use_container_width=True)

    return dados_empresa_editados, editar


@st.dialog("Editar Empresa")
def editar_empresa(empresa_selecionada, df_original):
    indice = empresa_selecionada.index[0]
    dados_empresa = df_original.loc[indice].to_dict()

    dados_empresa_editados, editar = formulario_editar_empresa(
        dados_empresa, df_original
    )

    if editar:
        erro = validar_empresa(dados_empresa_editados)

        if erro is None:
            conexao = conectar()

            try:
                empresa_repo = EmpresaRepository(conexao)

                razao_social_original = dados_empresa["razao_social"]
                cnpj_original = dados_empresa["cnpj"]

                nova_razao_social = dados_empresa_editados["razao_social"]
                novo_cnpj = dados_empresa_editados["cnpj"]

                alterou_empresa = (
                    razao_social_original != nova_razao_social
                    or cnpj_original != novo_cnpj
                )

                if alterou_empresa:
                    if empresa_repo.verificar_existencia(nova_razao_social, novo_cnpj):
                        st.error("Empresa já cadastrada!")
                        return
                else:
                    id_empresa = dados_empresa["id"]

                    empresa_editada = Empresa(**dados_empresa_editados)
                    empresa_repo.editar_empresa(id_empresa, empresa_editada)

                    st.success("Alterações realizadas com sucesso!")

                    sleep(2)
                    st.rerun()
            finally:
                conexao.close()
        else:
            st.error(erro)
