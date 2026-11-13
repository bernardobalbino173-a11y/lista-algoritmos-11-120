# Algoritmo 89: Calcular o peso em outro planeta a partir do peso na Terra
print("Planetas que podem ser analisados:")
print("1 - Mercurio")
print("2 - Venus")
print("3 - Marte")
print("4 - Jupiter")
print("5 - Saturno")
print("6 - Urano")

op = int(input("Escolha o planeta a ser analisado: "))
pterra = float(input("Entre com um peso na terra: "))

gravidades = {
    1: 0.37,
    2: 0.88,
    3: 0.38,
    4: 2.64,
    5: 1.15,
    6: 1.17
}

if op in gravidades:
    print("Seu peso no planeta escolhido e:", (pterra / 10) * gravidades[op])
else:
    print("Este planeta não pode ser analisado")
