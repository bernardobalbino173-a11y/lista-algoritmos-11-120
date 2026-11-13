# Algoritmo 107: Imprimir o nome somente se o prenome for JOSÉ
nome = input("Digite nome: ")
if nome[:5] == "JOSÉ " or nome == "JOSÉ":
    print(nome)
