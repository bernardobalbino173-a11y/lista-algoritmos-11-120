# Algoritmo 71: Ler hora e minuto atuais e informar quantos minutos se passaram desde o início do dia
hora = int(input("Entre com hora atual: "))
minuto = int(input("Entre com minutos: "))
tminuto = hora * 60 + minuto
print(f"Ate agora se passaram: {tminuto} minutos")
