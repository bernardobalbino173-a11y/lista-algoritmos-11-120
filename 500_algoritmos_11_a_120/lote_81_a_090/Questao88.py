# Algoritmo 88: Calculadora simples com as quatro operações básicas
print("*************")
print("*CALCULADORA*")
print("*************")
print("+ para somar")
print("- para subtrair")
print("* para multiplicar")
print("/ para dividir")

resp = input("Digite opcao: ")
if resp == "+":
    a = float(input("Digite 1 numero com ponto: "))
    b = float(input("Digite 2 numero com ponto: "))
    print("SOMA:", a + b)
elif resp == "-":
    a = float(input("Digite 1 numero com ponto: "))
    b = float(input("Digite 2 numero com ponto: "))
    print("SUBTRACAO:", a - b)
elif resp == "*":
    a = float(input("Digite 1 numero com ponto: "))
    b = float(input("Digite 2 numero com ponto: "))
    print("MULTIPLICACAO:", a * b)
elif resp == "/":
    a = float(input("Digite 1 numero com ponto: "))
    b = float(input("Digite 2 numero com ponto: "))
    print("DIVISAO:", a / b)
else:
    print("OPCAO NAO DISPONIVEL!")
