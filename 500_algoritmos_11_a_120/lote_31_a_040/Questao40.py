# Algoritmo 40: Entrar com dois números inteiros e imprimir dividendo, divisor, quociente e resto
val1 = int(input("Entre com o dividendo: "))
val2 = int(input("Entre com divisor: "))
quoc = val1 // val2
rest = val1 % val2
print("\ndividendo:", val1)
print("divisor  :", val2)
print("quociente:", quoc)
print("resto    :", rest)
