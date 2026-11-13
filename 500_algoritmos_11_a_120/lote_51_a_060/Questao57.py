# Algoritmo 57: Entrar com notas PR1 e PR2 e imprimir média final truncada e arredondada
pr1 = float(input("Digite pr1: "))
pr2 = float(input("Digite pr2: "))
mf = (pr1 + pr2) / 2
print("media truncada =", int(mf))
print("media arredondada =", round(mf + 0.001))
