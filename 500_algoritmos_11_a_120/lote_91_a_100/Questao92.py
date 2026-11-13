# Algoritmo 92: Somar dois números; se > 20 somar 8, senão subtrair 5
num1 = float(input("Digite 1 numero: "))
num2 = float(input("Digite 2 numero: "))
soma = num1 + num2
if soma > 20.0:
    print("soma:", soma + 8)
else:
    print("soma:", soma - 5)
