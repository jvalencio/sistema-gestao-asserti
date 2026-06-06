import pandas as pd


class EmpresaRepository:
    def __init__(self, conexao):
        self.conexao = conexao

    def cadastrar_empresa(self, empresa):
        cursor = self.conexao.cursor()

        cursor.execute(
            """
            INSERT INTO empresas (
                razao_social,
                nome_fantasia,
                cnpj,
                setor_ti,
                cidade,
                estado,
                faturamento_anual,
                colaboradores,
                exporta,
                praticas_esg_ods
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                empresa.razao_social,
                empresa.nome_fantasia,
                empresa.cnpj,
                empresa.setor_ti,
                empresa.cidade,
                empresa.estado,
                empresa.faturamento_anual,
                empresa.colaboradores,
                empresa.exporta,
                empresa.praticas_esg_ods
            )
        )

        self.conexao.commit()

    def buscar_empresa(self, termo_busca):
        termo = f"%{termo_busca}%"

        return pd.read_sql_query(
            """
            SELECT *
            FROM empresas
            WHERE razao_social LIKE ?
                OR nome_fantasia LIKE ?
                OR cnpj LIKE ?
            """,
            self.conexao,
            params=(termo, termo, termo)
        )

    def verificar_existencia(self, razao_social, cnpj):
        cursor = self.conexao.cursor()

        cursor.execute(
            """
            SELECT 1
            FROM empresas
            WHERE razao_social = ?
            OR cnpj = ?
            LIMIT 1
            """,
            (razao_social, cnpj)
        )

        return cursor.fetchone() is not None

    def listar_empresas(self):
        df = pd.read_sql_query(
            "SELECT * FROM empresas",
            self.conexao
        )

        return df

    def deletar_empresas(self, empresas_selecionadas):
        cursor = self.conexao.cursor()

        ids_selecionados = empresas_selecionadas["id"].tolist()
        placeholders = ", ".join(["?"] * len(ids_selecionados))

        cursor.execute(
            f"""
            DELETE
            FROM empresas
            WHERE id IN ({placeholders})
            """,
            ids_selecionados
        )

        self.conexao.commit()

    def editar_empresa(self, id_empresa, empresa_editada):
        cursor = self.conexao.cursor()

        cursor.execute(
            """
            UPDATE empresas
            SET    
                razao_social = ?,
                nome_fantasia = ?,
                cnpj = ?,
                setor_ti = ?,
                cidade = ?,
                estado = ?,
                faturamento_anual = ?,
                colaboradores = ?,
                exporta = ?,
                praticas_esg_ods = ?
            WHERE id = ?
            """,
            (
                empresa_editada.razao_social,
                empresa_editada.nome_fantasia,
                empresa_editada.cnpj,
                empresa_editada.setor_ti,
                empresa_editada.cidade,
                empresa_editada.estado,
                empresa_editada.faturamento_anual,
                empresa_editada.colaboradores,
                empresa_editada.exporta,
                empresa_editada.praticas_esg_ods,
                id_empresa
            )
        )

        self.conexao.commit()
