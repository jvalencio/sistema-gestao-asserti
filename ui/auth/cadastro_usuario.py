from time import sleep

import streamlit as st

from database import conectar
from models import Usuario
from repositories import UsuarioRepository

from utils import (
    transformar_em_hash,
    estilizar_inputs,
    validar_usuario,
    navegar_para
)


def cadastrar_usuario():
    st.set_page_config(
        page_title="Cadastro",
        page_icon="📋",
    )

    with st.form("form_cadastro_usuario"):
        st.title("Cadastro")
        st.write("*Preencha os dados abaixo para criar sua conta.*")
        st.divider()

        estilizar_inputs()

        nome = st.text_input(
            "Crie um nome de usuário",
            placeholder="Somente letras | 8 a 12 caracteres",
            max_chars=12
        )

        senha = st.text_input(
            "Crie uma senha",
            placeholder="Mínimo de 8 caracteres",
            type="password"
        )

        confirmar_senha = st.text_input("Confirme sua senha", type="password")

        _, col2, _ = st.columns([1, 2, 1])

        with col2:
            cadastrar = st.form_submit_button("**Cadastrar**", use_container_width=True)

        if cadastrar:
            erro = validar_usuario(nome, senha, confirmar_senha)

            if erro is None:
                conexao = conectar()

                try:
                    usuario_repo = UsuarioRepository(conexao)

                    if usuario_repo.buscar_usuario(nome):
                        st.error("Nome de usuário já cadastrado.")
                    else:
                        senha_hash = transformar_em_hash(senha)

                        novo_usuario = Usuario(nome, senha_hash)
                        usuario_repo.cadastrar_usuario(novo_usuario)

                        st.success(f"Usuário {nome} cadastrado com sucesso!")

                        sleep(2)
                        navegar_para("dashboard")
                finally:
                    conexao.close()
            else:
                st.error(erro)

    _, col2, _ = st.columns([2, 1, 2])

    with col2:
        st.write("")

        if st.button("↩️ Voltar", use_container_width=True):
            navegar_para("entrada")
