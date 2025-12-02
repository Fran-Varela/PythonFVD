hay_diez = False
nota = int(input("Introduce una nota (0-10, -1 para terminar): "))
while nota != -1:
    if nota == 10:
        hay_diez = True
    nota = int(input("Introduce una nota (0-10, -1 para terminar): "))
if hay_diez:
    print("Hubo al menos una nota 10")
else:
    print("No hubo ninguna nota 10")