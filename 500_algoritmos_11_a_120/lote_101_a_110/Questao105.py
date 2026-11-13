# Algoritmo 105: Identificar gentílico pela sigla do estado (RJ, SP, MG ou outros)
sigla = input("Digite sigla: ")
if sigla in ("RJ", "rj"):
    print("carioca")
elif sigla in ("SP", "sp"):
    print("paulista")
elif sigla in ("MG", "mg"):
    print("mineiro")
else:
    print("outros estados")
