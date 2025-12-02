positivos = 0
negativos = 0
for i in range(100):
    num = int(input("Introduce un número no nulo: "))
    if num > 0:
        positivos += 1
    else:
        negativos += 1
print("Positivos:", positivos)
print("Negativos:", negativos)