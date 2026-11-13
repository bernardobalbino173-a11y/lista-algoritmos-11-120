# Algoritmo 104: Verificar se pessoa é do sexo feminino e tem menos de 25 anos (ACEITA / NÃO ACEITA)
nome = input("Digite nome: ")
sexo = input("Digite sexo: ")
idade = int(input("Digite idade: "))
if (sexo == "F" or sexo == "f") and idade < 25:
    print(nome, "ACEITA")
else:
    print(nome, "NAO ACEITA")
