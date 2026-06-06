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

from utils import (
    limpar_formulario_empresa,
    obter_id_formulario_empresa,
    validar_empresa
)


def formulario_cadastro_empresa(formulario_id):
    with st.form(f"form_cadastro_empresa_{formulario_id}"):
        dados_empresa = {
            **campos_identificacao_empresa(formulario_id=formulario_id),
            **campos_localizacao_empresa(formulario_id=formulario_id),
            **campos_perfil_empresa(formulario_id=formulario_id)
        }

        _, col2, _ = st.columns([1, 2, 1])

        with col2:
            cadastrar = st.form_submit_button("**Cadastrar**", use_container_width=True)

    return dados_empresa, cadastrar


@st.dialog("Cadastrar Empresa")
def cadastrar_empresa():
    area_formulario = st.empty()

    with area_formulario.container():
        dados_empresa, cadastrar = formulario_cadastro_empresa(
            obter_id_formulario_empresa()
        )

    if cadastrar:
        erro = validar_empresa(dados_empresa)

        if erro is None:
            conexao = conectar()

            try:
                empresa_repo = EmpresaRepository(conexao)

                razao_social = dados_empresa["razao_social"]
                cnpj = dados_empresa["cnpj"]

                if empresa_repo.verificar_existencia(razao_social, cnpj):
                    st.error("Empresa já cadastrada!")
                else:
                    nova_empresa = Empresa(**dados_empresa)
                    empresa_repo.cadastrar_empresa(nova_empresa)

                    st.success("Empresa cadastrada com sucesso!")

                    sleep(2)
                    limpar_formulario_empresa()
                    area_formulario.empty()

                    with area_formulario.container():
                        formulario_cadastro_empresa(obter_id_formulario_empresa())
            finally:
                conexao.close()
        else:
            st.error(erro)
