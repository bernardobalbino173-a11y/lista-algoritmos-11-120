# Algoritmo 106: Imprimir nome se o primeiro caractere for 'A' ou 'a'
nome = input("Digite nome: ")
if nome and nome[0] in ("A", "a"):
    print(nome)
