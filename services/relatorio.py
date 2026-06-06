from io import BytesIO

from reportlab.lib.styles import getSampleStyleSheet

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from utils import (
    formatar_moeda,
    total_empresas,
    faturamento_anual_total,
    mediana_faturamento,
    maior_faturamento_ano,
    estado_lider_faturamento,
    setor_lider_faturamento,
    setor_com_mais_empresas,
    percentual_esg_ods,
)


def gerar_relatorio_pdf(df):
    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)

    estilos = getSampleStyleSheet()

    conteudo = [
        Paragraph("Relatório de Indicadores", estilos["Title"]),
        Spacer(1, 20),

        Paragraph(
            f"- Total de empresas: {total_empresas(df)}",
            estilos["Normal"]
        ),
        
        Paragraph(
            f"- Faturamento total: {formatar_moeda(faturamento_anual_total(df))}",
            estilos["Normal"]
        ),

        Paragraph(
            f"- Mediana de faturamento: {formatar_moeda(mediana_faturamento(df))}",
            estilos["Normal"]
        ),

        Paragraph(
            f"- Maior faturamento no ano: {formatar_moeda(maior_faturamento_ano(df))}",
            estilos["Normal"]
        ),

        Paragraph(
            f"- Estado líder de faturamento: {estado_lider_faturamento(df)}",
            estilos["Normal"]
        ),

        Paragraph(
            f"- Setor líder de faturamento: {setor_lider_faturamento(df)}",
            estilos["Normal"]
        ),

        Paragraph(
            f"- Setor com mais empresas: {setor_com_mais_empresas(df)}",
            estilos["Normal"]
        ),

        Paragraph(
            f"- % Empresas com práticas ESG alinhadas aos ODS: {percentual_esg_ods(df)}%",
            estilos["Normal"]
        )
    ]

    doc.build(conteudo)

    buffer.seek(0)

    return buffer
