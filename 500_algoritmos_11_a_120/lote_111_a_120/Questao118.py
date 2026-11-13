# Algoritmo 118: Entrar com três números diferentes e imprimi-los em ordem crescente
a = float(input("Digite 1 numero: "))
b = float(input("Digite 2 numero: "))
c = float(input("Digite 3 numero: "))
if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b
print("Ordem Crescente:", a, b, c)
