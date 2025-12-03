texto = input("Escribe una cadena: ")

nueva_cadena = ""

for caracter in texto:
    if caracter != " ":   
        nueva_cadena = nueva_cadena + caracter 

print("Cadena sin espacios:", nueva_cadena)

