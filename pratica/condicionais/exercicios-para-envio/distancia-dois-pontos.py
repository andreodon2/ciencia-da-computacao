import math
x1 = int(input("Coloque o número X1: "))
y1 = int(input("Coloque o número Y1: "))
x2 = int(input("Coloque o número X2: "))
y2 = int(input("Coloque o número Y2: "))

# Fórmula para o cálculo da distância entre dois pontos
d = math.sqrt(((x1 - x2)**2) + ((y1 - y2)**2))

distancia_x = x1 - x2
distancia_y = y1 - y2

if distancia_x or distancia_y >= 10:
    print("Longe")
else:
    print("Perto")