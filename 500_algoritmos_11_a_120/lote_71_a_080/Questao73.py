# Algoritmo 73: Receber número real e imprimir parte inteira, fracionária e arredondada
num = float(input("Entre com um numero com parte fracionaria: "))
numi = int(num)
numfrac = num - numi
numa = round(num + 0.00001)
print("parte inteira:", numi)
print(f"parte fracionaria: {numfrac + 0.00001:.3f}")
print("numero arredondado:", numa)
