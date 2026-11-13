# Algoritmo 52: Calcular perímetro, área e diagonal de um quadrado
import math

lado = float(input("Digite o lado do quadrado: "))
perimetro = 4 * lado
area = lado ** 2
diagonal = lado * math.sqrt(2)
print("perimetro:", perimetro)
print("area:", area)
print("diagonal:", diagonal)
