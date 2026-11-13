# Algoritmo 100: Ler número de 4 casas e verificar se o número das unidades de milhar e centenas é múltiplo de 4
num = int(input("Numero de 4 algarismos: "))
c = num // 100
if c % 4 == 0:
    print("O numero e multiplo de 4:", c)
else:
    print("O numero nao e multiplo de 4:", c)
