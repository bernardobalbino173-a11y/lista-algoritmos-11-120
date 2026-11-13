# Algoritmo 42: Entrar com um ângulo em graus e imprimir seno, cosseno, tangente, secante, cossecante e cotangente
import math

angulo = float(input("Digite um angulo em graus: "))
rang = angulo * math.pi / 180
print("seno:", math.sin(rang))
print("co-seno:", math.cos(rang))
print("tangente:", math.tan(rang))
print("co-secante:", 1 / math.sin(rang))
print("secante:", 1 / math.cos(rang))
print("cotangente:", 1 / math.tan(rang))
