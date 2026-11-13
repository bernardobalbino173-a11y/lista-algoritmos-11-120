# Algoritmo 103: Calcular idade validando o ano de nascimento
anoa = int(input("Entre com ano atual: "))
anon = int(input("Entre com ano de nascimento: "))
if anon > anoa:
    print("Ano de Nascimento Invalido")
else:
    print("Idade:", anoa - anon)
