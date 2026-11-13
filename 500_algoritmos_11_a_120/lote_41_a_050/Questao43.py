# Algoritmo 43: Entrar com um número e imprimir o logaritmo desse número na base 10
import math

num = float(input("Entre com o logaritmando: "))
logaritmo = math.log(num) / math.log(10)
print("logaritmo:", logaritmo)
