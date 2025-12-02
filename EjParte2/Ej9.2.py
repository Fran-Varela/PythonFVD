positivos = 0
negativos = 0
hay_negativo = False

num = int(input("Introduce un número (0 para terminar): "))
while num != 0:
    if num > 0:
        positivos += 1
    else:
        negativos += 1
        hay_negativo = True
    num = int(input("Introduce un número (0 para terminar): "))

print("Positivos:", positivos)
print("Negativos:", negativos)
if hay_negativo:
    print("Se ha leído algún número negativo")