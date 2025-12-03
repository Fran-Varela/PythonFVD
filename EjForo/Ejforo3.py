texto = input("Escribe una cadena: ")

caracter = input("Escribe el carácter a contar: ")

contador = 0

for i in range(len(texto)):
    if texto[i] == caracter: 
        contador = contador + 1

print(f"El carácter '{caracter}' aparece {contador} veces en la cadena.")
