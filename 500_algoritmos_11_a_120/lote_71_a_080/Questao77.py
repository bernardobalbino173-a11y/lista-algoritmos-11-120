# Algoritmo 77: Ler dois números reais e imprimir quadrado da diferença e diferença dos quadrados
a = float(input("Digite 1 numero: "))
b = float(input("Digite 2 numero: "))
d = (a - b) ** 2
q = (a ** 2) - (b ** 2)
print("O quadrado da diferenca =", d)
print("Diferenca dos quadrados =", q)
