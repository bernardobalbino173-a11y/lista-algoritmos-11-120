# Algoritmo 50: Calcular perímetro, área e diagonal de um retângulo
import math

base = float(input("Digite base: "))
altura = float(input("Digite altura: "))
perimetro = 2 * (base + altura)
area = base * altura
diagonal = math.sqrt(base ** 2 + altura ** 2)
print("perimetro =", perimetro)
print("area =", area)
print("diagonal =", diagonal)
