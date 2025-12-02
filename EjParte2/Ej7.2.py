hay_negativo = False
for i in range(100):
    num = int(input("Introduce un número no nulo: "))
    if num < 0:
        hay_negativo = True
if hay_negativo:
    print("Se ha leído algún número negativo")
else:
    print("No se ha leído ningún número negativo")