# Algoritmo 97: Informar se um número é divisível por 10, por 5, por 2 ou por nenhum destes
numero = int(input("Digite numero: "))
if numero % 10 == 0:
    print("múltiplo de 10")
elif numero % 2 == 0:
    print("múltiplo de 2")
elif numero % 5 == 0:
    print("múltiplo de 5")
else:
    print("não é múltiplo de 2 nem de 5")
