# Algoritmo 47: Entrar com um número no formato CDU e imprimir invertido: UDC
num = int(input("Entre com um número de 3 dígitos: "))
c = num // 100
d = (num % 100) // 10
u = num % 10
num1 = u * 100 + d * 10 + c
print("número:", num)
print("invertido:", num1)
