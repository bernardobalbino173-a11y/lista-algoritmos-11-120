# Algoritmo 83: Ler um número; se positivo imprimir inverso, senão imprimir valor absoluto
numero = float(input("Digite numero: "))
if numero > 0.0:
    print("inverso:", 1 / numero)
else:
    print("absoluto:", numero * -1)
