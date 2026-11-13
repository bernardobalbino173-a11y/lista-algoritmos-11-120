# Algoritmo 79: Calcular o valor acumulado de uma poupança programada
p = float(input("Digite o valor da aplicacao: "))
i = float(input("Digite a taxa (0 - 1): "))
n = int(input("Digite o numero de meses: "))
va = p * (((1 + i) ** n) - 1) / i
print("O valor acumulado:", va)
