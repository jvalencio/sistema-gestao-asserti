import streamlit as st


CHAVE_FORMULARIO_EMPRESA = "formulario_empresa_id"


def obter_id_formulario_empresa():
    return st.session_state.setdefault(CHAVE_FORMULARIO_EMPRESA, 0)


def limpar_formulario_empresa():
    st.session_state[CHAVE_FORMULARIO_EMPRESA] = obter_id_formulario_empresa() + 1
