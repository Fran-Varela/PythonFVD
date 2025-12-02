import math
x1 = float(input("Introduce x1: "))
y1 = float(input("Introduce y1: "))
x2 = float(input("Introduce x2: "))
y2 = float(input("Introduce y2: "))
distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("La distancia entre los puntos es:", distancia)