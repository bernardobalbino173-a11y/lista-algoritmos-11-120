# Algoritmo 63: Cálculo do salário líquido de um professor com desconto do INSS
na = int(input("Horas trabalhadas (numero de aulas): "))
vha = float(input("Valor da hora-aula: "))
pd = float(input("Percentual de desconto: "))
sb = na * vha
td = (pd / 100) * sb
sl = sb - td
print("salario liquido:", sl)
