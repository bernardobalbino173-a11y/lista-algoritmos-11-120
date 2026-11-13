# Algoritmo 26: Entrar com uma data no formato ddmmaa e imprimir no formato mmddaa
data = int(input("Digite data no formato DDMMAA: "))
dia = data // 10000
mes = (data % 10000) // 100
ano = data % 100
ndata = mes * 10000 + dia * 100 + ano
print("DIA:", dia)
print("MES:", mes)
print("ANO:", ano)
print("DATA NO FORMATO MMDDAA:", ndata)
