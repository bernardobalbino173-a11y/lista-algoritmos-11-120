# Algoritmo 101: Indicar se o número digitado está compreendido entre 20 e 90
num = float(input("Digite numero: "))
if 20.0 < num < 90.0:
    print("O número está na faixa de 20 a 90, exclusive")
else:
    print("O número está fora da faixa de 20 a 90")
