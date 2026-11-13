# Algoritmo 51: Calcular perímetro e área de um círculo
import math

raio = float(input("Digite raio: "))
perimetro = 2 * math.pi * raio
area = math.pi * raio ** 2
print("perimetro:", perimetro)
print("area:", area)
