# Algoritmo 120: Armazenar três números diferentes nas variáveis maior, intermediario e menor
a = float(input("Digite 1 numero: "))
b = float(input("Digite 2 numero: "))
c = float(input("Digite 3 numero: "))
if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b
maior = c
intermediario = b
menor = a
print("maior:", maior)
print("intermediario:", intermediario)
print("menor:", menor)
