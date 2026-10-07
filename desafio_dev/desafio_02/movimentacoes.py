import json
from uuid import uuid4

with open("estoque.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)


if "movimentacoes" not in dados:
    dados["movimentacoes"] = []

while True:
    print("\n--- PRODUTOS ---")

    for produto in dados["estoque"]:
        print(
            f'{produto["codigoProduto"]} - '
            f'{produto["descricaoProduto"]} | '
            f'Estoque: {produto["estoque"]}'
        )

    print("\n1 - Entrada de mercadoria")
    print("2 - Saída de mercadoria")
    print("0 - Encerrar")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "0":
        break

    if opcao not in ("1", "2"):
        print("Opção inválida.")
        continue

    try:
        codigo = int(input("Código do produto: "))
        quantidade = int(input("Quantidade: "))
    except ValueError:
        print("Informe números inteiros para o código e a quantidade.")
        continue

    if quantidade <= 0:
        print("A quantidade deve ser maior que zero.")
        continue

    produto_encontrado = None

    for produto in dados["estoque"]:
        if produto["codigoProduto"] == codigo:
            produto_encontrado = produto
            break

    if produto_encontrado is None:
        print("Produto não encontrado.")
        continue

    estoque_anterior = produto_encontrado["estoque"]

    if opcao == "2" and quantidade > estoque_anterior:
        print(f"Estoque insuficiente. Disponível: {estoque_anterior}")
        continue

    descricao = input(
        "Descrição da movimentação (ex.: compra, venda, devolução): "
    ).strip()

    if not descricao:
        print("A descrição é obrigatória.")
        continue

    if opcao == "1":
        tipo = "Entrada"
        estoque_final = estoque_anterior + quantidade
    else:
        tipo = "Saída"
        estoque_final = estoque_anterior - quantidade

    identificador = uuid4().int

    movimentacao = {
        "id": identificador,
        "codigoProduto": codigo,
        "tipo": tipo,
        "descricao": descricao,
        "quantidade": quantidade,
        "estoqueAnterior": estoque_anterior,
        "estoqueFinal": estoque_final
    }

    produto_encontrado["estoque"] = estoque_final
    dados["movimentacoes"].append(movimentacao)


    with open("estoque.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)

    print("\nMovimentação registrada!")
    print(f"Identificador: {identificador}")
    print(f"Produto: {produto_encontrado['descricaoProduto']}")
    print(f"Tipo: {tipo}")
    print(f"Descrição: {descricao}")
    print(f"Quantidade movimentada: {quantidade}")
    print(f"Estoque final: {estoque_final}")