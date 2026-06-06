import streamlit as st

from utils import ESTADOS, SETORES


def criar_chave_formulario(campo, formulario_id=None):
    if formulario_id is None:
        return campo

    return f"{campo}_{formulario_id}"


def campos_identificacao_empresa(formulario_id=None, dados_empresa=None):
    if dados_empresa is None:
        dados_empresa = {}

    razao_social = st.text_input(
        "Razão Social",
        value=dados_empresa.get("razao_social", ""),
        placeholder="Máximo de 80 caracteres",
        max_chars=80,
        key=criar_chave_formulario("razao_social", formulario_id)
    )

    nome_fantasia = st.text_input(
        "Nome Fantasia",
        value=dados_empresa.get("nome_fantasia", ""),
        placeholder="Máximo de 60 caracteres",
        max_chars=60,
        key=criar_chave_formulario("nome_fantasia", formulario_id)
    )

    col1, col2 = st.columns([1, 2])

    with col1:
        cnpj = st.text_input(
            "CNPJ",
            value=dados_empresa.get("cnpj", ""),
            placeholder="Som. números",
            max_chars=14,
            key=criar_chave_formulario("cnpj", formulario_id)
        )

    with col2:
        setor_empresa = dados_empresa.get("setor_ti")

        indice_setor = (
            SETORES.index(setor_empresa)
            if setor_empresa in SETORES
            else None
        )

        setor_ti = st.selectbox(
            "Setor de TI",
            SETORES,
            index=indice_setor,
            placeholder="Selecione",
            key=criar_chave_formulario("setor_ti", formulario_id)
        )

    return {
        "razao_social": razao_social,
        "nome_fantasia": nome_fantasia,
        "cnpj": cnpj,
        "setor_ti": setor_ti
    }


def campos_localizacao_empresa(formulario_id=None, dados_empresa=None):
    if dados_empresa is None:
        dados_empresa = {}

    col1, col2 = st.columns([2, 1])

    with col1:
        cidade = st.text_input(
            "Cidade",
            value=dados_empresa.get("cidade", ""),
            placeholder="Máximo de 30 caracteres",
            max_chars=30,
            key=criar_chave_formulario("cidade", formulario_id)
        )

    with col2:
        estado_empresa = dados_empresa.get("estado")

        indice_estado = (
            ESTADOS.index(estado_empresa)
            if estado_empresa in ESTADOS
            else None
        )

        estado = st.selectbox(
            "UF",
            ESTADOS,
            index=indice_estado,
            placeholder="Selecione",
            key=criar_chave_formulario("estado", formulario_id)
        )

    return {
        "cidade": cidade,
        "estado": estado
    }


def campos_perfil_empresa(formulario_id=None, dados_empresa=None):
    if dados_empresa is None:
        dados_empresa = {}

    col1, col2 = st.columns(2)

    with col1:
        faturamento_anual = st.number_input(
            "Faturamento Anual (R$)",
            min_value=0.0,
            step=10000.0,
            format="%.2f",
            value=float(dados_empresa.get("faturamento_anual", 0.0)),
            placeholder="Ex: 250000.00",
            key=criar_chave_formulario("faturamento_anual", formulario_id)
        )

        exporta = st.toggle(
            "Exporta? (S/N)",
            value=bool(dados_empresa.get("exporta", 0)),
            help="Indica se a empresa exporta produtos ou serviços.",
            key=criar_chave_formulario("exporta", formulario_id)
        )

    with col2:
        colaboradores = st.number_input(
            "Colaboradores",
            min_value=1,
            step=1,
            value=int(dados_empresa.get("colaboradores", 1)),
            placeholder="Qtd.",
            key=criar_chave_formulario("colaboradores", formulario_id)
        )

        praticas_esg_ods = st.toggle(
            "ESG/ODS? (S/N)",
            value=bool(dados_empresa.get("praticas_esg_ods", 0)),
            help="Indica se a empresa possui práticas ESG alinhadas aos ODS.",
            key=criar_chave_formulario("praticas_esg_ods", formulario_id)
        )

    return {
        "faturamento_anual": faturamento_anual,
        "colaboradores": colaboradores,
        "exporta": exporta,
        "praticas_esg_ods": praticas_esg_ods
    }
