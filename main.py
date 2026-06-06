from database import criar_tabelas
from ui.auth import cadastrar_usuario, login_usuario, entrada
from ui.system import dashboard
from utils import obter_pagina_atual


PAGINAS = {
    "entrada": entrada,
    "cadastro": cadastrar_usuario,
    "login": login_usuario,
    "dashboard": dashboard,
}


def main():
    criar_tabelas()

    pagina = obter_pagina_atual()
    PAGINAS[pagina]()


main()
