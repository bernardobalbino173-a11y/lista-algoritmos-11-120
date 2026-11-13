# Algoritmo 85: Ler três números e armazenar o maior na variável max usando ifs aninhados
a = float(input("Digite 1 numero: "))
b = float(input("Digite 2 numero: "))
c = float(input("Digite 3 numero: "))
if a > b:
    if a > c:
        max_val = a
    else:
        max_val = c
else:
    if b > c:
        max_val = b
    else:
        max_val = c
print(max_val)
