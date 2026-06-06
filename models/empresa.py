from dataclasses import dataclass

@dataclass
class Empresa:
    razao_social: str
    nome_fantasia: str
    cnpj: str
    setor_ti: str
    cidade: str
    estado: str
    faturamento_anual: float
    colaboradores: int
    exporta: bool
    praticas_esg_ods: bool
