# Algoritmo 108: Imprimir o nome se o prenome for JOSÉ, José ou josé
nome = input("Digite nome: ")
prenome = nome[:5]
if prenome in ("JOSÉ ", "José ", "josé ") or nome in ("josé", "José", "JOSÉ"):
    print(nome)
