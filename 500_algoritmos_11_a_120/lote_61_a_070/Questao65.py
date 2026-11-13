# Algoritmo 65: Calcular o volume de uma lata de óleo
import math

altura = float(input("Digite a altura da lata: "))
raio = float(input("Digite o raio da lata: "))
volume = math.pi * (raio ** 2) * altura
print("O volume da lata e:", volume)
