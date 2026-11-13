# Algoritmo 117: Entrar com três números e armazenar o maior na variável maior
a = float(input("Digite 1 numero: "))
b = float(input("Digite 2 numero: "))
c = float(input("Digite 3 numero: "))
maior = a
if b > maior:
    maior = b
if c > maior:
    maior = c
print("maior:", maior)
