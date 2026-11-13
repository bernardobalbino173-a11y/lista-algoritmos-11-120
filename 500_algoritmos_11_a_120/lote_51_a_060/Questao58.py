# Algoritmo 58: Calcular expressão matemática com xnum1, xnum2 e xnum3
import math

xnum1 = float(input("Entrar com 1 valor: "))
xnum2 = float(input("Entrar com 2 valor: "))
xnum3 = float(input("Entrar com 3 valor: "))
x = xnum1 + xnum2 / (xnum3 + xnum1) + 2 * (xnum1 - xnum2) + math.log(64) / math.log(2)
print("X =", x)
