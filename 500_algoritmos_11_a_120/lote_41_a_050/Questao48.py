# Algoritmo 48: Cálculo de quilowatts (100 kW = 1/7 do salário mínimo) e desconto de 10%
sm = float(input("Entre com o salário mínimo: "))
qtdade = float(input("Entre com a quantidade em quilowatt: "))
preco = sm / 700
vp = preco * qtdade
vd = vp * 0.9
print(f"preço do quilowatt: {preco:.2f}")
print(f"valor a ser pago: {vp:.2f}")
print(f"valor com desconto: {vd:.2f}")
