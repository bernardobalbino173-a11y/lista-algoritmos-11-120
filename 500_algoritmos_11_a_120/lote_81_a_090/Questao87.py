# Algoritmo 87: Verificar resposta para a capital do Brasil
resp = input("Qual a capital do Brasil? ")
if resp == "BRASÍLIA" or resp == "Brasília":
    print("PARABÉNS!")
elif resp in ("brasília", "Brazília", "brazília", "BRAZÍLIA"):
    print("CERTO! Mas atenção para grafia: Brasília ou BRASÍLIA")
else:
    print("ERRADO! ESTUDE MAIS!")
