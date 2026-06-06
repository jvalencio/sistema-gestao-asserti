from babel.numbers import format_currency


def converter_booleano(coluna):
    return coluna.map({
        0: "Não",
        1: "Sim"
    })


def formatar_cnpj(cnpj):
    return (
        f"{cnpj[:2]}."
        f"{cnpj[2:5]}."
        f"{cnpj[5:8]}/"
        f"{cnpj[8:12]}-"
        f"{cnpj[12:]}"
    )


def formatar_moeda(valor):
    return format_currency(valor, "R$", locale="pt_BR")
