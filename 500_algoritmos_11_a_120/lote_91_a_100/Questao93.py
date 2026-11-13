# Algoritmo 93: Imprimir raiz quadrada se positivo e quadrado se negativo
import math

numero = float(input("Digite numero: "))
if numero > 0.0:
    print("raiz:", math.sqrt(numero))
elif numero < 0.0:
    print("quadrado:", numero ** 2)
