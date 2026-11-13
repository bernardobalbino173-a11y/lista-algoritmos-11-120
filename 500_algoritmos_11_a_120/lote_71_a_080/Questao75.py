# Algoritmo 75: Ler peso inteiro em kg, converter para gramas e calcular novo peso com +12%
peso = int(input("Entre com seu peso, só a parte inteira: "))
pesogramas = peso * 1000
novopeso = pesogramas * 1.12
print("peso em gramas:", pesogramas)
print("novo peso:", novopeso)
