# Algoritmo 59: Calcular a hipotenusa de um triângulo retângulo
import math

b = float(input("Entrar com 1 cateto: "))
c = float(input("Entrar com 2 cateto: "))
a = math.sqrt(b ** 2 + c ** 2)
print("A hipotenusa e:", a)
