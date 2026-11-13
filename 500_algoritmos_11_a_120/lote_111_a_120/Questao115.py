# Algoritmo 115: Imprimir raiz quadrada do maior número e quadrado do menor número
import math

x = float(input("Digite valor de x: "))
y = float(input("Digite valor de y: "))
if x > y:
    print(math.sqrt(x))
    print(y ** 2)
elif y > x:
    print(math.sqrt(y))
    print(x ** 2)
else:
    print("numeros iguais")
