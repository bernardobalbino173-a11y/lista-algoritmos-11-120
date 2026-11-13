# Algoritmo 20: Manipulação de strings (tamanho, concatenação, cópia, fatiamento)
c = input("Digite palavra 1: ")
c1 = input("Digite palavra 2: ")

print("Tamanho da 1a palavra:", len(c))
print("Concatenando:", c + c1)
d = c
print("O conteudo de d:", d)
d1 = c + c1
print("Concatenacao:", d1)
print("Primeiro caractere:", c[0] if c else "")
print("Ultimo caractere:", c[-1] if c else "")
print("Todos menos o primeiro:", c[1:])
print("O terceiro elemento (indice 3 / 4o caractere):", c[3] if len(c) > 3 else "")
print("Os tres primeiros elementos:", c[:3])
print("Os elementos apos os tres primeiros:", c[3:])
