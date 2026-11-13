# Algoritmo 116: Entrar com três números diferentes e imprimir o maior
a = float(input("Digite 1 numero: "))
b = float(input("Digite 2 numero: "))
c = float(input("Digite 3 numero: "))
if a > b and a > c:
    print("maior:", a)
elif b > c:
    print("maior:", b)
else:
    print("maior:", c)
