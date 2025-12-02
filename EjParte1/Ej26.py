dado1 = int(input("Ingrese el valor del primer dado: "))
dado2 = int(input("Ingrese el valor del segundo dado: "))
dado3 = int(input("Ingrese el valor del tercer dado: "))

cantidad_seis = 0

if dado1 == 6:
    cantidad_seis += 1
if dado2 == 6:
    cantidad_seis += 1
if dado3 == 6:
    cantidad_seis += 1

if cantidad_seis == 3:
    print("Excelente")
elif cantidad_seis == 2:
    print("Muy bien")
elif cantidad_seis == 1:
    print("Regular")
else:
    print("Pésimo")
