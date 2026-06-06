class UsuarioRepository:
    def __init__(self, conexao):
        self.conexao = conexao

    def cadastrar_usuario(self, usuario):
        cursor = self.conexao.cursor()

        cursor.execute(
            """
            INSERT INTO usuarios (nome, senha)
            VALUES (?, ?)
            """,
            (usuario.nome, usuario.senha)
        )

        self.conexao.commit()

    def buscar_usuario(self, nome):
        cursor = self.conexao.cursor()

        cursor.execute(
            """
            SELECT senha
            FROM usuarios
            WHERE nome = ?
            """,
            (nome,)
        )

        return cursor.fetchone()
