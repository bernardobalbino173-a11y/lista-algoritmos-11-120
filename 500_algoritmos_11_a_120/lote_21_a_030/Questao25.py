# Algoritmo 25: Entrar com uma data no formato ddmmaa e imprimir dia, mês e ano separados
data = int(input("Digite data no formato ddmmaa: "))
dia = data // 10000
mes = (data % 10000) // 100
ano = data % 100
print("DIA:", dia)
print("MES:", mes)
print("ANO:", ano)
