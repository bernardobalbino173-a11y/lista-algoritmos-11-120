# Algoritmo 66: Calcular litros de combustível gastos em uma viagem (12 km/L)
tempo = float(input("Digite o tempo gasto: "))
vel = float(input("Digite a velocidade media: "))
dist = tempo * vel
litros = dist / 12
print("velocidade =", vel)
print("tempo =", tempo)
print("distancia =", dist)
print("litros =", litros)
