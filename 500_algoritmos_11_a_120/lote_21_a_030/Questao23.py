# Algoritmo 23: Entrar com um número inteiro de 3 casas e imprimir o algarismo da casa das dezenas
a = int(input("Digite numero de tres casas: "))
d = (a % 100) // 10
print("Algarismo da casa das dezenas:", d)
