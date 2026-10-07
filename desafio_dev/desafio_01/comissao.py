import json
from decimal import Decimal, ROUND_HALF_UP


with open("vendas.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo, parse_float=Decimal, parse_int=Decimal)

comissoes = {}

for venda in dados["vendas"]:
    vendedor = venda["vendedor"]
    valor = venda["valor"]

    if valor < 100:
        comissao = Decimal("0")
    elif valor < 500:
        comissao = valor * Decimal("0.01")
    else:
        comissao = valor * Decimal("0.05")

    comissoes[vendedor] = comissoes.get(vendedor, Decimal("0")) + comissao

for vendedor, total in comissoes.items():
    total = total.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    valor_formatado = f"{total:.2f}".replace(".", ",")
    print(f"{vendedor}: R$ {valor_formatado}")