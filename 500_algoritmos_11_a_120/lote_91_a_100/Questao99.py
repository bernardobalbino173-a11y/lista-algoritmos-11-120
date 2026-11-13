# Algoritmo 99: Ler número de 3 casas e imprimir se o algarismo das centenas é par ou ímpar
num = int(input("Numero de 3 algarismos: "))
c = num // 100
if c % 2 == 0:
    print("O algarismo das centenas e par:", c)
else:
    print("O algarismo das centenas e impar:", c)
