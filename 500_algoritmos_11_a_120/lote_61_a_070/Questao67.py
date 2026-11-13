# Algoritmo 67: Calcular o valor de uma prestação em atraso
valor = float(input("Digite o valor da prestação: "))
taxa = float(input("Digite a taxa: "))
tempo = int(input("Digite o tempo (numero de meses): "))
prest = valor + (valor * (taxa / 100) * tempo)
print("O valor da prestacao em atraso e =", prest)
