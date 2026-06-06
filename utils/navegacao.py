import streamlit as st


PAGINA_INICIAL = "entrada"
PAGINAS_VALIDAS = ("entrada", "login", "cadastro", "dashboard")


def sincronizar_url(pagina):
    for parametro in list(st.query_params.keys()):
        if parametro != "page":
            del st.query_params[parametro]

    st.query_params["page"] = pagina


def obter_pagina_atual():
    pagina = st.query_params.get("page", PAGINA_INICIAL)

    if pagina not in PAGINAS_VALIDAS:
        pagina = PAGINA_INICIAL

    st.session_state.pagina = pagina
    sincronizar_url(pagina)

    return pagina


def navegar_para(pagina):
    if pagina not in PAGINAS_VALIDAS:
        pagina = PAGINA_INICIAL

    st.session_state.pagina = pagina
    sincronizar_url(pagina)
    st.rerun()
