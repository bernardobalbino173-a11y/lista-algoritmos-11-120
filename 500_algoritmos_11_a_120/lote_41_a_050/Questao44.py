# Algoritmo 44: Entrar com o número e a base em que se deseja calcular o logaritmo
import math

num = float(input("Entre com o logaritmando: "))
base = float(input("Entre com a base: "))
logaritmo = math.log(num) / math.log(base)
print(f"O logaritmo de {num} na base {base} e: {logaritmo}")
