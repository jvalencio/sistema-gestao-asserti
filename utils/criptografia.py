import bcrypt


def transformar_em_hash(senha):
    return bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())


def comparar_senhas(senha_login, senha_banco):
    if bcrypt.checkpw(senha_login.encode('utf-8'), senha_banco):
        return True
    else:
        return False
