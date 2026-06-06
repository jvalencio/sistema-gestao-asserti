from time import sleep

import streamlit as st

from database import conectar
from repositories import UsuarioRepository

from utils import (
    comparar_senhas,
    estilizar_inputs,
    navegar_para
)


def login_usuario():
    st.set_page_config(
        page_title="Login",
        page_icon="🔐",
    )

    with st.form("form_login"):
        st.title("Login")
        st.write("*Acesse sua conta para continuar.*")
        st.divider()

        estilizar_inputs()

        nome = st.text_input("Nome de usuário", max_chars=12)
        senha = st.text_input("Senha", type="password")

        _, col2, _ = st.columns([1, 2, 1])

        with col2:
            login = st.form_submit_button("**Entrar**", use_container_width=True)

        if login:
            if nome and senha:
                conexao = conectar()

                try:
                    usuario_repo = UsuarioRepository(conexao)
                    resultado = usuario_repo.buscar_usuario(nome)

                    if resultado is None:
                        st.error("Usuário não encontrado.")
                    else:
                        senha_banco = resultado[0]

                        if comparar_senhas(senha, senha_banco):
                            st.success("Login realizado com sucesso!")

                            sleep(2)
                            navegar_para("dashboard")
                        else:
                            st.error("Senha incorreta.")
                finally:
                    conexao.close()
            else:
                st.error("Campos obrigatórios não preenchidos.")

    _, col2, _ = st.columns([2, 1, 2])

    with col2:
        st.write("")

        if st.button("↩️ Voltar", use_container_width=True):
            navegar_para("entrada")
