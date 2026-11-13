# Algoritmo 98: Verificar se prestação ultrapassa 30% do salário bruto para linha de crédito
sb = float(input("Digite o salario: "))
vp = float(input("Digite o valor da prestacao: "))
if vp <= 0.3 * sb:
    print("emprestimo concedido")
else:
    print("emprestimo negado")
