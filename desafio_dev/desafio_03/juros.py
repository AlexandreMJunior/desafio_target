from datetime import datetime

valor = float(input("Valor: ").replace(",", "."))
vencimento = datetime.strptime(input("Vencimento (dd/mm/aaaa): "), "%d/%m/%Y").date()

hoje = datetime.now().date()
dias = max(0, (hoje - vencimento).days)

juros = valor * 0.025 * dias

print(f"Dias de atraso: {dias}")
print(f"Juros: R$ {juros:.2f}")
print(f"Total: R$ {valor + juros:.2f}")