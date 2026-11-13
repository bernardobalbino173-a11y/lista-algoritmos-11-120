# Algoritmo 72: Calcular rendimento e valor total após taxa de juros sobre um depósito
deposito = float(input("Entre com depósito: "))
taxa = float(input("Entre com a taxa de juros: "))
valor = deposito * taxa / 100
total = deposito + valor
print("Rendimentos:", valor)
print("Total:", total)
