from .conexao import conectar


def criar_tabelas():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL UNIQUE,
            senha TEXT NOT NULL
        )
        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS empresas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            razao_social TEXT NOT NULL UNIQUE,
            nome_fantasia TEXT,
            cnpj TEXT NOT NULL UNIQUE,
            setor_ti TEXT NOT NULL,
            cidade TEXT NOT NULL,
            estado TEXT NOT NULL,
            faturamento_anual REAL,
            colaboradores INTEGER DEFAULT 0,
            exporta INTEGER DEFAULT 0,
            praticas_esg_ods INTEGER DEFAULT 0
        )
        """
    )

    conexao.commit()
    conexao.close()
