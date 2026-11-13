# Algoritmo 24: Entrar com um número inteiro de 3 casas e imprimir o algarismo da casa das dezenas (com parênteses)
a = int(input("Digite numero de tres casas: "))
d = (a // 10) % 10
print("Algarismo da casa das dezenas:", d)
