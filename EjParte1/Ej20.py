calificacion = int(input("Ingrese la nota del alumno:"))

if (calificacion in ( 0, 1, 2)):
    print("Muy deficiente")
elif (calificacion in (3, 4)):
    print("Deficiente")
elif (calificacion == 5):
    print("Suficiente")
elif (calificacion == 6):
    print("Bien")
elif (calificacion in (7, 8)):
    print("Notable")
elif (calificacion in (9, 10)):
    print("Sobresaliente")
else:
    print("No es una nota del 1 al 10")