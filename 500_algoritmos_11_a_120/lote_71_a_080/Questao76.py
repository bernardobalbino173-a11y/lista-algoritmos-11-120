# Algoritmo 76: Ler número entre 0 e 60 e imprimir sucessor circular (sucessor de 60 é 0) sem condicionais
num = int(input("Digite numero: "))
print("sucessor:", (num + 1) % 61)
