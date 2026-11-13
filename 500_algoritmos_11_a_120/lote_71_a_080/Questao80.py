# Algoritmo 80: Faturamento anual, multas mensais e quantidade final de fitas de uma locadora
quant = int(input("Digite a quantidade de fitas: "))
valAluguel = float(input("Digite o valor do aluguel: "))
fatAnual = (quant / 3) * valAluguel * 12
multas = valAluguel * 0.1 * ((quant / 3) / 10)
quantFinal = quant - (quant * 0.02) + (quant / 10)
print("Faturamento anual:", fatAnual)
print("Multas mensais:", multas)
print("Quantidade de fitas no final do ano:", quantFinal)
