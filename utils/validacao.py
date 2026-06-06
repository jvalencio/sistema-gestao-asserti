def validar_empresa(dados_empresa):
    for valor in dados_empresa.values():
        if valor is None or str(valor).strip() == "":
            return "Campos obrigatórios não preenchidos."

    if len(dados_empresa["cnpj"]) != 14:
        return "O CNPJ precisa ter 14 caracteres."

    if not dados_empresa["cnpj"].isdigit():
        return "O CNPJ pode conter apenas números."

    if not dados_empresa["cidade"].replace(" ", "").isalpha():
        return "O nome da cidade pode conter apenas letras."

    return None


def validar_usuario(nome, senha, confirmar_senha):
    if not nome or not senha or not confirmar_senha:
        return "Campos obrigatórios não preenchidos."

    if not 8 <= len(nome) <= 12:
        return "O nome de usuário precisa ter entre 8 e 12 caracteres."

    if not nome.isalpha():
        return "O nome de usuário pode conter apenas letras."

    if len(senha) < 8:
        return "A senha precisa ter no mínimo 8 caracteres."

    if senha != confirmar_senha:
        return "As senhas digitadas não estão iguais."

    return None


def df_vazio(df):
    if df.empty:
        return True
    
    return False


def verificar_selecionadas(empresas_selecionadas, mensagem, acao):
    if not empresas_selecionadas.empty:
        if acao == "editar" and len(empresas_selecionadas) > 1:
            mensagem.warning("Selecione no máximo uma empresa para executar essa ação.")
            return False

        return True
    
    mensagem.warning("Selecione pelo menos uma empresa para executar essa ação.")
    return False
