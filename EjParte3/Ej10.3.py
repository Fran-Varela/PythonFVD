parcial1 = float(input("Introduce la primera nota parcial: "))
parcial2 = float(input("Introduce la segunda nota parcial: "))
parcial3 = float(input("Introduce la tercera nota parcial: "))
examen_final = float(input("Introduce la nota del examen final: "))
trabajo_final = float(input("Introduce la nota del trabajo final: "))

promedio_parciales = (parcial1 + parcial2 + parcial3) / 3
calificacion = promedio_parciales * 0.55 + examen_final * 0.30 + trabajo_final * 0.15
print("Calificación final:", calificacion)